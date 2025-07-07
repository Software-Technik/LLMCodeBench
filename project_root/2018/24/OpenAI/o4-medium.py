import re,sys
p_numbers=re.compile(r"\d+")
p_immunity=re.compile(r"(?<=immune to ).*?(?=[;)])")
p_weakness=re.compile(r"(?<=weak to ).*?(?=[;)])")
p_attack_type=re.compile(r"\d+ (\w+) damage")
def parse(fn):
    specs=[]
    with open(fn) as f:
        side=enemy=None
        for line in f:
            l=line.strip()
            if not l: continue
            if l.endswith(":"):
                if l.startswith("Immune"):
                    side="immune_system"; enemy="infection"
                else:
                    side="infection"; enemy="immune_system"
                continue
            nums=list(map(int,p_numbers.findall(l)))
            units,hp,damage,initiative=nums[0],nums[1],nums[2],nums[3]
            imm=p_immunity.findall(l)
            immunity=set(imm[0].split(', ')) if imm else set()
            wk=p_weakness.findall(l)
            weakness=set(wk[0].split(', ')) if wk else set()
            attack_type=p_attack_type.search(l).group(1)
            specs.append((side,enemy,units,hp,immunity,weakness,damage,attack_type,initiative))
    return specs

class Army:
    __slots__=('ident','side','enemy','units','hp','immunity','weakness','damage','attack_type','initiative')
    def __init__(self,ident,side,enemy,units,hp,immunity,weakness,damage,attack_type,initiative):
        self.ident=ident;self.side=side;self.enemy=enemy;self.units=units;self.hp=hp
        self.immunity=immunity;self.weakness=weakness;self.damage=damage;self.attack_type=attack_type;self.initiative=initiative
    def __hash__(self): return self.ident

class Disease:
    __slots__=('sides',)
    def __init__(self,specs,boost):
        self.sides={'immune_system':[],'infection':[]}
        for ident,(side,enemy,units,hp,imm,weak,damage,atype,init) in enumerate(specs):
            dmg=damage+boost if side=='immune_system' else damage
            self.sides[side].append(Army(ident,side,enemy,units,hp,imm,weak,dmg,atype,init))
    def battle(self):
        total=lambda:sum(a.units for sl in self.sides.values() for a in sl)
        old_units=total()
        while self.sides['immune_system'] and self.sides['infection']:
            targeted=set();target_map={}
            attackers=sorted(self.sides['immune_system']+self.sides['infection'],key=lambda a:(-a.units*a.damage,-a.initiative))
            for a in attackers:
                best=None;best_score=(-1,0,0)
                eff=a.units*a.damage
                for c in self.sides[a.enemy]:
                    if c in targeted or a.attack_type in c.immunity: continue
                    dmg=eff*(2 if a.attack_type in c.weakness else 1)
                    score=(dmg,c.units*c.damage,c.initiative)
                    if score>best_score: best_score, best=score, c
                if best: targeted.add(best); target_map[a]=best
            for a in sorted(target_map, key=lambda a:-a.initiative):
                if a.units<=0: continue
                b=target_map[a]
                eff=a.units*a.damage
                dmg=eff*(2 if a.attack_type in b.weakness else 1)
                killed=dmg//b.hp
                if killed>0: b.units-=min(killed,b.units)
            self.sides['immune_system']=[a for a in self.sides['immune_system'] if a.units>0]
            self.sides['infection']=[a for a in self.sides['infection'] if a.units>0]
            new_units=total()
            if new_units==old_units: return False,None
            old_units=new_units
        if self.sides['immune_system']:
            return True,sum(a.units for a in self.sides['immune_system'])
        return False,sum(a.units for a in self.sides['infection'])

fn=sys.argv[1]
specs=parse(fn)
_,r1=Disease(specs,0).battle()
for boost in range(10000):
    win,r2=Disease(specs,boost).battle()
    if win: break
sys.stdout.write(f"{r1} {r2}")