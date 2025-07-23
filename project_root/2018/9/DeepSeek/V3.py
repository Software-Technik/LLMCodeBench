import re
import sys
from collections import deque

def run_game(players, last_marb):
    scores = [0] * players
    circle = deque([0])
    next_marble = 0
    player = 0
    while True:
        next_marble += 1
        if next_marble > last_marb:
            break
        if next_marble % 23 == 0:
            circle.rotate(7)
            scores[player] += circle.popleft() + next_marble
        else:
            circle.rotate(-2)
            circle.appendleft(next_marble)
        player = (player + 1) % players
    return max(scores)

with open(sys.argv[1], 'r') as file:
    players, last_marb = map(int, re.findall(r'\d+', file.readline()))

print(f"{run_game(players, last_marb)} {run_game(players, last_marb * 100)}")