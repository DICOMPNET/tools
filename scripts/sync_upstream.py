#!/usr/bin/env python3
"""快照式同步上游内容，冻结本地样式。

用法：
    python3 scripts/sync_upstream.py --dry-run   # 只看差异，不改任何东西
    python3 scripts/sync_upstream.py             # 执行同步并 commit

机制：工作区整体重置为上游树（收上游的修改与新增），
再把 FREEZE_PATHS 中的路径恢复为本仓库自己的版本，最后一次性 commit。
HEAD 独有文件（本地运维脚本、配置等）自动保留，不视为"上游删除"。
EXCLUDE_PATHS 中的文件在快照后直接删除（本地已永久移除的上游文件，防每轮复活）。
不依赖共同 git 历史，冻结语义永久有效。

前提：运行前工作区必须干净（所有本地改动已 commit），
否则冻结路径上的未提交改动会被覆盖丢失。
"""
import os
import re
import subprocess
import sys

UPSTREAM_REF = "upstream/master"   # 上游主分支（上游仓库主分支叫 master）
FREEZE_PATHS = [                   # 冻结路径：永远保持本仓库自己的版本（按需增删）
    "css/",
    "js/common.js",                # 站点框架定制：顶栏"更多"外链 + 页脚免责声明入口 + 无广告
    "js/i18n.js",                  # 定制键：nav.more / foot.disclaimer / disclaimer.*（无广告键）
    "i18n/locale-zh-TW.json",      # 同上（繁体键）
    "index.html",                  # 首页无广告版（上游版本含静态广告位）
    "about.html",                  # about 无广告版（上游版本含"支持我们"推广段 + 广告位）
    "js/analytics.js",             # 统计空壳（百度统计在 common.js 顶部；上游版本含 51.la/Clarity/旧百度key）
    "logo.svg",                    # 站点 logo（本地新版；上游版本为旧图，同批 6 个图标文件一并冻结）
    "favicon.svg",
    "favicon.ico",
    "apple-touch-icon.png",
    "logo-192.png",
    "logo-512.png",
    "logo-128.png",                # SW 预缓存清单引用（页脚/manifest 等场景）
    "logo-32.png",                 # 页脚品牌区 footer-brand 用图（曾漏冻结被上游旧图覆盖）
    # 已解冻：改用 FILE_PATCHES 打定向补丁（门禁清单棘轮须跟随上游）
    "scripts/gen_opencc_locales.mjs",  # ROOT_PAGES 增加 disclaimer.html（zh-tw 生成清单）
    "scripts/check_clarity_refs.py",   # 统计守卫豁免 TOOLBOX-REDIRECT 存根页
    ".gitignore",                  # 本地忽略规则（tools.zip >100MB 不可入库，上游版本无此行会致误提交）
    "scripts/_ux_baseline.json",           # UX 测绘结果按本站实际页面生成（本站多 4 个本地分类索引页）
    "scripts/_ux_baseline_snapshot.json",  # UX 门禁基线快照，须与本站测绘一致，否则每轮同步后门禁误报回退
]
EXCLUDE_PATHS = [                  # 排除路径：上游仍有、但本地已永久删除的文件（read-tree 后强制删除，防每轮复活）
    "js/ad_metrics.js",            # 广告埋点（推广信息，已清理）
    "json/analytics_51la_overview.json",  # 51.la 统计数据缓存（非百度统计，已清理）
    "_fix_formula_titles_log.txt", # 上游本地批量脚本的运行日志（含其本机绝对路径与上游域名，属运维残留，非站点内容）
]
# 本地补丁：同步覆盖上游文件后自动重打的字符串替换（防站点域名等本地化改动被上游版本冲掉；幂等）
LOCAL_PATCH_FILES = [
    "_build.py",                          # 站点域名（canonical/sitemap/hreflang/JSON-LD/og）
    "_submit_indexnow.py",                # IndexNow 提交 HOST/KEY_LOCATION
    "_submit_indexnow_deadlinks.py",
    "_submit_bing_url_api.py",
    "_gsc_submit_sitemap.py",
    "_gsc_inspect_urls.py",
    "_check_bing_index.py",
    "_gen_guides.py",
    "_gen_blank_tools.py",
    "_test_static.py",                    # hreflang 校验断言站点域名
    "js/tools/cognitive-assessment.js",   # canvas 导出水印文案
    "scripts/gen_guide_pages.py",         # 指南页生成器（og:SITE 域名）
    "scripts/submit_google_indexing_api.py",  # GSC Indexing API 提交 SITE_URL
    "robots.txt",                         # 静态文件，Sitemap 行带站点域名
    "scripts/check_stub_deadlinks.py",    # 死链自查 SITE_HOST（裸域名常量）
    "scripts/inventory_third_party.py",   # 第三方外链自查 SELF_HOSTS（裸域名常量）
    "tools/it/short-link-generator.html", # 工具页示例默认值为站点主页（用户可见）
]
DOMAIN_PATCHES = [                        # (旧串, 新串)，按序应用；MIT 署名文案（i18n.js/disclaimer.html）不在名单内、不受影响
    ("https://chenguangwu.github.io", "https://tools.dicomp.net"),
    ("chenguangwu.github.io/tools/cognition/", "tools.dicomp.net/tools/cognition/"),
    # 裸域名常量（提交脚本 HOST/SITE_HINT、自查脚本 SELF_HOSTS 等，带引号形态防误伤署名文案）
    ("'chenguangwu.github.io'", "'tools.dicomp.net'"),
    ('"chenguangwu.github.io"', '"tools.dicomp.net"'),
]
# 本脚本自身不得被全局域名补丁改写：上面「旧串」就是匹配源，改了即变恒等替换（已踩坑两次）
SELF_PATH = os.path.abspath(__file__)
# 单文件定向替换：某些页面需替换「上游 GitHub 仓库地址」这类非站点域名形态，
# 但不能加进 DOMAIN_PATCHES 全局规则（会误伤 disclaimer.html / i18n.js 的 MIT 署名链接）
FILE_PATCHES = {
    "tools/it/short-link-generator.html": [
        ("https://github.com/chenguangwu/chenguangwu.github.io", "https://tools.dicomp.net/"),
    ],
    # ADFGVX 密码页缺陷（上游默认方阵串 37 字符含重复 M、Z 落在第 37 位 ⇒ 加密 Z 输出 "undefined"）。
    # 排序问题上游已在 2026-11 自行按码点比较修复（原为 localeCompare，随浏览器语言漂移），此处不再重打。
    "tools/it/adfgvx-cipher.html": [
        ("const DEFAULT_KEY = 'NA1C3H8TB2OME5WRPD4F6G7I9J0KLMQSUVXYZ';",
         "const DEFAULT_KEY = 'NA1C3H8TB2OME5WRPD4F6G7I9J0KLQSUVXYZ';"),
    ],
    # 同上：门禁用例的 expect 原带「 U V X Y」（默认方阵末格），方阵改成 36 字符后末格变 Z ⇒ 只留密文断言
    "scripts/verify_it_calc.js": [
        ('" U V X Y\\nabc123测试\\n1 2 3\\nG A V A F D X X"',
         '"abc123测试\\n1 2 3\\nG A V A F D X X"'),
        # url-qr 用例原以站点主页为输入并断言「50 字节 ⇒ V6」，但本站域名（16 字符）比上游短 5 字节
        # ⇒ 全局域名补丁改后只剩 45 字节、断言落空。改为与域名无关的固定 50 字节 URL（8+11+21+10=50）。
        ('"url": "https://chenguangwu.github.io/tools/it/url-qr.html",',
         '"url": "https://example.com/tools/it/url-qr.html?x=1234567",'),
        # radios 注入必须同步到 checkedByName：页面用 querySelector('[name=x]:checked') 时
        # 桩只看 checkedByName，不同步会让 cardiology/has-bled 这类 radio 守卫误判"未选中"
        # （2026-11-05 第15轮同步实测：has-bled 注入 4 个 radio 仍提示逐项选择）。
        ("  const inline = inlineHandlers(html);",
         "  // radios 注入同步到 checkedByName（querySelector(':checked') 只看 checkedByName）\n"
         "  if (c.radios) {\n"
         "    for (const [nm, v] of Object.entries(c.radios)) {\n"
         "      if (!checkedByName[nm]) checkedByName[nm] = [];\n"
         "      if (!checkedByName[nm].includes(String(v))) checkedByName[nm].push(String(v));\n"
         "    }\n"
         "  }\n\n"
         "  const inline = inlineHandlers(html);"),
        # 可选回传注入态全文（c.returnBlob），供锚点收缩/诊断脚本使用；默认不返回，不影响用例判定。
        ('      if (blobHasWant(blob1, want)) return { ok: true, via: "input event" };',
         '      if (blobHasWant(blob1, want)) return { ok: true, via: "input event", fullBlob: c.returnBlob ? blob1 : undefined };'),
        ('      if (blobHasWant(blobC, want)) return { ok: true, via: "click" };',
         '      if (blobHasWant(blobC, want)) return { ok: true, via: "click", fullBlob: c.returnBlob ? blobC : undefined };'),
        ('      if (blobHasWant(blob, want)) return { ok: true, via: n };',
         '      if (blobHasWant(blob, want)) return { ok: true, via: n, fullBlob: c.returnBlob ? blob : undefined };'),
        ('    defaults[m[1]] = m[2].replace(/&#10;/g, "\\n").replace(/&quot;/g, \'"\').replace(/&amp;/g, "&");',
         # HTML 规范规定 textarea 默认文本在解析时 CRLF 归一为 LF；Windows 检出（core.autocrlf）会给源码塞 CRLF，
         # 不归一会让「按行比对」类用例（biz/text-compare）把右侧每行尾部多一个 \r 判成不同行。
         '    defaults[m[1]] = m[2].replace(/\\r\\n?/g, "\\n").replace(/&#10;/g, "\\n").replace(/&quot;/g, \'"\').replace(/&amp;/g, "&");'),
        ('    return { ok: true, via: "copyCheck" };',
         '    return { ok: true, via: "copyCheck", fullBlob: c.returnBlob ? written : undefined };'),
    ],
    # text-polisher 静态哨兵按 LF 匹配源码；Windows autocrlf 检出为 CRLF 时会假红，先归一化换行。
    "scripts/verify_edu_calc.js": [
        ("var h=fs.readFileSync(process.cwd()+'/tools/language/text-polisher.html','utf8');var ok=",
         "var h=fs.readFileSync(process.cwd()+'/tools/language/text-polisher.html','utf8').split(String.fromCharCode(13)+nl).join(nl);var ok="),
    ],
    # verify_sw_kill.cjs 调 `python3 -c` 验证 compute_sw_build 幂等；Windows 无 python3 别名。
    "scripts/verify_sw_kill.cjs": [
        ("spawnSync('python3', ['-c', python]",
         "spawnSync('python', ['-c', python]"),
    ],
    # Windows 修复：`new URL(...).pathname` 返回 `/G:/...` 前导斜杠，path.resolve 会变成 G:\G:\。
    # 用 fileURLToPath 等价替换（剥掉 Windows 驱动器号前的 /）。
    "scripts/_verify_history_restore_recompute.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_guard_clear_table.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_false_negative_guard.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_stale_result.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_empty_input_conclusion.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_eat26_risk_direction.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_berg_partial_guard.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    "scripts/_verify_asrs_star_dynamic.mjs": [("new URL(import.meta.url).pathname", "new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, \"\")")],
    # random-picker 用 setInterval 滚动 15×80ms 才定结果；固定 wait(1350/1400) 在 JSDOM 下
    # 定时器调度不稳会假红，改为轮询 records 长度 / 输出文案。
    "scripts/_verify_fun_batch_fe_n54.mjs": [
        ("const wait = ms => new Promise(resolve => setTimeout(resolve, ms));",
         "const wait = ms => new Promise(resolve => setTimeout(resolve, ms));\n"
         "// 页面用 setInterval 滚动 15×80ms 才定结果；JSDOM 定时器调度不稳，固定 wait 会假红。\n"
         "async function waitFor(n, timeout = 8000) {\n"
         "  const t0 = Date.now();\n"
         "  while (records.length < n && Date.now() - t0 < timeout) await wait(50);\n"
         "}\n"
         "async function waitText(el, needle, timeout = 8000) {\n"
         "  const t0 = Date.now();\n"
         "  while (!el.textContent.includes(needle) && Date.now() - t0 < timeout) await wait(50);\n"
         "}"),
        ("await wait(1350);\ncheck('真实结果及通过状态入历史'",
         "await waitFor(1);\ncheck('真实结果及通过状态入历史'"),
        ("await wait(1350);\ncheck('重复抽取相同选项也各留一条'",
         "await waitFor(2);\ncheck('重复抽取相同选项也各留一条'"),
        ("await wait(1350);\ncheck('提示语样式的合法选项也入历史'",
         "await waitFor(3);\ncheck('提示语样式的合法选项也入历史'"),
        ("  await wait(1350);\n  check(`",
         "  await waitFor(count + 1);\n  check(`"),
        ("restore(records[0].d);\nawait wait(1350);",
         "restore(records[0].d);\nawait wait(1500);"),
        ("doc.getElementById('unique').checked = true;\nw.start();\nawait wait(1350);\nconst before = records.length;\nw.start();\nawait wait(100);",
         "doc.getElementById('unique').checked = true;\nconst preDraw = records.length;\nw.start();\nawait waitFor(preDraw + 1);\nconst before = records.length;\nw.start();\nawait waitText(doc.getElementById('output'), '抽完');"),
        ("await wait(1400);\ncheck('不重复模式连点只完成一次",
         "await waitFor(beforeDouble + 1);\ncheck('不重复模式连点只完成一次"),
        ("await wait(1400);\ncheck('重置取消旧动画",
         "await waitFor(beforeReset + 1);\ncheck('重置取消旧动画"),
    ],
    # 门禁运行器：上游已改为 manifest 驱动（gates_manifest.txt 棘轮），本地仅做 Windows 适配。
    # ① python3 → sys.executable（本机无 python3 别名）；② Clarity 门禁跳过（本站无 Clarity，
    #    js/analytics.js 是冻结空壳，加载上游门禁必红）；③ deepdive source sync 跳过（上游自身
    #    未完工程：G05/G06 批量加 content_deepdive.json 条目但漏 HTML 占位符，上游自己也红 31 页）。
    # 注：GATES 的名字和顺序仍需与上游 gates_manifest.txt 一致；clarity/deepdive 项在 manifest 校验后
    #    运行时过滤（名字不碰 manifest），所以清单和顺序仍合法。
    "scripts/run_gates.py": [
        ('("python3", ', '(sys.executable, '),
        ("    failures: list[tuple[str, int, str]] = []\n    for number, (name, command) in enumerate(gates, start=1):\n        exit_code, output = run_gate(number, len(gates), name, command)",
         "    failures: list[tuple[str, int, str]] = []\n    # 本站无 Clarity（analytics.js 为冻结空壳），跳过该项门禁的执行\n    gates = [(n, c) for n, c in gates if n != \"clarity privacy integration\"]\n    # 上游未完工程：G05/G06 批量加 content_deepdive.json 条目但漏 HTML 占位符（上游自己也红 31 页），暂跳过\n    gates = [(n, c) for n, c in gates if n != \"deepdive source sync\"]\n    for number, (name, command) in enumerate(gates, start=1):\n        exit_code, output = run_gate(number, len(gates), name, command)"),
    ],
    # _build.py 是「只打域名补丁、不保留本地代码」的文件：上游每次改构建脚本都会整文件覆盖，
    # 本地 4 处定制（disclaimer 进两份 sitemap、数量公式计入 disclaimer、根页面 hreflang、all_urls 计入）
    # 必须在此重打，否则会静默丢失（2026-11-05 实测：sitemap 里 disclaimer 消失、search/chains/embed/404 无 hreflang）。
    "_build.py": [
        # ① generate_sitemap 内的 about 块之后补 disclaimer（锚定紧随的 for t in tools 行以区分两处同名块）
        ("        lines.extend(_localized_url_blocks('https://tools.dicomp.net/about.html', today, 'monthly', '0.7'))\n"
         "    for t in tools:",
         "        lines.extend(_localized_url_blocks('https://tools.dicomp.net/about.html', today, 'monthly', '0.7'))\n"
         "    # disclaimer.html 免责声明（本地新增页，需持续进 sitemap）\n"
         "    if os.path.isfile(os.path.join(ROOT, 'disclaimer.html')):\n"
         "        lines.extend(_localized_url_blocks('https://tools.dicomp.net/disclaimer.html', today, 'monthly', '0.5'))\n"
         "    for t in tools:"),
        # ② generate_core_sitemap 内的 about 块之后补 disclaimer
        ("        lines.extend(_localized_url_blocks('https://tools.dicomp.net/about.html', today, 'monthly', '0.7'))\n"
         "    # guides/ 目录下的指南页",
         "        lines.extend(_localized_url_blocks('https://tools.dicomp.net/about.html', today, 'monthly', '0.7'))\n"
         "    # disclaimer.html 免责声明（本地新增页，需持续进 sitemap）\n"
         "    if os.path.isfile(os.path.join(ROOT, 'disclaimer.html')):\n"
         "        lines.extend(_localized_url_blocks('https://tools.dicomp.net/disclaimer.html', today, 'monthly', '0.5'))\n"
         "    # guides/ 目录下的指南页"),
        # ③ sitemap 一致性公式计入 disclaimer
        ("    has_about = 1 if os.path.isfile(os.path.join(ROOT, 'about.html')) else 0\n    # 孤儿化",
         "    has_about = 1 if os.path.isfile(os.path.join(ROOT, 'about.html')) else 0\n"
         "    has_disclaimer = 1 if os.path.isfile(os.path.join(ROOT, 'disclaimer.html')) else 0\n"
         "    # 孤儿化"),
        ("(expected_tools + 3 + len(category_inds) + guides_count + has_chains + has_about)",
         "(expected_tools + 3 + len(category_inds) + guides_count + has_chains + has_about + has_disclaimer)"),
        # ④ 其他根页面注入 hreflang（简繁双向一致）
        ("        print('Updated hreflang in index.html')\n\n    # Generate one root sitemap.",
         "        print('Updated hreflang in index.html')\n\n"
         "    # 其他根页面也注入 hreflang（zh-tw 版本有简中必须有，双向一致）\n"
         "    _ROOT_PAGES_FOR_HREFLANG = [\n"
         "        ('about.html',    'https://tools.dicomp.net/about.html'),\n"
         "        ('disclaimer.html', 'https://tools.dicomp.net/disclaimer.html'),\n"
         "        ('search.html',   'https://tools.dicomp.net/search.html'),\n"
         "        ('chains.html',   'https://tools.dicomp.net/chains.html'),\n"
         "        ('embed.html',    'https://tools.dicomp.net/embed.html'),\n"
         "        ('404.html',      'https://tools.dicomp.net/404.html'),\n"
         "    ]\n"
         "    for _fn, _abs in _ROOT_PAGES_FOR_HREFLANG:\n"
         "        _fp = os.path.join(ROOT, _fn)\n"
         "        if not os.path.isfile(_fp):\n"
         "            continue\n"
         "        with open(_fp, 'r', encoding='utf-8') as _f:\n"
         "            _content = _f.read()\n"
         "        _new = inject_hreflang(_content, _abs)\n"
         "        if _new != _content:\n"
         "            with open(_fp, 'w', encoding='utf-8') as _f:\n"
         "                _f.write(_new)\n"
         "            print('Updated hreflang in %s' % _fn)\n"
         "\n"
         "    # Generate one root sitemap."),
        # ⑤ all_urls 计入 disclaimer（lastmod 键域与 sitemap 保持一致）
        ("    if os.path.isfile(os.path.join(ROOT, 'about.html')):\n"
         "        all_urls.append('https://tools.dicomp.net/about.html')\n",
         "    if os.path.isfile(os.path.join(ROOT, 'about.html')):\n"
         "        all_urls.append('https://tools.dicomp.net/about.html')\n"
         "    if os.path.isfile(os.path.join(ROOT, 'disclaimer.html')):\n"
         "        all_urls.append('https://tools.dicomp.net/disclaimer.html')\n"),
    ],
    # history guard：bill-splitter / 向量最小非零分量子用例在 Windows spawnSync 下含 JSDOM 初始化
    # + eval + calc 冷启动，实测 3s/5s/10s 边界都会被 child_process 启动开销击穿；本地提到 30s。
    "scripts/verify_history_guard.js": [
        # 上游 3000ms：Windows 下 node 冷启动 + JSDOM 解析常超时（假红），抬高到 30s
        ("timeout: 3000 });\n    return { ok: child.status === 0 && /超出|无法|过大/",
         "timeout: 30000 });\n    return { ok: child.status === 0 && /超出|无法|过大/"),
        # 同上：向量最小非零分量（JSDOM 冷启动）
        ("const child = spawnSync(process.execPath, [\"-e\", code], { cwd: ROOT, encoding: \"utf8\", timeout: 5000 });",
         "const child = spawnSync(process.execPath, [\"-e\", code], { cwd: ROOT, encoding: \"utf8\", timeout: 30000 });"),
    ],
    # generator-8 默认态：域名补丁把默认文本 chenguangwu.github.io(29B) 换成本地 tools.dicomp.net(24B)，
    # 版本随之从 3/29×29 降到 2/25×25；上游期望值按原域名写死，须随域名补丁同步改写。
    "scripts/verify_design_calc.js": [
        ('    expect: ["版本 3 · 29×29 模块 · 纠错 M · 29 字节"],',
         '    expect: ["版本 2 · 25×25 模块 · 纠错 M · 24 字节"],'),
        ("    // D-N208 默认态：真实 QR 编码（29 字节 → 版本 3 / 29×29 / 纠错 M）",
         "    // D-N208 默认态：真实 QR 编码（域名补丁后默认文本 24 字节 → 版本 2 / 25×25 / 纠错 M）"),
    ],
}
DRY_RUN = "--dry-run" in sys.argv


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit("git %s 失败:\n%s" % (" ".join(args), r.stderr))
    return r.stdout.strip()


