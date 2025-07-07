import sys

with open(sys.argv[1]) as f:
    p1 = p2 = 0
    for raw in f:
        line = raw.rstrip('\n')
        n = len(line)
        m = 0
        i = 1
        end = n - 1
        while i < end:
            if line[i] == '\\':
                if line[i+1] == 'x':
                    i += 4
                else:
                    i += 2
                m += 1
            else:
                i += 1
                m += 1
        p1 += n - m
        new = 2
        for c in line:
            new += 2 if c == '\\' or c == '"' else 1
        p2 += new - n
    sys.stdout.write(f"{p1}\n{p2}\n")