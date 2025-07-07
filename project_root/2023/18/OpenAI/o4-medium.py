import sys
lines = open(sys.argv[1]).read().splitlines()
DIRS = "RDLU"
steps1 = s1 = 0
x01 = y01 = 0
steps2 = s2 = 0
x02 = y02 = 0
for line in lines:
    p = line.split()
    d1 = p[0]; n1 = int(p[1])
    i = line.rfind('#'); h = line[i+1:-1]
    d2 = DIRS[int(h[-1])]; n2 = int(h[:-1],16)
    steps1 += n1
    if d1 == 'U': nx1, ny1 = x01 - n1, y01
    elif d1 == 'D': nx1, ny1 = x01 + n1, y01
    elif d1 == 'R': nx1, ny1 = x01, y01 + n1
    else: nx1, ny1 = x01, y01 - n1
    s1 += x01*ny1 - nx1*y01
    x01, y01 = nx1, ny1
    steps2 += n2
    if d2 == 'U': nx2, ny2 = x02 - n2, y02
    elif d2 == 'D': nx2, ny2 = x02 + n2, y02
    elif d2 == 'R': nx2, ny2 = x02, y02 + n2
    else: nx2, ny2 = x02, y02 - n2
    s2 += x02*ny2 - nx2*y02
    x02, y02 = nx2, ny2
s1 += x01*0 - 0*y01
s2 += x02*0 - 0*y02
res1 = (abs(s1)+steps1)//2+1
res2 = (abs(s2)+steps2)//2+1
sys.stdout.write(f"{res1} {res2}")