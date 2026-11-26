#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_absolute_asset_paths.py — 子路径部署适配：把写死的根绝对路径静态资源引用改为相对路径。

背景：正式域名 tools.dicomp.net 站点挂在根路径（/），预览站 dicompnet.github.io/tools/
挂在子路径。HTML 里写死的 /css /js /vendor /favicon /logo /apple-touch-icon 等绝对路径
在预览站会丢失 /tools 前缀 → 404。改为相对路径后，两种部署都正确。

规则（幂等）：
- 只替换资源前缀（href/src="/(css|js|vendor|favicon|logo|apple-touch-icon|manifest)..."）
- 按文件相对项目根的目录深度，自动补相应数量的 ../（根级页补 0，子目录补 ../）
- 不动站内导航链接（/tools /guides /it 等），不动 data-page-node-id 等属性顺序
- 重复运行安全：已是相对路径的不会再加前缀

用法：
    python3 scripts/fix_absolute_asset_paths.py            # 干跑（只统计）
    python3 scripts/fix_absolute_asset_paths.py --apply    # 实际改写
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 资源前缀（绝对路径需改相对）。注意顺序：长的在前。
ASSET_PREFIXES = [
    "vendor/fonts/", "vendor/",
    "css/", "js/", "json/",
    "favicon.svg", "favicon.ico",
    "logo.svg", "logo-32.png", "logo-192.png", "logo-512.png",
    "apple-touch-icon.png",
    "manifest.json",
]

# 匹配 (href|src)="/<前缀> 这种形态（引号必须紧跟 /）
RE_SRC = re.compile(r'((?:href|src)\s*=\s*")/(' + "|".join(re.escape(p) for p in ASSET_PREFIXES) + r')')

def depth_prefix(relpath):
    """根据文件相对项目根的目录深度，返回需要回退到站点根的相对前缀（不含结尾 /）。"""
    d = os.path.dirname(relpath.replace("\\", "/"))
    if not d or d == ".":
        return ""  # 根级页，相对路径无前缀
    segs = d.split("/")
    return "../" * len(segs)  # guides/ → ../, zh-tw/ → ../, zh-tw/guides/ → ../../

def process_file(relpath, apply):
    abspath = os.path.join(ROOT, relpath.replace("/", os.sep))
    if not os.path.isfile(abspath):
        return 0
    with open(abspath, encoding="utf-8") as f:
        text = f.read()
    prefix = depth_prefix(relpath)

    count = [0]
    def repl(m):
        count[0] += 1
        return m.group(1) + prefix + m.group(2)

    new = RE_SRC.sub(repl, text)
    if count[0] == 0:
        return 0
    if apply:
        with open(abspath, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
    return count[0]

def collect_files():
    files = []
    # 根级 html
    for f in glob.glob(os.path.join(ROOT, "*.html")):
        files.append(os.path.relpath(f, ROOT).replace("\\", "/"))
    # guides 与 zh-tw/guides
    for pat in ("guides/*.html", "zh-tw/*.html", "zh-tw/guides/*.html"):
        files += [os.path.relpath(p, ROOT).replace("\\", "/") for p in glob.glob(os.path.join(ROOT, pat))]
    # 工具页（tools/<industry>/*.html 与 zh-tw/tools/<industry>/*.html）
    for pat in ("tools/*/*.html", "zh-tw/tools/*/*.html"):
        files += [os.path.relpath(p, ROOT).replace("\\", "/") for p in glob.glob(os.path.join(ROOT, pat))]
    return files

def main():
    apply = "--apply" in sys.argv
    files = collect_files()
    total_files = 0
    total_hits = 0
    for rel in sorted(set(files)):
        n = process_file(rel, apply)
        if n:
            total_files += 1
            total_hits += n
    mode = "APPLIED" if apply else "DRY-RUN"
    print(f"[{mode}] 改写 {total_files} 个文件，共 {total_hits} 处资源引用")

if __name__ == "__main__":
    main()
