import sys

def main():
    with open(sys.argv[1]) as f:
        raw_rules, raw_updates = f.read().strip().split('\n\n')
    adj = {}
    rule_set = set()
    for line in raw_rules.splitlines():
        a, b = map(int, line.split('|'))
        adj.setdefault(a, []).append(b)
        rule_set.add((a, b))
    ans1 = ans2 = 0
    for line in raw_updates.splitlines():
        seq = list(map(int, line.split(',')))
        mid = len(seq) // 2
        idx = {v: i for i, v in enumerate(seq)}
        ok = True
        for a, ia in idx.items():
            for b in adj.get(a, ()):
                ib = idx.get(b)
                if ib is not None and ia >= ib:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ans1 += seq[mid]
        else:
            s = seq
            n = len(s)
            while True:
                sw = False
                for i in range(n - 1):
                    if (s[i+1], s[i]) in rule_set:
                        s[i], s[i+1] = s[i+1], s[i]
                        sw = True
                if not sw:
                    break
            ans2 += s[mid]
    print(ans1, ans2)

if __name__ == '__main__':
    main()