import sys
input_path = sys.argv[1]
lines = open(input_path).read().split("\n\n")
passports = [p.replace("\n", " ").strip() for p in lines]

required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_fields = {r: False for r in required}

import re
height_regex = re.compile(r"^(\d+)(cm|in)$")
hair_color_regex = re.compile(r"^#[0-9a-f]{6}$")
pass_id_regex = re.compile(r"^[0-9]{9}$")

def is_valid_height(h):
    if match := height_regex.match(h):
        num, unit = match.groups()
        num = int(num)
        return (unit == "cm" and 150 <= num <= 193) or (unit == "in" and 59 <= num <= 76)
    return False

def is_valid_entry(entry, field):
    if field == "byr": return 1920 <= int(entry) <= 2002
    elif field == "iyr": return 2010 <= int(entry) <= 2020
    elif field == "eyr": return 2020 <= int(entry) <= 2030
    elif field == "hgt": return is_valid_height(entry)
    elif field == "hcl": return bool(hair_color_regex.match(entry))
    elif field == "ecl": return entry in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    elif field == "pid": return bool(pass_id_regex.match(entry))

valid1 = sum(all(required.issubset(set(p.split())) for p in passports))
for passport in passports:
    fields = dict(f.split(":") for f in passport.split())
    if all(is_valid_entry(fields.get(req, ""), req) for req in required):
        valid_fields["byr"] = True
        valid_fields["iyr"] = True
        valid_fields["eyr"] = True
        valid_fields["hgt"] = True
        valid_fields["hcl"] = True
        valid_fields["ecl"] = True
        valid_fields["pid"] = True

valid2 = sum(all(valid_fields.values()) for _ in passports)
print (valid1, valid2)