import sys,re

def valid_height(s):
    if s.endswith("cm"):
        try:
            v=int(s[:-2]); return 150<=v<=193
        except: return False
    if s.endswith("in"):
        try:
            v=int(s[:-2]); return 59<=v<=76
        except: return False
    return False

pid_re=re.compile(r"^\d{9}$")
hcl_re=re.compile(r"^#[0-9a-f]{6}$")
eye_colors={"amb","blu","brn","gry","grn","hzl","oth"}

input_path=sys.argv[1]
with open(input_path) as f:
    raw=f.read().split("\n\n")

passports=[dict(field.split(":",1) for field in block.split()) for block in raw]

required_keys={"byr","iyr","eyr","hgt","hcl","ecl","pid"}

result1=sum(1 for p in passports if required_keys<=p.keys())

def valid_passport(p):
    try:
        if not (len(p["byr"])==4 and 1920<=int(p["byr"])<=2002): return False
        if not (len(p["iyr"])==4 and 2010<=int(p["iyr"])<=2020): return False
        if not (len(p["eyr"])==4 and 2020<=int(p["eyr"])<=2030): return False
        if not valid_height(p["hgt"]): return False
        if not hcl_re.fullmatch(p["hcl"]): return False
        if p["ecl"] not in eye_colors: return False
        if not pid_re.fullmatch(p["pid"]): return False
        return True
    except:
        return False

result2=sum(1 for p in passports if required_keys<=p.keys() and valid_passport(p))

print(result1, result2)