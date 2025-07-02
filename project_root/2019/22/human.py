import sys

def num(line):
  return int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))

def rev(position, size):
  return size - position - 1

def inc(position, size, n):
  return (n * position) % size

def cut(position, size, n):
  return position - n if position >= n else size - (n - position)

def part1(data, size):
  program = [
    (1, None) if "stack" in line else
    (2, num(line)) if "inc" in line else
    (3, num(line)) if "cut" in line else
    None # Problem!
    for line in data
  ]

  position = 2019

  for op in program:
    if op[0] == 1: position = rev(position, size)
    elif op[0] == 2: position = inc(position, size, op[1])
    elif op[0] == 3: position = cut(position, size, op[1])

  return position 

DECK = 119315717514047
REPEAT = 101741582076661
POSITION = 2020

# The do-nothing shuffle: 0 + 1*x
IDENTITY = [ 0, 1 ]

# Applies shuffle f() to position x
def shuffle_apply(f, x):
    return (f[0] + f[1] * x) % DECK

# Takes shuffle f() and g() and returns the shuffle f(g())
#   f(x) = a + b*x
#   g(x) = c + d*x
#   f(g(x)) = a + b*(c + d*x)
#           = (a + b*c) + b*d*x
#           = f(c) + b*d*x
def shuffle_compose(f, g):
    return [ shuffle_apply(f, g[0]), (f[1] * g[1]) % DECK ]

# Compose a shuffle many times with itself.
#   repeat - how many repetitions to apply
#   f      - the shuffle f()
#   step   - how many repetitions f() currently represents
def shuffle_repeat(repeat, f, step = 1):
    fN = IDENTITY
    if step <= repeat:
        fN, repeat = shuffle_repeat(repeat, shuffle_compose(f, f), step * 2)
    if step <= repeat:
        fN, repeat = shuffle_compose(f, fN), repeat - step
    return fN, repeat

#part2 repo: https://gist.github.com/Voltara/7d417c77bc2308be4c831f1aa5a5a48d
def part2(data):
    # Read the input and compose all of the shuffle steps
    shuf = IDENTITY
    for line in data:
        #print(line)
        f = line.split()
        if line == "deal into new stack":
            shuf = shuffle_compose([ -1, -1 ], shuf)
        elif line.startswith("cut"):
            shuf = shuffle_compose([ -int(f[1]), 1 ], shuf)
        elif line.startswith("deal with increment"):
            shuf = shuffle_compose([ 0, int(f[3]) ], shuf)

    # Observation: Repeating the shuffle (DECK - 1) times returns it to
    # the original ordering.  While this does not necessarily hold true
    # for all deck sizes, it works for the deck size given in Part 2.
    # (Experiment idea: What deck sizes does it work for?)
    assert(shuffle_repeat(DECK - 1, shuf)[0] == IDENTITY)

    # This gives us a way to apply the shuffle in reverse.  If we repeat
    # the shuffle (DECK - 1 - n) times, it brings the deck to a state where
    # n more shuffles will restore it to factory order.  This is exactly
    # the same as reversing the shuffle n times.
    shufN, _ = shuffle_repeat(DECK - 1 - REPEAT, shuf)
    return shuffle_apply(shufN, POSITION)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data.copy(), 10007)} {part2(data.copy())}")