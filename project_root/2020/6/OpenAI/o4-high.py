import sys
result1 = result2 = 0
with open(sys.argv[1]) as f:
    persons = []
    for line in f:
        line = line.strip()
        if line:
            persons.append(line)
        else:
            s = set().union(*persons)
            result1 += len(s)
            c = set(persons[0])
            for p in persons[1:]:
                c &= set(p)
            result2 += len(c)
            persons = []
    if persons:
        s = set().union(*persons)
        result1 += len(s)
        c = set(persons[0])
        for p in persons[1:]:
            c &= set(p)
        result2 += len(c)
print(result1, result2)