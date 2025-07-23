import sys
counter, claim_id = {}, {}

for label in open(sys.argv[1]):
    number, _, specs = label.partition(" @ ")
    coor, _, size = specs.partition(": ")
    x, y = map(int, coor.split(","))
    width, height = map(int, size.strip().split("x"))
    claim_id[int(number[1:])] = (x, y)

    for i in range(width):
        for j in range(height):
            if (x+i,y+j) not in counter:
                counter[(x+i,y+j)] = [int(number[1:])]
            else:
                claimed_id = counter[x+i,y+j]+[int(number[1:])]
                for id_ in claimed_id:
                    claim_id[id_] = 0
                counter[x+i,y+j] = claimed_id

overlap_squares,claim_without_overlap= sum(len(v)> 1   for v in counter.values()), [k for k,v in claim_id.items() if v][0]

sys.stdout.write(f"{overlap_squares} {claim_without_overlap}")