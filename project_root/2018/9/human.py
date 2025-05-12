from collections import deque
import sys


def play_marbles(players, last_marble):
    circle = deque([0])
    scores = [0]*players

    for i in range(1, last_marble+1):
        if i % 23:
            circle.rotate(-2)
            circle.appendleft(i)
        else:
            circle.rotate(7)
            scores[i % players] += i + circle.popleft()

    return max(scores)



def do_test_cases_part_one(fn):
    with open(fn) as f:
        test_cases = [[int(n) for n in line.strip().split(",")] for line in f]

        for case in test_cases:
            players, last_marble, winning_score = case
            result = play_marbles(players, last_marble)
            print(result, winning_score)
            #assert(result == winning_score)


if __name__ == "__main__":
    inout_strings = sys.argv[1]
    do_test_cases_part_one(inout_strings)
