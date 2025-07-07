import sys

def part1(data):
    count=0
    for line in data:
        outs=line.split('|')[1].split()
        for o in outs:
            l=len(o)
            if l==2 or l==3 or l==4 or l==7:
                count+=1
    return count

def part2(data):
    total=0
    for line in data:
        left,right=line.split('|')
        patterns=left.split()
        outputs=right.split()
        one=four=seven=eight=None
        for p in patterns:
            l=len(p)
            if l==2: one=set(p)
            elif l==3: seven=set(p)
            elif l==4: four=set(p)
            elif l==7: eight=set(p)
        zero=nine=six=two=three=five=None
        for p in patterns:
            s=set(p)
            l=len(p)
            if l==6:
                if four<=s: nine=s
                elif one<=s: zero=s
                else: six=s
            elif l==5:
                if one<=s: three=s
                elif len(s&four)==2: two=s
                else: five=s
        mapping={frozenset(zero):'0',frozenset(one):'1',frozenset(two):'2',frozenset(three):'3',frozenset(four):'4',frozenset(five):'5',frozenset(six):'6',frozenset(seven):'7',frozenset(eight):'8',frozenset(nine):'9'}
        val=''.join(mapping[frozenset(o)] for o in outputs)
        total+=int(val)
    return total

data=[l.strip() for l in open(sys.argv[1]) if l.strip()]
print(part1(data),part2(data))