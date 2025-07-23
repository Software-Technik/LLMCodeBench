import sys

def part1(boxes):
    total = 0
    for box in boxes:
        l, w, h = box
        lw = l * w
        lh = l * h
        wh = w * h
        total += 2 * (lw + lh + wh) + min(lw, lh, wh)
    return total

def part2(boxes):
    total = 0
    for box in boxes:
        l, w, h = box
        sorted_box = sorted(box)
        total += 2 * (sorted_box[0] + sorted_box[1]) + l * w * h
    return total

with open(sys.argv[1]) as f:
    boxes = [tuple(map(int, line.strip().split('x'))) for line in f]

sys.stdout.write(f"{part1(boxes)}\n{part2(boxes)}\n")