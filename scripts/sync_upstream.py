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
    "scripts/run_gates.py",        # Windows 适配：python3 → sys.executable
    "scripts/gen_opencc_locales.mjs",  # ROOT_PAGES 增加 disclaimer.html（zh-tw 生成清单）
    "scripts/check_clarity_refs.py",   # 统计守卫豁免 TOOLBOX-REDIRECT 存根页
    ".gitignore",                  # 本地忽略规则（tools.zip >100MB 不可入库，上游版本无此行会致误提交）
]
EXCLUDE_PATHS = [                  # 排除路径：上游仍有、但本地已永久删除的文件（read-tree 后强制删除，防每轮复活）
    "js/ad_metrics.js",            # 广告埋点（推广信息，已清理）
    "json/analytics_51la_overview.json",  # 51.la 统计数据缓存（非百度统计，已清理）
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
    ("https://tools.dicomp.net", "https://tools.dicomp.net"),
    ("tools.dicomp.net/tools/cognition/", "tools.dicomp.net/tools/cognition/"),
    # 裸域名常量（提交脚本 HOST/SITE_HINT、自查脚本 SELF_HOSTS 等，带引号形态防误伤署名文案）
    ("'tools.dicomp.net'", "'tools.dicomp.net'"),
    ("\"chenguangwu.github.io\"", "\"tools.dicomp.net\""),
]
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
head_only = [l for l in git("diff", "--name-only", "--diff-filter=D",
                            "HEAD", UPSTREAM_REF).splitlines() if l]

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

# 4. 快照式同步：整体重置为上游树
git("read-tree", "-u", "--reset", UPSTREAM_REF)

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

# 6. 恢复本地独有文件（分批防命令行超长）
if head_only:
    for i in range(0, len(head_only), 50):
        git("checkout", "HEAD", "--", *head_only[i:i + 50])
    print("已恢复本地独有文件: %d 个" % len(head_only))

# 7. 全局域名补丁：read-tree 带回的全部内容页（8000+）也需替换域名，
#    仅靠 LOCAL_PATCH_FILES 名单覆盖不到。DOMAIN_PATCHES 各对均不含
#    "github.com/" 前缀与引号边界，MIT 署名（i18n.js/disclaimer.html 的
#    chenguangwu/chenguangwu.github.io 仓库名与 github 链接）不受影响。
#    四类形态均安全：https://tools.dicomp.net、cognition 特例、
#    带引号裸域名（仓库署名串前有 / 无引号，不匹配）。
dom_files = []
tracked = [f for f in git("ls-files").splitlines() if f]
for p in tracked:
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

# 8. 提交
git("commit", "-m", "同步上游内容（css 样式保持本地版本）")
print("\n完成。确认无误后: git push origin main")
