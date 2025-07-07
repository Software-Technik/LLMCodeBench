import sys
def run(inp,prog):
    mem=prog[:]; i=0; out=0
    while True:
        ins=mem[i]; op=ins%100
        if op==99: break
        m1=ins//100%10; m2=ins//1000%10
        if op==1:
            a=mem[i+1] if m1 else mem[mem[i+1]]; b=mem[i+2] if m2 else mem[mem[i+2]]
            mem[mem[i+3]]=a+b; i+=4
        elif op==2:
            a=mem[i+1] if m1 else mem[mem[i+1]]; b=mem[i+2] if m2 else mem[mem[i+2]]
            mem[mem[i+3]]=a*b; i+=4
        elif op==3:
            mem[mem[i+1]]=inp; i+=2
        elif op==4:
            out=mem[i+1] if m1 else mem[mem[i+1]]; i+=2
        elif op==5:
            a=mem[i+1] if m1 else mem[mem[i+1]]; b=mem[i+2] if m2 else mem[mem[i+2]]
            i=b if a else i+3
        elif op==6:
            a=mem[i+1] if m1 else mem[mem[i+1]]; b=mem[i+2] if m2 else mem[mem[i+2]]
            i=b if not a else i+3
        elif op==7:
            a=mem[i+1] if m1 else mem[mem[i+1]]; b=mem[i+2] if m2 else mem[mem[i+2]]
            mem[mem[i+3]]=1 if a<b else 0; i+=4
        elif op==8:
            a=mem[i+1] if m1 else mem[mem[i+1]]; b=mem[i+2] if m2 else mem[mem[i+2]]
            mem[mem[i+3]]=1 if a==b else 0; i+=4
    return out

data=list(map(int,open(sys.argv[1]).read().split(',')))
p1=run(1,data); p2=run(5,data)
sys.stdout.write(str(p1)+' '+str(p2))