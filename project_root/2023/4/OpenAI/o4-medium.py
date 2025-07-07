import sys
data = open(sys.argv[1]).read().splitlines()
total1 = 0
cards = []
for line in data:
    if not line: continue
    w,n = line.split(':',1)[1].split('|',1)
    a = w.split(); b = n.split()
    if len(a) < len(b):
        sset = set(a); other = b
    else:
        sset = set(b); other = a
    c = 0
    for x in other:
        if x in sset: c += 1
    if c: total1 += 1 << (c-1)
    cards.append(c)
n = len(cards)
F = [0]*n
pref = [0]*(n+1)
for i in range(n-1, -1, -1):
    end = i + cards[i]
    if end >= n: end = n-1
    s = pref[i+1] - pref[end+1]
    F[i] = cards[i] + s
    pref[i] = F[i] + pref[i+1]
total2 = pref[0] + n
sys.stdout.write(f"{total1} {total2}")