import sys
with open(sys.argv[1]) as f:
    lower,upper=map(int,f.readline().split('-'))
c1=c2=0
for x in range(lower,upper):
    s=str(x)
    inc=True;cnt=1;has_rep=False;exact2=False
    for i in range(1,6):
        if s[i]<s[i-1]:
            inc=False;break
        if s[i]==s[i-1]:
            cnt+=1
        else:
            if cnt>=2:has_rep=True
            if cnt==2:exact2=True
            cnt=1
    if not inc:continue
    if cnt>=2:has_rep=True
    if cnt==2:exact2=True
    if has_rep:c1+=1
    if exact2:c2+=1
sys.stdout.write(f"{c1} {c2}")