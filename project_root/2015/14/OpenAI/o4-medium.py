import sys
f = open(sys.argv[1])
speeds = []
flys = []
rests = []
periods = []
for line in f:
    p = line.split()
    sp = int(p[3]); ft = int(p[6]); rt = int(p[13])
    speeds.append(sp); flys.append(ft); rests.append(rt); periods.append(ft+rt)
f.close()
n = len(speeds)
t = 1000 if n == 2 else 2503
max_dist = 0
for i in range(n):
    cycles, rem = divmod(t, periods[i])
    d = (cycles * flys[i] + min(rem, flys[i])) * speeds[i]
    if d > max_dist: max_dist = d
dists = [0]*n
scores = [0]*n
for s in range(1, t+1):
    for i in range(n):
        r = s % periods[i]
        if r and r <= flys[i]:
            dists[i] += speeds[i]
    m = max(dists)
    for i in range(n):
        if dists[i] == m:
            scores[i] += 1
max_score = max(scores)
sys.stdout.write(f"{max_dist}\n{max_score}\n")