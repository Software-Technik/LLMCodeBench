import sys,re
from array import array
def main():
    with open(sys.argv[1]) as f:
        players, last = map(int, re.findall(r'\d+', f.readline()))
    t1 = last
    t2 = last * 100
    size = t2 + 1
    nxt = array('I', [0]) * size
    prv = array('I', [0]) * size
    scores = [0] * players
    current = 0
    player = 0
    part1 = 0
    for mar in range(1, size):
        if mar % 23 == 0:
            for _ in range(7):
                current = prv[current]
            removed = current
            left = prv[removed]
            right = nxt[removed]
            nxt[left] = right
            prv[right] = left
            scores[player] += mar + removed
            current = right
        else:
            a = nxt[current]
            b = nxt[a]
            nxt[a] = mar
            prv[mar] = a
            nxt[mar] = b
            prv[b] = mar
            current = mar
        if mar == t1:
            part1 = max(scores)
        player += 1
        if player == players:
            player = 0
    part2 = max(scores)
    sys.stdout.write(f"{part1} {part2}")
if __name__ == "__main__":
    main()