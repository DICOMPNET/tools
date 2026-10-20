#!/usr/bin/env python3
"""快照式同步上游内容，冻结本地样式。

用法：
    python3 scripts/sync_upstream.py --dry-run   # 只看差异，不改任何东西
    python3 scripts/sync_upstream.py             # 执行同步并 commit

机制：工作区整体重置为上游树（收上游的修改与新增），
再把 FREEZE_PATHS 中的路径恢复为本仓库自己的版本，最后一次性 commit。
HEAD 独有文件（本地运维脚本、配置等）自动保留，不视为"上游删除"。
不依赖共同 git 历史，冻结语义永久有效。

前提：运行前工作区必须干净（所有本地改动已 commit），
否则冻结路径上的未提交改动会被覆盖丢失。
"""
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
    "scripts/run_gates.py",        # Windows 适配：python3 → sys.executable
    "scripts/gen_opencc_locales.mjs",  # ROOT_PAGES 增加 disclaimer.html（zh-tw 生成清单）
    "scripts/check_clarity_refs.py",   # 统计守卫豁免 TOOLBOX-REDIRECT 存根页
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

# 3. 差异摘要（排除冻结路径与本地独有文件，只看会真正更新的内容）
pathspec = (["."] + [":(exclude)%s" % p for p in FREEZE_PATHS]
            + [":(exclude)%s" % f for f in head_only])
stat = git("diff", "--stat", "HEAD", UPSTREAM_REF, "--", *pathspec)
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

# 6. 恢复本地独有文件（分批防命令行超长）
if head_only:
    for i in range(0, len(head_only), 50):
        git("checkout", "HEAD", "--", *head_only[i:i + 50])
    print("已恢复本地独有文件: %d 个" % len(head_only))

# 7. 提交
git("commit", "-m", "同步上游内容（css 样式保持本地版本）")
print("\n完成。确认无误后: git push origin main")
