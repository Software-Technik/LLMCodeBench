import sys
from dataclasses import dataclass
from functools import lru_cache

@dataclass(eq=True, frozen=True)
class State:
    position1: int
    position2: int
    score1: int
    score2: int
    player_turn: int

dicesum_odds = (
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1),
)

def new_position(position, dice_sum):
    return (position + dice_sum - 1) % 10 + 1

@lru_cache(maxsize=None)
def count_wins(s: State):
    if s.score1 >= 21:
        return (1, 0)
    if s.score2 >= 21:
        return (0, 1)

    wins = [0, 0]
    for dice_sum, odds in dicesum_odds:
        if s.player_turn == 1:
            pos = new_position(s.position1, dice_sum)
            new_s = State(pos, s.position2, s.score1 + pos, s.score2, 2)
        else:
            pos = new_position(s.position2, dice_sum)
            new_s = State(s.position1, pos, s.score1, s.score2 + pos, 1)
        result = count_wins(new_s)
        wins[0] += result[0] * odds
        wins[1] += result[1] * odds

    return tuple(wins)

def part1(data):
    position_1 = int(data[0].split(" ")[-1])
    position_2 = int(data[1].split(" ")[-1])
    score_1, score_2 = 0, 0

    die_value, rolled = 0, 0

    def roll():
        nonlocal die_value, rolled
        rolled += 1
        die_value = die_value % 100 + 1
        return die_value

    while True:
        position_1 = (position_1 + roll() + roll() + roll() - 1) % 10 + 1
        score_1 += position_1
        if score_1 >= 1000:
            return score_2 * rolled

        position_2 = (position_2 + roll() + roll() + roll() - 1) % 10 + 1
        score_2 += position_2
        if score_2 >= 1000:
            return score_1 * rolled

def part2(data):
    position1 = int(data[0].split(" ")[-1])
    position2 = int(data[1].split(" ")[-1])
    return max(count_wins(State(position1, position2, 0, 0, 1)))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")