import sys
from array import array
def main():
    parts = open(sys.argv[1]).read().strip().split(',')
    start = list(map(int, parts))
    N1 = 2020; N2 = 30000000
    last = array('I', [0]) * N2
    for i, num in enumerate(start[:-1]):
        last[num] = i + 1
    last_num = start[-1]
    res1 = 0
    for turn in range(len(start) + 1, N2 + 1):
        prev = last[last_num]
        last[last_num] = turn - 1
        if prev:
            num = turn - 1 - prev
        else:
            num = 0
        last_num = num
        if turn == N1:
            res1 = num
    print(res1, last_num)

if __name__ == '__main__':
    main()