import sys
import re

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

part2_pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        number = ""
        for c in line:
            if c.isdigit():
                number += c
                break
        for c in reversed(line):
            if c.isdigit():
                number += c
                break
        total += int(number)
    return total

def part2(text: str) -> int:
    total = 0
    for line in text.splitlines():
        matches = part2_pattern.findall(line)
        if matches:
            first_digit = matches[0]
            last_digit = matches[-1]
            number = words_to_digits.get(first_digit, first_digit) + words_to_digits.get(last_digit, last_digit)
            total += int(number)
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")