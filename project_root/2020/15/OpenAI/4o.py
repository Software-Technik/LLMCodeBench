import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read().strip()

def compute(turns):
    last_spoken = {}
    for turn, num in enumerate(map(int, data.split(","))):
        last_spoken[num] = turn + 1
        last_number = num

    for turn in range(len(last_spoken) + 1, turns + 1):
        last_turn = last_spoken.get(last_number, 0)
        last_spoken[last_number] = turn - 1
        last_number = turn - 1 - last_turn if last_turn else 0

    return last_number

result1 = compute(2020)
result2 = compute(30000000)
print(result1, result2)