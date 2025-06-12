import sys
from collections import defaultdict
from time import time

def firsteight(freqs):
  return ''.join(list(map(str, freqs))[:8])

def part1(data):
  freqs = list(map(int, data))
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)

  for _ in range(100):
    newfreqs = []

    for i in range(maxlength):
      newf = 0
      j = 0
      for j in range(maxlength):
        repeats = i + 1
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newf += freqs[j] * factor
        
      newfreqs.append(abs(newf) % 10)
    
    freqs = newfreqs
  
  return firsteight(freqs)

officialRepeatCount = 10000

def part2(data, messageRepeat = officialRepeatCount):
  messageoffset = int(data[:7])
  freqs = list(map(int, data)) * messageRepeat
  pattern = [0, 1, 0, -1]
  maxlength = len(freqs)
  start = time()
  newfreqs = [0] * maxlength

  for step in range(100):
    #print('step', str(step).ljust(2, ' '), 'time', str(round(time() - start, 4)).ljust(7, "0"))

    for i in range(messageoffset, maxlength):
      newFrequency = 0
      repeats = i + 1
      for j in range(i, maxlength):
        pidx = (j + 1) // repeats
        pidx = pidx % 4
        factor = pattern[pidx]
        newFrequency += freqs[j] * factor
      newfreqs[i] = abs(newFrequency) % 10
    
    freqs = newfreqs.copy()

  return firsteight(freqs[messageoffset:])

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()[0]

sys.stdout.write(f"{part1(data)} {part2(data)}")