import sys
with open(sys.argv[1]) as f:
    data = [l.strip() for l in f if l.strip()]
repls = [line.split(" => ") for line in data[:-1]]
mol = data[-1]
new = set()
for a,b in repls:
    start = 0
    la = len(a)
    while True:
        i = mol.find(a, start)
        if i < 0: break
        new.add(mol[:i] + b + mol[i+la:])
        start = i + 1
cnt1 = len(new)
cnt = rn = ar = y = 0
s = mol
i = 0
L = len(s)
while i < L:
    c = s[i]
    if c.isupper():
        if i+1 < L and s[i+1].islower():
            tok = s[i:i+2]; i += 2
        else:
            tok = c; i += 1
        cnt += 1
        if tok == "Rn": rn += 1
        elif tok == "Ar": ar += 1
        elif tok == "Y": y += 1
    else:
        i += 1
cnt2 = cnt - rn - ar - 2*y - 1
sys.stdout.write(f"{cnt1}\n{cnt2}\n")