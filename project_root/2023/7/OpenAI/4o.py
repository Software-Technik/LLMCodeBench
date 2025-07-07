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

def get_hand_type(hand):
    counter = Counter(hand)
    counts = sorted(counter.values(), reverse=True)
    if counts == [5]:
        return FIVE_OF_A_KIND
    if counts == [4, 1]:
        return FOUR_OF_A_KIND
    if counts in ([3, 2],):
        return FULL_HOUSE
    if counts == [3, 1, 1]:
        return THREE_OF_A_KIND
    if counts == [2, 2, 1]:
        return TWO_PAIR
    if counts == [2, 1, 1, 1]:
        return ONE_PAIR
    return HIGH_CARD

def get_hand_type_with_jokers(hand):
    hand_without_jokers = hand.replace("J", "")
    jokers = len(hand) - len(hand_without_jokers)
    hand_type = get_hand_type(hand_without_jokers)
    if not jokers:
        return hand_type
    if hand_type == FOUR_OF_A_KIND or (hand_type == THREE_OF_A_KIND and jokers >= 1):
        return FIVE_OF_A_KIND
    if hand_type == THREE_OF_A_KIND:
        return FOUR_OF_A_KIND
    if hand_type == TWO_PAIR or (hand_type == ONE_PAIR and jokers >= 2):
        return FULL_HOUSE
    if hand_type == ONE_PAIR:
        return THREE_OF_A_KIND
    if jokers == 1:
        return ONE_PAIR
    if jokers == 2:
        return THREE_OF_A_KIND
    if jokers == 3:
        return FOUR_OF_A_KIND
    return FIVE_OF_A_KIND

def cmp(a, b):
    a, b = a[0], b[0]
    a_type, b_type = get_hand_type(a), get_hand_type(b)
    if a_type != b_type:
        return a_type - b_type
    return sum(CARDS[card_a] - CARDS[card_b] for card_a, card_b in zip(a, b))

def solve(text: str) -> (int, int):
    cards = [line.split() for line in text.splitlines()]
    sorted_cards = sorted(cards, key=lambda hand: (get_hand_type_with_jokers(hand[0]), [CARDS[c] for c in hand[0]]))
    return sum((i + 1) * int(hand[1]) for i, hand in enumerate(sorted_cards)), sum((i + 1) * int(hand[1]) for i, hand in enumerate(sorted_cards))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{solve(text)}")