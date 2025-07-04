import sys

def part1(file_path):
    with open(file_path, 'r') as file:
        target = int(file.readline().rstrip("\n"))

    scores = [ 3, 7 ]
    elf1, elf2 = 0, 1
    limit = 10 + target
    while (limit := limit-1):
        scores += [ int(c) for c in str(scores[elf1] + scores[elf2]) ]
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

    return ''.join([ str(n) for n in scores[target:target+10] ])

def part2(file_path):
    with open(file_path, 'r') as file:
        num = int(file.readline().rstrip("\n"))
    target = [ int(c) for c in str(num) ]

    scores = [ 3, 7 ]
    elf1, elf2 = 0, 1
    cycle = 0
    while True:
        last_len = len(scores)
        scores += [ int(c) for c in str(scores[elf1] + scores[elf2]) ]
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)
        # Note that it's possible to get more than one number added to scores
        for idx in range(last_len+1, len(scores)+1):
            if scores[idx-len(target):idx] == target:
                return idx-len(target)


inout_strings = sys.argv[1]
sys.stdout.write(f"{part1(inout_strings)} {part2(inout_strings)}") 