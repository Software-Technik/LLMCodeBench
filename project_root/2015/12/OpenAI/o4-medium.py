import sys,re,json
s=open(sys.argv[1]).read()
print(sum(map(int,re.findall(r"-?\d+",s))))
def g(x):
    if isinstance(x,int):return x
    if isinstance(x,list):return sum(g(e) for e in x)
    if isinstance(x,dict):
        if "red" in x.values():return 0
        return sum(g(e) for e in x.values())
    return 0
print(g(json.loads(s)))