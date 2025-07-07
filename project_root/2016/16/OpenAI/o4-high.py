import sys
DISK_SIZES = 272, 35651584
TRANS = bytes.maketrans(b'01', b'10')
def fill_disk(data, size):
    d = bytearray(data, 'ascii')
    while len(d) < size:
        r = d[::-1].translate(TRANS)
        d += b'0' + r
    del d[size:]
    return d
def checksum(d):
    while len(d) % 2 == 0:
        n = len(d) // 2
        o = bytearray(n)
        for i in range(n):
            o[i] = 49 if d[2*i] == d[2*i+1] else 48
        d = o
    return d.decode()
s = open(sys.argv[1]).read().strip()
print(checksum(fill_disk(s, DISK_SIZES[0])), checksum(fill_disk(s, DISK_SIZES[1])))