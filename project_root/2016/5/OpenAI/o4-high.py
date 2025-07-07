import sys,hashlib
def main():
    data=open(sys.argv[1]).readline().strip()
    b=data.encode()
    base=hashlib.md5(b)
    base_copy=base.copy
    hc='0123456789abcdef'
    first=[]
    second=['']*8
    need=8
    i=0
    while len(first)<8 or need:
        m=base_copy()
        m.update(str(i).encode())
        d=m.digest()
        if d[0] or d[1] or d[2]>=16:
            i+=1
            continue
        v=d[2]&0xF
        if len(first)<8:
            first.append(hc[v])
        if v<8 and second[v]=='':
            second[v]=hc[d[3]>>4]
            need-=1
        i+=1
    sys.stdout.write(''.join(first)+' '+''.join(second))

if __name__=='__main__':
    main()