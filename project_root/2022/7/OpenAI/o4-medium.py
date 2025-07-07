import sys
from collections import defaultdict

def parse_commands(data):
    idx = 0
    dirs = {"/": 0}
    sub_dirs = defaultdict(list)
    wd = []
    while idx < len(data):
        line = data[idx]
        if line.startswith("$ cd"):
            tgt = line[5:]
            if tgt == "..":
                wd.pop()
            else:
                wd.append(tgt)
            idx += 1
        elif line.startswith("$ ls"):
            idx += 1
            curr = "/".join(wd)
            while idx < len(data) and not data[idx].startswith("$"):
                t, name = data[idx].split()
                if t == "dir":
                    p = f"{curr}/{name}"
                    dirs[p] = 0
                    sub_dirs[curr].append(p)
                else:
                    dirs[curr] += int(t)
                idx += 1
        else:
            idx += 1
    return dirs, sub_dirs

def main():
    path = sys.argv[1]
    with open(path) as f:
        data = f.read().splitlines()
    dirs, sub_dirs = parse_commands(data)
    sizes = {}
    def dfs(p):
        s = dirs[p]
        for c in sub_dirs.get(p, ()):
            s += dfs(c)
        sizes[p] = s
        return s
    dfs("/")
    total1 = sum(v for v in sizes.values() if v <= 100000)
    unused = 70000000 - sizes["/"]
    need = 30000000 - unused
    total2 = min(v for v in sizes.values() if v >= need)
    print(total1)
    print(total2)

if __name__ == "__main__":
    main()