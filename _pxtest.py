s = open('index.html', encoding='utf-8').read()

def grab(name):
    i = s.find('const ' + name + '=[')
    j = s.find(']];', i)
    return s[i:j + 3]

frag = '\n'.join([grab('SPR_WAITER'), grab('SPR_DOG'), grab('SPR_GUEST')])

js = frag + r'''
function check(name, frames, expectW){
  console.log('--- ' + name + ' ---');
  frames.forEach((rows, fi) => {
    const widths = [...new Set(rows.map(r => r.length))];
    const bad = rows.filter(r => r.length !== expectW).length;
    const chars = new Set(rows.join('').split(''));
    const unknown = [...chars].filter(c => !'.kshwcCpayr'.includes(c));
    console.log('  frame' + fi + ': 行数=' + rows.length + ' 宽度=' + JSON.stringify(widths) +
                ' 行宽统一=' + (widths.length === 1 ? '✓' : '✗') +
                (bad ? '  ✗有' + bad + '行不等于' + expectW : ''));
    if (unknown.length) console.log('    ✗ 未知颜色字符:', unknown.join(','));
  });
  const n = frames[0].length;
  console.log('  两帧行数一致:', frames[0].length === frames[1].length ? '✓' : '✗');
}
check('服务员', SPR_WAITER, 14);
check('狗子', SPR_DOG, 16);
check('客人', SPR_GUEST, 14);
'''

open('_px_test.js', 'w', encoding='utf-8').write(js)
print('written')
