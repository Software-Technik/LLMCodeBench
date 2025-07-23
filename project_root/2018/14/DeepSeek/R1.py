import sys

def part1(file_path):
    with open(file_path, 'r') as file:
        target = int(file.readline().rstrip("\n"))

    scores = [3, 7]
    elf1, elf2 = 0, 1
    for _ in range(10 + target):
        total = scores[elf1] + scores[elf2]
        if total >= 10:
            scores.append(total // 10)
            scores.append(total % 10)
        else:
            scores.append(total)
        n = len(scores)
        elf1 = (elf1 + scores[elf1] + 1) % n
        elf2 = (elf2 + scores[elf2] + 1) % n

    return ''.join(str(n) for n in scores[target:target+10])

def part2(file_path):
    with open(file_path, 'r') as file:
        num = int(file.readline().rstrip("\n"))
    target = [int(c) for c in str(num)]
    L = len(target)

    scores = [3, 7]
    elf1, elf2 = 0, 1
    while True:
        total = scores[elf1] + scores[elf2]
        if total >= 10:
            d1 = total // 10
            scores.append(d1)
            n = len(scores)
            if n >= L:
                start = n - L
                if scores[start:start+L] == target:
                    return start
            d2 = total % 10
            scores.append(d2)
            n = len(scores)
            if n >= L:
                start = n - L
                if scores[start:start+L] == target:
                    return start
        else:
            scores.append(total)
            n = len(scores)
            if n >= L:
                start = n - L
                if scores[start:start+L] == target:
                    return start
        n = len(scores)
        elf1 = (elf1 + scores[elf1] + 1) % n
        elf2 = (elf2 + scores[elf2] + 1) % n

inout_strings = sys.argv[1]
sys.stdout.write(f"{part1(inout_strings)} {part2(inout_strings)}")