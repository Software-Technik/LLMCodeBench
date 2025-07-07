import sys, math
from functools import reduce
from collections import deque

bus = deque()

class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
    def send(self):
        s = self.state
        for d in self.destinations:
            bus.append((self.name, d, s))
    def instantiate_destinations(self, modules):
        self.destinations = [modules.get(dest[1:] if dest[0] in "%&" else dest, Module(dest, [])) if isinstance(dest, str) else dest for dest in self.destinations]
    def recv(self, source, signal):
        pass
    def reset(self):
        pass

class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.state = 0
    def recv(self, source, signal):
        if signal == 0:
            self.state ^= 1
            self.send()
    def reset(self):
        self.state = 0

class Conjunction(Module):
    def __init__(self, name, destinations, sources):
        super().__init__(name, destinations)
        self.signals = {src:0 for src in sources}
    @property
    def state(self):
        return int(not all(self.signals.values()))
    def recv(self, source, signal):
        self.signals[source] = signal
        self.send()
    def reset(self):
        for k in self.signals:
            self.signals[k] = 0

class Broadcaster(Module):
    def recv(self, source, signal):
        self.state = signal
        self.send()

def strip_prefix(n):
    return n[1:] if n and n[0] in "%&" else n

def parse_network(text):
    lines = text.strip().splitlines()
    network = {}
    modules = {}
    for l in lines:
        src, dsts = l.split(" -> ")
        network[src] = dsts.split(", ")
    for src, dsts in network.items():
        if src.startswith("%"):
            modules[src[1:]] = FlipFlop(src[1:], dsts)
        elif src.startswith("&"):
            sources = [strip_prefix(k) for k, v in network.items() if src[1:] in v]
            modules[src[1:]] = Conjunction(src[1:], dsts, sources)
        elif src == "broadcaster":
            modules["broadcaster"] = Broadcaster("broadcaster", dsts)
    for m in modules.values():
        m.instantiate_destinations(modules)
    return network, modules

def part1(text):
    _, modules = parse_network(text)
    counts = [0,0]
    for _ in range(1000):
        bus.clear()
        bus.append(("button", modules["broadcaster"], 0))
        while bus:
            src, dst, sig = bus.popleft()
            counts[sig] += 1
            dst.recv(src, sig)
    return counts[0]*counts[1]

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

def lcm_all(nums):
    return reduce(lcm, nums)

def part2(text):
    _, modules = parse_network(text)
    rx_input = next(mod.name for mod in modules.values() for d in mod.destinations if d.name=="rx")
    inputs_to_rx = [n for n,m in modules.items() if rx_input in [d.name for d in m.destinations]]
    seen = {}
    i = 0
    while len(seen) < len(inputs_to_rx):
        bus.clear()
        bus.append(("button", modules["broadcaster"], 0))
        while bus:
            src, dst, sig = bus.popleft()
            if dst.name==rx_input and sig==1 and src in inputs_to_rx and src not in seen:
                seen[src] = i+1
            dst.recv(src, sig)
        i += 1
    return lcm_all(seen.values())

if __name__=="__main__":
    text = open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")