import sys,math
data=open(sys.argv[1]).read().splitlines()
bits=[1 if c=='R' else 0 for c in data[0]]
m=len(bits)
node_parts=[line.split(None,2) for line in data[2:]]
idx={p[0]:i for i,p in enumerate(node_parts)}
n=len(node_parts)
left=[0]*n;right=[0]*n;start_ids=[];is_endZ=[False]*n
for name,_,nbrs in node_parts:
    i=idx[name];a,b=nbrs[1:-1].split(', ')
    left[i],right[i]=idx[a],idx[b]
    if name.endswith('A'):start_ids.append(i)
    if name.endswith('Z'):is_endZ[i]=True
start1=idx['AAA'];target=idx['ZZZ']
di=0;cur=start1;total=0
while cur!=target:
    cur=left[cur] if bits[di]==0 else right[cur]
    di+=1
    if di==m:di=0
    total+=1
zs=[]
for s in start_ids:
    di=0;cur=s;st=0
    while not is_endZ[cur]:
        cur=left[cur] if bits[di]==0 else right[cur]
        di+=1
        if di==m:di=0
        st+=1
    zs.append(st)
p2=math.lcm(*zs)
sys.stdout.write(f"{total} {p2}")