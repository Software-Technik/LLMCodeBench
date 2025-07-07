import sys

def main():
    import sys
    data = [line.strip() for line in open(sys.argv[1])]
    ingr = []
    for line in data:
        parts = line.split(": ")[1].split(", ")
        vals = {k:int(v) for k,v in (p.split(" ") for p in parts)}
        ingr.append((vals["capacity"], vals["durability"], vals["flavor"], vals["texture"], vals["calories"]))
    n = len(ingr)
    best1 = 0
    best2 = 0
    def dfs(i, rem, c0, d0, f0, t0, cal0):
        nonlocal best1, best2
        cap, dur, fla, tex, cal = ingr[i]
        if i == n - 1:
            v = rem
            c = c0 + v*cap
            d = d0 + v*dur
            f = f0 + v*fla
            t = t0 + v*tex
            c = c if c>0 else 0
            d = d if d>0 else 0
            f = f if f>0 else 0
            t = t if t>0 else 0
            score = c*d*f*t
            best1 = score if score>best1 else best1
            if cal0 + v*cal == 500 and score>best2:
                best2 = score
        else:
            for v in range(rem+1):
                dfs(i+1, rem-v, c0+v*cap, d0+v*dur, f0+v*fla, t0+v*tex, cal0+v*cal)
    dfs(0,100,0,0,0,0,0)
    sys.stdout.write(f"{best1}\n{best2}\n")

if __name__=="__main__":
    main()