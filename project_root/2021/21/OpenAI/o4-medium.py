import sys
from functools import lru_cache

dicesum_odds = ((3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1))

@lru_cache(maxsize=None)
def count_wins(p1,p2,s1,s2,turn):
    if s1>=21: return (1,0)
    if s2>=21: return (0,1)
    w1=w2=0
    for d,odd in dicesum_odds:
        if turn==1:
            np1=(p1+d-1)%10+1
            a,b = count_wins(np1,p2,s1+np1,s2,2)
        else:
            np2=(p2+d-1)%10+1
            a,b = count_wins(p1,np2,s1,s2+np2,1)
        w1+=a*odd; w2+=b*odd
    return w1,w2

def part1(data):
    p1=int(data[0].split()[-1]); p2=int(data[1].split()[-1])
    s1=s2=0; die=0; rolls=0
    while True:
        total=0
        for _ in range(3):
            die=die%100+1; total+=die; rolls+=1
        p1=(p1+total-1)%10+1; s1+=p1
        if s1>=1000: return s2*rolls
        total=0
        for _ in range(3):
            die=die%100+1; total+=die; rolls+=1
        p2=(p2+total-1)%10+1; s2+=p2
        if s2>=1000: return s1*rolls

def part2(data):
    p1=int(data[0].split()[-1]); p2=int(data[1].split()[-1])
    w1,w2=count_wins(p1,p2,0,0,1)
    return w1 if w1>w2 else w2

with open(sys.argv[1]) as f:
    data=f.read().splitlines()
r1=part1(data); r2=part2(data)
sys.stdout.write(f"{r1} {r2}")