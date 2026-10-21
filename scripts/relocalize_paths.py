#!/usr/bin/env python3
"""构建后处理：站点根绝对引用 → 相对引用，使产物可部署在任意子路径。

处理范围（全部幂等，可重复执行）：
  1. 全站 HTML（含 zh-tw/guides/ui/tools）：非 <script>/<style> 块内的
     src="/xxx"、href="/xxx"、content="/xxx" 按页面目录深度改写为 ../ 相对引用。
     <script>/<style> 块（含 JSON-LD）整体跳过，避免误伤 JS 字符串与 SEO 结构化数据。
  2. manifest.json：start_url / scope / icons 改为相对（基准 = manifest 所在目录 = 挂载根）。
  3. sw.js：PRECACHE 与 caches.match / fetch 的站点路径改为 './' 相对（基准 = SW 脚本位置）。

配合 js 层 TB_ROOT（从 document.currentScript.src 回推站点根）实现任意路径部署。
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 仅处理属性值以单根斜杠开头的引用（排除协议相对 //、锚点 #、data: 等）
ATTR_RE = re.compile(r'((?:src|href|content)\s*=\s*")/(?!/)([^"]*)(")')
# 外部脚本标签（含 src 属性）：开标签属于"块"，须在块保护前单独先行处理其 src
EXT_SCRIPT_RE = re.compile(r'(<script\b[^>]*?\bsrc\s*=\s*")/(?!/)([^"]*)(")')
# 内联 <script>（无 src 属性，含 JSON-LD）与 <style> 块整体保护。注意捕获组必须有：
# re.split 只有在模式含捕获组时才会把分隔符（块内容）保留在结果里。
BLOCK_RE = re.compile(r'(<script\b(?![^>]*\bsrc=)[^>]*>.*?</script\s*>|<style\b[^>]*>.*?</style\s*>)', re.S | re.I)

EXCLUDE_DIRS = {'.git', 'node_modules', '.workbuddy', 'scripts', 'backup'}


def html_prefix(rel_parts):
    depth = len(rel_parts) - 1
    return './' if depth == 0 else '../' * depth


def rel_index(pre_parts):
    """纯根引用（"/" 或 "/./"）→ 显式 index.html：审计器不认裸目录引用（./ 或 ../）。"""
    depth = len(pre_parts)
    return './index.html' if depth == 0 else '../' * (depth - 1) + 'index.html'


def fix_html(path):
    pre = html_prefix(path.relative_to(ROOT).parts)
    rel = path.relative_to(ROOT).parts[:-1]

    def attr_sub(m):
        # 纯根引用 → 显式 index.html，其余 → 深度相对前缀
        if m.group(2) in ('', './', '.'):
            return m.group(1) + rel_index(rel) + m.group(3)
        return m.group(1) + pre + m.group(2) + m.group(3)

    orig = path.read_text(encoding='utf-8')
    if not ATTR_RE.search(orig) and not EXT_SCRIPT_RE.search(orig) and not BLOCK_RE.search(orig):
        return False
    # 第一遍：外部 <script src> 标签（无内容，src 即资源引用）先行相对化
    text = EXT_SCRIPT_RE.sub(lambda m: m.group(1) + pre + m.group(2) + m.group(3), orig)
    # 第二遍：内联 script/style 块保护下的普通属性相对化
    segs = BLOCK_RE.split(text)
    out = []
    for i, seg in enumerate(segs):
        if i % 2 == 1:  # 内联块保持原样
            out.append(seg)
        else:
            out.append(ATTR_RE.sub(attr_sub, seg))
    new = ''.join(out)
    if new != orig:  # 与磁盘原文比较（两遍 sub 的变更都要落盘）
        path.write_text(new, encoding='utf-8')
        return True
    return False


def fix_manifest(path):
    obj = json.loads(path.read_text(encoding='utf-8'))
    changed = False
    for key in ('start_url', 'scope'):
        v = obj.get(key, '')
        if isinstance(v, str) and v.startswith('/'):
            obj[key] = '.' + v
            changed = True
    for icon in obj.get('icons', []):
        src = icon.get('src', '')
        if src.startswith('/'):
            icon['src'] = src.lstrip('/')
            changed = True
    if changed:
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return changed


# sw.js 内被引号包住的站点根路径统一改 './' 前缀（PRECACHE、caches.match、fetch）
SW_PATH_RE = re.compile(r'(["\'])/(?!/)([A-Za-z0-9_\-./])')


def fix_sw(path):
    text = path.read_text(encoding='utf-8')
    new = SW_PATH_RE.sub(lambda m: m.group(1) + './' + m.group(2), text)
    if new != text:
        path.write_text(new, encoding='utf-8')
        return True
    return False


def main():
    n_html = n_manifest = n_sw = 0
    for path in ROOT.rglob('*.html'):
        if EXCLUDE_DIRS & set(path.relative_to(ROOT).parts[:-1]):
            continue
        if fix_html(path):
            n_html += 1
    manifest = ROOT / 'manifest.json'
    if manifest.exists() and fix_manifest(manifest):
        n_manifest += 1
    sw = ROOT / 'sw.js'
    if sw.exists() and fix_sw(sw):
        n_sw += 1
    print('relocalize: html={} manifest={} sw={}'.format(n_html, n_manifest, n_sw))


if __name__ == '__main__':
    sys.exit(main())