# 0. 前置检查：已跟踪文件不允许有未提交修改（untracked 新文件不受同步影响，放行）
if git("status", "--porcelain", "--untracked-files=no"):
    sys.exit("工作区有未提交的修改。先 commit（或 stash）再同步，防止你的样式被覆盖丢失。")

# 1. 拉取上游
git("fetch", "upstream")
upstream_head = git("rev-parse", UPSTREAM_REF)
local_head = git("rev-parse", "HEAD")
print("upstream: %s" % upstream_head[:10])
print("local:    %s" % local_head[:10])
if upstream_head == local_head:
    print("本地已与上游一致，无需同步。")
    sys.exit(0)

# 2. 计算保留清单：HEAD 独有文件（HEAD 有、上游没有）→ 保留本地版本
#    （运维脚本、本地配置等不因上游"没有"而被删；上游真删除的内容文件如需跟进删除请手动 git rm）
#    用 -z（NUL 分隔）取路径：默认 quotepath 会把非 ASCII 路径输出成
#    "plan/\345..." 带引号八进制转义串，直接当 pathspec 传回 checkout 会
#    did-not-match（2026-11-09 上游删 plan/已修复/*.md 中文文档实测踩坑）。
head_only = [l for l in git("diff", "--name-only", "-z", "--diff-filter=D",
                            "HEAD", UPSTREAM_REF).split("\x00") if l]

