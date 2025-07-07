import hashlib
import sys

def main(data):
    i = 0
    pass1 = []
    pass2 = [''] * 8
    avail = set(range(8))
    db = data.encode()
    while len(pass1) < 8 or avail:
        s = db + str(i).encode()
        h = hashlib.md5(s).hexdigest()
        if h.startswith('00000'):
            c5 = h[5]
            if len(pass1) < 8:
                pass1.append(c5)
            pos = ord(c5) - 48
            if pos in avail:
                pass2[pos] = h[6]
                avail.remove(pos)
        i += 1
    return ''.join(pass1), ''.join(pass2)

if __name__ == '__main__':
    fn = sys.argv[1]
    with open(fn) as f:
        data = f.readline().strip()
    p1, p2 = main(data)
    sys.stdout.write(f"{p1} {p2}")