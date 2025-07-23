import sys
from collections import defaultdict

def runComputer(data, input):
  program = defaultdict(int, enumerate(data))
  output = None
  i = 0
  relbase = 0

  while True:
    opcode = program[i] % 100
    mode1 = (program[i] - opcode) // 100 % 10
    mode2 = (program[i] - opcode) // 1000 % 10
    mode3 = (program[i] - opcode) // 10000 % 10

    p1, p2, p3 = None, None, None
    if mode1 == 0: p1 = program[i + 1]
    elif mode1 == 1: p1 = i + 1
    elif mode1 == 2: p1 = program[i + 1] + relbase

    if mode2 == 0: p2 = program[i + 2]
    elif mode2 == 1: p2 = i + 2
    elif mode2 == 2: p2 = program[i + 2] + relbase

    if mode3 == 0: p3 = program[i + 3]
    elif mode3 == 1: raise ValueError('Immediate mode invalid for param 3')
    elif mode3 == 2: p3 = program[i + 3] + relbase

    if opcode == 99:
      break
    elif opcode in (1, 7, 8): # addition, less than, equals
      program[p3] = program[p1] + program[p2] if opcode == 1 else int(program[p1] < program[p2]) * (opcode == 7) + int(program[p1] == program[p2]) * (opcode == 8)
      i += 4
    elif opcode in (2, 5, 6): # multiplication, jump-if-true, jump-if-false
      if opcode != 5 and opcode != 6:
        program[p3] = program[p1] * program[p2]
        i += 4
      else:
        i = program[p2] if (program[p1] != 0) * (opcode == 5) + (program[p1] == 0) * (opcode == 6) else i + 3
    elif opcode == 3: # input
      program[p1] = input
      i += 2
    elif opcode == 4: # output
      output = program[p1]
      i += 2
    elif opcode == 9: # relative base adjust
      relbase += program[p1]
      i += 2
    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')

  return output

def part1(data):
    return runComputer(data, 1)

def part2(data):
    return runComputer(data, 2)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))
sys.stdout.write(f"{part1(data)} {part2(data)}")