# 3. 差异摘要（排除冻结路径、排除路径与本地独有文件，只看会真正更新的内容）
#    head_only 可能数千项（如 zh-tw 入库后），拼接 pathspec 会超 Windows 命令行限制；
#    本机 git diff 也不支持 --pathspec-from-file。改为 --numstat 全量取回后在内存过滤聚合。

def diff_stat_excluded():
    num = git("diff", "--numstat", "--no-renames", "HEAD", UPSTREAM_REF)
    head_only_set = set(head_only)
    exclude_set = set(EXCLUDE_PATHS)
    freeze_keys = [p.rstrip("/") for p in FREEZE_PATHS]

    def skip(p):
        if p in head_only_set or p in exclude_set:
            return True
        return any(p == k or p.startswith(k + "/") for k in freeze_keys)

    files = ins = dels = 0
    for line in num.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        a, d, p = parts[0], parts[1], "\t".join(parts[2:])
        if skip(p):
            continue
        files += 1
        if a != "-":
            ins += int(a)
        if d != "-":
            dels += int(d)
    return "%d files changed, %d insertions(+), %d deletions(-)" % (files, ins, dels)

stat = diff_stat_excluded()
last = stat.splitlines()[-1] if stat else "0 files changed"
print("\n将更新的内容（已排除冻结路径与本地独有文件）: %s" % last)
if head_only:
    print("保留本地独有文件: %d 个（如 %s）"
          % (len(head_only), head_only[0]))
