import sys
def main():
    path = sys.argv[1]
    with open(path) as f:
        s = f.read()
    p1 = p2 = 0
    enabled = True
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == 'm' and s.startswith('mul(', i):
            j = i + 4
            if j < n and s[j].isdigit():
                a = 0
                while j < n and s[j].isdigit():
                    a = a * 10 + ord(s[j]) - 48
                    j += 1
                if j < n and s[j] == ',':
                    j += 1
                    if j < n and s[j].isdigit():
                        b = 0
                        while j < n and s[j].isdigit():
                            b = b * 10 + ord(s[j]) - 48
                            j += 1
                        if j < n and s[j] == ')':
                            prod = a * b
                            p1 += prod
                            if enabled:
                                p2 += prod
                            i = j + 1
                            continue
            i += 1
        elif ch == 'd':
            if s.startswith('do()', i):
                enabled = True
                i += 4
                continue
            elif s.startswith("don't()", i):
                enabled = False
                i += 7
                continue
            else:
                i += 1
        else:
            i += 1
    print(p1, p2)

if __name__ == '__main__':
    main()