import sys
from collections import deque
from hashlib import md5

with open(sys.argv[1]) as file:
    INPUT_b = file.read().strip().encode()

def find_vault():
    q = deque([((0,0), b'')])
    shortest = None
    longest = 0
    while q:
        (x,y), path = q.popleft()
        if (x,y) == (3,3):
            if shortest is None:
                shortest = path
            if len(path) > longest:
                longest = len(path)
            continue
        h = md5(INPUT_b + path).hexdigest()
        if h[0] > 'a' and y>0: q.append(((x,y-1), path+b'U'))
        if h[1] > 'a' and y<3: q.append(((x,y+1), path+b'D'))
        if h[2] > 'a' and x>0: q.append(((x-1,y), path+b'L'))
        if h[3] > 'a' and x<3: q.append(((x+1,y), path+b'R'))
    return shortest, longest

first, second = find_vault()
sys.stdout.write(f"{first.decode()} {second}")