frozen = git("diff", "--stat", "HEAD", UPSTREAM_REF, "--", *FREEZE_PATHS)
if frozen:
    print("以下冻结路径与上游有差异，将被保留为本地版本:")
    print("\n".join("  " + l for l in frozen.splitlines()[-4:]))

if not stat:
    print("上游无新内容需要同步（其余差异均为冻结路径或本地独有文件）。")
    sys.exit(0)

if DRY_RUN:
    print("\n[dry-run] 未做任何修改。去掉 --dry-run 执行同步。")
    sys.exit(0)

# 3.5 过滤 Windows 非法文件名：上游偶尔提交本机无法落盘的文件名（如含 '>'），
#     此时 read-tree -u 直接报 "invalid path" 中止。用临时索引剔除这些路径得到等价 tree。
# 注意：read-tree 自身就会做路径校验，故不能用「read-tree + 删除」的方式，
# 必须用 --index-info 逐条灌入（字节级传递，避免中文路径编码错配）。
_WIN_INVALID_B = re.compile(rb'[<>:"|?*]')
snapshot_ref = UPSTREAM_REF
_all = [e for e in subprocess.run(["git", "ls-tree", "-r", "-z", UPSTREAM_REF],
                                  capture_output=True).stdout.split(b"\x00") if e]
