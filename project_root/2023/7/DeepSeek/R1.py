import sys
from collections import Counter

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

CARDS = {
    "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10,
    "9": 9, "8": 8, "7": 7, "6": 6, "5": 5,
    "4": 4, "3": 3, "2": 2
}

CARDS_PART2 = {
    "A": 14, "K": 13, "Q": 12, "T": 10, "9": 9,
    "8": 8, "7": 7, "6": 6, "5": 5, "4": 4,
    "3": 3, "2": 2, "J": 1
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
    if jokers == 5:
        return FIVE_OF_A_KIND
    hand_without_jokers = hand.replace('J', '')
    counter = Counter(hand_without_jokers)
    counts = sorted(counter.values(), reverse=True)
    counts[0] += jokers
    if counts[0] == 5:
        return FIVE_OF_A_KIND
    if counts[0] == 4:
        return FOUR_OF_A_KIND
    if counts[0] == 3:
        return FULL_HOUSE if counts[1] == 2 else THREE_OF_A_KIND
    return ONE_PAIR

def part1(text: str) -> int:
    lines = text.splitlines()
    cards = [line.split() for line in lines]
    hand_data = []
    for hand, bid in cards:
        hand_type = get_hand_type(hand)
        card_vals = tuple(CARDS[c] for c in hand)
        hand_data.append((hand_type, card_vals, int(bid)))
    hand_data.sort()
    total = 0
    for i, (_, _, bid) in enumerate(hand_data):
        total += (i + 1) * bid
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    cards = [line.split() for line in lines]
    hand_data = []
    for hand, bid in cards:
        hand_type = get_hand_type_with_jokers(hand)
        card_vals = tuple(CARDS_PART2[c] for c in hand)
        hand_data.append((hand_type, card_vals, int(bid)))
    hand_data.sort()
    total = 0
    for i, (_, _, bid) in enumerate(hand_data):
        total += (i + 1) * bid
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")