import sys
import math
from functools import reduce
from collections import deque

class Module:
    __slots__ = ('name','dest_names','destinations')
    def __init__(self,name,dest_names):
        self.name=name
        self.dest_names=dest_names
        self.destinations=[]
    def send(self):
        for d in self.destinations: bus.append((self.name,d,self.state))
    def recv(self,source,signal): pass
    def reset(self): pass

class FlipFlop(Module):
    __slots__=('state',)
    def __init__(self,name,dest_names):
        super().__init__(name,dest_names)
        self.state=0
    def recv(self,source,signal):
        if signal==0:
            self.state^=1
            self.send()
    def reset(self): self.state=0

class Conjunction(Module):
    __slots__=('signals',)
    def __init__(self,name,dest_names,sources):
        super().__init__(name,dest_names)
        self.signals={src:0 for src in sources}
    @property
    def state(self): return int(not all(self.signals.values()))
    def recv(self,source,signal):
        self.signals[source]=signal
        self.send()
    def reset(self):
        for k in self.signals: self.signals[k]=0

class Broadcaster(Module):
    __slots__=('state',)
    def recv(self,source,signal):
        self.state=signal
        self.send()

def strip_prefix(n): return n[1:] if n and n[0] in '%&' else n

def parse_network(text):
    lines=text.strip().splitlines()
    raw_dests={}
    for line in lines:
        k,v=line.split(" -> ")
        raw_dests[k]=v.split(", ")
    incoming={}
    for src,dlist in raw_dests.items():
        for d in dlist:
            dn=strip_prefix(d)
            incoming.setdefault(dn,[]).append(strip_prefix(src))
    modules={}
    for k,dlist in raw_dests.items():
        if k.startswith('%'):
            modules[k[1:]]=FlipFlop(k[1:],[strip_prefix(d) for d in dlist])
        elif k.startswith('&'):
            nm=k[1:]; modules[nm]=Conjunction(nm,[strip_prefix(d) for d in dlist],incoming.get(nm,[]))
        elif k=='broadcaster':
            modules['broadcaster']=Broadcaster('broadcaster',[strip_prefix(d) for d in dlist])
    for m in modules.values():
        m.destinations=[modules[d] for d in m.dest_names]
    return modules

def part1(text):
    modules=parse_network(text)
    counts=[0,0]
    for _ in range(1000):
        for m in modules.values(): m.reset()
        global bus; bus=deque([("button",modules["broadcaster"],0)])
        while bus:
            src,dst,sig=bus.popleft()
            counts[sig]+=1
            dst.recv(src,sig)
    return counts[0]*counts[1]

def lcm(a,b): return abs(a*b)//math.gcd(a,b)
def lcm_all(nums): return reduce(lcm,nums)

def part2(text):
    modules=parse_network(text)
    rx_input=None
    for m in modules.values():
        for d in m.destinations:
            if d.name=='rx': rx_input=m.name
    inputs=[m.name for m in modules.values() if any(d.name==rx_input for d in m.destinations)]
    seen={}
    i=0
    while len(seen)<len(inputs):
        for m in modules.values(): m.reset()
        global bus; bus=deque([("button",modules["broadcaster"],0)])
        while bus:
            src,dst,sig=bus.popleft()
            if dst.name==rx_input and sig==1 and src in inputs and src not in seen:
                seen[src]=i+1
            dst.recv(src,sig)
        i+=1
    return lcm_all(seen.values())

if __name__=='__main__':
    t=open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(t)} {part2(t)}")