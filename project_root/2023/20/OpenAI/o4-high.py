import sys
import math
from collections import deque

bus = deque()

class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
    def send(self):
        for d in self.destinations:
            bus.append((self.name, d, self.state))
    def recv(self, source, signal):
        pass

class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.state = 0
    def recv(self, source, signal):
        if signal == 0:
            self.state ^= 1
            self.send()

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

class Broadcaster(Module):
    def recv(self, source, signal):
        self.state = signal
        self.send()

def strip_prefix(name):
    return name[1:] if name and name[0] in '%&' else name

def parse_network(text):
    modules = {}
    network = {}
    for line in text.strip().splitlines():
        src, dests = line.split(' -> ')
        network[src] = dests.split(', ')
    for src, dests in network.items():
        if src.startswith('%'):
            modules[src[1:]] = FlipFlop(src[1:], dests)
        elif src.startswith('&'):
            nm = src[1:]
            modules[nm] = Conjunction(nm, dests,
                                     [strip_prefix(k) for k,v in network.items() if nm in v])
        elif src == 'broadcaster':
            modules['broadcaster'] = Broadcaster('broadcaster', dests)
    for m in modules.values():
        nd = []
        for d in m.destinations:
            mm = modules.get(d)
            nd.append(mm if mm else Module(d, []))
        m.destinations = nd
    return modules

def part1(text):
    global bus
    modules = parse_network(text)
    c0, c1 = 0, 0
    for _ in range(1000):
        bus = deque([("button", modules["broadcaster"], 0)])
        while bus:
            src, dst, sig = bus.popleft()
            if sig: c1 += 1
            else: c0 += 1
            dst.recv(src, sig)
    return c0 * c1

def part2(text):
    global bus
    modules = parse_network(text)
    rx_input = None
    for name, m in modules.items():
        for d in m.destinations:
            if d.name == "rx":
                rx_input = name
    inputs = [n for n,m in modules.items() if any(d.name == rx_input for d in m.destinations)]
    seen = {}
    i = 0
    while len(seen) < len(inputs):
        bus = deque([("button", modules["broadcaster"], 0)])
        while bus:
            src, dst, sig = bus.popleft()
            if dst.name == rx_input and sig == 1 and src in inputs and src not in seen:
                seen[src] = i + 1
            dst.recv(src, sig)
        i += 1
    l = 1
    for v in seen.values():
        l = l * v // math.gcd(l, v)
    return l

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")