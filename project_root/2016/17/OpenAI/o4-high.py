import sys
from collections import deque
from hashlib import md5
with open(sys.argv[1]) as f:
    p = f.read().strip()
md5f = md5
dq = deque([(0,0,"")])
short = ""
while dq:
    x,y,path = dq.popleft()
    if x==3 and y==3:
        short = path
        break
    h = md5f((p+path).encode()).hexdigest()
    if h[0]>'a' and y>0: dq.append((x,y-1,path+'U'))
    if h[1]>'a' and y<3: dq.append((x,y+1,path+'D'))
    if h[2]>'a' and x>0: dq.append((x-1,y,path+'L'))
    if h[3]>'a' and x<3: dq.append((x+1,y,path+'R'))
maxl = 0
stack = [(0,0,"")]
while stack:
    x,y,path = stack.pop()
    if x==3 and y==3:
        l = len(path)
        if l>maxl: maxl = l
        continue
    h = md5f((p+path).encode()).hexdigest()
    if h[0]>'a' and y>0: stack.append((x,y-1,path+'U'))
    if h[1]>'a' and y<3: stack.append((x,y+1,path+'D'))
    if h[2]>'a' and x>0: stack.append((x-1,y,path+'L'))
    if h[3]>'a' and x<3: stack.append((x+1,y,path+'R'))
sys.stdout.write(f"{short} {maxl}")