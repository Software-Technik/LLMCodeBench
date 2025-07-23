import sys

def get_hash(word: str) -> int:
    total = 0
    for c in word:
        total = ((total + ord(c)) * 17) % 256
    return total

def part1(words: list) -> int:
    return sum(get_hash(word) for word in words)

def part2(words: list) -> int:
    boxes = [{} for _ in range(256)]
    for word in words:
        if word[-1] == '-':
            label = word[:-1]
            box_i = get_hash(label)
            boxes[box_i].pop(label, None)
        else:
            label = word[:-2]
            focall = int(word[-1])
            box_i = get_hash(label)
            boxes[box_i][label] = focall

    total = 0
    for box_i, box in enumerate(boxes):
        for slot_i, (_, focall) in enumerate(box.items(), start=1):
            total += (box_i + 1) * slot_i * focall
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    words = f.read().strip().split(',')

sys.stdout.write(f"{part1(words)} {part2(words)}")