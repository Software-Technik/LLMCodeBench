import sys,re
line_re=re.compile(r'(\d+) units each with (\d+) hit points(?: \(([^)]+)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)')
blueprint=[]
side=None
for line in open(sys.argv[1]):
    line=line.strip()
    if not line: continue
    if line.endswith(':'):
        side=0 if line.startswith('Immune') else 1
    else:
        m=line_re.match(line)
        units=int(m.group(1)); hp=int(m.group(2)); specials=m.group(3)
        base_damage=int(m.group(4)); attack_type=m.group(5); initiative=int(m.group(6))
        immun=set(); weak=set()
        if specials:
            for part in specials.split('; '):
                if part.startswith('immune to '): immun=set(part[10:].split(', '))
                elif part.startswith('weak to '): weak=set(part[8:].split(', '))
        blueprint.append((side,units,hp,immun,weak,base_damage,attack_type,initiative))
class Army:
    __slots__=('side','units','hp','immunity','weakness','damage','attack_type','initiative','target')
    def __init__(self,side,units,hp,immunity,weakness,damage,attack_type,initiative):
        self.side=side;self.units=units;self.hp=hp;self.immunity=immunity
        self.weakness=weakness;self.damage=damage;self.attack_type=attack_type
        self.initiative=initiative;self.target=None
def simulate(boost,specs=blueprint):
    immune=[];infection=[]
    for side,units,hp,immunity,weakness,base_damage,attack_type,initiative in specs:
        dmg=base_damage+boost if side==0 else base_damage
        a=Army(side,units,hp,immunity,weakness,dmg,attack_type,initiative)
        (immune if side==0 else infection).append(a)
    old_total=sum(a.units for a in immune)+sum(a.units for a in infection)
    while immune and infection:
        sel=immune+infection
        sel.sort(key=lambda a:(a.units*a.damage,a.initiative),reverse=True)
        targeted=set();attackers=[]
        for a in sel:
            EP=a.units*a.damage
            best=None;bd=0;be=0;bi=0
            atk_t=a.attack_type
            enemy=infection if a.side==0 else immune
            for d in enemy:
                if d in targeted or atk_t in d.immunity: continue
                mult=2 if atk_t in d.weakness else 1
                dmg=EP*mult
                if dmg==0: continue
                d_EP=d.units*d.damage; ini=d.initiative
                if dmg>bd or (dmg==bd and (d_EP>be or (d_EP==be and ini>bi))):
                    best=d;bd=dmg;be=d_EP;bi=ini
            if best:
                targeted.add(best);a.target=best;attackers.append(a)
        attackers.sort(key=lambda a:a.initiative,reverse=True)
        for a in attackers:
            if a.units<=0: continue
            d=a.target
            if d.units<=0: continue
            EP=a.units*a.damage
            mult=2 if a.attack_type in d.weakness else 1
            killed=EP*mult//d.hp
            if killed>0: d.units-=killed
        immune=[a for a in immune if a.units>0]
        infection=[a for a in infection if a.units>0]
        new_total=sum(a.units for a in immune)+sum(a.units for a in infection)
        if new_total==old_total: return False,None
        old_total=new_total
    if immune: return True,sum(a.units for a in immune)
    return False,sum(a.units for a in infection)
win0,units0=simulate(0)
result1=units0
if win0:
    result2=units0
else:
    lo=0;hi=None;b=1
    while True:
        win,units=simulate(b)
        if win:
            hi=b;break
        lo=b;b*=2
    low=lo+1;high=hi
    while low<high:
        mid=(low+high)//2
        win,_=simulate(mid)
        if win: high=mid
        else: low=mid+1
    _,result2=simulate(low)
sys.stdout.write(f"{result1} {result2}")