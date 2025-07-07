import sys
from collections import defaultdict
data=open(sys.argv[1]).read().splitlines()
reactions={}
for line in data:
    a,b=line.split("=>")
    oq,oc=b.split()
    ins=[]
    for t in a.split(","):
        q,c=t.strip().split()
        ins.append((int(q),c))
    reactions[oc]=(int(oq),ins)
def ore_for(fuel):
    need=defaultdict(int); need['FUEL']=fuel
    spare=defaultdict(int)
    while True:
        chem=next((c for c,q in need.items() if c!='ORE' and q>0),None)
        if chem is None: break
        q=need[chem]; avail=spare[chem]
        use=avail if avail<q else q; q-=use; spare[chem]-=use; need[chem]=0
        if q>0:
            out,ins=reactions[chem]; m=(q+out-1)//out; spare[chem]+=m*out-q
            for iq,ic in ins: need[ic]+=iq*m
    return need['ORE']
p1=ore_for(1)
tr=10**12; lo=1; hi=tr
while lo<hi:
    mid=(lo+hi+1)//2
    if ore_for(mid)<=tr: lo=mid
    else: hi=mid-1
print(p1,lo)