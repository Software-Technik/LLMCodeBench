import sys
import io

def part1(data):
    w, h = 25, 6
    layer_size = w * h
    best = None
    best_score = 0
    for i in range(0, len(data), layer_size):
        layer = data[i:i+layer_size]
        c0 = layer.count(0)
        if best is None or c0 < best:
            best = c0
            best_score = layer.count(1) * layer.count(2)
    return best_score

def part2(data):
    w, h = 25, 6
    layer_size = w * h
    pixels = []
    layers = len(data) // layer_size
    for p in range(layer_size):
        for l in range(layers):
            v = data[l*layer_size + p]
            if v < 2:
                pixels.append(v)
                break
        else:
            pixels.append(2)
    rows = []
    for r in range(h):
        row = ''
        for c in range(w):
            v = pixels[r*w+c]
            row += '█' if v==1 else '░' if v==0 else ' '
        rows.append(row)
    LETTERS = {
        tuple(v):k for k,v in {
    "A":["0110","1001","1111","1001","1001","1001"],
    "B":["1110","1001","1110","1001","1001","1110"],
    "C":["0110","1001","1000","1000","1001","0110"],
    "D":["1110","1001","1001","1001","1001","1110"],
    "E":["1111","1000","1110","1000","1000","1111"],
    "F":["1111","1000","1110","1000","1000","1000"],
    "G":["0111","1000","1000","1011","1001","0111"],
    "H":["1001","1001","1111","1001","1001","1001"],
    "I":["1110","0100","0100","0100","0100","1110"],
    "J":["0011","0001","0001","0001","1001","0110"],
    "K":["1001","1010","1100","1100","1010","1001"],
    "L":["1000","1000","1000","1000","1000","1111"],
    "M":["1001","1111","1111","1001","1001","1001"],
    "N":["1001","1101","1101","1011","1011","1001"],
    "O":["0110","1001","1001","1001","1001","0110"],
    "P":["1110","1001","1001","1110","1000","1000"],
    "Q":["0110","1001","1001","1001","1010","0101"],
    "R":["1110","1001","1001","1110","1010","1001"],
    "S":["0111","1000","0110","0001","0001","1110"],
    "T":["1111","0100","0100","0100","0100","0100"],
    "U":["1001","1001","1001","1001","1001","0110"],
    "V":["1001","1001","1001","1001","0110","0100"],
    "W":["1001","1001","1001","1111","1111","1001"],
    "X":["1001","1001","0110","0110","1001","1001"],
    "Y":["1001","1001","0110","0100","0100","0100"],
    "Z":["1111","0001","0010","0100","1000","1111"]
    }.items()}
    bin_rows = [r.replace('█','1').replace('░','0').replace(' ','0') for r in rows]
    result = ''
    for c in range(0, w, 5):
        block = tuple(r[c:c+4] for r in bin_rows)
        result += LETTERS.get(block, '?')
    return result

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().strip()))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout.write(f"{part1(data)} {part2(data)}")