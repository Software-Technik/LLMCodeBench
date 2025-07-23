import re

def part1(text: str) -> int:
    total = 0
    first_digit_pattern = re.compile(r"\d")
    for line in text.splitlines():
        number = min([c for c in line if c.isdigit()]) + max([c for c in line if c.isdigit()])
        total += int(number)
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
    first_digit_pattern = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
    last_digit_pattern = re.compile(r".*(\d|one|two|three|four|five|six|seven|eight|nine).*$")
    for line in text.splitlines():
        match = first_digit_pattern.search(line)
        assert match is not None
        first_digit = match.group(1)

        match = last_digit_pattern.search(line)
        assert match is not None
        last_digit = match.group(1)

        number = words_to_digits.get(first_digit, first_digit) + words_to_digits.get(last_digit, last_digit)
        total += int(number)
    return total

import sys
inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")