import sys
import math
from functools import reduce

bus = []

class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def send(self, signal):
        for destination in self.destinations:
            bus.append((self.name, destination, signal))

    def recv(self, source, signal):
        pass

class FlipFlop(Module):
    def __init__(self, name, destinations):
        super().__init__(name, destinations)
        self.state = 0

    def recv(self, source, signal):
        if signal == 0:
            self.state ^= 1
            self.send(self.state)

    def reset(self):
        self.state = 0

class Conjunction(Module):
    def __init__(self, name, destinations, sources):
        super().__init__(name, destinations)
        self.signals = {src: 0 for src in sources}

    @property
    def state(self):
        return int(not all(self.signals.values()))

    def recv(self, source, signal):
        self.signals[source] = signal
        self.send(self.state)

    def reset(self):
        self.signals.clear()

class Broadcaster(Module):
    def recv(self, source, signal):
        self.send(signal)

def parse_network(text):
    lines = text.strip().splitlines()
    network = {}
    modules = {}

    for line in lines:
        source, dests = line.split(" -> ")
        network[source] = dests.split(", ")

    for key in network:
        if key.startswith("%"):
            modules[key[1:]] = FlipFlop(key[1:], network[key])
        elif key.startswith("&"):
            sources = [strip_prefix(k) for k in network if key[1:] in network[k]]
            modules[key[1:]] = Conjunction(key[1:], network[key], sources)
        elif key == "broadcaster":
            modules["broadcaster"] = Broadcaster("broadcaster", network[key])

    return network, modules

def part1(text):
    global bus
    _, modules = parse_network(text)
    counts = [0] * 2

    for _ in range(1000):
        bus = [("button", modules["broadcaster"], 0)]
        while bus:
            source, destination, signal = bus.pop(0)
            counts[signal] += 1
            if isinstance(destination, Module):
                destination.recv(source, signal)

    return counts[0] * counts[1]

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_all(nums):
    return reduce(lcm, nums)

def part2(text):
    global bus
    _, modules = parse_network(text)

    rx_input = None
    for name, mod in modules.items():
        for dest in mod.destinations:
            if isinstance(dest, Module) and "rx" == dest.name:
                rx_input = mod.name

    inputs_to_rx_input = [
        name for name, mod in modules.items()
        if rx_input in [d.name for d in mod.destinations]
    ]

    seen = {}
    i = 0
    while len(seen) < len(inputs_to_rx_input):
        bus = [("button", modules["broadcaster"], 0)]
        while bus:
            source, dest, signal = bus.pop(0)
            if isinstance(dest, Module) and dest.name == rx_input and signal == 1 and source in inputs_to_rx_input:
                seen.setdefault(source, i + 1)
            if isinstance(dest, Module):
                dest.recv(source, signal)
        i += 1

    return lcm_all(seen.values())

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")