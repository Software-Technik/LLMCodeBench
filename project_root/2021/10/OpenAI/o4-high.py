import sys

def main():
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    err = {')': 3, ']': 57, '}': 1197, '>': 25137}
    auto = {'(': 1, '[': 2, '{': 3, '<': 4}
    total = 0
    autos = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            stack = []
            corrupt = False
            for c in line:
                if c in pairs:
                    if not stack or stack[-1] != pairs[c]:
                        total += err[c]
                        corrupt = True
                        break
                    stack.pop()
                else:
                    stack.append(c)
            if not corrupt and stack:
                s = 0
                while stack:
                    s = s * 5 + auto[stack.pop()]
                autos.append(s)
    autos.sort()
    sys.stdout.write(f"{total} {autos[len(autos)//2]}")

if __name__ == '__main__':
    main()