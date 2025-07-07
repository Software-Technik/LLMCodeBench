import sys

def calculate_hash(word: str) -> int:
    total = 0
    for c in word:
        total = ((total + ord(c)) * 17) % 256
    return total

def part1(text: str) -> int:
    total = sum(calculate_hash(word) for word in text.strip().split(","))
    return total

def part2(text: str) -> int:
    boxes = [{} for _ in range(256)]

    for word in text.strip().split(","):
        if "=" in word:
            label, focall = word.split("=")
            box_i = calculate_hash(label)
            boxes[box_i][label] = int(focall)
        else:
            label = word.split("-")[0]
            box_i = calculate_hash(label)
            if label in boxes[box_i]:
                del boxes[box_i][label]

    total = sum((box_i + 1) * (label_i + 1) * focall 
                for box_i, box in enumerate(boxes)
                for label_i, focall in enumerate(box.values()))

    return total

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")