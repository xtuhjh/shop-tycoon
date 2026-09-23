import json
import time
import urllib.request

time.sleep(75)
d = json.loads(urllib.request.urlopen('https://api.github.com/repos/xtuhjh/shop-tycoon/pages/builds/latest').read().decode())
print('build status:', d.get('status'), '| err:', (d.get('error') or {}).get('message'), '| commit:', str(d.get('commit'))[:8])

live = urllib.request.urlopen('https://xtuhjh.github.io/shop-tycoon/').read().decode('utf-8')
local = open('index.html', encoding='utf-8').read()
print('content_equal', live == local, '| live_chars', len(live))
for k in ['const ACHS', 'settleOffline', 'fillShelf', 'fitShelf', 'achBonus', 'shelfPointerMove']:
    print(' ', k, '=>', live.count(k))
