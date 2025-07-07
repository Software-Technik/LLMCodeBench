import sys

def part1(data):
    i = 0
    total = 0
    n = len(data)
    while i < n:
        if data[i] == '(':
            j = i + 1
            while data[j] != ')': j += 1
            a,b = data[i+1:j].split('x')
            A, B = int(a), int(b)
            total += A * B
            i = j + 1 + A
        else:
            total += 1
            i += 1
    return total

def part2(data, i=0, j=None):
    if j is None: j = len(data)
    total = 0
    while i < j:
        if data[i] == '(':
            k = i + 1
            while data[k] != ')': k += 1
            a,b = data[i+1:k].split('x')
            A, B = int(a), int(b)
            i = k + 1
            total += B * part2(data, i, i + A)
            i += A
        else:
            total += 1
            i += 1
    return total

with open(sys.argv[1], 'r') as f:
    data = f.read().strip()
print(part1(data), part2(data))