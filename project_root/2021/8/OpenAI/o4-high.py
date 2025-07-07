import sys
segmap={c:1<<i for i,c in enumerate('abcdefg')}
total1=0
total2=0
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        left,right=line.split('|')
        pats=left.split()
        outs=right.split()
        pm=[sum(segmap[c] for c in p) for p in pats]
        om=[sum(segmap[c] for c in o) for o in outs]
        for m in om:
            bc=m.bit_count()
            if bc in (2,3,4,7): total1+=1
        one=four=seven=eight=0
        for m in pm:
            bc=m.bit_count()
            if bc==2: one=m
            elif bc==3: seven=m
            elif bc==4: four=m
            elif bc==7: eight=m
        zero=six=nine=two=three=five=0
        for m in pm:
            bc=m.bit_count()
            if bc==6:
                if m&four==four: nine=m
                elif m&one==one: zero=m
                else: six=m
            elif bc==5:
                if m&one==one: three=m
                elif (m&four).bit_count()==2: two=m
                else: five=m
        d={zero:'0',one:'1',two:'2',three:'3',four:'4',five:'5',six:'6',seven:'7',eight:'8',nine:'9'}
        total2+=int(''.join(d[m] for m in om))
sys.stdout.write(f"{total1} {total2}")