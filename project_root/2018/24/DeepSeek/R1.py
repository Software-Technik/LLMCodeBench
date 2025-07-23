from dataclasses import dataclass
import re
import sys

@dataclass
class Army:
    ident: int
    side: str
    enemy: str
    units: int
    hp: int
    immunity: set
    weakness: set
    damage: int
    attack_type: str
    initiative: int
    target: 'Army' = None

    @property
    def effective_power(self):
        return self.units * self.damage

    def __hash__(self):
        return hash(self.ident)

    @property
    def alive(self):
        return self.units > 0

    def damage_estimation(self, attack_type, effective_power):
        factor = 1
        if attack_type in self.immunity:
            factor = 0
        elif attack_type in self.weakness:
            factor = 2
        return (factor * effective_power, self.effective_power, self.initiative)

    def attack(self):
        self.target.take_damage(self.attack_type, self.effective_power)

    def take_damage(self, attack_type, effective_power):
        factor = 1
        if attack_type in self.immunity:
            factor = 0
        elif attack_type in self.weakness:
            factor = 2
        damage = factor * effective_power
        killed = damage // self.hp
        self.units -= killed

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
            enemy = None
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if ":" in line:
                    current_side = "immune_system" if line.startswith("Immune") else "infection"
                    enemy = "immune_system" if current_side == "infection" else "infection"
                    continue

                units, hp, damage, initiative = (int(n) for n in p_numbers.findall(line))
                damage += boost if current_side == "immune_system" else 0
                immunity = p_immunity.findall(line)
                immunity = set(immunity[0].split(', ')) if immunity else set()
                weakness = p_weakness.findall(line)
                weakness = set(weakness[0].split(', ')) if weakness else set()
                attack_type = p_attack_type.search(line)[0]

                army = Army(next(ident), current_side, enemy, units, hp, immunity, weakness,
                            damage, attack_type, initiative)
                self.sides[current_side].add(army)
                self.selection_order.append(army)
        self.selection_order.sort(key=lambda a: (a.effective_power, a.initiative), reverse=True)

    def selection_phase(self):
        self.attack_order = []
        self.targeted = set()
        for attacker in self.selection_order:
            if not attacker.alive:
                continue
            best_candidate = None
            best_key = None
            attack_type = attacker.attack_type
            effective_power = attacker.effective_power
            for c in self.sides[attacker.enemy]:
                if not c.alive or c in self.targeted or attack_type in c.immunity:
                    continue
                key = c.damage_estimation(attack_type, effective_power)
                if best_candidate is None or key > best_key:
                    best_candidate = c
                    best_key = key
            if best_candidate is not None:
                self.targeted.add(best_candidate)
                attacker.target = best_candidate
                self.attack_order.append(attacker)
        self.attack_order.sort(key=lambda a: a.initiative, reverse=True)

    def attack_phase(self):
        for attacker in self.attack_order:
            if attacker.alive and attacker.target.alive:
                attacker.attack()
                if not attacker.target.alive:
                    self.sides[attacker.enemy].discard(attacker.target)
        self.selection_order = []
        for army in self.sides["immune_system"]:
            if army.alive:
                self.selection_order.append(army)
        for army in self.sides["infection"]:
            if army.alive:
                self.selection_order.append(army)
        self.selection_order.sort(key=lambda a: (a.effective_power, a.initiative), reverse=True)

    def battle(self):
        old_units = sum(army.units for side in self.sides.values() for army in side)
        while self.sides["immune_system"] and self.sides["infection"]:
            self.selection_phase()
            self.attack_phase()
            new_units = sum(army.units for side in self.sides.values() for army in side)
            if old_units == new_units:
                return False, None
            old_units = new_units

        if self.sides["immune_system"]:
            return True, sum(army.units for army in self.sides["immune_system"])
        else:
            return False, sum(army.units for army in self.sides["infection"])

def count():
    i = 0
    while True:
        yield i
        i += 1

input_f = sys.argv[1]
disease = Disease(input_f)
found, result1 = disease.battle()

boost = 0
while True:
    body = Disease(input_f, boost)
    found, result2 = body.battle()
    if found:
        break
    boost += 1

sys.stdout.write(f"{result1} {result2}")