import sys

def part1(text: str) -> int:
    total = 0
    for word in text.strip().split(","):
        subtotal = 0
        for c in word:
            subtotal = ((subtotal + ord(c)) * 17) & 0xFF
        total += subtotal
    return total

def get_hash(word: str) -> int:
    total = 0
    for c in word:
        total = ((total + ord(c)) * 17) & 0xFF
    return total

def part2(text: str) -> int:
    boxes = [{} for _ in range(256)]
    for word in text.strip().split(","):
        if "=" in word:
            label, val = word.split("=")
            h = get_hash(label)
            boxes[h][label] = int(val)
        else:
            label = word.split("-", 1)[0]
            boxes[get_hash(label)].pop(label, None)
    total = 0
    for i, box in enumerate(boxes, 1):
        for j, (_, v) in enumerate(box.items(), 1):
            total += i * j * v
    return total

text = open(sys.argv[1]).read()
print(part1(text), part2(text))