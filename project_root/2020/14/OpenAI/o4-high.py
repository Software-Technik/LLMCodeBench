import sys

def main():
    lines = open(sys.argv[1]).read().splitlines()
    mem1 = {}
    mem2 = {}
    mask_or = mask_and = float_mask_all = 0
    float_positions = []
    float_combinations = []
    for line in lines:
        if line[1] == 'a':
            m = line[7:]
            mask_or = mask_and = float_mask_all = 0
            float_positions = []
            for i, c in enumerate(m):
                pos = 35 - i
                if c == '1':
                    mask_or |= 1 << pos
                    mask_and |= 1 << pos
                elif c == 'X':
                    float_positions.append(pos)
                    mask_and |= 1 << pos
                    float_mask_all |= 1 << pos
            n = len(float_positions)
            float_combinations = []
            for b in range(1 << n):
                off = 0
                for i, pos in enumerate(float_positions):
                    if b >> i & 1:
                        off |= 1 << pos
                float_combinations.append(off)
        else:
            p = line.find(']')
            addr = int(line[4:p])
            val = int(line[p+4:])
            mem1[addr] = (val | mask_or) & mask_and
            base = (addr | mask_or) & ~float_mask_all
            for off in float_combinations:
                mem2[base | off] = val
    print(sum(mem1.values()), sum(mem2.values()))

if __name__ == '__main__':
    main()