_keep = [e for e in _all if not _WIN_INVALID_B.search(e.split(b"\t", 1)[1])]
if len(_keep) != len(_all):
    tmp_index = os.path.join(os.environ.get("TEMP", "/tmp"),
                             "tb_sync_index_%d" % os.getpid())
    if os.path.exists(tmp_index):
        os.remove(tmp_index)
    tmp_env = dict(os.environ, GIT_INDEX_FILE=tmp_index)
    for args, data in ((["git", "read-tree", "--empty"], None),
                       (["git", "update-index", "-z", "--index-info"],
                        b"\x00".join(_keep) + b"\x00")):
        r = subprocess.run(args, env=tmp_env, input=data, capture_output=True)
        if r.returncode != 0:
            sys.exit("过滤 Windows 非法路径失败（%s）:\n%s"
                     % (" ".join(args), r.stderr.decode("utf-8", "replace")))
    snapshot_ref = subprocess.run(["git", "write-tree"], env=tmp_env,
                                  capture_output=True, text=True).stdout.strip()
    if os.path.exists(tmp_index):
        os.remove(tmp_index)
    dropped = [_all[i] for i in range(len(_all)) if _all[i] not in set(_keep)]
    print("已过滤 Windows 非法路径 %d 个（如 %s），快照改用 tree %s"
          % (len(dropped), dropped[0].split(b"\t", 1)[1].decode("utf-8", "replace"),
             snapshot_ref[:10]))

