import sys
def main():
    f = open(sys.argv[1])
    reps = []
    rev = []
    mol = ''
    for line in f:
        line = line.strip()
        if not line:
            continue
        if '=>' in line:
            a, b = line.split(' => ')
            reps.append((a, b))
            rev.append((b, a))
        else:
            mol = line
    f.close()
    new = set()
    add = new.add
    find = mol.find
    for a, b in reps:
        la = len(a)
        i = 0
        while True:
            idx = mol.find(a, i)
            if idx < 0:
                break
            add(mol[:idx] + b + mol[idx+la:])
            i = idx + 1
    out1 = len(new)
    mol2 = mol
    count = 0
    while mol2 != 'e':
        best_i = -1
        for rep, orig in rev:
            if orig == 'e' and rep != mol2:
                continue
            idx = mol2.rfind(rep)
            if idx > best_i:
                best_i = idx
                br = rep
                bo = orig
        mol2 = mol2[:best_i] + bo + mol2[best_i+len(br):]
        count += 1
    sys.stdout.write(f"{out1}\n{count}\n")
if __name__ == '__main__':
    main()