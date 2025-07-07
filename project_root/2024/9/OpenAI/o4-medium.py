import sys
def main():
    input_path = sys.argv[1]
    with open(input_path) as f:
        s = f.read().strip()
    arr = [int(c) for c in s]
    file_lengths = []
    initial_file_pos = []
    free_spaces = []
    pos = 0
    for i in range(0, len(arr), 2):
        L = arr[i]
        file_lengths.append(L)
        initial_file_pos.append(pos)
        pos += L
        if i + 1 < len(arr):
            F = arr[i + 1]
            if F > 0:
                free_spaces.append([pos, F])
            pos += F
    prev = 0
    p1 = 0
    for fid, L in enumerate(file_lengths):
        p1 += fid * (L * prev + L * (L - 1) // 2)
        prev += L
    spaces = [fs[:] for fs in free_spaces]
    new_pos = initial_file_pos[:]
    for fid in range(len(file_lengths) - 1, -1, -1):
        orig = initial_file_pos[fid]
        L = file_lengths[fid]
        for sp in spaces:
            if sp[0] < orig and sp[1] >= L:
                new_pos[fid] = sp[0]
                sp[0] += L; sp[1] -= L
                break
    p2 = 0
    for fid, L in enumerate(file_lengths):
        start = new_pos[fid]
        p2 += fid * (L * start + L * (L - 1) // 2)
    print(p1, p2)

if __name__ == "__main__":
    main()