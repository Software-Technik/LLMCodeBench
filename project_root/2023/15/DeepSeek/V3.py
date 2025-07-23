import sys

def get_hash(word: str) -> int:
    total = 0
    for c in word:
        total = ((total + ord(c)) * 17) & 255
    return total

def part1(text: str) -> int:
    total = 0
    for word in text.strip().split(","):
        total += get_hash(word)
    return total

def part2(text: str) -> int:
    boxes = [{} for _ in range(256)]
    for word in text.strip().split(","):
        if "=" in word:
            label, focall = word.split("=")
            boxes[get_hash(label)][label] = int(focall)
        else:
            label = word[:-1]
            boxes[get_hash(label)].pop(label, None)
    total = 0
    for box_i, box in enumerate(boxes, 1):
        for slot_i, focall in enumerate(box.values(), 1):
            total += box_i * slot_i * focall
    return total

with open(sys.argv[1]) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")