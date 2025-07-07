import sys
from collections import deque
from itertools import islice

def read_decks(path):
    with open(path) as f:
        parts = f.read().strip().split("\n\n")
    p1 = deque(int(x) for x in parts[0].splitlines()[1:])
    p2 = deque(int(x) for x in parts[1].splitlines()[1:])
    return p1, p2

def score(deck):
    return sum((i+1)*c for i,c in enumerate(reversed(deck)))

def play_simple(p1, p2):
    p1, p2 = deque(p1), deque(p2)
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return score(p1 or p2)

def play_recursive(p1, p2):
    def game(d1, d2):
        seen = set()
        while d1 and d2:
            state = (tuple(d1), tuple(d2))
            if state in seen:
                return 1, d1
            seen.add(state)
            c1, c2 = d1.popleft(), d2.popleft()
            if len(d1) >= c1 and len(d2) >= c2:
                sub1 = deque(islice(d1, 0, c1))
                sub2 = deque(islice(d2, 0, c2))
                winner, _ = game(sub1, sub2)
            else:
                winner = 1 if c1 > c2 else 2
            if winner == 1:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        if d1:
            return 1, d1
        else:
            return 2, d2
    _, winning_deck = game(deque(p1), deque(p2))
    return score(winning_deck)

if __name__ == "__main__":
    p1, p2 = read_decks(sys.argv[1])
    result1 = play_simple(p1, p2)
    result2 = play_recursive(p1, p2)
    print(result1, result2)