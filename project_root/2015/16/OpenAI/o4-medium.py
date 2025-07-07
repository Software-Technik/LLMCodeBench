import sys

tests = {'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}
greater = {'cats','trees'}
less = {'pomeranians','goldfish'}

sues = []
for line in open(sys.argv[1]):
    name, rest = line.strip().split(': ', 1)
    num = int(name.split()[1])
    props = {k: int(v) for item in rest.split(', ') for k, v in [item.split(': ')]}
    sues.append((num, props))

ans1 = next(n for n, p in sues if all(p[k] == tests[k] for k in p))
ans2 = next(n for n, p in sues if all((p[k] > tests[k] if k in greater else p[k] < tests[k] if k in less else p[k] == tests[k]) for k in p))

sys.stdout.write(f"{ans1}\n{ans2}\n")