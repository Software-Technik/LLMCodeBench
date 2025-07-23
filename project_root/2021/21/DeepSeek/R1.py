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

    wins1, wins2 = 0, 0
    for dice_sum, odds in dicesum_odds:
        if s.player_turn == 1:
            pos = new_position(s.position1, dice_sum)
            new_s = State(pos, s.position2, s.score1 + pos, s.score2, 2)
        else:
            pos = new_position(s.position2, dice_sum)
            new_s = State(s.position1, pos, s.score1, s.score2 + pos, 1)
        w1, w2 = count_wins(new_s)
        wins1 += w1 * odds
        wins2 += w2 * odds

    return (wins1, wins2)


def part1(data):
    position1 = int(data[0].split(" ")[-1])
    position2 = int(data[1].split(" ")[-1])
    score1, score2 = 0, 0
    die_value = 1
    die_rolled = 0

    while True:
        total = 0
        for _ in range(3):
            total += die_value
            die_value = die_value % 100 + 1
            die_rolled += 1
        position1 = (position1 + total - 1) % 10 + 1
        score1 += position1
        if score1 >= 1000:
            return score2 * die_rolled

        total = 0
        for _ in range(3):
            total += die_value
            die_value = die_value % 100 + 1
            die_rolled += 1
        position2 = (position2 + total - 1) % 10 + 1
        score2 += position2
        if score2 >= 1000:
            return score1 * die_rolled


def part2(data):
    position1 = int(data[0].split(" ")[-1])
    position2 = int(data[1].split(" ")[-1])
    wins1, wins2 = count_wins(State(position1, position2, 0, 0, 1))
    return wins1 if wins1 > wins2 else wins2


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")