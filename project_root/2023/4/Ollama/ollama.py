import sys

def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        _, numbers_str = line.split(":")
        winning_numbers, drawn_numbers = map(str.split, numbers_str.split("|"))
        winning_set = set(winning_numbers)
        drawn_set = set(drawn_numbers)
        matched_count = len(winning_set & drawn_set)
        if matched_count:
            total += 2 ** (matched_count - 1)
    return total

cache = {}

def get_card_points(cards, card) -> int:
    return cache.setdefault(card, cards[card] + sum(get_card_points(cards, card + i + 1) for i in range(cards[card])))

def part2(text: str) -> int:
    cards = [len(set(winning_numbers.split()) & set(drawn_numbers.split())) for _, numbers_str in (line.split(":") for line in text.splitlines()) for winning_numbers, drawn_numbers in (numbers_str.split("|"),)]
    cache.clear()
    return sum(get_card_points(cards, i) + 1 for i in range(len(cards)))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")