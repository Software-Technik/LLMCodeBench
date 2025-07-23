import sys

def main():
    h1 = d1 = 0
    aim2 = h2 = d2 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split()
            cmd = parts[0]
            val = int(parts[1])
            if cmd == 'forward':
                h1 += val
                h2 += val
                d2 += val * aim2
            elif cmd == 'down':
                d1 += val
                aim2 += val
            elif cmd == 'up':
                d1 -= val
                aim2 -= val
            else:
                raise ValueError('Invalid command')
    sys.stdout.write(f"{h1 * d1} {h2 * d2}")

if __name__ == "__main__":
    main()