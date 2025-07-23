import sys

def redistribute(banks):
    length = len(banks)
    seen = {}
    step_count = 0
    current_state = tuple(banks)
    
    while current_state not in seen:
        seen[current_state] = step_count
        lst = list(current_state)
        max_val = max(lst)
        idx = lst.index(max_val)
        lst[idx] = 0
        for i in range(1, max_val+1):
            lst[(idx+i) % length] += 1
        current_state = tuple(lst)
        step_count += 1
        
    first_occurrence = seen[current_state]
    return step_count, step_count - first_occurrence

input_strings = sys.argv[1]
with open(input_strings) as f:
    banks = list(map(int, f.read().strip().split()))
    
part1, part2 = redistribute(banks)
print(part1)
print(part2)