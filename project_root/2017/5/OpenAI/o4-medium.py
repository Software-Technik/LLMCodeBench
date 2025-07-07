import sys

def step(instructions, second=False):
    ins = instructions[:]
    n = len(ins)
    i = 0
    steps = 0
    if second:
        while 0 <= i < n:
            j = ins[i]
            ins[i] = j - 1 if j >= 3 else j + 1
            i += j
            steps += 1
    else:
        while 0 <= i < n:
            j = ins[i]
            ins[i] = j + 1
            i += j
            steps += 1
    return steps

def main():
    with open(sys.argv[1]) as f:
        ins = [int(line) for line in f if line.strip()]
    print(step(ins, False))
    print(step(ins, True))

if __name__ == '__main__':
    main()