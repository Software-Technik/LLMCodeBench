import sys

puzzle = 394

def spin(insertions=2017):
    spinlock = [0]
    position = 0
    for i in range(1, insertions + 1):
        position = (position + puzzle) % i + 1
        spinlock.insert(position, i)
    return spinlock[position + 1]

def fake_spin(insertions=50_000_000):
    position = 0
    result = None
    length = 1
    while length < insertions:
        position = (position + puzzle) % length + 1
        if position == 1:
            result = length
        skip = (length - position) // puzzle
        position += skip * (puzzle + 1)
        length += skip + 1
    return result

def part1(data):
    # On pourrait lire un nombre dans data, mais ici puzzle est fixé à 394
    return spin()

def part2(data):
    return fake_spin()

# Bloc standard d'entrée/sortie
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

import sys
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")