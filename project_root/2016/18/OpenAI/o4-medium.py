import sys
fn=sys.argv[1]
with open(fn) as f: s=f.read().strip()
M=len(s);mask=(1<<M)-1
row=0
for i,ch in enumerate(s):
    if ch=='^':row|=1<<i
safe=0
for i in range(400000):
    if i==40:first=safe
    safe+=M-row.bit_count()
    row=((row<<1)^(row>>1))&mask
sys.stdout.write(f"{first} {safe}")