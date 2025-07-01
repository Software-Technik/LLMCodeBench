"""
I am almost sure there's an off by one in this program
or an unchecked range, but I found answers nonetheless
"""

import os
import sys

input_path = sys.argv[1]


# change to dir of script
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    with open(input_path) as f:
    # with open(r"project_root\2020\9\input.txt") as f:
        data = f.read()  # entire file as string
        lines = data.splitlines()
except:
    # print("no input.txt")
    data, lines = "", []

# print(lines)
# print(len(lines), "lines in input.txt")


def ans(answer):
    pass
    # store answer to clipboard
    # print(answer, "| in clipboard")
    # os.system(f'echo "{answer}"| xclip -selection clipboard -in')


def line_transform(line):
    # split = [line.split() for line in lines]
    return int(line)


line_groups = data.split("\n\n")  # lines split by double newlines
lines = [line_transform(line) for line in lines]  # apply line_transform to each line

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map
## end of boilerplate

result1 = 0
def check25(prev25, goal):
    for i, a in enumerate(prev25):
        for j, b in enumerate(prev25):
            if i != j and a + b == goal:
                return True
    return False

offset = 25
print(f"Lines length: {len(lines)}")
print("Erste 30 Werte:", lines[:25])
while offset < len(lines):
    prev25 = lines[offset - 25 : offset]
    goal = lines[offset]
    if not check25(prev25, goal):
        result1 = goal
        break
    offset += 1


goalie = result1

start = 0
end = 0
while True:
    sl = lines[start : end + 1]
    s = sum(sl)
    if s == goalie:
        # print(sl)
        ans(max(sl) + min(sl))  # 3340942
        result2 = max(sl) + min(sl)
        print(result1,result2)
        exit()
    if s > goalie:
        start += 1
        end = start
        continue
    end += 1
    