import sys,math
def main():
    lines=open(sys.argv[1]).read().splitlines()
    dirs=[0 if c=='L' else 1 for c in lines[0]]
    dlen=len(dirs)
    nodes={}
    starts=[]
    for line in lines[2:]:
        node,_,rest=line.split(maxsplit=2)
        nbrs=rest[1:-1].split(', ')
        nodes[node]=(nbrs[0],nbrs[1])
        if node.endswith('A'): starts.append(node)
    cur='AAA';di=0;tot=0
    while cur!='ZZZ':
        cur=nodes[cur][dirs[di]]; di=di+1 if di+1<dlen else 0; tot+=1
    zs=[]
    for s in starts:
        cur=s;di=0;st=0
        while not cur.endswith('Z'):
            cur=nodes[cur][dirs[di]]; di=di+1 if di+1<dlen else 0; st+=1
        zs.append(st)
    sys.stdout.write(f"{tot} {math.lcm(*zs)}")
if __name__=='__main__':
    main()