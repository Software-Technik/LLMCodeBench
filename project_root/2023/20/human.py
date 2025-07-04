import sys
import math
from functools import reduce

bus = []

class Module:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def send(self):
        for destination in self.destinations:
            bus.append((self.name, destination, self.state))

    def instantiate_destinations(self, modules):
        self.destinations = [modules.get(dest, Module(dest, [])) if isinstance(dest, str) else dest for dest in self.destinations]

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
        self.signals = {src: 0 for src in sources}

    @property
    def state(self):
        return int(not all(self.signals.values()))

    def recv(self, source, signal):
        self.signals[source] = signal
        self.send()

    def reset(self):
        for key in self.signals:
            self.signals[key] = 0


class Broadcaster(Module):
    def recv(self, source, signal):
        self.state = signal
        self.send()


def strip_prefix(name):
    return name[1:] if name[0] in "%&" else name


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

    for mod in modules.values():
        mod.instantiate_destinations(modules)

    return network, modules


def part1(text):
    global bus
    _, modules = parse_network(text)
    counts = [0, 0]

    for _ in range(1000):
        bus = [("button", modules["broadcaster"], 0)]
        while bus:
            source, destination, signal = bus.pop(0)
            counts[signal] += 1
            destination.recv(source, signal)

    return counts[0] * counts[1]


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_all(nums):
    return reduce(lcm, nums)


def part2(text):
    global bus
    network, modules = parse_network(text)

    rx_input = None
    for name, mod in modules.items():
        for dest in mod.destinations:
            if dest.name == "rx":
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
            if dest.name == rx_input and signal == 1 and source in inputs_to_rx_input:
                if source not in seen:
                    seen[source] = i + 1
            dest.recv(source, signal)
        i += 1

    return lcm_all(seen.values())


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")