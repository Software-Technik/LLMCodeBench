import sys

moves = {'R':(1,0),'L':(-1,0),'D':(0,1),'U':(0,-1)}

keypad1 = {}
for r,row in enumerate([[1,2,3],[4,5,6],[7,8,9]]):
    for c,v in enumerate(row):
        keypad1[(c-1,r-1)] = str(v)
valid1 = set(keypad1.keys())

keypad2 = {}
for r,row in enumerate([[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]):
    for c,v in enumerate(row):
        if v:
            keypad2[(c-2,r-2)] = str(v)
valid2 = set(keypad2.keys())

path = sys.argv[1]
with open(path) as f:
    lines = [l.strip() for l in f]

x1=y1=0
x2,y2 = -2,0
code1=[]
code2=[]
for line in lines:
    for ch in line:
        dx,dy = moves[ch]
        nx1,ny1 = x1+dx,y1+dy
        if (nx1,ny1) in valid1: x1,y1 = nx1,ny1
        nx2,ny2 = x2+dx,y2+dy
        if (nx2,ny2) in valid2: x2,y2 = nx2,ny2
    code1.append(keypad1[(x1,y1)])
    code2.append(keypad2[(x2,y2)])

sys.stdout.write(''.join(code1)+' '+''.join(code2))