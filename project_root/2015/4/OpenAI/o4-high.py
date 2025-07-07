import sys, hashlib
from itertools import count

def main():
    fn = sys.argv[1]
    with open(fn) as f:
        key = f.readline().strip()
    base = hashlib.md5(key.encode())
    cpy = base.copy
    s = str
    p1 = p2 = None
    for i in count(1):
        m = cpy()
        m.update(s(i).encode())
        h = m.digest()
        z = h[0] | h[1]
        if z == 0:
            t = h[2]
            if p1 is None and t < 16:
                p1 = i
            if p2 is None and t == 0:
                p2 = i
            if p1 is not None and p2 is not None:
                break
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == "__main__":
    main()