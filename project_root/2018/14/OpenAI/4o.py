import sys

def part1(file_path):
    with open(file_path, 'r') as file:
        target = int(file.readline().strip())

    scores = [3, 7]
    elf1, elf2 = 0, 1
    while len(scores) < target + 10:
        new_score = scores[elf1] + scores[elf2]
        scores.extend(divmod(new_score, 10) if new_score >= 10 else (new_score,))
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

    return ''.join(map(str, scores[target:target+10]))

def part2(file_path):
    with open(file_path, 'r') as file:
        num = file.readline().strip()
    target = [int(c) for c in num]

    scores = [3, 7]
    elf1, elf2 = 0, 1
    target_length = len(target)
    while True:
        new_score = scores[elf1] + scores[elf2]
        scores.extend(divmod(new_score, 10) if new_score >= 10 else (new_score,))
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

        if scores[-target_length:] == target:
            return len(scores) - target_length
        if scores[-target_length-1:-1] == target:
            return len(scores) - target_length - 1

inout_strings = sys.argv[1]
sys.stdout.write(f"{part1(inout_strings)} {part2(inout_strings)}")