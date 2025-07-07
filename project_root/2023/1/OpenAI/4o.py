import sys
import re

def part1(text: str) -> int:
    total = 0
    digit_pattern = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
    for line in text.splitlines():
        match = digit_pattern.findall(line)
        if match:
            first_digit = words_to_digits.get(match[0], match[0])
            last_digit = words_to_digits.get(match[-1], match[-1])
            total += int(first_digit + last_digit)
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
    digit_pattern = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")
    for line in text.splitlines():
        match = digit_pattern.findall(line)
        if match:
            first_digit = words_to_digits.get(match[0], match[0])
            last_digit = words_to_digits.get(match[-1], match[-1])
            total += int(first_digit + last_digit)
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")