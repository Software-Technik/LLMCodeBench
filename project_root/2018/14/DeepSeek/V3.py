import sys

def part1(file_path):
    with open(file_path, 'r') as file:
        target = int(file.readline().rstrip("\n"))

    scores = [3, 7]
    elf1, elf2 = 0, 1
    while len(scores) < target + 10:
        total = scores[elf1] + scores[elf2]
        if total >= 10:
            scores.append(1)
            scores.append(total % 10)
        else:
            scores.append(total)
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

    return ''.join(map(str, scores[target:target+10]))

def part2(file_path):
    with open(file_path, 'r') as file:
        num = file.readline().rstrip("\n")
    target = [int(c) for c in num]
    target_len = len(target)
    target_num = int(num)

    scores = [3, 7]
    elf1, elf2 = 0, 1
    check_len = 0
    while True:
        total = scores[elf1] + scores[elf2]
        if total >= 10:
            scores.append(1)
            if len(scores) >= target_len:
                if scores[-target_len:] == target:
                    return len(scores) - target_len
            scores.append(total % 10)
        else:
            scores.append(total)
        if len(scores) >= target_len:
            if scores[-target_len:] == target:
                return len(scores) - target_len
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

input_file = sys.argv[1]
sys.stdout.write(f"{part1(input_file)} {part2(input_file)}")