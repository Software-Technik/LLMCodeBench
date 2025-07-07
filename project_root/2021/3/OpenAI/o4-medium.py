import sys

def part1(data):
    cols = zip(*data)
    half = len(data) / 2
    gamma = ''.join('1' if col.count('1') > half else '0' for col in cols)
    eps = ''.join('0' if c == '1' else '1' for c in gamma)
    return int(gamma, 2) * int(eps, 2)

def part2(data):
    def rating(lst, most):
        bit = 0
        while len(lst) > 1:
            ones = sum(1 for x in lst if x[bit] == '1')
            zeros = len(lst) - ones
            if most:
                keep = '1' if ones >= zeros else '0'
            else:
                keep = '0' if zeros <= ones else '1'
            lst = [x for x in lst if x[bit] == keep]
            bit += 1
        return int(lst[0], 2)
    return rating(data, True) * rating(data, False)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = f.read().split()
    sys.stdout.write(f"{part1(data)} {part2(data)}")