import sys
from heapq import heappush, heappop

def astar_blocked_thresh(thresh, return_cost):
    N = 70
    size = N + 1
    INF = 10**9
    visited = [[False]*size for _ in range(size)]
    gscore = [[INF]*size for _ in range(size)]
    dd = ((1,0),(0,1),(-1,0),(0,-1))
    def h(i,j):
        return abs(N-i)+abs(N-j)
    gscore[0][0] = 0
    heap = [(h(0,0), 0, 0, 0)]
    while heap:
        f, g, i, j = heappop(heap)
        if visited[i][j]: continue
        visited[i][j] = True
        if (i,j)==(N,N):
            return g if return_cost else True
        for di,dj in dd:
            ii, jj = i+di, j+dj
            if 0 <= ii < size and 0 <= jj < size and not visited[ii][jj] and grid_idx[ii][jj] >= thresh:
                ng = g+1
                if ng < gscore[ii][jj]:
                    gscore[ii][jj] = ng
                    heappush(heap, (ng + h(ii,jj), ng, ii, jj))
    return False

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().splitlines()

coords = [tuple(map(int, line.split(','))) for line in lines]
N = 70
size = N+1
L = len(coords)
INF = L+1
grid_idx = [[INF]*size for _ in range(size)]
for idx, (i,j) in enumerate(coords):
    if 0 <= i <= N and 0 <= j <= N:
        grid_idx[i][j] = idx

part1 = astar_blocked_thresh(1024, True)
lo, hi = 0, L
while lo < hi:
    mid = (lo + hi)//2
    if astar_blocked_thresh(mid, False):
        lo = mid+1
    else:
        hi = mid
res2 = coords[lo-1]
print(part1, f"{res2[0]},{res2[1]}")