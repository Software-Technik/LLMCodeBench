import re, sys
from collections import deque

def run_game(players, last_marb):
    scores = [0] * players
    circle = deque([0])
    player = 0
    for marble in range(1, last_marb + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += circle.popleft() + marble
        else:
            circle.rotate(-2)
            circle.appendleft(marble)
        player = (player + 1) % players
    return max(scores)

input_file = sys.argv[1]
with open(input_file, 'r') as file:
    data = file.readline()
    players, last_marb = map(int, re.findall(r'\d+', data))

part1 = run_game(players, last_marb)
part2 = run_game(players, last_marb * 100)
sys.stdout.write(f"{part1} {part2}")