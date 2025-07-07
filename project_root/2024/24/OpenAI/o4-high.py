#!/usr/bin/env python3
import sys

def part1(lines):
    i=lines.index('\n')
    first=lines[:i]; second=lines[i+1:]
    vals={k:int(v) for k,v in (line.strip().split(':') for line in first)}
    gates={out:(a,b,op) for a,op,b,_,out in (line.split() for line in second)}
    while gates:
        for out,(a,b,op) in list(gates.items()):
            if a in vals and b in vals:
                if op=='AND':v=vals[a]&vals[b]
                elif op=='OR':v=vals[a]|vals[b]
                else: v=vals[a]^vals[b]
                vals[out]=v
                del gates[out]
    zs=sorted(x for x in vals if x[0]=='z')
    b=''.join(str(vals[z]) for z in zs[::-1])
    return int(b,2)

def part2(lines):
    i=lines.index('\n')
    second=lines[i+1:]
    formulas={out:(a,b,op) for a,op,b,_,out in (line.split() for line in second)}
    def progress():
        vz_cache={}; vix_cache={}; vdc_cache={}; vcb_cache={}; vrc_cache={}
        def vz(w,n):
            key=(w,n)
            if key in vz_cache: return vz_cache[key]
            if w not in formulas: r=False
            else:
                a,b,op=formulas[w]
                if op!='XOR': r=False
                elif n==0: r={a,b}=={'x00','y00'}
                else:
                    xi=f'x{n:02d}'; yi=f'y{n:02d}'
                    r=(vix(a,n) and vcb(b,n)) or (vix(b,n) and vcb(a,n))
            vz_cache[key]=r; return r
        def vix(w,n):
            key=(w,n)
            if key in vix_cache: return vix_cache[key]
            if w not in formulas: r=False
            else:
                a,b,op=formulas[w]
                if op!='XOR': r=False
                else:
                    xi=f'x{n:02d}'; yi=f'y{n:02d}'
                    r=(a==xi and b==yi) or (a==yi and b==xi)
            vix_cache[key]=r; return r
        def vdc(w,n):
            key=(w,n)
            if key in vdc_cache: return vdc_cache[key]
            if w not in formulas: r=False
            else:
                a,b,op=formulas[w]
                if op!='AND': r=False
                else:
                    xi=f'x{n:02d}'; yi=f'y{n:02d}'
                    r=(a==xi and b==yi) or (a==yi and b==xi)
            vdc_cache[key]=r; return r
        def vcb(w,n):
            key=(w,n)
            if key in vcb_cache: return vcb_cache[key]
            if w not in formulas: r=False
            else:
                a,b,op=formulas[w]
                if n==1: r=(op=='AND' and {a,b}=={'x00','y00'})
                elif op!='OR': r=False
                else: r=(vdc(a,n-1) and vrc(b,n-1)) or (vdc(b,n-1) and vrc(a,n-1))
            vcb_cache[key]=r; return r
        def vrc(w,n):
            key=(w,n)
            if key in vrc_cache: return vrc_cache[key]
            if w not in formulas: r=False
            else:
                a,b,op=formulas[w]
                if op!='AND': r=False
                else: r=(vix(a,n) and vcb(b,n)) or (vix(b,n) and vcb(a,n))
            vrc_cache[key]=r; return r
        n=0
        while vz(f'z{n:02d}',n): n+=1
        return n
    swaps=[]; keys=list(formulas)
    for _ in range(4):
        base=progress()
        for x in keys:
            for y in keys:
                if x==y: continue
                formulas[x],formulas[y]=formulas[y],formulas[x]
                if progress()>base:
                    swaps+=[x,y]; break
                formulas[x],formulas[y]=formulas[y],formulas[x]
            else: continue
            break
    return ','.join(sorted(swaps))

def main():
    lines=open(sys.argv[1]).read().splitlines(True)
    print(part1(lines), part2(lines))

if __name__=='__main__':
    main()