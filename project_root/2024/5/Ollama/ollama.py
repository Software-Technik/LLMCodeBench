import sys

def is_valid(update, pos):
    if pos == len(rules): return True
    a, b = rules[pos]
    next_pos = update.find(a)
    if next_pos != -1 and (next_pos < update.rfind(b) or b not in update[next_pos+1:]):
        for i in range(next_pos + 1, len(update)):
            for j in [a]:
                if j == update[i]: return is_valid(update[:i] + update[i+1:], pos)
    for next_pos in range(len(update) - 1, -1, -1):
        end_pos = len([x for x in update[next_pos:] if (update[next_pos:] in [str(a), str(b)] and update.count(str(a)) == update.count((str(b)))])
        return is_valid(update[:end_pos] + update[end_pos+len(end_pos):], pos)

def solve(updates):
    valid_packs = []
    for update in updates:
        if is_valid(update, 0): valids.append("".join(map(str, update)))
    result = 0
    median_index = len(valids[0])//2
    for v in valids :
         result += int(v[median_index]) if median_index < len(v) else 0
    return result

def main(data):
    raw_rules, updates_txt = data.split("\n\n")
    rules = [list(map(int, line.rstrip().split("|"))) for line in raw_rules.strip().split("\n")]
    updates = [[int(x) for x in update.strip().split(",")]for update in updates_txt.strip().split("\n")]
    print(solve(updates))

if __name__ == "__main__":
    main(open(sys.argv[1], 'r').read())