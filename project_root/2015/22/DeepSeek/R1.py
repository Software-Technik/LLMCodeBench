To solve this problem, we need to determine the minimal amount of mana a player needs to spend to defeat a boss in a turn-based game, considering both normal and hard modes. The player can cast various spells with different effects, and the boss attacks each turn. The solution involves simulating all possible sequences of spells while optimizing for minimal mana usage.

### Approach
1. **Problem Analysis**: The game involves the player and the boss taking turns. The player can cast spells that deal damage, heal, or provide ongoing effects (like armor or damage over time). The boss attacks the player each turn. The goal is to find the minimal mana cost sequence of spells that defeats the boss without the player dying.
2. **State Representation**: The game state is represented by the player's hit points (HP), mana points, the boss's HP, and the remaining durations of active spells (Shield, Poison, Recharge). The turn (player's or boss's) is also part of the state.
3. **Priority Queue (Min-Heap)**: To efficiently explore states with the least mana spent first, we use a priority queue. Each entry in the queue is a tuple `(spent_mana, state)`, where `state` encapsulates the current game conditions.
4. **State Transitions**:
   - **Player's Turn**: The player can cast any affordable spell not currently active. Instant spells apply effects immediately, while timer spells start their durations.
   - **Boss's Turn**: The boss attacks the player, reducing the player's HP based on the player's armor (from active Shield spells).
5. **Effects Application**: At the start of each turn, active spells apply their effects (damage, healing, mana regeneration) and their durations are decremented.
6. **Termination Conditions**: The game ends if the boss's HP drops to zero (player wins) or the player's HP drops to zero (boss wins). In hard mode, the player loses 1 HP at the start of their turn.

### Solution Code

import heapq
import sys

def solve(boss_hp, boss_damage, part2=False):
    spells = {
        "missile": {"cost": 53, "damage": 4, "armor": 0, "heal_hp": 0, "heal_mana": 0, "turns": 0},
        "drain": {"cost": 73, "damage": 2, "armor": 0, "heal_hp": 2, "heal_mana": 0, "turns": 0},
        "shield": {"cost": 113, "damage": 0, "armor": 7, "heal_hp": 0, "heal_mana": 0, "turns": 6},
        "poison": {"cost": 173, "damage": 3, "armor": 0, "heal_hp": 0, "heal_mana": 0, "turns": 6},
        "recharge": {"cost": 229, "damage": 0, "armor": 0, "heal_hp": 0, "heal_mana": 101, "turns": 5},
    }
    start = (50, 500, boss_hp, 0, 0, 0, True)
    heap = [(0, start)]
    best = {start: 0}
    while heap:
        spent_mana, state = heapq.heappop(heap)
        if best.get(state, float('inf')) < spent_mana:
            continue
        player_hp, player_mana, boss_hp, shield, poison, recharge, is_player_turn = state
        
        if is_player_turn and part2:
            player_hp -= 1
            if player_hp <= 0:
                continue
        
        armor = 7 if shield > 0 else 0
        boss_damage_effect = 3 if poison > 0 else 0
        mana_gain = 101 if recharge > 0 else 0
        
        new_shield = shield - 1 if shield > 0 else 0
        new_poison = poison - 1 if poison > 0 else 0
        new_recharge = recharge - 1 if recharge > 0 else 0
        
        new_player_mana = player_mana + mana_gain
        new_boss_hp = boss_hp - boss_damage_effect
        new_player_hp = player_hp
        
        if new_boss_hp <= 0:
            return spent_mana
        
        if is_player_turn:
            for spell_name, spell in spells.items():
                if spell_name == 'shield' and new_shield > 0:
                    continue
                if spell_name == 'poison' and new_poison > 0:
                    continue
                if spell_name == 'recharge' and new_recharge > 0:
                    continue
                if new_player_mana < spell['cost']:
                    continue
                
                if spell_name in ['missile', 'drain']:
                    boss_after = new_boss_hp - spell['damage']
                    player_hp_after = new_player_hp + spell.get('heal_hp', 0)
                    player_mana_after = new_player_mana - spell['cost']
                    new_spent = spent_mana + spell['cost']
                    state_next = (
                        player_hp_after,
                        player_mana_after,
                        boss_after,
                        new_shield,
                        new_poison,
                        new_recharge,
                        False
                    )
                else:
                    if spell_name == 'shield':
                        updated_shield = spell['turns']
                        updated_poison = new_poison
                        updated_recharge = new_recharge
                    elif spell_name == 'poison':
                        updated_shield = new_shield
                        updated_poison = spell['turns']
                        updated_recharge = new_recharge
                    elif spell_name == 'recharge':
                        updated_shield = new_shield
                        updated_poison = new_poison
                        updated_recharge = spell['turns']
                    else:
                        updated_shield = new_shield
                        updated_poison = new_poison
                        updated_recharge = new_recharge
                    player_mana_after = new_player_mana - spell['cost']
                    new_spent = spent_mana + spell['cost']
                    state_next = (
                        new_player_hp,
                        player_mana_after,
                        new_boss_hp,
                        updated_shield,
                        updated_poison,
                        updated_recharge,
                        False
                    )
                
                if state_next in best and best[state_next] <= new_spent:
                    continue
                best[state_next] = new_spent
                heapq.heappush(heap, (new_spent, state_next))
        else:
            damage = max(1, boss_damage - armor)
            new_player_hp_after = new_player_hp - damage
            if new_player_hp_after <= 0:
                continue
            state_next = (
                new_player_hp_after,
                new_player_mana,
                new_boss_hp,
                new_shield,
                new_poison,
                new_recharge,
                True
            )
            if state_next in best and best[state_next] <= spent_mana:
                continue
            best[state_next] = spent_mana
            heapq.heappush(heap, (spent_mana, state_next))
    
    return float('inf')

def main():
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    boss_hp = int(data[0].split(": ")[1])
    boss_damage = int(data[1].split(": ")[1])
    part1_ans = solve(boss_hp, boss_damage, False)
    part2_ans = solve(boss_hp, boss_damage, True)
    sys.stdout.write(f"{part1_ans}\n{part2_ans}\n")

if __name__ == "__main__":
    main()


### Explanation
1. **Initialization**: The `solve` function initializes the game state with the player's starting HP and mana, and the boss's HP and damage. It uses a priority queue to explore states in order of increasing mana spent.
2. **State Processing**: For each state popped from the queue:
   - **Hard Mode**: If enabled, the player loses 1 HP at the start of their turn.
   - **Effects Application**: Active spells (Shield, Poison, Recharge) apply their effects (armor, damage, mana gain) and their durations are decremented.
   - **Termination Check**: If the boss's HP drops to zero, the current mana spent is returned as the solution.
3. **Player's Turn**: The player can cast any affordable spell not currently active. Instant spells apply effects immediately, while timer spells start their durations. New states are pushed into the queue.
4. **Boss's Turn**: The boss attacks the player, reducing the player's HP based on the player's armor. The resulting state is pushed back into the queue.
5. **Efficiency**: By using a priority queue and tracking the best mana cost for each state, the solution efficiently explores the minimal mana path to victory without redundant checks. This approach ensures optimal performance even for complex game states.