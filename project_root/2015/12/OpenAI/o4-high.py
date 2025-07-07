import sys, re, json
s = open(sys.argv[1]).read()
print(sum(int(m.group()) for m in re.finditer(r'-?\d+', s)))
def f(o):
    if type(o) is int: return o
    if type(o) is list: return sum(f(x) for x in o)
    if type(o) is dict:
        if 'red' in o.values(): return 0
        return sum(f(x) for x in o.values())
    return 0
print(f(json.loads(s)))