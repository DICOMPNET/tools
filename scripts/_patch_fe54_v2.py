import re
with open("scripts/_verify_fun_batch_fe_n54.mjs", "r", encoding="utf-8") as f:
    s = f.read()
# 把 wait(50)/wait(1250) 改成轮询 records.length
old = """await wait(50);
doc.getElementById('items').value = '';
w.start();
check('空池不产生历史', records.length === 0);
doc.getElementById('items').value = '错误';
doc.getElementById('seed').value = 'fixed';
doc.getElementById('unique').checked = false;
w.start();
check('抽取中不写入历史', records.length === 0);
await wait(1250);
check('真实结果及通过状态入历史', records.length === 1 && records[0].d['结果'] === '错误' && records[0].d.__tbScore === 1);
w.start();
await wait(1250);
check('重复抽取相同选项也各留一条', records.length === 2 && records.every(r => r.d['结果'] === '错误' && r.d.__tbScore === 1));
doc.getElementById('items').value = '请输入文本';
w.start();
await wait(1250);
check('提示语样式的合法选项也入历史', records.length === 3 && records[2].d['结果'] === '请输入文本');
restore(records[0].d);
await wait(1250);
check('恢复历史不新增记录', records.length === 3);
w.__random_pickerExport();
check('导出只包含真实结果且不含占位', exports.length === 1 && exports[0].length === 3 && exports[0].every(row => (row.includes('错误') || row.includes('请输入文本')) && row.includes('通过') && !row.some(v => String(v).includes('抽取中'))));
doc.getElementById('unique').checked = true;
w.start();
await wait(1250);
const before = records.length;
w.start();"""
new = """// 轮询 records 长度：页面 setInterval 依赖 JSDOM 定时器调度，wait 固定时长不可靠。
async function waitFor(n, timeout = 5000) {
  const t0 = Date.now();
  while (records.length < n && Date.now() - t0 < timeout) await wait(50);
}
await wait(50);
doc.getElementById('items').value = '';
w.start();
check('空池不产生历史', records.length === 0);
doc.getElementById('items').value = '错误';
doc.getElementById('seed').value = 'fixed';
doc.getElementById('unique').checked = false;
w.start();
check('抽取中不写入历史', records.length === 0);
await waitFor(1);
check('真实结果及通过状态入历史', records.length === 1 && records[0].d['结果'] === '错误' && records[0].d.__tbScore === 1);
w.start();
await waitFor(2);
check('重复抽取相同选项也各留一条', records.length === 2 && records.every(r => r.d['结果'] === '错误' && r.d.__tbScore === 1));
doc.getElementById('items').value = '请输入文本';
w.start();
await waitFor(3);
check('提示语样式的合法选项也入历史', records.length === 3 && records[2].d['结果'] === '请输入文本');
restore(records[0].d);
await wait(1500);
check('恢复历史不新增记录', records.length === 3);
w.__random_pickerExport();
check('导出只包含真实结果且不含占位', exports.length === 1 && exports[0].length === 3 && exports[0].every(row => (row.includes('错误') || row.includes('请输入文本')) && row.includes('通过') && !row.some(v => String(v).includes('抽取中'))));
doc.getElementById('unique').checked = true;
w.start();
await waitFor(4);
const before = records.length;
w.start();"""
assert old in s
s = s.replace(old, new, 1)
with open("scripts/_verify_fun_batch_fe_n54.mjs", "w", encoding="utf-8") as f:
    f.write(s)
print("patched with waitFor")
