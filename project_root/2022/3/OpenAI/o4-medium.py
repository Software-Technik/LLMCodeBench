import sys
p1=p2=i=0
with open(sys.argv[1]) as f:
    r1=r2=None
    for line in f:
        s=line.strip()
        h=len(s)>>1
        a=set(s[:h]); b=set(s[h:])
        badge=(a&b).pop()
        o=ord(badge)
        p1+=o-(96 if badge>='a' else 38)
        if i==0: r1=set(s)
        elif i==1: r2=set(s)
        else:
            badge=(r1&r2&set(s)).pop()
            o=ord(badge)
            p2+=o-(96 if badge>='a' else 38)
        i=(i+1)%3
print(p1)
print(p2)