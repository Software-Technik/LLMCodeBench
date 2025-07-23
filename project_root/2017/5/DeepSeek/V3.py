import sys

def step_by_step(instructions, second_part=False):
    instructions = instructions.copy()
    i = 0
    steps = 0
    length = len(instructions)

    while 0 <= i < length:
        jump = instructions[i]
        if second_part and jump >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += jump
        steps += 1

    return steps

with open(sys.argv[1]) as f:
    instructions = list(map(int, f.read().splitlines()))

print(step_by_step(instructions))
print(step_by_step(instructions, second_part=True))