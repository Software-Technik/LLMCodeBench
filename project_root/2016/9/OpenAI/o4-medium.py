import sys

def part1(data):
    total = i = 0
    n = len(data)
    while i < n:
        if data[i] == '(':
            j = data.find(')', i)
            a, b = map(int, data[i+1:j].split('x'))
            total += a * b
            i = j + 1 + a
        else:
            total += 1
            i += 1
    return total

def part2(data):
    def helper(i, end):
        total = 0
        while i < end:
            if data[i] == '(':
                j = data.find(')', i)
                a, b = map(int, data[i+1:j].split('x'))
                i = j + 1
                total += b * helper(i, i + a)
                i += a
            else:
                total += 1
                i += 1
        return total
    return helper(0, len(data))

data = open(sys.argv[1], 'r').read()
sys.stdout.write(f"{part1(data)} {part2(data)}")