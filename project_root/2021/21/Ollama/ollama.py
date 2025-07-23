import sys
from dataclasses import dataclass
from functools import lru_cache

class Die:
    def __init__(self):
        self.value, self.rolled = 0, 0
    def roll(self):
        self.rolled += 1; self.value = (self.value % 100) + 1
        return self.value

@dataclass(eq=True, frozen=True)
class State:
    p1: int; p2: int; s1: int; s2: int; turn: int

def new_position(p, d):
    return (p + d - 1) % 10 + 1

dicesum_odds = ((3 , 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))

@lru_cache(None)
def count_wins(s: State):
    if s.s1 >= 21:
        return (1, 0) if s.turn == 1 else (0, 1)
    if s.s2 >= 21:
        return (0, 1) if s.turn == 2 else (1, 0)

    wins = [0, 0]
    for dice_sum, odds in dicesum_odds:
        new_pos = State(
            p1=new_position(s.p1, dice_sum) if s.turn == 1 else s.p1,
            p2=new_position(s.p2, dice_sum) if s.turn == 2 else s.p2,
            s1=s.s1 + (new_position(s.p1, dice_sum) if s.turn == 1 else 0),
            s2=s.s2 + (new_position(s.p2, dice_sum) if s.turn == 2 else 0),
            turn=3 - s.turn
        )
        wins[0] += count_wins(new_pos)[0] * odds if s.turn == 1 else count_wins(new_pos)[1] * odds
        wins[1] += count_wins(new_pos)[1] * odds if s.turn == 2 else count_wins(new_pos)[0] * odds

    return tuple(wins)

def part1(data):
    p1, p2 = int(data[0].split()[-1]), int(data[1].split()[-1])
    score_1, score_2 = 0, 0
    die = Die()

    while True:
        pos = sum(die.roll() for _ in range(3))
        p1 += pos - 1; p1 %= 10; p1 += 1
        score_1 += p1
        if score_1 >= 1000: return die.rolled * score_2

        pos = sum(die.roll() for _ in range(3))
        p2 += pos - 1; p2 %= 10; p2 += 1
        score_2 += p2
        if score_2 >= 1000: return die.rolled * score_1

def part2(data):
    p1, p2 = int(data[0].split()[-1]), int(data[1].split()[-1])
    state = State(p1, p2, 0, 0, 1)
    wins = count_wins(state)
    return max(wins)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

print(part1(data), part2(data))