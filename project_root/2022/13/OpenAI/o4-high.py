import sys, json
from functools import cmp_to_key
def compare(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return (a>b)-(a<b)
    if isinstance(a,int):
        return compare([a],b)
    if isinstance(b,int):
        return compare(a,[b])
    for x,y in zip(a,b):
        r=compare(x,y)
        if r:
            return r
    return (len(a)>len(b))-(len(a)<len(b))
def part1(p):
    return sum(i+1 for i,(a,b) in enumerate(zip(p[0::2],p[1::2])) if compare(a,b)<0)
def part2(p):
    q=p+[[[2]],[[6]]]
    q.sort(key=cmp_to_key(compare))
    return (q.index([[2]])+1)*(q.index([[6]])+1)
with open(sys.argv[1]) as f:
    packets=[json.loads(line) for line in f if line.strip()]
print(part1(packets))
print(part2(packets))