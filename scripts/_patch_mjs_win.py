import os
files = [
    '_verify_history_restore_recompute.mjs', '_verify_guard_clear_table.mjs',
    '_verify_false_negative_guard.mjs', '_verify_stale_result.mjs',
    '_verify_empty_input_conclusion.mjs', '_verify_eat26_risk_direction.mjs',
    '_verify_berg_partial_guard.mjs', '_verify_asrs_star_dynamic.mjs',
]
for fn in files:
    p = os.path.join('scripts', fn)
    with open(p, 'r', encoding='utf-8') as f:
        s = f.read()
    n = s.count('new URL(import.meta.url).pathname')
    s = s.replace('new URL(import.meta.url).pathname', 'new URL(import.meta.url).pathname.replace(/^\\/(?=[A-Za-z]:)/, "")')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'{fn}: {n} patched')
