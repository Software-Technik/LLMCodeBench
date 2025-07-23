import sys
from functools import cmp_to_key, reduce
from collections import Counter

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

CARDS = "AKQJT98765432"

def rank(hand):
    return sorted(reduce(lambda acc, c: acc + Counter(c.replace("J", "")), hand, Counter()).values(), reverse=True)

def get_hand_type_with_jokers(hand):
    if len(set(hand) - {"J"}) == 1:
        return FIVE_OF_A_KIND
    counts = sorted((hand.count(c) for c in set(hand) if c != "J"), reverse=True)
    if len(counts) == 2 or (len(counts) > 2 and counts[0] - counts[1] >= 2):
        return FIVE_OF_A_KIND
    elif len(counts) == 3 or (len(counts) > 3 and counts[0] - counts[1] >= 2):
        return FOUR_OF_A_KIND + int("J" in set(hand))
    return TWO_PAIR if len(set([c for c in hand if c != "J"])) == 2 else ONE_PAIR

def cmp(a, b):
    a = a[0]
    b = b[0]
    types_a = get_hand_type_with_jokers(a)
    types_b = get_hand_type_with_jokers(b)
    if (diff := types_a - types_b) != 0:
        return diff
    for ai, bi in zip(a, b):
        ai, bi = CARDS.index(ai), CARDS.index(bi)
        if ai != bi:
            return ai - bi

def part1(text: str) -> int:
    cards = [line.split() for line in text.strip().splitlines()]
    cards.sort(key=cmp_to_key(cmp))
    winnings = (rank * int(bid) for rank, (_, bid) in enumerate(cards, start=1))
    return sum(winnings)

def part2(text: str):
    pass

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")