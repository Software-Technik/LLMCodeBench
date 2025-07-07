import sys

M = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
R = {v: k for k, v in M.items()}

def s2d(s):
    n = 0
    for c in s:
        n = n * 5 + M[c]
    return n

def d2s(n):
    if n == 0:
        return '0'
    res = []
    while n:
        n, r = divmod(n, 5)
        if r > 2:
            r -= 5
            n += 1
        res.append(R[r])
    return ''.join(reversed(res))

def main():
    with open(sys.argv[1]) as f:
        total = sum(s2d(line.strip()) for line in f)
    print(d2s(total))

if __name__ == '__main__':
    main()