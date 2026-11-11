import re
with open("scripts/run_gates.py", "r", encoding="utf-8") as f:
    s = f.read()
# GATES 项里的字符串 "python3" 已误替换成 "sys.executable"，回退为 sys.executable 变量（无引号）
n = s.count('"sys.executable"')
s = s.replace('"sys.executable"', 'sys.executable')
with open("scripts/run_gates.py", "w", encoding="utf-8") as f:
    f.write(s)
print(f"fixed {n} quoted sys.executable occurrences")
# 验证
import importlib.util
spec = importlib.util.spec_from_file_location("rg", "scripts/run_gates.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
print("first 3 gates:", [(n, c[0]) for n, c in m.GATES[:3]])
