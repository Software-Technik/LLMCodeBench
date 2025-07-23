import sys

def get_hash(word: str) -> int:
    value = 0
    for char in word:
        value = (value + ord(char)) * 17 % 256
    return value

def part1(text: str) -> int:
    return sum(((val := ((value := 0) + ord(c)) * 17) % 256) for line in text.strip().split(",") for c in line)

def part2(text: str) -> int:
    boxes = [[] for _ in range(256)]

    for word in text.strip().split(","):
        if '=' in word:
            label, focal = word.split('=')
            hash_val = get_hash(label)
            try:
                old_index = next(i for i, (l, f) in enumerate(boxes[hash_val]) if l == label)
                boxes[hash_val][old_index] = (label, int(focal))
            except StopIteration:
                boxes[hash_val].append((label, int(focal)))
        elif '-' in word:
            label = word[:-1]
            hash_val = get_hash(label)
            try:
                box = boxes[hash_val]
                box[:] = [elem for elem in box if elem[0] != label]
            except IndexError:
                continue

    result = 0
    for box_id, box in enumerate(boxes):
        for slot_id, (label, focal) in enumerate(box):
            result += (box_id + 1) * (slot_id + 1) * focal
    return result

input_file = sys.argv[1]
with open(input_file, 'r') as f:
    text = f.read().strip()
sys.stdout.write(f"{part1(text)} {part2(text)}\n")