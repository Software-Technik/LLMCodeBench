import sys
p1=p2=i=0
b0=b1=0
with open(sys.argv[1]) as f:
    for line in f:
        s=line.strip()
        m1=m2=full=0
        h=len(s)//2
        idx=0
        for c in s:
            o=ord(c)
            bit=1<<(o-97) if o>90 else 1<<(o-65+26)
            if idx<h: m1|=bit
            else: m2|=bit
            full|=bit
            idx+=1
        p1+=(m1&m2).bit_length()
        if i==0: b0=full
        elif i==1: b1=full
        else: p2+=(b0&b1&full).bit_length()
        i=(i+1)%3
print(p1)
print(p2)