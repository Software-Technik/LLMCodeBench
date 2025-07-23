import hashlib
import sys

def solve_combined(data):
    part1_chars = []
    part2_list = [''] * 8
    available = set(range(8))
    i = 0
    while len(part1_chars) < 8 or available:
        s = data + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h.startswith('00000'):
            if len(part1_chars) < 8:
                part1_chars.append(h[5])
            if '0' <= h[5] <= '7':
                pos = int(h[5])
                if pos in available:
                    part2_list[pos] = h[6]
                    available.remove(pos)
        i += 1
    return ''.join(part1_chars), ''.join(part2_list)

with open(sys.argv[1]) as f:
    data = f.readline().strip()

p1, p2 = solve_combined(data)
sys.stdout.write(f"{p1} {p2}")