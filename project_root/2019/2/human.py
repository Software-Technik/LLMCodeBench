import sys

def part1(data):
    program = data.copy()
    program[1] = 12
    program[2] = 2
    
    i = 0

    while True:
        if program[i] == 1:
            program[program[i+3]] = program[program[i+2]] + program[program[i+1]]
            i += 4
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+2]] * program[program[i+1]]
            i += 4
        elif program[i] == 99:
            return program[0]  

def part2(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = data.copy()

            program[1] = noun
            program[2] = verb

            i = 0

            while True:
                if program[i] == 1:
                    program[program[i+3]] = program[program[i+2]] + program[program[i+1]]
                    i += 4
                elif program[i] == 2:
                    program[program[i+3]] = program[program[i+2]] * program[program[i+1]]
                    i += 4
                elif program[i] == 99:
                    break
      
            if program[0] == 19690720:
                return 100 * noun + verb

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")  