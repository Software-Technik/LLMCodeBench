import sys
import re

input_path = sys.argv[1]

with open(input_path) as f:
    passports = f.read().split("\n\n")
passports = [p.replace("\n", " ").strip() for p in passports]

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid1 = sum(1 for p in passports if all(r in p for r in required))

hcl_prog = re.compile(r"^#[0-9a-f]{6}$")
pid_prog = re.compile(r"^[0-9]{9}$")
ecl_set = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def valid_height(s):
    if s.endswith("cm"):
        num = s[:-2]
        return num.isdigit() and 150 <= int(num) <= 193
    elif s.endswith("in"):
        num = s[:-2]
        return num.isdigit() and 59 <= int(num) <= 76
    return False

def validate_passport(p):
    fields = {}
    for field in p.split():
        if ':' in field:
            k, v = field.split(':', 1)
            fields[k] = v
    for r in required:
        if r not in fields:
            return False
    try:
        if not (1920 <= int(fields["byr"]) <= 2002):
            return False
        if not (2010 <= int(fields["iyr"]) <= 2020):
            return False
        if not (2020 <= int(fields["eyr"]) <= 2030):
            return False
        if not valid_height(fields["hgt"]):
            return False
        if not hcl_prog.match(fields["hcl"]):
            return False
        if fields["ecl"] not in ecl_set:
            return False
        if not pid_prog.match(fields["pid"]):
            return False
    except (ValueError, KeyError):
        return False
    return True

valid2 = sum(1 for p in passports if validate_passport(p))
print(valid1, valid2)