import numpy as np
import sys
from timeit import default_timer

class NoCycleFound(Exception):
    pass

class Lumberyard:
    def __init__(self, file_name: str, max_iter: int = 10000):
        if max_iter < 10:
            raise ValueError
        self.start_time = default_timer()
        self.max_iter = max_iter
        self.land = self._load(file_name)
        self.values = []
        self.seen = {}

    def _load(self, fn):
        m = {'.':1,'|':10,'#':100}
        with open(fn) as f:
            data = [list(map(lambda c: m[c], line.strip())) for line in f]
        arr = np.zeros((len(data)+2, len(data[0])+2), np.uint16)
        arr[1:-1,1:-1] = data
        return arr

    def step(self):
        L = self.land
        n = (
            L[:-2,:-2]+L[:-2,1:-1]+L[:-2,2:]+
            L[1:-1,:-2]+L[1:-1,2:]+
            L[2:,:-2]+L[2:,1:-1]+L[2:,2:]
        )
        center = L[1:-1,1:-1]
        np.copyto(center,10,where=(center==1)&(n%100>=30))
        np.copyto(center,100,where=(center==10)&(n>=300))
        cond = (n>=100)&(n%100>=10)
        np.copyto(center,100,where=(center==100)&cond)
        np.copyto(center,1,where=(center==100)&~cond)

    def run(self):
        for i in range(self.max_iter):
            self.step()
            v = (self.land==10).sum()*(self.land==100).sum()
            h = hash(self.land.tobytes())
            if h in self.seen:
                start = self.seen[h]
                cycle = i - start
                self.ans1 = self.values[9]
                idx = start + ((1000000000 - start) % cycle) - 1
                self.ans2 = self.values[idx]
                return
            self.seen[h] = i
            self.values.append(v)
        raise NoCycleFound

if __name__=="__main__":
    inst = Lumberyard(sys.argv[1])
    inst.run()
    sys.stdout.write(f"{inst.ans1} {inst.ans2}")