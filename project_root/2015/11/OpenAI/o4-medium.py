import sys
AL="abcdefghjkmnpqrstuvwxyz"
C2I={c:i for i,c in enumerate(AL)}
def next_password(pw):
    pw=list(pw)
    i=len(pw)-1
    carry=1
    while i>=0 and carry:
        idx=C2I[pw[i]]+carry
        if idx>=23:
            pw[i]=AL[0]
            carry=1
        else:
            pw[i]=AL[idx]
            carry=0
        i-=1
    return "".join(pw)
def valid_password(pw):
    for c in pw:
        if c=="i" or c=="o" or c=="l":
            return False
    straight=False
    for i in range(len(pw)-2):
        a=ord(pw[i])
        if ord(pw[i+1])==a+1 and ord(pw[i+2])==a+2:
            straight=True
            break
    if not straight:
        return False
    pairs=0
    i=0
    n=len(pw)
    while i<n:
        j=i+1
        while j<n and pw[j]==pw[i]:
            j+=1
        pairs+=(j-i)//2
        i=j
    return pairs>1
def part1(pw):
    pw=next_password(pw)
    while not valid_password(pw):
        pw=next_password(pw)
    return pw
def main():
    with open(sys.argv[1]) as f:
        pw=f.readline().strip()
    p1=part1(pw)
    p2=part1(p1)
    sys.stdout.write(p1+"\n"+p2+"\n")
if __name__=="__main__":
    main()