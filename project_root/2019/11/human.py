import sys
from collections import defaultdict
import io

def runComputer(data, input):
  program = defaultdict(int, { k: v for k, v in enumerate(data) })
  output = None
  i = 0
  relbase = 0

  while True:
    opcode = program[i] % 100

    if opcode == 99:
      break

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

    #print('i =', i, '--- operation', opcode, '--- modes', mode1, mode2, mode3, '--- positions', str(p1).rjust(4, ' '), str(p2).rjust(4, ' '), str(p3).rjust(4, ' '))

    if opcode == 1: # addition
      program[p3] = program[p1] + program[p2]
      i += 4
    elif opcode == 2: # multiplication
      program[p3] = program[p1] * program[p2]
      i += 4
    elif opcode == 3: # input
      program[p1] = input.pop()
      i += 2
    elif opcode == 4: # output
      yield program[p1]
      i += 2
    elif opcode == 5: # jump-if-true
      i = program[p2] if program[p1] != 0 else i + 3
    elif opcode == 6: # jump-if-false
      i = program[p2] if program[p1] == 0 else i + 3
    elif opcode == 7: # less-than
      program[p3] = 1 if program[p1] < program[p2] else 0
      i += 4
    elif opcode == 8: # equals
      program[p3] = 1 if program[p1] == program[p2] else 0
      i += 4
    elif opcode == 9: # relative base adjust
      relbase += program[p1]
      i += 2
    else:
      raise ValueError(f'opcode {opcode} from {program[i]}')

directions = [(0,-1), (1,0), (0,1), (-1,0)]
turns = [-1, +1]

def part1(data):
  direction, x, y = 0, 0, 0
  colors = defaultdict(int)
  inputs = [0]
  inputs = inputs[::-1]
  runner = runComputer(data, inputs)

  while True:
    color = next(runner, 'halt')
    turn = next(runner, 'halt')
    if color == 'halt': break

    colors[(x,y)] = color

    direction = (direction + turns[turn] + 4) % 4

    x += directions[direction][0]
    y += directions[direction][1]

    inputs.append(colors[(x,y)])

  return len(colors)

def part2(data):
    direction, x, y = 0, 0, 0
    colors = defaultdict(int)
    inputs = [1]
    runner = runComputer(data, inputs)

    directions = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]  # Up, Right, Down, Left
    turns = { 0: -1, 1: 1 }

    while True:
        color = next(runner, 'halt')
        turn = next(runner, 'halt')
        if color == 'halt': break

        colors[(x, y)] = color
        direction = (direction + turns[turn] + 4) % 4
        x += directions[direction][0]
        y += directions[direction][1]
        inputs.append(colors[(x, y)])

    minx = min(p[0] for p in colors)
    maxx = max(p[0] for p in colors)
    miny = min(p[1] for p in colors)
    maxy = max(p[1] for p in colors)

    LETTER_BITMAPS_4x6 = {
        "A": ["0110", "1001", "1001", "1111", "1001", "1001"],
        "B": ["1110", "1001", "1110", "1001", "1001", "1110"],
        "C": ["0110", "1001", "1000", "1000", "1001", "0110"],
        "D": ["1110", "1001", "1001", "1001", "1001", "1110"],
        "E": ["1111", "1000", "1110", "1000", "1000", "1111"],
        "F": ["1111", "1000", "1110", "1000", "1000", "1000"],
        "G": ["0111", "1000", "1000", "1011", "1001", "0111"],
        "H": ["1001", "1001", "1111", "1001", "1001", "1001"],
        "I": ["1110", "0100", "0100", "0100", "0100", "1110"],
        "J": ["0011", "0001", "0001", "0001", "1001", "0110"],
        "K": ["1001", "1010", "1100", "1100", "1010", "1001"],
        "L": ["1000", "1000", "1000", "1000", "1000", "1111"],
        "M": ["1001", "1111", "1111", "1001", "1001", "1001"],
        "N": ["1001", "1101", "1101", "1011", "1011", "1001"],
        "O": ["0110", "1001", "1001", "1001", "1001", "0110"],
        "P": ["1110", "1001", "1001", "1110", "1000", "1000"],
        "Q": ["0110", "1001", "1001", "1001", "1010", "0101"],
        "R": ["1110", "1001", "1001", "1110", "1010", "1001"],
        "S": ["0111", "1000", "0110", "0001", "0001", "1110"],
        "T": ["1111", "0100", "0100", "0100", "0100", "0100"],
        "U": ["1001", "1001", "1001", "1001", "1001", "0110"],
        "V": ["1001", "1001", "1001", "1001", "0110", "0100"],
        "W": ["1001", "1001", "1001", "1111", "1111", "1001"],
        "X": ["1001", "1001", "0110", "0110", "1001", "1001"],
        "Y": ["1001", "1001", "0110", "0100", "0100", "0100"],
        "Z": ["1111", "0001", "0010", "0100", "1000", "1111"]
    }
    LETTER_BITMAPS_4x6 = {tuple(v): k for k, v in LETTER_BITMAPS_4x6.items()}

    result = ""
    for x in range(minx + 1, maxx + 1, 5):
        block = []
        for y in range(miny, miny + 6):
            line = ""
            for dx in range(4):
                if colors[(x + dx, y)] == 1:
                    line += "1"
                else:
                    line += "0"
            block.append(line)

        if all(line == "0000" for line in block):
           continue

        result += LETTER_BITMAPS_4x6.get(tuple(block), '?')

    return result

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdout.write(f"{part1(data)} {part2(data)}")