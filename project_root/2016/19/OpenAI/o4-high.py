import sys

def part1(n):
    p=1<<(n.bit_length()-1)
    return 2*(n-p)+1

def part2(n):
    p=1
    while p*3<=n:
        p*=3
    if n==p:
        return n
    if n<=2*p:
        return n-p
    return 2*n-3*p

with open(sys.argv[1]) as f:
    n=int(f.read())
sys.stdout.write(f"{part1(n)} {part2(n)}")