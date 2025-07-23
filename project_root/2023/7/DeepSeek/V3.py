import sys
from functools import cmp_to_key
from collections import Counter

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

CARDS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

CARDS_J = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

def get_hand_type(hand):
    counter = Counter(hand)
    counts = sorted(counter.values(), reverse=True)
    if counts[0] == 5:
        return FIVE_OF_A_KIND
    if counts[0] == 4:
        return FOUR_OF_A_KIND
    if counts[0] == 3:
        return FULL_HOUSE if counts[1] == 2 else THREE_OF_A_KIND
    if counts[0] == 2:
        return TWO_PAIR if counts[1] == 2 else ONE_PAIR
    return HIGH_CARD

def get_hand_type_with_jokers(hand):
    jokers = hand.count('J')
    if jokers == 0:
        return get_hand_type(hand)
    counts = sorted(Counter(hand.replace('J', '')).values(), reverse=True)
    if not counts:
        return FIVE_OF_A_KIND
    counts[0] += jokers
    if counts[0] >= 5:
        return FIVE_OF_A_KIND
    if counts[0] == 4:
        return FOUR_OF_A_KIND
    if counts[0] == 3:
        return FULL_HOUSE if len(counts) > 1 and counts[1] == 2 else THREE_OF_A_KIND
    if counts[0] == 2:
        return TWO_PAIR if len(counts) > 1 and counts[1] == 2 else ONE_PAIR
    return HIGH_CARD

def cmp(a, b):
    a_hand, a_type = a[0], get_hand_type(a[0])
    b_hand, b_type = b[0], get_hand_type(b[0])
    if a_type != b_type:
        return a_type - b_type
    for ca, cb in zip(a_hand, b_hand):
        va, vb = CARDS[ca], CARDS[cb]
        if va != vb:
            return va - vb
    return 0

def cmp_j(a, b):
    a_hand, a_type = a[0], get_hand_type_with_jokers(a[0])
    b_hand, b_type = b[0], get_hand_type_with_jokers(b[0])
    if a_type != b_type:
        return a_type - b_type
    for ca, cb in zip(a_hand, b_hand):
        va, vb = CARDS_J[ca], CARDS_J[cb]
        if va != vb:
            return va - vb
    return 0

def part1(text: str) -> int:
    cards = [line.split() for line in text.splitlines()]
    cards.sort(key=cmp_to_key(cmp))
    return sum((i + 1) * int(hand[1]) for i, hand in enumerate(cards))

def part2(text: str) -> int:
    cards = [line.split() for line in text.splitlines()]
    cards.sort(key=cmp_to_key(cmp_j))
    return sum((i + 1) * int(hand[1]) for i, hand in enumerate(cards))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    print(f"{part1(text)} {part2(text)}")