import sys
from array import array

def main():
    instrs = []
    with open(sys.argv[1]) as f:
        for line in f:
            s = line.split()
            if s[0] == 'toggle':
                code = 2; a = s[1]; b = s[3]
            else:
                code = 0 if s[1] == 'on' else 1; a = s[2]; b = s[4]
            x1,y1 = map(int, a.split(','))
            x2,y2 = map(int, b.split(','))
            instrs.append((code, x1, y1, y2, x2-x1+1))
    grid1 = [0]*1000
    for code, x1, y1, y2, w in instrs:
        mask = ((1<<w)-1) << x1
        if code == 0:
            for y in range(y1, y2+1):
                grid1[y] |= mask
        elif code == 1:
            inv = ~mask
            for y in range(y1, y2+1):
                grid1[y] &= inv
        else:
            for y in range(y1, y2+1):
                grid1[y] ^= mask
    ans1 = sum(r.bit_count() for r in grid1)
    grid2 = array('I', [0]) * 1000000
    for code, x1, y1, y2, w in instrs:
        if code == 0:
            for y in range(y1, y2+1):
                idx = y*1000 + x1
                for i in range(w):
                    grid2[idx+i] += 1
        elif code == 1:
            for y in range(y1, y2+1):
                idx = y*1000 + x1
                for i in range(w):
                    if grid2[idx+i]:
                        grid2[idx+i] -= 1
        else:
            for y in range(y1, y2+1):
                idx = y*1000 + x1
                for i in range(w):
                    grid2[idx+i] += 2
    ans2 = sum(grid2)
    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()