import sys
import re

def main():
    with open(sys.argv[1]) as f:
        s = f.read()
    pattern = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
    ans1 = ans2 = 0
    enabled = True
    for m in pattern.finditer(s):
        a = m.group(1)
        if a:
            prod = int(a) * int(m.group(2))
            ans1 += prod
            if enabled:
                ans2 += prod
        else:
            t = m.group(0)
            if t == 'do()':
                enabled = True
            else:
                enabled = False
    print(ans1, ans2)

if __name__ == '__main__':
    main()