from dataclasses import dataclass
from itertools import count
from bisect import insort_left
from operator import methodcaller
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
            enemy = None
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
                damage += addition
                immunity_match = p_immunity.search(line)
                immunity = set(immunity_match[0].split(', ')) if immunity_match else set()
                weakness_match = p_weakness.search(line)
                weakness = set(weakness_match[0].split(', ')) if weakness_match else set()
                attack_type = p_attack_type.search(line)[0]

                army = Army(next(ident), current_side, enemy, units, hp, immunity, weakness,
                            damage, attack_type, initiative)
                self.sides[current_side].add(army)
                insort_left(self.selection_order, army)

    def selection_phase(self):
        self.attack_order = []
        self.targeted = set()
        for attacker in self.selection_order:
            if not attacker.alive:
                continue
            max_damage = -1
            candidate = None
            for c in self.sides[attacker.enemy]:
                if c in self.targeted or attacker.attack_type in c.immunity:
                    continue
                damage_est = c.damage_estimation(attacker.attack_type, attacker.effective_power)
                if damage_est[0] > max_damage or (damage_est[0] == max_damage and (c.effective_power > (candidate.effective_power if candidate else 0) or (c.effective_power == (candidate.effective_power if candidate else 0) and c.initiative > (candidate.initiative if candidate else 0)))):
                    max_damage = damage_est[0]
                    candidate = c
            if candidate:
                self.targeted.add(candidate)
                attacker.target = candidate
                insort_left(self.attack_order, (-attacker.initiative, attacker))

    def attack_phase(self):
        new_selection_order = []
        for _, attacker in self.attack_order:
            if not attacker.alive or not attacker.target.alive:
                continue
            attacker.attack()
            if not attacker.target.alive:
                self.sides[attacker.enemy].remove(attacker.target)
        for side in self.sides.values():
            for army in side:
                if army.alive:
                    insort_left(new_selection_order, army)
        self.selection_order = new_selection_order

    def battle(self):
        old_units = sum(sum(army.units for army in side) for side in self.sides.values())
        while self.sides["immune_system"] and self.sides["infection"]:
            self.selection_phase()
            self.attack_phase()
            new_units = sum(sum(army.units for army in side) for side in self.sides.values())
            if old_units == new_units:
                return False, None
            old_units = new_units

        if self.sides["immune_system"]:
            return True, sum(army.units for army in self.sides["immune_system"])
        else:
            return False, sum(army.units for army in self.sides["infection"])


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

    def __lt__(self, other):
        return (self.effective_power, self.initiative) > (other.effective_power, other.initiative)

    def __hash__(self):
        return hash(self.ident)

    @property
    def alive(self):
        return self.units > 0

    def damage_estimation(self, attack_type, effective_power):
        multiplier = 2 if attack_type in self.weakness else 1 if attack_type not in self.immunity else 0
        return (multiplier * effective_power, self.effective_power, self.initiative)

    def attack(self):
        if not self.target.alive:
            return
        damage = self.damage_estimation(self.attack_type, self.effective_power)[0]
        killed = damage // self.target.hp
        self.target.units -= killed


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