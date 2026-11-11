with open("js/common.js", "r", encoding="utf-8") as f:
    s = f.read()
old = """function escHtml(s){
  var d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}"""
new = """function escHtml(s){
  // 同时转义引号：escHtml 常被用于 value="..." 等属性上下文，仅转义 &<> 会造成属性逃逸
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}"""
assert old in s, "escHtml anchor missing"
s = s.replace(old, new, 1)
with open("js/common.js", "w", encoding="utf-8") as f:
    f.write(s)
print("escHtml updated")
