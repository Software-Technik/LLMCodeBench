import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.read().strip().splitlines()
    lines.sort()
    guards_sleep = {}
    guards_total = {}
    guard = sleep = None
    for line in lines:
        minute = int(line[15:17])
        if line[19] == 'G':
            guard = int(line.split()[3][1:])
            if guard not in guards_sleep:
                guards_sleep[guard] = [0]*60
                guards_total[guard] = 0
        elif line[19] == 'f':
            sleep = minute
        else:
            for m in range(sleep, minute):
                guards_sleep[guard][m] += 1
            guards_total[guard] += minute - sleep
    guard1 = max(guards_total, key=guards_total.get)
    minute1 = max(range(60), key=lambda m: guards_sleep[guard1][m])
    guard2 = minute2 = freq2 = 0
    for g, counts in guards_sleep.items():
        m = max(range(60), key=lambda m: counts[m])
        if counts[m] > freq2:
            freq2 = counts[m]
            guard2 = g
            minute2 = m
    print(guard1*minute1, guard2*minute2)

if __name__ == '__main__':
    main()