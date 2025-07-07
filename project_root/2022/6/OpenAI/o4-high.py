import sys
def find_marker(s,n):
    d={}
    for i in range(n):
        d[s[i]] = d.get(s[i],0)+1
    if len(d)==n: return n
    for i in range(n,len(s)):
        x=s[i]; y=s[i-n]
        d[x]=d.get(x,0)+1
        if d[y]>1: d[y]-=1
        else: del d[y]
        if len(d)==n: return i+1

with open(sys.argv[1]) as f:
    s=f.readline().strip()
print(find_marker(s,4))
print(find_marker(s,14))