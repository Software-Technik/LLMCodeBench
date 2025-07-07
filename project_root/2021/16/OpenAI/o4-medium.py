import sys

def parse(b, i):
    vs = int(b[i:i+3], 2); t = int(b[i+3:i+6], 2); i += 6
    if t == 4:
        val = 0
        while True:
            g = b[i]; val = (val << 4) | int(b[i+1:i+5], 2); i += 5
            if g == '0': break
        return i, vs, val
    lt = b[i]; i += 1
    vals = []
    s = 0
    if lt == '0':
        total = int(b[i:i+15], 2); i += 15
        end = i + total
        while i < end:
            i, vsv, v = parse(b, i); s += vsv; vals.append(v)
    else:
        count = int(b[i:i+11], 2); i += 11
        for _ in range(count):
            i, vsv, v = parse(b, i); s += vsv; vals.append(v)
    vs += s
    if t == 0:
        val = sum(vals)
    elif t == 1:
        p = 1
        for x in vals: p *= x
        val = p
    elif t == 2:
        val = min(vals)
    elif t == 3:
        val = max(vals)
    elif t == 5:
        val = int(vals[0] > vals[1])
    elif t == 6:
        val = int(vals[0] < vals[1])
    else:
        val = int(vals[0] == vals[1])
    return i, vs, val

def main():
    data = open(sys.argv[1]).read().strip()
    bits = bin(int(data, 16))[2:].zfill(len(data) * 4)
    _, vs, val = parse(bits, 0)
    sys.stdout.write(f"{vs} {val}")

if __name__ == '__main__':
    main()