import sys

table = bytes.maketrans(b'01', b'10')

def fill_disk(data, size):
    while len(data) < size:
        data = data + b'0' + data[::-1].translate(table)
    return data[:size]

def checksum(data):
    while not len(data) & 1:
        n = len(data) // 2
        b = bytearray(n)
        d = data
        for i in range(n):
            b[i] = 49 if d[2*i] == d[2*i+1] else 48
        data = b
    return data.decode()

with open(sys.argv[1], 'rb') as f:
    data = f.read().strip()
p1 = checksum(fill_disk(data, 272))
p2 = checksum(fill_disk(data, 35651584))
sys.stdout.write(p1 + ' ' + p2)