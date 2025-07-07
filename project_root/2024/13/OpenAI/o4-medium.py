import sys

def main():
    data = []
    with open(sys.argv[1]) as f:
        for block in f.read().strip().split('\n\n'):
            l0, l1, l2 = block.split('\n')
            i = l0.find('X+') + 2; a0 = int(l0[i:l0.find(',', i)])
            j = l0.find('Y+') + 2; a1 = int(l0[j:])
            i = l1.find('X+') + 2; b0 = int(l1[i:l1.find(',', i)])
            j = l1.find('Y+') + 2; b1 = int(l1[j:])
            i = l2.find('X=') + 2; p0 = int(l2[i:l2.find(',', i)])
            j = l2.find('Y=') + 2; p1 = int(l2[j:])
            data.append((a0, a1, b0, b1, p0, p1))
    total1 = 0
    for a0, a1, b0, b1, p0, p1 in data:
        best = None
        for i in range(100):
            ai0 = a0 * i; ai1 = a1 * i
            for j in range(100):
                if ai0 + b0*j == p0 and ai1 + b1*j == p1:
                    c = 3*i + j
                    if best is None or c < best: best = c
        if best is not None:
            total1 += best
    total2 = 0
    for a0, a1, b0, b1, p0, p1 in data:
        P0 = p0 + 10000000000000
        P1 = p1 + 10000000000000
        D = a0*b1 - b0*a1
        if D == 0: continue
        i = (P0*b1 - b0*P1) // D
        if i < 0: continue
        if b1:
            j = (P1 - a1*i) // b1
        else:
            if b0:
                j = (P0 - a0*i) // b0
            else:
                continue
        if j < 0: continue
        if a0*i + b0*j == P0 and a1*i + b1*j == P1:
            total2 += 3*i + j
    print(total1, total2)

if __name__ == '__main__':
    main()