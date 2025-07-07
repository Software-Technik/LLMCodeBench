import sys

p1 = p2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        in_hyper = False
        prev4 = []
        prev3 = []
        abba_sup = abba_hyp = False
        need_babs = set()
        babs = set()
        for c in line:
            if c == '[':
                in_hyper = True
                prev4.clear(); prev3.clear()
            elif c == ']':
                in_hyper = False
                prev4.clear(); prev3.clear()
            else:
                prev4.append(c)
                if len(prev4) > 4: prev4.pop(0)
                if len(prev4) == 4 and prev4[0] == prev4[3] and prev4[1] == prev4[2] and prev4[0] != prev4[1]:
                    if in_hyper: abba_hyp = True
                    else: abba_sup = True
                prev3.append(c)
                if len(prev3) > 3: prev3.pop(0)
                if len(prev3) == 3 and prev3[0] == prev3[2] and prev3[0] != prev3[1]:
                    s = ''.join(prev3)
                    if in_hyper:
                        babs.add(s)
                    else:
                        need_babs.add(prev3[1] + prev3[0] + prev3[1])
        if abba_sup and not abba_hyp:
            p1 += 1
        if need_babs & babs:
            p2 += 1

sys.stdout.write(f"{p1} {p2}")