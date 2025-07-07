import sys
def main():
    setup={"red":12,"green":13,"blue":14}
    total1=0
    total2=0
    with open(sys.argv[1]) as f:
        for i,line in enumerate(f,1):
            idx=line.find(':')
            s=line[idx+1:].replace(';',',')
            ok=1
            p=1
            maxc={}
            for entry in s.split(','):
                entry=entry.strip()
                if not entry: continue
                j=entry.find(' ')
                n=int(entry[:j])
                color=entry[j+1:]
                if ok and n>setup[color]: ok=0
                prev=maxc.get(color)
                if prev is None or n>prev: maxc[color]=n
            if ok: total1+=i
            for v in maxc.values(): p*=v
            total2+=p
    sys.stdout.write(f"{total1} {total2}")
if __name__=='__main__':
    main()