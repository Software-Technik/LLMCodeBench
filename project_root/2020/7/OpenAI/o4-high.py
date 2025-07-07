import sys
from functools import lru_cache
rev={}
tree={}
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if not line:continue
        parent,rest=line.split(" bags contain ")
        rest=rest[:-1]
        tree[parent]={}
        for part in rest.split(", "):
            if part.startswith("no other"):continue
            num,adj,col,_=part.split()
            name=adj+" "+col
            cnt=int(num)
            tree[parent][name]=cnt
            rev.setdefault(name,[]).append(parent)
visited=set()
stack=["shiny gold"]
while stack:
    bag=stack.pop()
    for p in rev.get(bag,()):
        if p not in visited:
            visited.add(p)
            stack.append(p)
result1=len(visited)
@lru_cache(None)
def count_inside(bag):
    return sum(cnt*(1+count_inside(c)) for c,cnt in tree[bag].items())
result2=count_inside("shiny gold")
print(result1,result2)