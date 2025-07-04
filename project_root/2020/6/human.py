import sys

input_path = sys.argv[1]

lines = []
with open(input_path) as f:
    # with open("input.txt") as f:
    data = f.read()
    lines = data.splitlines()
# print(lines)
# print(len(lines), "lines in input.txt")


def line_transform(line):
    split = [line.split() for line in lines]
    return line


lines = [line_transform(line) for line in lines]

groups = data.split("\n\n")
groups = [set(ans.strip().replace("\n", "").replace(" ", ""))
          for ans in groups]
# print(sum(map(len, groups)))  # 6249
result1 = sum(map(len, groups))
groups = data.split("\n\n")
tot = 0
for group in groups:
    ppl = group.splitlines()
    # print(ppl)
    consensus = len(
        set.intersection(
            *[set(p.strip().replace("\n", "").replace(" ", "")) for p in ppl]
        )
    )
    tot += consensus
# print(tot)  # 3103
result2 = tot
print(result1, result2)

# 11 minutes
