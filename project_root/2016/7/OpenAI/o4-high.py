import sys
p1=0
p2=0
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        supers=[]
        hypers=[]
        s=[]
        inside=False
        for ch in line:
            if ch=='[':
                if s:
                    (hypers if inside else supers).append(''.join(s)); s=[]
                inside=True
            elif ch==']':
                if s:
                    (hypers if inside else supers).append(''.join(s)); s=[]
                inside=False
            else:
                s.append(ch)
        if s:
            (hypers if inside else supers).append(''.join(s))
        fa=False
        fh=False
        for seg in supers:
            for i in range(len(seg)-3):
                a,b,c,d=seg[i],seg[i+1],seg[i+2],seg[i+3]
                if a!=b and a==d and b==c:
                    fa=True; break
            if fa: break
        for seg in hypers:
            for i in range(len(seg)-3):
                a,b,c,d=seg[i],seg[i+1],seg[i+2],seg[i+3]
                if a!=b and a==d and b==c:
                    fh=True; break
            if fh: break
        if fa and not fh:
            p1+=1
        bab=set()
        for seg in supers:
            for i in range(len(seg)-2):
                a,b,c=seg[i],seg[i+1],seg[i+2]
                if a==c and a!=b:
                    bab.add(b+a+b)
        fs=False
        if bab:
            for seg in hypers:
                for bbb in bab:
                    if bbb in seg:
                        fs=True; break
                if fs: break
        if fs:
            p2+=1
sys.stdout.write(f"{p1} {p2}")