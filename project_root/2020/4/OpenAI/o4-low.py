import sys,re

def valid_height(s):
    if s.endswith("cm"):
        try: return 150 <= int(s[:-2]) <= 193
        except: return False
    if s.endswith("in"):
        try: return 59 <= int(s[:-2]) <= 76
        except: return False
    return False

prog = re.compile(r"^#[0-9a-f]{6}$")
pid_prog = re.compile(r"^[0-9]{9}$")
required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
ecl_set = {"amb","blu","brn","gry","grn","hzl","oth"}

validators = {
    "byr": lambda x: len(x)==4 and 1920<=int(x)<=2002,
    "iyr": lambda x: len(x)==4 and 2010<=int(x)<=2020,
    "eyr": lambda x: len(x)==4 and 2020<=int(x)<=2030,
    "hgt": valid_height,
    "hcl": lambda x: bool(prog.match(x)),
    "ecl": lambda x: x in ecl_set,
    "pid": lambda x: bool(pid_prog.match(x)),
}

data = open(sys.argv[1]).read().strip().split("\n\n")
passports = [dict(field.split(":") for field in p.split()) for p in data]

count1 = sum(1 for p in passports if all(k in p for k in required))
count2 = 0
for p in passports:
    if all(k in p and validators[k](p[k]) for k in required):
        count2 += 1

print(count1, count2)