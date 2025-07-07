import re, sys
def run_game(players, last_marble):
    scores = [0] * players
    size = last_marble + 1
    left = [0] * size
    right = [0] * size
    curr = 0
    player = 0
    for marble in range(1, size):
        if marble % 23 == 0:
            m = curr
            for _ in range(7):
                m = left[m]
            scores[player] += marble + m
            ln = left[m]
            rn = right[m]
            right[ln] = rn
            left[rn] = ln
            curr = rn
        else:
            first = right[curr]
            second = right[first]
            right[first] = marble
            left[marble] = first
            right[marble] = second
            left[second] = marble
            curr = marble
        player += 1
        if player == players:
            player = 0
    return max(scores)

infile = sys.argv[1]
with open(infile) as f:
    players, last = map(int, re.findall(r'\d+', f.readline()))
out1 = run_game(players, last)
out2 = run_game(players, last * 100)
sys.stdout.write(f"{out1} {out2}")