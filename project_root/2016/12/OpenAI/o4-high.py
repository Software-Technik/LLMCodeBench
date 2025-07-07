import sys
m={'a':0,'b':1,'c':2,'d':3}
lines=open(sys.argv[1]).read().splitlines()
ops=[]; xrs=[]; xvs=[]; yrs=[]; yvs=[]
for L in lines:
    p=L.split(); op=p[0]
    if op=='cpy':
        x=p[1]; y=p[2]
        xrs.append(x in m); xvs.append(m[x] if x in m else int(x))
        yrs.append(True); yvs.append(m[y]); ops.append(0)
    elif op=='inc':
        r=p[1]
        ops.append(1); xrs.append(True); xvs.append(m[r]); yrs.append(False); yvs.append(0)
    elif op=='dec':
        r=p[1]
        ops.append(2); xrs.append(True); xvs.append(m[r]); yrs.append(False); yvs.append(0)
    else:
        x=p[1]; y=p[2]
        xrs.append(x in m); xvs.append(m[x] if x in m else int(x))
        yrs.append(y in m); yvs.append(m[y] if y in m else int(y)); ops.append(3)
def run(ci):
    r=[0,0,ci,0]; i=0
    ops_l=ops; xrs_l=xrs; xvs_l=xvs; yrs_l=yrs; yvs_l=yvs; N=len(ops_l)
    while i<N:
        o=ops_l[i]
        if o==0:
            r[yvs_l[i]] = r[xvs_l[i]] if xrs_l[i] else xvs_l[i]
        elif o==1:
            r[xvs_l[i]] += 1
        elif o==2:
            r[xvs_l[i]] -= 1
        else:
            if (r[xvs_l[i]] if xrs_l[i] else xvs_l[i]) != 0:
                i += (r[yvs_l[i]] if yrs_l[i] else yvs_l[i]); continue
        i+=1
    return r[0]
sys.stdout.write(f"{run(0)} {run(1)}")