import sys,re
w2d={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
get=w2d.get
pat=re.compile("one|two|three|four|five|six|seven|eight|nine|\\d")
res1=res2=0
with open(sys.argv[1]) as f:
    for line in f:
        line=line.rstrip("\n")
        f1=l1=f2=l2=None
        for m in pat.finditer(line):
            s=m.group()
            if f2 is None: f2=s
            l2=s
            if s.isdigit():
                if f1 is None: f1=s
                l1=s
        res1+=int(f1+l1)
        res2+=int(get(f2,f2)+get(l2,l2))
sys.stdout.write(f"{res1} {res2}")