import sys

char_to_val = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
val_to_char = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}

def s2d(s):
    d = 0
    for c in s:
        d = d * 5 + char_to_val[c]
    return d

def d2s(d):
    if d == 0:
        return '0'
    digits = []
    while d:
        r = d % 5
        if r <= 2:
            digits.append(r)
            d //= 5
        else:
            digits.append(r - 5)
            d = d // 5 + 1
    return ''.join(val_to_char[x] for x in reversed(digits))

if __name__ == '__main__':
    total = 0
    with open(sys.argv[1]) as f:
        for line in f:
            total += s2d(line.strip())
    print(d2s(total))