import sys

def part1(text: str) -> int:
    total = 0
    for word in text.strip().split(","):
        subtotal = 0
        for c in word:
            subtotal = ((subtotal + ord(c)) * 17) % 256
        total += subtotal

    return total

def get_hash(word: str) -> int:
    total = 0
    for c in word:
        total = ((total + ord(c)) * 17) % 256
    return total


def part2(text: str) -> int:
    boxes = [{} for _ in range(256)]

    for word in text.strip().split(","):
        if "=" in word:
            label, focall = word.split("=")
            box_i = get_hash(label)
            boxes[box_i][label] = int(focall)
        else:
            label = word.split("-")[0]
            box_i = get_hash(label)
            boxes[box_i].pop(label, None)

    total = 0
    for box_i, box in enumerate(boxes):
        for label_i, (label, focall) in enumerate(box.items()):
            total += (box_i + 1) * (label_i + 1) * focall
    return total



inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")