import sys

def main(path):
    setup = {'red':12,'green':13,'blue':14}
    total1 = total2 = 0
    with open(path) as f:
        for i,line in enumerate(f,1):
            game = line.partition(':')[2].strip()
            possible = True
            maxn = {}
            for sp in game.split(';'):
                for cp in sp.split(','):
                    n_str,color = cp.strip().split(' ',1)
                    n = int(n_str)
                    if possible and n > setup[color]:
                        possible = False
                    prev = maxn.get(color)
                    if prev is None or n > prev:
                        maxn[color] = n
            if possible:
                total1 += i
            prod = 1
            for v in maxn.values():
                prod *= v
            total2 += prod
    sys.stdout.write(f"{total1} {total2}")

if __name__=='__main__':
    main(sys.argv[1])