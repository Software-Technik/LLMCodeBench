import sys
def main():
    data = sys.argv[1]
    with open(data) as f:
        words = f.read().strip().split(",")
    total1 = 0
    boxes = [{} for _ in range(256)]
    for w in words:
        h = 0
        for c in w:
            h = (h + ord(c)) * 17 & 0xFF
        total1 += h
        if "=" in w:
            lbl, val = w.split("=")
            boxes[h][lbl] = int(val)
        else:
            lbl = w.split("-")[0]
            boxes[h].pop(lbl, None)
    total2 = 0
    for i, box in enumerate(boxes):
        mul_i = i + 1
        for j, (_, v) in enumerate(box.items(), 1):
            total2 += mul_i * j * v
    sys.stdout.write(f"{total1} {total2}")

if __name__ == "__main__":
    main()