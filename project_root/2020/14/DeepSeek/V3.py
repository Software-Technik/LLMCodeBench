import sys
from itertools import product

def main():
    input_path = sys.argv[1]
    with open(input_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    # Part 1
    mem = {}
    mask = None
    for line in lines:
        l, r = line.split('=')
        l, r = l.strip(), r.strip()
        if l == 'mask':
            mask = r
        else:
            addr = int(l[4:-1])
            val = int(r)
            masked_val = 0
            for i, c in enumerate(mask):
                bit_pos = 35 - i
                if c == '1':
                    masked_val |= (1 << bit_pos)
                elif c == '0':
                    pass
                else:
                    masked_val |= (val & (1 << bit_pos))
            mem[addr] = masked_val
    result1 = sum(mem.values())

    # Part 2
    mem = {}
    mask = None
    for line in lines:
        l, r = line.split('=')
        l, r = l.strip(), r.strip()
        if l == 'mask':
            mask = r
        else:
            addr = int(l[4:-1])
            val = int(r)
            floating_bits = []
            base_addr = 0
            for i, c in enumerate(mask):
                bit_pos = 35 - i
                if c == '1':
                    base_addr |= (1 << bit_pos)
                elif c == 'X':
                    floating_bits.append(bit_pos)
                else:
                    base_addr |= (addr & (1 << bit_pos))
            for bits in product([0, 1], repeat=len(floating_bits)):
                current_addr = base_addr
                for bit, pos in zip(bits, floating_bits):
                    if bit:
                        current_addr |= (1 << pos)
                    else:
                        current_addr &= ~(1 << pos)
                mem[current_addr] = val
    result2 = sum(mem.values())

    print(result1, result2)

if __name__ == "__main__":
    main()