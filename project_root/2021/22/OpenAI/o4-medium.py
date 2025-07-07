import sys
from dataclasses import dataclass

@dataclass(frozen=True)
class Cube:
    x1: int; x2: int; y1: int; y2: int; z1: int; z2: int
    def volume(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)
    def intersect(self, other):
        x1 = max(self.x1, other.x1); x2 = min(self.x2, other.x2)
        y1 = max(self.y1, other.y1); y2 = min(self.y2, other.y2)
        z1 = max(self.z1, other.z1); z2 = min(self.z2, other.z2)
        if x1 <= x2 and y1 <= y2 and z1 <= z2:
            return Cube(x1, x2, y1, y2, z1, z2)
    def subtract(self, other):
        i = self.intersect(other)
        if not i:
            return [self]
        res = []
        if self.x1 < i.x1:
            res.append(Cube(self.x1, i.x1-1, self.y1, self.y2, self.z1, self.z2))
        if i.x2 < self.x2:
            res.append(Cube(i.x2+1, self.x2, self.y1, self.y2, self.z1, self.z2))
        if self.y1 < i.y1:
            res.append(Cube(i.x1, i.x2, self.y1, i.y1-1, self.z1, self.z2))
        if i.y2 < self.y2:
            res.append(Cube(i.x1, i.x2, i.y2+1, self.y2, self.z1, self.z2))
        if self.z1 < i.z1:
            res.append(Cube(i.x1, i.x2, i.y1, i.y2, self.z1, i.z1-1))
        if i.z2 < self.z2:
            res.append(Cube(i.x1, i.x2, i.y1, i.y2, i.z2+1, self.z2))
        return res

def process(steps, limit=None):
    on_cubes = []
    if limit:
        limcube = Cube(-limit, limit, -limit, limit, -limit, limit)
    for tog, cube in steps:
        if limit:
            cube = cube.intersect(limcube)
            if not cube: continue
        new_on = []
        for oc in on_cubes:
            new_on.extend(oc.subtract(cube))
        if tog:
            new_on.append(cube)
        on_cubes = new_on
    return sum(c.volume() for c in on_cubes)

def parse(data):
    steps = []
    for line in data:
        t, rest = line.split(' ', 1)
        tog = t == 'on'
        parts = rest.split(',')
        x1, x2 = map(int, parts[0][2:].split('..'))
        y1, y2 = map(int, parts[1][2:].split('..'))
        z1, z2 = map(int, parts[2][2:].split('..'))
        steps.append((tog, Cube(x1, x2, y1, y2, z1, z2)))
    return steps

def main():
    data = open(sys.argv[1]).read().splitlines()
    steps = parse(data)
    p1 = process(steps, limit=50)
    p2 = process(steps, limit=None)
    print(f"{p1} {p2}")

if __name__ == "__main__":
    main()