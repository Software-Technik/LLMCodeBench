import sys
import numpy as np

def part1(data):
    data = [x.split('|') for x in data]
    data = [(i.split(), o.split()) for i, o in data]

    total = 0
    for d in data:
        nb_segments = [len(x) for x in d[1]]
        nb_segments = np.array(nb_segments)
        is1 = (nb_segments == 2).sum()
        is4 = (nb_segments == 4).sum()
        is7 = (nb_segments == 3).sum()
        is8 = (nb_segments == 7).sum()
        total += is1 + is4 + is7 + is8

    return total    # 416

def part2(data):
    data = [x.split('|') for x in data]
    data = [(i.split(), o.split()) for i, o in data]


    def intersect(a, b):
        return len(set(a).intersection(b))


    total = 0
    for d in data:

        # Find wires representations of 1, 4, 7, 8 based on number of wires used
        for n in d[0]:
            n = ''.join(sorted(n))
            length = len(n)

            # 1 has 2 segments
            if length == 2:
                one = n
            # 4 has 4 segments
            elif length == 4:
                four = n
            # 7 has 3 segments
            elif length == 3:
                seven = n
            # 8 has 7 segments
            elif length == 7:
                eight = n

        # Deduce others digits only by comparing wires with representation of 1, 4, 7, 8
        for n in d[0]:
            n = ''.join(sorted(n))
            length = len(n)

            # 0, 6 and 9 have 6 segments
            if length == 6:
                if intersect(n, four) == 4:
                    nine = n
                elif intersect(n, one) == 2:
                    zero = n
                else:
                    six = n

            # 2, 3 and 5 have 5 segments
            if length == 5:
                if intersect(n, one) == 2:
                    three = n
                elif intersect(n, four) == 2:
                    two = n
                else:
                    five = n

        match = {
            zero: '0',
            one: '1',
            two: '2',
            three: '3',
            four: '4',
            five: '5',
            six: '6',
            seven: '7',
            eight: '8',
            nine: '9'
        }

        value = ''.join(match[''.join(sorted(x))] for x in d[1])
        total += int(value)

    return total    # 1043697

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")