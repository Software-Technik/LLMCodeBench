import sys

def main():
    with open(sys.argv[1], 'r') as file:
        n_elves = int(file.read().strip())
    
    # Calculate part1
    m = 1
    while m <= n_elves:
        m <<= 1
    m >>= 1
    part1_ans = 2 * (n_elves - m) + 1
    
    # Calculate part2
    p = 1
    while p * 3 <= n_elves:
        p *= 3
    if n_elves == p:
        part2_ans = p
    elif n_elves <= 2 * p:
        part2_ans = n_elves - p
    else:
        part2_ans = p + 2 * (n_elves - 2 * p)
    
    sys.stdout.write(f"{part1_ans} {part2_ans}")

if __name__ == '__main__':
    main()