#!/usr/bin/env python3
"""快照式同步上游内容，冻结本地样式。

用法：
    python3 scripts/sync_upstream.py --dry-run   # 只看差异，不改任何东西
    python3 scripts/sync_upstream.py             # 执行同步并 commit

机制：工作区整体重置为上游树（含上游的删除/新增/修改），
再把 FREEZE_PATHS 中的路径恢复为本仓库自己的版本，最后一次性 commit。
不依赖共同 git 历史，冻结语义永久有效。

前提：运行前工作区必须干净（所有本地改动已 commit），
否则冻结路径上的未提交改动会被覆盖丢失。
"""
import subprocess
import sys

UPSTREAM_REF = "upstream/master"   # 上游主分支（上游仓库主分支叫 master）
FREEZE_PATHS = ["css/"]            # 冻结路径：永远保持本仓库自己的版本（可按需追加，如 "js/"）
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

# 2. 差异摘要（排除冻结路径，只看会真正更新的内容）
pathspec = ["."] + [":(exclude)%s" % p for p in FREEZE_PATHS]
stat = git("diff", "--stat", "HEAD", UPSTREAM_REF, "--", *pathspec)
last = stat.splitlines()[-1] if stat else "0 files changed"
print("\n将更新的内容（已排除冻结路径）: %s" % last)
frozen = git("diff", "--stat", "HEAD", UPSTREAM_REF, "--", *FREEZE_PATHS)
if frozen:
    print("以下冻结路径与上游有差异，将被保留为本地版本:")
    print("\n".join("  " + l for l in frozen.splitlines()[-4:]))

if DRY_RUN:
    print("\n[dry-run] 未做任何修改。去掉 --dry-run 执行同步。")
    sys.exit(0)

# 3. 快照式同步：整体重置为上游树
git("read-tree", "-u", "--reset", UPSTREAM_REF)

# 4. 恢复冻结路径为本仓库版本
for p in FREEZE_PATHS:
    key = p.rstrip("/")
    check = subprocess.run(["git", "cat-file", "-e", "HEAD:%s" % key],
                           capture_output=True)
    if check.returncode == 0:
        git("checkout", "HEAD", "--", key)
        print("已冻结: %s" % p)
    else:
        print("跳过冻结: %s（本仓库尚无此路径）" % p)

# 5. 提交
git("commit", "-m", "同步上游内容（css 样式保持本地版本）")
print("\n完成。确认无误后: git push origin main")
