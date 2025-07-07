import sys

def parse_data(data):
    rock = set()
    for line in data:
        pts = [tuple(map(int, p.split(','))) for p in line.split(' -> ')]
        for (x1,y1),(x2,y2) in zip(pts, pts[1:]):
            if x1==x2:
                if y1>y2: y1,y2 = y2,y1
                for y in range(y1, y2+1): rock.add((x1,y))
            else:
                if x1>x2: x1,x2 = x2,x1
                for x in range(x1, x2+1): rock.add((x,y1))
    return rock

def part1(data):
    rock = parse_data(data)
    occ = set(rock)
    maxd = max(y for _,y in rock)
    falls = ((0,1),(-1,1),(1,1))
    count = 0
    while True:
        x,y = 500,0
        while y<=maxd:
            for dx,dy in falls:
                nx,ny = x+dx, y+dy
                if (nx,ny) not in occ:
                    x,y = nx,ny
                    break
            else:
                occ.add((x,y))
                count +=1
                break
        else:
            return count

def part2(data):
    rock = parse_data(data)
    occ = set(rock)
    floor = max(y for _,y in rock)+2
    falls = ((0,1),(-1,1),(1,1))
    count = 0
    while (500,0) not in occ:
        x,y = 500,0
        while True:
            moved=False
            for dx,dy in falls:
                nx,ny = x+dx, y+dy
                if ny<floor and (nx,ny) not in occ:
                    x,y = nx,ny
                    moved=True
                    break
            if not moved:
                occ.add((x,y))
                count+=1
                break
    return count

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        data = [l.strip() for l in f]
    print(part1(data))
    print(part2(data))