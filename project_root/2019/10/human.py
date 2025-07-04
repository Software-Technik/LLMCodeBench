import sys
import math

def part1(data):
  points = dict()
  x, y = -1, -1

  for line in data:
    y += 1
    x = -1
    for char in line:
      x += 1
      if char == "#":
        points[(x,y)] = dict()
  
  for p in points.keys():
    for other in points.keys():
      if p == other: continue
      rad = math.atan2(other[1]-p[1], other[0]-p[0])
      key = int(rad * 100000) + 1
      if key not in points[p]:
        points[p][key] = list()
      points[p][key].append(other)

  result = max(points, key = lambda p: len(points[p].values()))

  return len(points[result].values())

def part2(data):
  points = dict()
  x, y = -1, -1

  for line in data:
    y += 1
    x = -1
    for char in line:
      x += 1
      if char == "#":
        points[(x,y)] = dict()
  
  for p in points.keys():
    for other in points.keys():
      if p == other: continue
      rad = math.atan2(other[1]-p[1], other[0]-p[0])
      if rad < (math.pi / 2 * -1): rad = math.pi + math.pi + rad
      key = int(rad * 1000000)
      if key not in points[p]:
        points[p][key] = list()
      points[p][key].append(other)
    
  station = max(points, key = lambda p: len(points[p].values()))

  for p in points.keys():
    for key in points[p].keys():
      points[p][key].sort(key = lambda p2: abs(p[0] - p2[0]) + abs(p[1] - p2[1]))

  i = 0
  printed = True
  while i < 200 and printed:
    printed = False
    for key in sorted(points[station].keys()):
      if len(points[station][key]) == 0: continue
      i += 1
      target = points[station][key].pop(0)
      result = target[0] * 100 + target[1]
      printed = True
      if i == 200: return result

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(f.read().splitlines())

sys.stdout.write(f"{part1(data)} {part2(data)}")