import sys

def part1(data):
    N = len(data[0])
    counts = [0]*N
    for line in data:
        for i, c in enumerate(line):
            counts[i] += c=='1'
    gamma = 0
    eps = 0
    half = len(data)/2
    for c in counts:
        gamma = (gamma<<1) | (c>half)
        eps   = (eps<<1)  | (c<=half)
    return gamma*eps

def part2(data):
    N = len(data[0])
    o2 = data[:]
    for i in range(N):
        if len(o2)==1: break
        ones = sum(line[i]=='1' for line in o2)
        bit = '1' if ones*2>=len(o2) else '0'
        o2 = [line for line in o2 if line[i]==bit]
    co2 = data[:]
    for i in range(N):
        if len(co2)==1: break
        ones = sum(line[i]=='1' for line in co2)
        bit = '0' if ones*2>=len(co2) else '1'
        co2 = [line for line in co2 if line[i]==bit]
    return int(o2[0],2)*int(co2[0],2)

data = [l.strip() for l in open(sys.argv[1]) if l.strip()]
print(part1(data), part2(data))