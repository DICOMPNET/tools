with open("scripts/_verify_fun_batch_fe_n54.mjs", "r", encoding="utf-8") as f:
    s = f.read()
# 撤掉 start 覆盖（那会替换页面真实 start，导致什么都不发生）
s = s.replace("""const dom = new JSDOM(html, {
  url: 'https://x.test/', runScripts: 'dangerously', virtualConsole: new VirtualConsole(),
  beforeParse(w) { w.TBKit = kit; w.alert = noop; w.start = (() => { let n = 0; return () => { n++; startCount = n; }; })(); },
});""", """const dom = new JSDOM(html, {
  url: 'https://x.test/', runScripts: 'dangerously', virtualConsole: new VirtualConsole(),
  beforeParse(w) { w.TBKit = kit; w.alert = noop; },
});""")
s = s.replace("""// 记录 start() 触发次数：页面用「最后一次点击后再 15×80ms 才定结果」的方式防恢复污染，
// 测试里恢复历史会立即触发 start()，需要等「最后一次 start 之后再经过一轮完整滚动」。
let startCount = 0;
""", "")
s = s.replace("""const beforeRestore = startCount;
restore(records[0].d);
// 等恢复触发的 start 完整跑完一轮滚动（15×80ms）再断言
await wait(1250);
check('恢复历史不新增记录', records.length === 3);""",
"""restore(records[0].d);
await wait(1250);
check('恢复历史不新增记录', records.length === 3);""")
with open("scripts/_verify_fun_batch_fe_n54.mjs", "w", encoding="utf-8") as f:
    f.write(s)
print("reverted")
