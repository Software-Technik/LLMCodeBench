import sys

with open(sys.argv[1]) as f:
    total1 = total2 = 0
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split('|')
        left = parts[0].split()
        right = parts[1].split()
        for o in right:
            l = len(o)
            if l == 2 or l == 3 or l == 4 or l == 7:
                total1 += 1
        patterns = [set(p) for p in left]
        one = four = seven = eight = None
        for p in patterns:
            l = len(p)
            if l == 2:
                one = p
            elif l == 4:
                four = p
            elif l == 3:
                seven = p
            elif l == 7:
                eight = p
        zero = six = nine = None
        two = three = five = None
        for p in patterns:
            l = len(p)
            if l == 6:
                if four.issubset(p):
                    nine = p
                elif one.issubset(p):
                    zero = p
                else:
                    six = p
            elif l == 5:
                if one.issubset(p):
                    three = p
                elif len(p & four) == 2:
                    two = p
                else:
                    five = p
        m = {
            frozenset(zero): '0',
            frozenset(one): '1',
            frozenset(two): '2',
            frozenset(three): '3',
            frozenset(four): '4',
            frozenset(five): '5',
            frozenset(six): '6',
            frozenset(seven): '7',
            frozenset(eight): '8',
            frozenset(nine): '9'
        }
        v = 0
        for o in right:
            v = v * 10 + int(m[frozenset(o)])
        total2 += v
    sys.stdout.write(f"{total1} {total2}")