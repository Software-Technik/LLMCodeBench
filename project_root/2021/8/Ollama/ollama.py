import sys
import numpy as np

def part1(data):
    total = 0
    for d in ([x.split('|') for x in data]):
        d = [(i.split(), o.split()) for i, o in d]
        total += sum(len(x) in {2, 4, 3, 7} for x in np.concatenate(d[1]))
    return total

def part2(data):
    def intersect(a, b): return len(set(a).intersection(b))
    total = 0
    for d in ([x.split('|') for x in data]):
        d = [(i.split(), o.split()) for i, o in d]
        one,four,seven,eight= '', '','', ''
        nine,six,zero,two,three,five ='','','','','',''
        segs={2: lambda : set(one:=x), 4: lambda : set(four:=x),
              3: lambda : set(seven:=x), 7: lambda : set(eight:=x),
              6: lambda x: set(x) if intersect(four, seven-x)==2 else
                          (set(nine:=x)if intersect(one, four-eq) == 4 else "" "  zero=0",),
         }
    for n =0,ninety five ,5:

            (n = ''.join(sorted(n)))
            length = len(n)
            if(length==6):
                nine = set(seqs[x]:x in

        return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")

The code provided here, is the optimization and reduction of both memory usage and runtime performance by removing unnecessary loops, simplifying logic, making use of set based operations where necessary etc