import sys

p1=0
p2=0
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        m=int(line)
        f1=m//3-2
        p1+=f1
        t=0
        while f1>0:
            t+=f1
            f1=f1//3-2
        p2+=t
sys.stdout.write(f"{p1} {p2}")