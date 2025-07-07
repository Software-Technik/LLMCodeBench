import sys,hashlib
with open(sys.argv[1]) as f:
    key=f.readline().strip().encode()
m5=hashlib.md5
base=m5(key)
p1=p2=None
i=1
while p1 is None or p2 is None:
    h=base.copy()
    h.update(str(i).encode())
    d=h.digest()
    if d[0]==0 and d[1]==0:
        if p1 is None and d[2]<16: p1=i
        if p2 is None and d[2]==0: p2=i
    i+=1
sys.stdout.write(f"{p1}\n{p2}\n")