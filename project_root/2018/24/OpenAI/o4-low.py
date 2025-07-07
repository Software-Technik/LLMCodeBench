import re, sys
from itertools import count

class Disease:
    def __init__(self, fn: str, boost: int=0):
        self.sides = {"immune_system": [], "infection": []}
        self.process(fn, boost)

    def process(self, fn, boost):
        p_numbers = re.compile(r"\d+")
        p_immunity = re.compile(r"(?<=immune to ).*?(?=[;)])")
        p_weakness = re.compile(r"(?<=weak to ).*?(?=[;)])")
        p_attack = re.compile(r"(?<=[\d+] )(\w+)(?= dam)")
        ident = count()
        current, enemy, add = None, None, 0
        for line in open(fn):
            line = line.strip()
            if not line: continue
            if ':' in line:
                if line.startswith("Immune"):
                    current, enemy, add = "immune_system", "infection", boost
                else:
                    current, enemy, add = "infection", "immune_system", 0
                continue
            nums = list(map(int, p_numbers.findall(line)))
            units, hp, dmg, init = nums[0], nums[1], nums[2]+add, nums[3]
            imm = set(p_immunity.findall(line)[0].split(', ')) if 'immune to' in line else set()
            weak = set(p_weakness.findall(line)[0].split(', ')) if 'weak to' in line else set()
            atk = p_attack.search(line)[0]
            army = Army(next(ident), current, enemy, units, hp, dmg, atk, init, imm, weak)
            self.sides[current].append(army)

    def battle(self):
        total = lambda: sum(a.units for side in self.sides.values() for a in side)
        prev = total()
        while self.sides["immune_system"] and self.sides["infection"]:
            order = sorted(self.sides["immune_system"]+self.sides["infection"])
            targets = set()
            attackers = []
            for a in order:
                cand = [e for e in self.sides[a.enemy] if e not in targets and a.attack_type not in e.immunity]
                if cand:
                    t = max(cand, key=lambda e: (e.damage_est(a.attack_type), e.effective_power, e.initiative))
                    targets.add(t); a.target = t
                    attackers.append(a)
            attackers.sort(key=lambda a: -a.initiative)
            for a in attackers:
                if a.units>0 and a.target and a.target.units>0:
                    dmg = a.damage_est(a.attack_type)
                    k = dmg//a.target.hp
                    a.target.units -= k
                    if a.target.units<=0:
                        self.sides[a.enemy].remove(a.target)
            curr = total()
            if curr==prev: return False, None
            prev = curr
        immune = sum(a.units for a in self.sides["immune_system"])
        inf = sum(a.units for a in self.sides["infection"])
        return (True, immune) if immune else (False, inf)

class Army:
    __slots__ = ("id","side","enemy","units","hp","damage","attack_type","initiative","immunity","weakness","target")
    def __init__(self,i,side,enemy,u,h,d,atype,init,imm,weak):
        self.id, self.side, self.enemy, self.units, self.hp = i, side, enemy, u, h
        self.damage, self.attack_type, self.initiative = d, atype, init
        self.immunity, self.weakness, self.target = imm, weak, None
    def __lt__(self, other):
        ep = self.effective_power; oep = other.effective_power
        return (ep, self.initiative) > (oep, other.initiative)
    @property
    def effective_power(self): return self.units*self.damage
    def damage_est(self, atype): return self.effective_power*(2 if atype in self.weakness else 1)

fn = sys.argv[1]
d = Disease(fn)
_, r1 = d.battle()
for b in range(10000):
    d = Disease(fn, b)
    f, r2 = d.battle()
    if f: break
sys.stdout.write(f"{r1} {r2}")