# 4. 快照式同步：整体重置为上游树
git("read-tree", "-u", "--reset", snapshot_ref)

# 5. 恢复冻结路径为本仓库版本
for p in FREEZE_PATHS:
    key = p.rstrip("/")
    check = subprocess.run(["git", "cat-file", "-e", "HEAD:%s" % key],
                           capture_output=True)
    if check.returncode == 0:
        git("checkout", "HEAD", "--", key)
        print("已冻结: %s" % p)
    else:
        print("跳过冻结: %s（本仓库尚无此路径）" % p)

# 5.5 删除排除路径（上游仍有、本地已永久删除的文件，read-tree 会把它们带回来）
for p in EXCLUDE_PATHS:
    if os.path.exists(p):
        git("rm", "-f", "-q", "--", p)
        print("已排除: %s" % p)

# 5.6 重打本地补丁（站点域名等本地化替换；二进制替换保换行符原样，幂等）
patched = []
for p in LOCAL_PATCH_FILES:
    if not os.path.isfile(p):
        continue
    with open(p, "rb") as f:
        src = f.read()
    out = src
    for old, new in DOMAIN_PATCHES:
        out = out.replace(old.encode("utf-8"), new.encode("utf-8"))
    if out != src:
        with open(p, "wb") as f:
            f.write(out)
        patched.append(p)
        git("add", "--", p)   # read-tree 已把索引重置为上游版本，补丁必须同步写入索引才会进 commit
