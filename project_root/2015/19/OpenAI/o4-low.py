import sys
def part1(data):
    reps=data[:-2]; mol=data[-1]; out=set()
    for r in reps:
        a,b=r.split(" => ")
        la=len(a)
        i=mol.find(a)
        while i>=0:
            out.add(mol[:i]+b+mol[i+la:])
            i=mol.find(a,i+1)
    return len(out)
def part2(data):
    mol=data[-1]
    rev=[tuple(r.split(" => ")[::-1]) for r in data[:-2]]
    count=0
    while mol!="e":
        best_i=-1; best_r=None; best_d=None
        for rep,dest in rev:
            if dest=="e" and rep!=mol: continue
            i=mol.rfind(rep)
            if i>best_i:
                best_i=i; best_r=rep; best_d=dest
        mol=best_d.join(mol.rsplit(best_r,1))
        count+=1
    return count
d=[l.strip() for l in open(sys.argv[1])]
print(part1(d)); print(part2(d))