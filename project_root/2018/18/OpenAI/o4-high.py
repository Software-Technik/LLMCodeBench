import sys
import numpy as np

class NoCycleFound(Exception): pass

class Lumberyard:
    def __init__(self, file_name, max_iter=10000):
        if max_iter < 10: raise ValueError
        self.max_iter = max_iter
        self.land = self.file_to_array(file_name)
        self.neighbors = np.zeros_like(self.land)
        self.H, self.W = self.land.shape[0]-2, self.land.shape[1]-2
        self.land_hashes = {}
        self.land_values = []
    @staticmethod
    def file_to_array(fn):
        m = {'.':1,'|':10,'#':100}
        with open(fn) as f: lines = [l.strip() for l in f]
        H, W = len(lines), len(lines[0])
        arr = np.zeros((H+2, W+2), dtype=int)
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                arr[i+1, j+1] = m[c]
        return arr
    def advance_minute(self):
        land = self.land; neigh = self.neighbors
        neigh.fill(0)
        inner = neigh[1:-1,1:-1]
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx or dy:
                    inner += land[1+dx:1+dx+self.H,1+dy:1+dy+self.W]
        n100 = neigh % 100
        empty = land == 1; trees = land == 10; lumber = land == 100
        land[empty & (n100 >= 30)] = 10
        land[trees & (neigh >= 300)] = 100
        cond = (neigh >= 100) & (n100 >= 10)
        land[lumber & cond] = 100
        land[lumber & ~cond] = 1
    def run_until_cycle(self):
        land = self.land; seen = self.land_hashes; lvals = self.land_values
        for i in range(self.max_iter):
            self.advance_minute()
            v = (land == 10).sum() * (land == 100).sum()
            h = hash(land.tobytes())
            if h in seen:
                start = seen[h]; length = i - start
                self.answer_one = lvals[9]
                loc = (1000000000 - start) % length
                self.answer_two = lvals[start + loc - 1]
                return
            seen[h] = i; lvals.append(v)
        raise NoCycleFound

if __name__ == "__main__":
    f = sys.argv[1]; c = Lumberyard(f); c.run_until_cycle(); sys.stdout.write(f"{c.answer_one} {c.answer_two}")