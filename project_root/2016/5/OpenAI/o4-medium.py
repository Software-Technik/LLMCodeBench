import hashlib, sys

hex_digits = '0123456789abcdef'
with open(sys.argv[1], 'r') as f:
    data = f.readline().strip()

first = []
second = [''] * 8
remain = 8
i = 0

while len(first) < 8 or remain:
    m = hashlib.md5((data + str(i)).encode()).digest()
    if m[0] == 0 and m[1] == 0 and m[2] < 16:
        c = hex_digits[m[2]]
        if len(first) < 8:
            first.append(c)
        p = m[2]
        if p < 8 and second[p] == '':
            second[p] = hex_digits[m[3] >> 4]
            remain -= 1
    i += 1

sys.stdout.write(''.join(first) + ' ' + ''.join(second))