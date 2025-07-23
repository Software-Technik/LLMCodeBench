import sys

def step_by_step(instructions, second_part=False):
    arr = instructions.copy()
    n = len(arr)
    i = 0
    steps = 0

    if not second_part:
        while 0 <= i < n:
            jump = arr[i]
            arr[i] = jump + 1
            i += jump
            steps += 1
    else:
        while 0 <= i < n:
            jump = arr[i]
            if jump >= 3:
                arr[i] = jump - 1
            else:
                arr[i] = jump + 1
            i += jump
            steps += 1

    return steps

input_file = sys.argv[1]
with open(input_file) as f:
    instructions_list = [int(line.strip()) for line in f if line.strip()]

print(step_by_step(instructions_list))
print(step_by_step(instructions_list, second_part=True))