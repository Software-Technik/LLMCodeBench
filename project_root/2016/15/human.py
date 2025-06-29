import sys
import re


def wait_a_sec(discs):
    time = 0
    while True:
        if not sum((position+time)%slot for (slot, position) in discs):
            return time
        time += 1


def part1(data):
    discs = []
    for i, line in enumerate(data, 1):
        settings = re.search(r'(\d+) positions; .+ (\d+)', line)
        slots = int(settings.group(1))
        position = int(settings.group(2)) + i
        discs.append((slots, position))
    time = 0
    wait_a_sec(discs)


def part2(data):
    discs = []
    for i, line in enumerate(data, 1):
        settings = re.search(r'(\d+) positions; .+ (\d+)', line)
        slots = int(settings.group(1))
        position = int(settings.group(2)) + i
        discs.append((slots, position))
    discs.append((11, 0+7))
    time = 0
    wait_a_sec(discs)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read().split('\n')


sys.stdout.write(f"{part1(data)} {part2(data)}")  