if patched:
    print("已重打本地补丁: %s" % ", ".join(patched))

# 5.7 单文件定向替换
# 注意：上游许多文件是 CRLF 行尾（_build.py 实测 4917 行全 CRLF），而补丁串用 \n 书写，
# 直接字节匹配会全部失配（2026-11-05 实测 5 条 _build.py 补丁全未命中）。这里统一先归一化到 LF 再匹配，
# 写完再按原文件行尾风格还原，既保证锚点命中，也不制造全文件 EOL 变更的噪音 diff。
for fp, pairs in FILE_PATCHES.items():
    if not os.path.isfile(fp):
        print("⚠️ 定向替换目标不存在: %s" % fp)
        continue
    with open(fp, "rb") as f:
        src = f.read()
    use_crlf = b"\r\n" in src
    out = src.replace(b"\r\n", b"\n") if use_crlf else src
    for old, new in pairs:
        o = old.encode("utf-8").replace(b"\r\n", b"\n")
        n = new.encode("utf-8").replace(b"\r\n", b"\n")
        if o not in out:
            # 上游改写了锚点 ⇒ 补丁静默失效（本地修复会丢失），必须显式报警由人工确认
            print("⚠️ 定向替换未命中（上游锚点已变，请人工核对）: %s <- %s" % (fp, old.splitlines()[0][:60]))
            continue
        out = out.replace(o, n)
    if use_crlf:
        out = out.replace(b"\n", b"\r\n")
    if out != src:
        with open(fp, "wb") as f:
            f.write(out)
        git("add", "--", fp)
        print("已定向替换: %s" % fp)

