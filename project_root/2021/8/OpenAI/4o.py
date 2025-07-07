import sys

def part1(data):
    data = [x.split('|') for x in data]
    total = 0
    for d in data:
        nb_segments = [len(x) for x in d[1].split()]
        total += sum(nb_segments.count(x) for x in (2, 4, 3, 7))
    return total

def part2(data):
    def intersect(a, b):
        return sum(1 for ch in a if ch in b)

    total = 0
    for entry in data:
        patterns, output = entry.split('|')
        patterns = [''.join(sorted(p)) for p in patterns.split()]

        one = four = seven = eight = ''
        for p in patterns:
            if len(p) == 2:
                one = p
            elif len(p) == 4:
                four = p
            elif len(p) == 3:
                seven = p
            elif len(p) == 7:
                eight = p

        match = {}
        for p in patterns:
            if len(p) == 6:
                if intersect(p, four) == 4:
                    match[p] = '9'
                elif intersect(p, one) == 2:
                    match[p] = '0'
                else:
                    match[p] = '6'
            elif len(p) == 5:
                if intersect(p, one) == 2:
                    match[p] = '3'
                elif intersect(p, four) == 2:
                    match[p] = '2'
                else:
                    match[p] = '5'
            else:
                match[p] = {'2': '1', '3': '7', '4': '4', '7': '8'}[str(len(p))]

        decoded_value = int(''.join(match[''.join(sorted(x))] for x in output.split()))
        total += decoded_value
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")