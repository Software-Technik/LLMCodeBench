import numpy as np
import sys

def main(fn):
    m = {'.':1, '|':10, '#':100}
    data = [ [m[c] for c in line.strip()] for line in open(fn) ]
    rows, cols = len(data), len(data[0])
    land = np.zeros((rows+2, cols+2), int)
    land[1:-1,1:-1] = data
    neighbors = np.zeros_like(land)
    land_hash_map = {}
    land_values = []
    max_iter = 10000
    for current_iter in range(max_iter):
        box = np.cumsum(land, axis=1)
        box[:,3:] -= box[:,:-3]
        box = np.cumsum(box, axis=0)
        box[3:,:] -= box[:-3,:]
        neighbors[1:-1,1:-1] = box[2:,2:] - land[1:-1,1:-1]
        nn100 = neighbors % 100
        empty = land==1; trees = land==10; lumber = land==100
        land[empty & (nn100>=30)] = 10
        land[trees & (neighbors>=300)] = 100
        lf = (neighbors>=100) & (nn100>=10)
        land[lumber & ~lf] = 1
        land[lumber & lf] = 100
        value = (land==10).sum() * (land==100).sum()
        h = hash(land.tobytes())
        if h in land_hash_map:
            cycle_start = land_hash_map[h]
            cycle_length = current_iter - cycle_start
            break
        land_hash_map[h] = current_iter
        land_values.append(value)
    ans1 = land_values[9]
    idx = cycle_start + ((1000000000 - cycle_start - 1) % cycle_length)
    ans2 = land_values[idx]
    print(ans1, ans2)

if __name__ == "__main__":
    main(sys.argv[1])