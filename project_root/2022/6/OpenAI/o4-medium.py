import sys

def find_marker(buf, size):
    counts = [0] * 256
    unique = 0
    for i, ch in enumerate(buf):
        o = ord(ch)
        counts[o] += 1
        if counts[o] == 1:
            unique += 1
        elif counts[o] == 2:
            unique -= 1
        if i >= size:
            o2 = ord(buf[i-size])
            counts[o2] -= 1
            if counts[o2] == 1:
                unique += 1
            elif counts[o2] == 0:
                unique -= 1
        if i >= size-1 and unique == size:
            return i + 1

with open(sys.argv[1]) as f:
    buf = f.readline().rstrip('\n')
print(find_marker(buf, 4))
print(find_marker(buf, 14))