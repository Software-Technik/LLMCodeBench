import sys

def main():
    tests = {'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}
    result1 = result2 = None
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            head, rest = line.split(': ', 1)
            num = int(head.split()[1])
            attrs = {}
            for item in rest.split(', '):
                k, v = item.split(': ')
                attrs[k] = int(v)
            if result1 is None and all(v == tests[k] for k, v in attrs.items()):
                result1 = num
            if result2 is None:
                ok = True
                for k, v in attrs.items():
                    if k in ('cats','trees'):
                        if v <= tests[k]:
                            ok = False; break
                    elif k in ('pomeranians','goldfish'):
                        if v >= tests[k]:
                            ok = False; break
                    elif v != tests[k]:
                        ok = False; break
                if ok:
                    result2 = num
            if result1 is not None and result2 is not None:
                break
    sys.stdout.write(f"{result1}\n{result2}\n")

if __name__ == '__main__':
    main()