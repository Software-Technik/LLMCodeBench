import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()

passports = data.split("\n\n")
passports = [p.replace("\n", " ").strip() for p in passports]

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid1 = 0
for p in passports:
    if all(r in p for r in required):
        valid1 += 1

valid2 = 0
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
for p in passports:
    fields = p.split()
    data = {}
    for field in fields:
        if ':' in field:
            parts = field.split(':', 1)
            key = parts[0]
            value = parts[1]
            if key not in data:
                data[key] = value
    if not all(key in data for key in required):
        continue
    try:
        byr = int(data['byr'])
        if byr < 1920 or byr > 2002:
            continue
        iyr = int(data['iyr'])
        if iyr < 2010 or iyr > 2020:
            continue
        eyr = int(data['eyr'])
        if eyr < 2020 or eyr > 2030:
            continue
        hgt = data['hgt']
        if hgt.endswith('cm'):
            h_val = int(hgt[:-2])
            if h_val < 150 or h_val > 193:
                continue
        elif hgt.endswith('in'):
            h_val = int(hgt[:-2])
            if h_val < 59 or h_val > 76:
                continue
        else:
            continue
        hcl = data['hcl']
        if len(hcl) != 7 or hcl[0] != '#':
            continue
        for char in hcl[1:]:
            if char not in '0123456789abcdef':
                continue
        if data['ecl'] not in eye_colors:
            continue
        pid = data['pid']
        if len(pid) != 9 or not pid.isdigit():
            continue
        valid2 += 1
    except Exception:
        continue

print(valid1, valid2)