import sys, difflib, re
a = open(sys.argv[1], encoding='utf-8').read().splitlines()
b = open(sys.argv[2], encoding='utf-8').read().splitlines()
# diff by line; for changed lines, show word diff
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        continue
    print(f"=== {tag} v9[{i1+1}:{i2}] v9-2[{j1+1}:{j2}]")
    A = ' '.join(a[i1:i2]); B = ' '.join(b[j1:j2])
    wa = re.split(r'(\s+)', A); wb = re.split(r'(\s+)', B)
    sm2 = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    out = []
    for t, x1, x2, y1, y2 in sm2.get_opcodes():
        if t == 'equal':
            seg = ''.join(wa[x1:x2])
            if len(seg) > 160: seg = seg[:60] + ' […] ' + seg[-60:]
            out.append(seg)
        else:
            if x2 > x1: out.append('[-' + ''.join(wa[x1:x2]) + '-]')
            if y2 > y1: out.append('{+' + ''.join(wb[y1:y2]) + '+}')
    print(''.join(out)); print()
