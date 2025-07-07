import sys

def main():
    text = open(sys.argv[1]).read()
    workflows_txt, parts_txt = text.split("\n\n", 1)
    workflows = {}
    for line in workflows_txt.splitlines():
        name, conds = line.split("{", 1)
        conds = conds[:-1]
        rules = []
        for rule in conds.split(","):
            if "<" in rule:
                cat, rest = rule.split("<", 1)
                v, wf = rest.split(":", 1)
                rules.append(("<", cat, int(v), wf))
            elif ">" in rule:
                cat, rest = rule.split(">", 1)
                v, wf = rest.split(":", 1)
                rules.append((">", cat, int(v), wf))
            else:
                rules.append(("=", None, None, rule))
        workflows[name] = rules

    total1 = 0
    for line in parts_txt.splitlines():
        part = {}
        for tok in line.split():
            cat, val = tok.split("=")
            part[cat] = int(val)
        wf = "in"
        while wf != "A" and wf != "R":
            for t, cat, val, nwf in workflows[wf]:
                if t == "<" and part[cat] < val:
                    wf = nwf
                    break
                elif t == ">" and part[cat] > val:
                    wf = nwf
                    break
                elif t == "=":
                    wf = nwf
                    break
        if wf == "A":
            total1 += sum(part.values())

    total2 = 0
    initial_ranges = {"x": [(1, 4000)], "m": [(1, 4000)], "a": [(1, 4000)], "s": [(1, 4000)]}

    def traverse(wf, ranges):
        nonlocal total2
        if wf == "A":
            s = 1
            for sub in ranges.values():
                n = 0
                for a, b in sub:
                    n += b - a + 1
                s *= n
            total2 += s
            return
        if wf == "R":
            return
        for t, cat, val, nwf in workflows[wf]:
            if t == "<":
                c, v = cat, val
                new_c = []
                rem = []
                for a, b in ranges[c]:
                    if b < v:
                        new_c.append((a, b))
                    elif a < v:
                        new_c.append((a, v - 1))
                        rem.append((v, b))
                    else:
                        rem.append((a, b))
                if new_c:
                    nr = ranges.copy()
                    nr[c] = new_c
                    traverse(nwf, nr)
                ranges = ranges.copy()
                ranges[c] = rem
                if not rem:
                    return
            elif t == ">":
                c, v = cat, val
                new_c = []
                rem = []
                for a, b in ranges[c]:
                    if a > v:
                        new_c.append((a, b))
                    elif b > v:
                        new_c.append((v + 1, b))
                        rem.append((a, v))
                    else:
                        rem.append((a, b))
                if new_c:
                    nr = ranges.copy()
                    nr[c] = new_c
                    traverse(nwf, nr)
                ranges = ranges.copy()
                ranges[c] = rem
                if not rem:
                    return
            else:
                traverse(nwf, ranges)

    traverse("in", initial_ranges)
    sys.stdout.write(f"{total1} {total2}")

if __name__ == "__main__":
    main()