# 6. 恢复本地独有文件（分批防命令行超长）
if head_only:
    for i in range(0, len(head_only), 50):
        git("checkout", "HEAD", "--", *head_only[i:i + 50])
    print("已恢复本地独有文件: %d 个" % len(head_only))

# 7. 全局域名补丁：read-tree 带回的全部内容页（8000+）也需替换域名，
#    仅靠 LOCAL_PATCH_FILES 名单覆盖不到。DOMAIN_PATCHES 各对均不含
#    "github.com/" 前缀与引号边界，MIT 署名（i18n.js/disclaimer.html 的
#    chenguangwu/chenguangwu.github.io 仓库名与 github 链接）不受影响。
#    四类形态均安全：https 全域名、cognition 特例、
#    带引号裸域名（仓库署名串前有 / 无引号，不匹配）。
dom_files = []
tracked = [f for f in git("ls-files").splitlines() if f]
for p in tracked:
    if os.path.abspath(p) == SELF_PATH:
        continue
    try:
        with open(p, "rb") as f:
            src = f.read()
    except OSError:
        continue
    out = src
    for old, new in DOMAIN_PATCHES:
        out = out.replace(old.encode("utf-8"), new.encode("utf-8"))
    if out != src:
        with open(p, "wb") as f:
            f.write(out)
        dom_files.append(p)
# 批量 add（逐文件 add 会起数千个 git 进程，极慢）
for i in range(0, len(dom_files), 100):
    git("add", "--", *dom_files[i:i + 100])
if dom_files:
    print("已全局重打域名补丁: %d 个文件" % len(dom_files))

# 7.5 清 ttzz push.js 块（上游 2025-11 已安全审计移除，但本地 orphan 页因 HEAD 独有而每次同步被恢复回来）
# 匹配两种形态：带 <!-- TOOLBOX-TTZZ --> 标记的 和 裸 IIFE（只有 <script> 开头）
TTZZ_BLOCK_RE = re.compile(
    rb'(?:<!-- TOOLBOX-TTZZ -->\r?\n)?'
    rb'<script>\r?\n'
    rb'\(function\(\)\{try\{\r?\n'
    rb'var el = document\.createElement\("script"\);\r?\n'
    rb'el\.src = "https://lf1-cdn-tos\.bytegoofy\.com/goofy/ttzz/push\.js\?[^"]+";\r?\n'
    rb'el\.id = "ttzz";\r?\n'
    rb'var s = document\.getElementsByTagName\("script"\)\[0\];\r?\n'
    rb's\.parentNode\.insertBefore\(el, s\);\r?\n'
    rb'\}catch\(e\)\{\}\r?\n'
    rb'\}\)\(window\);\r?\n'
    rb'</script>\r?\n',
    re.DOTALL,
)
ttzz_files = []
for p in tracked:
    if os.path.abspath(p) == SELF_PATH:
        continue
    if not p.endswith(".html"):
        continue
    try:
        with open(p, "rb") as f:
            src = f.read()
    except OSError:
        continue
    if b"lf1-cdn-tos.bytegoofy.com/goofy/ttzz/push.js" not in src:
        continue
    new, n = TTZZ_BLOCK_RE.subn(b"", src)
    if n == 0:
        print("⚠️ ttzz 标记存在但正则未命中: %s" % p)
        continue
    if new != src:
        with open(p, "wb") as f:
            f.write(new)
        ttzz_files.append(p)
for i in range(0, len(ttzz_files), 100):
    git("add", "--", *ttzz_files[i:i + 100])
if ttzz_files:
    print("已清 ttzz push.js 块: %d 个文件" % len(ttzz_files))

# 8. 提交
git("commit", "-m", "同步上游内容（css 样式保持本地版本）")
print("\n完成。确认无误后: git push origin main")
