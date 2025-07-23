import sys

def solve(file_path, part):
    with open(file_path, 'r') as file:
        lines = [line.rstrip("\n") for line in file]

    if part == 1:
        target = int(lines[0])
        scores = [3, 7]
        elf1, elf2 = 0, 1
        limit = target + 10

        while limit > len(scores):
            newscore = scores[elf1] + scores[elf2]
            for digit in str(newscore):
                scores.append(int(digit))
            elf1 = (elf1 + scores[elf1] + 1) % len(scores)
            elf2 = (elf2 + scores[elf2] + 1) % len(scores)

        return ''.join(map(str, scores[target:target+10]))

    elif part == 2:
        num = int(lines[0])
        target_digits = [int(digit) for digit in str(num)]

        scores = [3, 7]
        elf1, elf2 = 0, 1

        while True:
            newscore = scores[elf1] + scores[elf2]
            scores.extend(map(int, str(newscore)))
            elf1 = (elf1 + scores[elf1] + 1) % len(scores)
            elf2 = (elf2 + scores[elf2] + 1) % len(scores)

            if len(scores) >= len(target_digits):
                current_digits = [scores[i] for i in range(len(scores)-len(target_digits), len(scores))]
                if target_digits == current_digits:
                    return len(scores) - len(target_digits)
    else:
        raise ValueError("Invalid part specified")

def main():
    file_path = sys.argv[1]
    part_numbers = [int(arg) for arg in sys.argv[2:]]

    results = []
    for part in part_numbers:
        result = solve(file_path, part)
        results.append(result)

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()