import sys

def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        winning_numbers, numbers = line.split(":", 1)[1].split("|", 1)
        resulted_numbers = set(winning_numbers.split()).intersection(numbers.split())
        if resulted_numbers:
            total += 1 << (len(resulted_numbers) - 1)
    return total

def get_card_points(cards, card, cache) -> int:
    if card in cache:
        return cache[card]
    result = cards[card]
    for i in range(cards[card]):
        result += get_card_points(cards, card + i + 1, cache)
    cache[card] = result
    return result

def part2(text: str) -> int:
    cards = []
    for line in text.splitlines():
        winning_numbers, numbers = line.split(":", 1)[1].split("|", 1)
        resulted_numbers = set(winning_numbers.split()).intersection(numbers.split())
        cards.append(len(resulted_numbers))
    cache = {}
    return sum(get_card_points(cards, i, cache) + 1 for i in range(len(cards)))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")