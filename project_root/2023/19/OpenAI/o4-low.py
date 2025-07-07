import sys

def parse(text):
    workflows_txt, parts_txt = text.split("\n\n", 1)
    workflows = {}
    for line in workflows_txt.splitlines():
        name, conds = line.split("{",1)
        rules = []
        for rule in conds[:-1].split(","):
            if "<" in rule:
                cat, rest = rule.split("<")
                val, nxt = rest.split(":")
                rules.append((cat,int(val),"<",nxt))
            elif ">" in rule:
                cat, rest = rule.split(">")
                val, nxt = rest.split(":")
                rules.append((cat,int(val),">",nxt))
            else:
                rules.append((None,None,None,rule))
        workflows[name] = rules
    parts = []
    for line in parts_txt.splitlines():
        d={}
        for pair in line.split():
            cat,val=pair.split("="); d[cat]=int(val)
        parts.append(d)
    return workflows, parts

def part1(text):
    workflows, parts = parse(text)
    total=0
    for p in parts:
        wf="in"
        while wf not in ("A","R"):
            for cat,val,op,nxt in workflows[wf]:
                if op=="<":
                    if p[cat]<val: wf=nxt; break
                elif op==">":
                    if p[cat]>val: wf=nxt; break
                else:
                    wf=nxt; break
        if wf=="A": total+=sum(p.values())
    return total

def part2(text):
    workflows,_ = parse(text)
    results=[]
    def traverse(wf, rngs):
        if wf=="A":
            results.append(rngs); return
        if wf=="R": return
        for cat,val,op,nxt in workflows[wf]:
            if op in ("<",">"):
                curr = rngs[cat]
                low,high = [],[]
                for a,b in curr:
                    if op=="<":
                        if b<val: low.append((a,b))
                        elif a<val: low.append((a,val-1)); high.append((val,b))
                        else: high.append((a,b))
                    else:
                        if a>val: low.append((a,b))
                        elif b>val: low.append((val+1,b)); high.append((a,val))
                        else: high.append((a,b))
                if low:
                    nr = dict(rngs)
                    nr[cat]=low
                    traverse(nxt,nr)
                if high:
                    nr2 = dict(rngs)
                    nr2[cat]=high
                    traverse(nxt,nr2)
            else:
                traverse(nxt, rngs)
    init = {c:[(1,4000)] for c in ("x","m","a","s")}
    traverse("in",init)
    total=0
    for r in results:
        sub=1
        for segs in r.values():
            n=0
            for a,b in segs: n+=b-a+1
            sub*=n
        total+=sub
    return total

if __name__=="__main__":
    text=open(sys.argv[1]).read()
    print(part1(text), part2(text))