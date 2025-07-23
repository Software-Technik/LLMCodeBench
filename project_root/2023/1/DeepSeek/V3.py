import sys
import re

def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        digits = [c for c in line if c.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])
    return total

words_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def part2(text: str) -> int:
    total = 0
    pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    for line in text.splitlines():
        matches = pattern.findall(line)
        if matches:
            first = matches[0]
            last = matches[-1]
            total += int(words_to_digits.get(first, first) + words_to_digits.get(last, last))
    return total

with open(sys.argv[1]) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")