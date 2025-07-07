import sys,re
r=re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")
text=open(sys.argv[1]).read()
p1=p2=0
enabled=True
for m in r.finditer(text):
    if m.group(1):
        a=int(m.group(1)); b=int(m.group(2)); v=a*b
        p1+=v
        if enabled: p2+=v
    else:
        if m.group(0)=="do()":
            enabled=True
        else:
            enabled=False
print(p1, p2)