import sys



def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        winning_numbers, numbers = line.split(":", maxsplit=1)[1].split("|", maxsplit=1)
        winning_numbers = set(winning_numbers.split())
        numbers = set(numbers.split())
        resulted_numbers = winning_numbers.intersection(numbers)
        if resulted_numbers:
            total += 2 ** (len(resulted_numbers) - 1)
    return total

cache = {}


def get_card_points(cards, card) -> int:
    if card in cache:
        return cache[card]

    total = cards[card]
    for i in range(cards[card]):
        total += get_card_points(cards, card + i + 1)

    cache[card] = total
    return total


def part2(text: str) -> int:
    cards = []
    for line in text.splitlines():
        winning_numbers, numbers = line.split(":", maxsplit=1)[1].split("|", maxsplit=1)
        winning_numbers = set(winning_numbers.split())
        numbers = set(numbers.split())
        resulted_numbers = winning_numbers.intersection(numbers)
        cards.append(len(resulted_numbers))

    cache.clear()
    total = 0
    for i in range(len(cards)):
        total += get_card_points(cards, i) + 1
    return total



inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")