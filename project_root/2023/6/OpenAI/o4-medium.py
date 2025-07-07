import sys,math
def main():
    ceil=math.ceil;sqrt=math.sqrt
    t0,t1=open(sys.argv[1]).read().splitlines()
    times=[int(x) for x in t0.split(':',1)[1].split()]
    ds=[int(x) for x in t1.split(':',1)[1].split()]
    c=1
    for tm,d in zip(times,ds):
        i=ceil((tm-sqrt(tm*tm-4*d))*0.5)
        if i*(tm-i)<=d: i+=1
        diff=tm//2-i
        if diff>0: c*=diff*2+1 if tm&1==0 else (diff+1)*2
    tm0, d0 = times[0], ds[0]
    i=ceil((tm0-sqrt(tm0*tm0-4*d0))*0.5)
    if i*(tm0-i)<=d0: i+=1
    diff0=tm0//2-i
    r2=diff0*2+1 if diff0>0 and tm0&1==0 else (diff0+1)*2 if diff0>0 else 0
    sys.stdout.write(f"{c} {r2}")
if __name__=="__main__":
    main()