import sys

first = second = 0
with open(sys.argv[1]) as f:
    for line in f:
        words = line.split()
        seen = set()
        ok1 = True
        for w in words:
            if w in seen:
                ok1 = False
                break
            seen.add(w)
        if ok1:
            first += 1
        seen2 = set()
        ok2 = True
        for w in words:
            s = ''.join(sorted(w))
            if s in seen2:
                ok2 = False
                break
            seen2.add(s)
        if ok2:
            second += 1
print(first)
print(second)