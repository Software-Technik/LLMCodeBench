import sys, math

data = [line.split() for line in open(sys.argv[1]) if line.strip()]
instr = data[:11]

def interpret(x, reg):
    return reg[x] if x.isalpha() else int(x)

def sim(part):
    reg = {c:0 for c in "abcdefgh"}
    reg["a"] = part-1
    i = 0
    while i < 11:
        op, x, y = instr[i]
        v = interpret(y, reg)
        if op=="set":
            reg[x]=v
        elif op=="sub":
            reg[x]-=v
        elif op=="mul":
            reg[x]*=v
        elif op=="jnz" and interpret(x, reg)!=0:
            i+=v; continue
        i+=1
    return reg

r1 = sim(1)
b, c = sim(2)["b"], sim(2)["c"]
res1 = (r1["b"]-r1["e"])*(r1["b"]-r1["d"])
cnt = (c-b)//34+1
for x in range(b+17, c+1, 34):
    lim = int(math.isqrt(x))
    for d in range(3, lim+1, 2):
        if x%d==0:
            cnt+=1
            break
sys.stdout.write(f"{res1}\n{cnt}\n")