import sys

def main():
    banks = list(map(int, open(sys.argv[1]).read().split()))
    n = len(banks)
    seen = {tuple(banks): 0}
    cycles = 0
    while True:
        cycles += 1
        max_blocks = banks[0]; idx = 0
        for i in range(1, n):
            b = banks[i]
            if b > max_blocks:
                max_blocks = b; idx = i
        banks[idx] = 0
        base, rem = divmod(max_blocks, n)
        if base:
            for i in range(n):
                banks[i] += base
        for i in range(rem):
            banks[(idx + 1 + i) % n] += 1
        state = tuple(banks)
        if state in seen:
            print(cycles)
            print(cycles - seen[state])
            return
        seen[state] = cycles

if __name__ == "__main__":
    main()