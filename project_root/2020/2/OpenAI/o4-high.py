import sys
p1=p2=0
with open(sys.argv[1]) as f:
    for l in f:
        l=l.strip()
        if not l: continue
        i=l.find('-');a=int(l[:i])
        j=l.find(' ',i+1);b=int(l[i+1:j])
        c=l[j+1]
        pwd=l[j+4:]
        cnt=pwd.count(c)
        if a<=cnt<=b: p1+=1
        if (pwd[a-1]==c) ^ (pwd[b-1]==c): p2+=1
print(p1, p2)