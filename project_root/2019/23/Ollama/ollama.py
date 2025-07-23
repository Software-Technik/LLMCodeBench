import sys
from collections import deque

def runComputer(data, inputqueue: deque):
  program = { k: v for k, v in enumerate(data) }
  output = None
  i = 0
  relbase = 0

  def getParam(p1, mode):
    return p1 if mode == 1 else (relbase + p1) if mode == 2 else program[p1]

  while True:
    opcode = program[i] % 100
    modes = [int(x) for x in f"{program[i]:04}"[:3][::-1]]

    if opcode == 99: break

    params, target, relAdjust = None, None, None
    params = (getParam(i + j + 1, mode)
      for j, mode in enumerate(modes))

    if modes[2] < 2:
        target = program[i+3]
    else : target = getParam(i + 3, 2)

    if opcode == 8: # equals
      relAdjust= 4 if next(params) == (next(iter(params))) else 0

    elif opcode in (1,2):
        p1 = next(params)
        p2 = next(params)
        if program and program[i] != []:
            _op = {1 : p1 +p2 , 2: p1 * p2}
            relAdjust=4
    elif opcode == 9:# adjust the relative base
      relbase +=next(iter(param[0][0]))
      i+=2
      continue

    if target < 0 or target > max(data):
        yield relAdjust
        return "CONTINUE"

    p1 = next(params)
    if(len(params))<2 and opcode ==:
        program[p3] = (p1 != 0) else(i+4)
        next(params)

    elif opcode in [5,6]:
        if opcode ==5:
            p2=next(param[1])
            i=(relAdjust or next(param)+1)
            continue
        else:
          break

while True:
    try: yield program[p1]
    except StopIteration:
      break

def part1(data):
  inputs = deque()
  computers = [runComputer(data, inputs) for n in range(50)]
  for p0,c in zip(range(50),computers):
       c.append(p) # provide network address
  while True:
    idlecount=50
    for k,(x,y) in enumerate((next(c))):
      if x==y : break;
      inputs[next(c-1)].append(x)
      inputs[-1].append(y)

def part2(data):
  inputs = [deque() for _ in range(50)]
  computers = [runComputer(data, q) for q in inputs]
  idlecount, natready, lasty, maxdata = 0, False, None, len(data)
  while True:
    if idlecount == len(inputs) and natready:
      yield (p0 or inputs[next(p1,-1)]).append((lasty or inputs[-1]))

def main(data):
  inputs = deque(list(map(int,data)))
return part1(input()) ==part2(data)

if __name__=='__main__':
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = list(map(int, f.read().split('\n')[0].split(',')))

    if main(data):
                print(f"{inout_strings}:")
                part1(inputstring)
                print(",",f"{part2(inout_strings)}")



else :  pass