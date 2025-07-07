import sys
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a//gcd(a,b)*b
def main():
    data=open(sys.argv[1]).read().splitlines()
    dirs=[0 if c=='L' else 1 for c in data[0]]
    m=len(dirs)
    nodes={}
    starts=[]
    for line in data[2:]:
        node,_,nei=line.split(maxsplit=2)
        a,b=nei[1:-1].split(', ')
        nodes[node]=(a,b)
        if node.endswith('A'):
            starts.append(node)
    cur='AAA'; idx=0; tot=0
    while cur!='ZZZ':
        cur=nodes[cur][dirs[idx]]
        idx=(idx+1)%m
        tot+=1
    res=1
    for s in starts:
        cur=s; idx=0; cnt=0
        while not cur.endswith('Z'):
            cur=nodes[cur][dirs[idx]]
            idx=(idx+1)%m
            cnt+=1
        res=lcm(res,cnt)
    sys.stdout.write(f"{tot} {res}")
if __name__=='__main__':
    main()