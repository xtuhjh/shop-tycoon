const SPR_WAITER=[[
'.....wwww.....',
'....wwwwww....',
'...wwwwwwww...',
'..wwwwwwwwww..',
'...kkkkkkkk...',
'...khhhhhhk...',
'..khsssssshk..',
'..khsksskshk..',
'..khssssssshk.',
'...ksrrrrsk...',
'...kcccccck...',
'..kcccccccck..',
'.kcaaaaaaaack.',
'.kcawwwwwwack.',
'..kppppppppk..',
'..kppp..pppk..',
'..kppp..pppk..',
'..kkk....kkk..',
],[
'.....wwww.....',
'....wwwwww....',
'...wwwwwwww...',
'..wwwwwwwwww..',
'...kkkkkkkk...',
'...khhhhhhk...',
'..khsssssshk..',
'..khsksskshk..',
'..khssssssshk.',
'...ksrrrrsk...',
'...kcccccck...',
'..kcccccccck..',
'.kcaaaaaaaack.',
'.kcawwwwwwack.',
'..kppppppppk..',
'.kppp....pppk.',
'.kkk......kkk.',
'..............',
]];
const SPR_DOG=[[
'..kk........kk..',
'.khhk......khhk.',
'.khhhkkkkkkhhhk.',
'.khsskhhhhksshk.',
'..kssssssssssk..',
'..kssskkkksssk..',
'...kssssssssk...',
'..khhhhhhhhhhk.k',
'.khhhhhhhhhhhhkk',
'.khhhhhhhhhhhhk.',
'..kkhkkkkkkhkk..',
'..kk......kk....',
],[
'..kk........kk..',
'.khhk......khhk.',
'.khhhkkkkkkhhhk.',
'.khsskhhhhksshk.',
'..kssssssssssk..',
'..kssskkkksssk..',
'...kssssssssk...',
'..khhhhhhhhhhk.k',
'.khhhhhhhhhhhhkk',
'.khhhhhhhhhhhhk.',
'..kkhkkkkkkhkk..',
'.kk..........kk.',
]];
const SPR_GUEST=[[
'....hhhhhh....',
'...hhhhhhhh...',
'..hhhhhhhhhh..',
'..hhhhhhhhhh..',
'..khsssssshk..',
'..kskssssksk..',
'..kssssssssk..',
'..ksrrrrrrsk..',
'...kssssssk...',
'..kCCCCCCCCk..',
'.kcccccccccck.',
'.kcccccccccck.',
'.kcccccccccck.',
'..kppppppppk..',
'..kppp..pppk..',
'..kppp..pppk..',
'..kkk....kkk..',
],[
'....hhhhhh....',
'...hhhhhhhh...',
'..hhhhhhhhhh..',
'..hhhhhhhhhh..',
'..khsssssshk..',
'..kskssssksk..',
'..kssssssssk..',
'..ksrrrrrrsk..',
'...kssssssk...',
'..kCCCCCCCCk..',
'.kcccccccccck.',
'.kcccccccccck.',
'.kcccccccccck.',
'..kppppppppk..',
'.kppp....pppk.',
'.kkk......kkk.',
'..............',
]];
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
