import re, json

s = open('index.html', encoding='utf-8').read()

print('=== 上限类常量 ===')
for name in ['MAX_LV', 'GUEST_MAX_LV', 'GRID_SIZE', 'STOCK_CAP', 'RARE_CAP', 'PROD_SEC',
             'MERGE_MAX', 'VIP_RARE_CHANCE', 'RARE_PROD_MULT']:
    m = re.search(name + r'\s*=\s*([^;,]+)', s)
    print(' ', name, '=', (m.group(1) if m else '?')[:60])

print('=== 表格类 ===')
for name in ['MERGE_UP', 'GOLD_BUY', 'SHOPS', 'PRODUCTS', 'PET_STAGES', 'PET_NEED', 'EGGS', 'HIDDEN']:
    m = re.search(r'const ' + name + r'\s*=\s*', s)
    if not m:
        print(' ', name, 'NOT FOUND'); continue
    seg = s[m.end():m.end() + 700]
    print(' ', name, ': 条目数约', seg[:seg.find('\n];') if '\n];' in seg else 200].count('{'),
          '| 片段:', seg[:90].replace('\n', ' '))

print('=== 成长公式 ===')
for pat in [r'const upCost\s*=[^;]+', r'const genCost\s*=[^;]+', r'const speed\s*=[^;]+',
            r'const mult\s*=[^;]+', r'const energyRate\s*=[^;]+', r'const prodInterval\s*=[^;]+']:
    m = re.search(pat, s)
    print(' ', m.group(0)[:120] if m else 'not found')

i = s.find('const openCostCoins')
print(' openCostCoins:', s[i:i + 180].replace('\n', ' ')[:180])

print('=== fmt 数字格式化上限 ===')
i = s.find('function fmt')
print(' ', s[i:i + 300].replace('\n', ' '))

print('=== 已有但未被使用的累计计数器 ===')
for k in ['totalMerged', 'genCount', 'ordersDone', 'signClicks', 'fed', 'bond', 'lastDaily']:
    print(' ', k, '=> 出现', s.count(k), '次')

print('=== state 字段 ===')
i = s.find('const defaultState=')
seg = s[i:i + 1400]
keys = re.findall(r'^\s{2}([A-Za-z_]+):', seg, re.M)
print(' ', ', '.join(keys))
