import sys
import re

input_path = sys.argv[1]

with open(input_path) as f:
    lines = f.read()

passports = lines.split("\n\n")
passports = [p.replace("\n", " ").strip() for p in passports]

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

result1 = sum(all(r in p for r in required) for p in passports)

def valid_height(s):
    if s.endswith("cm"):
        return 150 <= int(s[:-2]) <= 193
    if s.endswith("in"):
        return 59 <= int(s[:-2]) <= 76
    return False

prog = re.compile(r"^#[0-9a-f]{6}$")
pid = re.compile(r"^[0-9]{9}$")
req_validators = [
    lambda x: 1920 <= int(x) <= 2002,
    lambda x: 2010 <= int(x) <= 2020,
    lambda x: 2020 <= int(x) <= 2030,
    valid_height,
    lambda x: bool(prog.match(x)),
    lambda x: x in "amb blu brn gry grn hzl oth".split(),
    lambda x: bool(pid.match(x)),
]

def get_val(p, key):
    for thing in p.split():
        k, v = thing.split(":")
        if k == key:
            return v

def find_and_validate_all(p):
    for idx in range(7):
        key = required[idx]
        validator = req_validators[idx]
        val = get_val(p, key)
        if not val or not validator(val):
            return False
    return True

result2 = sum(find_and_validate_all(p) for p in passports)

print(result1, result2)