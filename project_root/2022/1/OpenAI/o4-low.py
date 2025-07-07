import sys,heapq

def main():
    path = sys.argv[1]
    top3 = []
    max_sum = 0
    curr = 0
    with open(path) as f:
        for line in f:
            s = line.strip()
            if s:
                curr += int(s)
            else:
                if curr > max_sum: max_sum = curr
                if len(top3) < 3:
                    heapq.heappush(top3, curr)
                elif curr > top3[0]:
                    heapq.heapreplace(top3, curr)
                curr = 0
    if curr:
        if curr > max_sum: max_sum = curr
        if len(top3) < 3:
            heapq.heappush(top3, curr)
        elif curr > top3[0]:
            heapq.heapreplace(top3, curr)
    sys.stdout.write(f"{max_sum}\n{sum(top3)}\n")

if __name__ == "__main__":
    main()