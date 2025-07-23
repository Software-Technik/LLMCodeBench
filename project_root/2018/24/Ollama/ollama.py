from dataclasses import dataclass
from itertools import count
from bisect import insort_left
import re, sys

class Disease:
    def __init__(self, fn: str, boost: int=0) -> None:
        self.sides = {"immune_system": set(), "infection": set()}
        self.selection_order = []
        self.process_status_file(fn, boost)
        self.targeted = set()

    def process_status_file(self, fn: str, boost: int=0) -> None:
        p_numbers = re.compile(r"\d+")
        p_immunity = re.compile(r"(?<=immune to ).*?(?=[;)])")
        p_weakness = re.compile(r"(?<=weak to ).*?(?=[;)])")
        p_attack_type = re.compile(r"(?<=[\d+] )(\w+)(?= dam)")
        ident = count()

        with open(fn) as f:
            current_side = None
            addition = 0
            for line in f:
                line = line.strip()
                if not line:
                    continue

                if ":" in line:
                    current_side = "immune_system" if line.startswith("Immune") else "infection"
                    enemy = "infection" if current_side == "immune_system" else "immune_system"
                    addition = boost if current_side == "immune_system" else 0
                    continue

                units, hp, damage, initiative = map(int, p_numbers.findall(line))
                immunity = set(next(iter(p_immunity.findall(line)), "").split(", ") or [])
                weakness = set(next(iter(p_weakness.findall(line)), "").split(", ") or [])
                attack_type = p_attack_type.search(line).group()

                damage += addition
                army = Army(next(ident), current_side, enemy, units, hp, immunity, weakness,
                            damage, attack_type, initiative)
                self.sides[current_side].add(army)
                insort_left(self.selection_order, army)

    def selection_phase(self):
        self.attack_order = []
        self.targeted.clear()
        for attacker in reversed(self.selection_order):
            candidates = [c for c in self.sides[attacker.enemy]
                          if c not in self.targeted and attacker.attack_type not in c.immunity]
            if candidates:
                chosen_target = max(candidates, key=lambda c: (c.damage_estimation(attacker.attack_type, attacker.effective_power), -id(c)))
                self.targeted.add(chosen_target)
                insort_left(self.attack_order, (-attacker.initiative, attacker))
                attacker.target = chosen_target

    def attack_phase(self):
        for _, attacker in self.attack_order:
            if not attacker.alive or not attacker.target.alive:
                continue
            attacker.attack()
            if not attacker.target.alive:
                self.sides[attacker.enemy].remove(attacker.target)

    def battle(self):
        old_units = sum(sum(a.units for a in side) for side in self.sides.values())
        while self.sides["immune_system"] and self.sides["infection"]:
            self.selection_order.clear()
            self.selection_phase()
            self.attack_phase()
            new_units = sum(sum(a.units for a in side) for side in self.sides.values())
            if old_units == new_units:
                return False, None
            old_units = new_units

        winner_side = "immune_system" if self.sides["immune_system"] else "infection"
        return winner_side == "immune_system", sum(a.units for a in self.sides[winner_side])

@dataclass(order=True)
class Army:
    ident: int
    effective_power: int
    initiative: int
    side: str = ""
    enemy: str = ""
    units: int = 0
    hp: int = 0
    immunity: set[str] = None
    weakness: set[str] = None
    damage: int = 0
    attack_type: str = ""
    target = None

    @property
    def effective_power(self):
        return self.units * self.damage

    def __post_init__(self):
        self.immunity = set(str(attr for attr in self.immunity.split(", ")) if self.immunity else set())
        self.weakness = (set(str(attr for attr in self.weakness.split(", ")) if self.weakness else set()));s

    def damage_estimation(self, attack_type, effective_power):
        return (((attack_type in self.weakness) + 1) * effective_power,
                self.effective_power,
                self.initiative)

    @property
    def alive(self): return self.units > 0

    def attack(self):
        if not self.alive or not self.target.alive:
            return None
        target_damage = (2 * self.damage) if self.attack_type in self.target.weakness else self.damage
        killed_units = max(0, int(target_damage / self.target.hp))
        self.target.units -= killed_units

input_f = sys.argv[1]

disease = Disease(input_f)
found, result1 = disease.battle()
for boost in range(1, 10000):
    body=Disease(input_f,boost)
    found(result2)=body.battle()
	if "immune_system",result2 == True

s