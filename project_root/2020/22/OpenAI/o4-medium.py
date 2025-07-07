import sys
from collections import deque
from itertools import islice

def score(d):
    return sum((i+1)*c for i,c in enumerate(reversed(d)))

def play(d1,d2):
    seen=set()
    while d1 and d2:
        state=(tuple(d1),tuple(d2))
        if state in seen:
            return 1,d1
        seen.add(state)
        c1=d1.popleft(); c2=d2.popleft()
        if len(d1)>=c1 and len(d2)>=c2:
            nd1=deque(islice(d1,0,c1)); nd2=deque(islice(d2,0,c2))
            w,_=play(nd1,nd2)
        else:
            w=1 if c1>c2 else 2
        if w==1:
            d1.append(c1); d1.append(c2)
        else:
            d2.append(c2); d2.append(c1)
    return (1,d1) if d1 else (2,d2)

def main():
    with open(sys.argv[1]) as f:
        parts=f.read().strip().split('\n\n')
    p1=deque(map(int,parts[0].splitlines()[1:]))
    p2=deque(map(int,parts[1].splitlines()[1:]))
    d1=deque(p1); d2=deque(p2)
    while d1 and d2:
        c1=d1.popleft(); c2=d2.popleft()
        if c1>c2:
            d1.extend([c1,c2])
        else:
            d2.extend([c2,c1])
    r1=score(d1 or d2)
    _,wdeck=play(deque(p1),deque(p2))
    r2=score(wdeck)
    print(r1,r2)

if __name__=='__main__':
    main()