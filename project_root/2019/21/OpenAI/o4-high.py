import sys

def runprog(data,moves):
    mem={i:v for i,v in enumerate(data)}
    i=0;rel=0;idx=0
    inp=[ord(c) for line in moves for c in (line+"\n")]
    get=mem.get
    while True:
        ins=get(i,0);op=ins%100;m1=ins//100%10;m2=ins//1000%10;m3=ins//10000%10
        if op==99:break
        if m1==1:
            v1=get(i+1,0)
        else:
            a1=get(i+1,0)+(rel if m1==2 else 0);v1=get(a1,0)
        if op==3:
            a1=get(i+1,0)+(rel if m1==2 else 0);mem[a1]=inp[idx];idx+=1;i+=2;continue
        if op==4:
            if v1>512:return v1
            i+=2;continue
        if op==5 and v1!=0:
            if m2==1:i=get(i+2,0)
            else:i=get(get(i+2,0)+(rel if m2==2 else 0),0)
            continue
        if op==6 and v1==0:
            if m2==1:i=get(i+2,0)
            else:i=get(get(i+2,0)+(rel if m2==2 else 0),0)
            continue
        if op in (1,2,7,8):
            if m2==1:
                v2=get(i+2,0)
            else:
                a2=get(i+2,0)+(rel if m2==2 else 0);v2=get(a2,0)
            a3=get(i+3,0)+(rel if m3==2 else 0)
            if op==1:mem[a3]=v1+v2
            elif op==2:mem[a3]=v1*v2
            elif op==7:mem[a3]=1 if v1<v2 else 0
            else:mem[a3]=1 if v1==v2 else 0
            i+=4;continue
        if op==9:
            rel+=v1;i+=2;continue
        i+=3

def part1(data):
    return runprog(data,["NOT A J","NOT C T","AND D T","OR T J","WALK"])

def part2(data):
    return runprog(data,["NOT C T","OR T J","NOT E T","NOT T T","OR H T","AND T J","NOT A T","OR T J","AND D J","NOT B T","NOT T T","OR E T","NOT T T","OR T J","RUN"])

if __name__=="__main__":
    path=sys.argv[1]
    with open(path) as f:
        data=list(map(int,f.read().splitlines()[0].split(",")))
    sys.stdout.write(f"{part1(data)} {part2(data)}")