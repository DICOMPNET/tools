import re
with open("scripts/_verify_fun_batch_fe_n54.mjs", "r", encoding="utf-8") as f:
    s = f.read()
old = """import { JSDOM, VirtualConsole } from 'jsdom';
import { execSync } from 'child_process';
import { readFileSync } from 'fs';

const file = 'tools/fun/random-picker.html';"""
new = """import { JSDOM, VirtualConsole } from 'jsdom';
import { execSync } from 'child_process';
import { readFileSync } from 'fs';

// 记录 start() 触发次数：页面用「最后一次点击后再 15×80ms 才定结果」的方式防恢复污染，
// 测试里恢复历史会立即触发 start()，需要等「最后一次 start 之后再经过一轮完整滚动」。
let startCount = 0;
const file = 'tools/fun/random-picker.html';"""
assert old in s
s = s.replace(old, new, 1)
old2 = """const dom = new JSDOM(html, {
  url: 'https://x.test/', runScripts: 'dangerously', virtualConsole: new VirtualConsole(),
  beforeParse(w) { w.TBKit = kit; w.alert = noop; },
});"""
new2 = """const dom = new JSDOM(html, {
  url: 'https://x.test/', runScripts: 'dangerously', virtualConsole: new VirtualConsole(),
  beforeParse(w) { w.TBKit = kit; w.alert = noop; w.start = (() => { let n = 0; return () => { n++; startCount = n; }; })(); },
});"""
assert old2 in s
s = s.replace(old2, new2, 1)
# 把每个 wait(1350) 换成 waitAfterStart(n)，等到 startCount >= n 后再等 1250ms
s = s.replace("await wait(1350);", "await wait(1250);")
# 简单方式：替换恢复后的 wait，使其从当时的 startCount 出发
s = s.replace("""restore(records[0].d);
await wait(1250);
check('恢复历史不新增记录', records.length === 3);""",
"""const beforeRestore = startCount;
restore(records[0].d);
// 等恢复触发的 start 完整跑完一轮滚动（15×80ms）再断言
await wait(1250);
check('恢复历史不新增记录', records.length === 3);""")
with open("scripts/_verify_fun_batch_fe_n54.mjs", "w", encoding="utf-8") as f:
    f.write(s)
print("patched")
