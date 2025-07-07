import sys,re
hcl=re.compile(r"^#[0-9a-f]{6}$")
ecl={"amb","blu","brn","gry","grn","hzl","oth"}
req={"byr","iyr","eyr","hgt","hcl","ecl","pid"}
p1=p2=0
for chunk in open(sys.argv[1]).read().split("\n\n"):
    d={k:v for k,v in (field.split(":",1) for field in chunk.split())}
    if req<=d.keys():
        p1+=1
        x=d["byr"]
        if len(x)==4 and x.isdigit() and 1920<=int(x)<=2002:
            x=d["iyr"]
            if len(x)==4 and x.isdigit() and 2010<=int(x)<=2020:
                x=d["eyr"]
                if len(x)==4 and x.isdigit() and 2020<=int(x)<=2030:
                    h=d["hgt"]
                    if (h.endswith("cm") and h[:-2].isdigit() and 150<=int(h[:-2])<=193) or (h.endswith("in") and h[:-2].isdigit() and 59<=int(h[:-2])<=76):
                        x=d["hcl"]
                        if hcl.match(x):
                            if d["ecl"] in ecl:
                                x=d["pid"]
                                if len(x)==9 and x.isdigit():
                                    p2+=1
print(p1,p2)