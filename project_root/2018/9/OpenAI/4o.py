import re, sys
from collections import deque

def run_game(players, last_marb):
    scores = [0] * players
    circle = deque([0])
    player = 0
    for next_marble in range(1, last_marb):
        if next_marble % 23 == 0:
            circle.rotate(7)
            scores[player] += circle.popleft() + next_marble
        else:
            circle.rotate(-2)
            circle.appendleft(next_marble)
        player = (player + 1) % players
    return max(scores)

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as file:
    players, last_marb = map(int, re.findall(r'\d+', file.readline()))

sys.stdout.write(f"{run_game(players, last_marb)} {run_game(players, last_marb * 100)}")