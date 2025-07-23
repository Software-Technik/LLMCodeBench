import sys

with open(sys.argv[1]) as f:
    nums = list(map(int, f.read().split(',')))
data_len = len(nums)

before = {}
last_spoken = nums[-1]

for turn, num in enumerate(nums[-2::-1], start=1):
    before[num] = turn

turn = data_len
last = last_spoken

while True:
    novel_turn = turn - (before.get(last, 0) + 1)
    before[last] = turn
    last = novel_turn if novel_turn not in before else before[novel_turn]
    turn += 1

    if turn == 2020:
        ans1 = last
    elif turn == 30000000:
        ans2 = last
        break

print(ans1, ans2)