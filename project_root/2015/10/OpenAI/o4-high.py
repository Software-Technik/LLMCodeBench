import sys
def next_seq(s):
    res=[]; append=res.append
    n=len(s); i=0
    while i<n:
        c=s[i]; j=i+1
        while j<n and s[j]==c: j+=1
        append(str(j-i)); append(c)
        i=j
    return ''.join(res)
with open(sys.argv[1]) as f:
    seq=f.readline().strip()
for i in range(1,51):
    seq=next_seq(seq)
    if i==40: p1=len(seq)
sys.stdout.write(f"{p1}\n{len(seq)}\n")