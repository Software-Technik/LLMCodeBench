import sys
def fill_disk(data, size):
    d = bytearray(int(c) for c in data)
    while len(d) < size:
        r = d[::-1]
        for i in range(len(r)): r[i] ^= 1
        d.append(0)
        d.extend(r)
    del d[size:]
    return d

def checksum(d):
    while len(d) & 1 == 0:
        n = len(d) // 2
        c = bytearray(n)
        for i in range(n):
            c[i] = 1 if d[2*i] == d[2*i+1] else 0
        d = c
    return ''.join('01'[b] for b in d)

def solve(data, size):
    return checksum(fill_disk(data, size))

data = open(sys.argv[1]).read().strip()
sys.stdout.write(solve(data, 272) + " " + solve(data, 35651584))