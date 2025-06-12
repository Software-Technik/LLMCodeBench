import sys

def draw(level):
  size = 5 # assume a square
  for y in range(size):
    line = "".join([level[(x,y)] for x in range(size)])
    print(line)

def stringify(level):
  return "".join(level.values())

def neighbors(level, p):
  return [p for p in [
    (p[0] - 1, p[1]),
    (p[0] + 1, p[1]),
    (p[0], p[1] - 1),
    (p[0], p[1] + 1),
  ] if p in level]

def part1(data):
  level = dict()

  x,y = 0,0
  for line in data:
    for c in line:
      level[(x,y)] = c
      x += 1
    y += 1
    x = 0
  
  layouts = set()

  while True:
    txt = stringify(level)
    if txt in layouts: break
    layouts.add(txt)
    newlevel = dict()
    for p in level:
      ns = neighbors(level, p)
      bugcount = sum([1 for n in ns if level[n] == "#"])
      if level[p] == "#" and not bugcount == 1: newlevel[p] = "."
      elif level[p] == "." and (bugcount == 1 or bugcount == 2): newlevel[p] = "#"
      else: newlevel[p] = level[p]
    level = newlevel

  power = 1
  result = 0
  for p in level:
    if level[p] == "#": result += power
    power = power * 2

  return result

def drawsingle2(level):
  size = 5 # assume a square
  for y in range(size):
    line = "".join([level[(x,y)] for x in range(size)])
    print(line)

def draw2(levels):
  mini = min(levels.keys())
  maxi = max(levels.keys())

  for i in range(mini, maxi + 1):
    print("\nLevel", i)
    drawsingle2(levels[i])

def neighbors2(levels, rec, p):
  ns = []

  if (p[0] - 1, p[1]) != (2,2) and (p[0] - 1, p[1]) in levels[rec]: ns.append(levels[rec][(p[0] - 1, p[1])])
  if (p[0] + 1, p[1]) != (2,2) and (p[0] + 1, p[1]) in levels[rec]: ns.append(levels[rec][(p[0] + 1, p[1])])
  if (p[0], p[1] - 1) != (2,2) and (p[0], p[1] - 1) in levels[rec]: ns.append(levels[rec][(p[0], p[1] - 1)])
  if (p[0], p[1] + 1) != (2,2) and (p[0], p[1] + 1) in levels[rec]: ns.append(levels[rec][(p[0], p[1] + 1)])

  if rec + 1 in levels:
    if p[1] == 0: ns.append(levels[rec + 1][(2,1)]) # add 8 to A-E
    if p[1] == 4: ns.append(levels[rec + 1][(2,3)]) # add 18 to U-Y
    if p[0] == 0: ns.append(levels[rec + 1][(1,2)]) # add 12 to A/F/K/P/U
    if p[0] == 4: ns.append(levels[rec + 1][(3,2)]) # add 14 to E/J/O/T/Y

  if rec - 1 in levels:
    if p == (2,1): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[1] == 0]) # add toprow to H
    if p == (1,2): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[0] == 0]) # add leftrow to L
    if p == (3,2): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[0] == 4]) # add right to N
    if p == (2,3): ns.extend([levels[rec - 1][p] for p in levels[rec - 1] if p[1] == 4]) # add botrow to R

  return ns

def createlevel2(data):
  level = dict()

  x,y = 0,0
  for line in data:
    for c in line:
      level[(x,y)] = c
      x += 1
    y += 1
    x = 0

  level[(2,2,)] = "?" # just to be sure

  return level

def part2(data):
  levels = dict()
  levels[0] = createlevel2(data)
  empty = createlevel2([".....", ".....", "..?..", ".....", "....."])
  
  for minutes in range(200):
    #print(f"At minute {minutes}")
    
    newlevels = dict()

    for depth in range(-minutes-1, minutes+2):
      if depth not in levels:
        levels[depth] = empty.copy()

      level = levels[depth]
      newlevel = dict()
      newlevels[depth] = newlevel

      for p in level:
        ns = neighbors2(levels, depth, p)
        bugcount = sum([1 for n in ns if n == "#"])
        if level[p] == "#" and not bugcount == 1: newlevel[p] = "."
        elif level[p] == "." and (bugcount == 1 or bugcount == 2): newlevel[p] = "#"
        else: newlevel[p] = level[p]

    levels = newlevels

  # draw2(levels)

  result = 0
  for rec in range(min(levels.keys()), max(levels.keys())):
    result += sum([1 for p in levels[rec] if levels[rec][p] == "#"])

  return result

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")