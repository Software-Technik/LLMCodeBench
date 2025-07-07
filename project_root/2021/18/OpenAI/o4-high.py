import sys
def parse_line(s):
    res=[]; depth=0; i=0; n=len(s)
    while i<n:
        c=s[i]
        if c=='[':
            depth+=1; i+=1
        elif c==']':
            depth-=1; i+=1
        elif c==',':
            i+=1
        else:
            v=0
            while i<n and s[i].isdigit():
                v=v*10+ord(s[i])-48; i+=1
            res.append((v,depth))
    return res
def add(a,b):
    return [(v,d+1) for v,d in a]+[(v,d+1) for v,d in b]
def explode(num):
    for i in range(len(num)-1):
        v,d=num[i]; v2,d2=num[i+1]
        if d>4 and d==d2:
            if i>0:
                v0,d0=num[i-1]; num[i-1]=(v0+v,d0)
            if i+2<len(num):
                v3,d3=num[i+2]; num[i+2]=(v3+v2,d3)
            num[i:i+2]=[(0,d-1)]
            return True
    return False
def split(num):
    for i,(v,d) in enumerate(num):
        if v>=10:
            l=v//2; r=v-l
            num[i:i+1]=[(l,d+1),(r,d+1)]
            return True
    return False
def reduce(num):
    while True:
        if explode(num): continue
        if split(num): continue
        break
    return num
def magnitude(num):
    while len(num)>1:
        for i in range(len(num)-1):
            v1,d1=num[i]; v2,d2=num[i+1]
            if d1==d2:
                num[i:i+2]=[(3*v1+2*v2,d1-1)]
                break
    return num[0][0]
def main():
    lines=open(sys.argv[1]).read().splitlines()
    numbers=[parse_line(s) for s in lines]
    cur=numbers[0]
    for num in numbers[1:]:
        cur=reduce(add(cur,num))
    res1=magnitude(cur)
    maxm=0
    for i,s1 in enumerate(lines):
        for j,s2 in enumerate(lines):
            if s1!=s2:
                mag=magnitude(reduce(add(numbers[i],numbers[j])))
                if mag>maxm: maxm=mag
    sys.stdout.write(f"{res1} {maxm}")
if __name__=="__main__":
    main()