import sys
inc1=inc2=0
last=None
buf=[]
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        x=int(line)
        if last is not None and x>last: inc1+=1
        if len(buf)==3:
            if x>buf[0]: inc2+=1
            del buf[0]
        buf.append(x)
        last=x
sys.stdout.write(f"{inc1} {inc2}")