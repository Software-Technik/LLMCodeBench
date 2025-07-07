import sys

def parse_instruction(instruction):
    c=instruction[0]; v=instruction[1:]
    if c=='s': return ('s',int(v))
    if c=='x':
        a,b=v.split('/'); return ('x',int(a),int(b))
    return ('p',v[0],v[2])

def dance(dancers, instructions):
    d=list(dancers)
    for instr in instructions:
        t=instr[0]
        if t=='s':
            x=instr[1]; d=d[-x:]+d[:-x]
        elif t=='x':
            a,b=instr[1],instr[2]; d[a],d[b]=d[b],d[a]
        else:
            a,b=instr[1],instr[2]
            ia,ib=d.index(a),d.index(b)
            d[ia],d[ib]=d[ib],d[ia]
    return ''.join(d)

def long_dance(dancers,instructions,iterations):
    seen_map={} ; seq=[]
    current=dancers
    for i in range(iterations):
        if current in seen_map:
            start=seen_map[current]
            cycle_len=i-start
            return seq[(iterations-start)%cycle_len+start]
        seen_map[current]=i
        seq.append(current)
        current=dance(current,instructions)
    return current

with open(sys.argv[1]) as f:
    content=f.read().strip().split(',')
parsed=[parse_instruction(x) for x in content]
programs="abcdefghijklmnop"
print(dance(programs,parsed))
print(long_dance(programs,parsed,1000000000))