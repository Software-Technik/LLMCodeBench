To solve this problem, we need to find valid keys based on specific cryptographic hashing rules. The solution involves generating MD5 hashes for input strings combined with an index, then checking these hashes for sequences of three identical characters (triplets) and five identical characters (quintuplets). A key is considered valid if a triplet at some index is followed by a quintuplet of the same character within the next 1000 indices.

### Approach
1. **Hash Generation**: For each index, generate an MD5 hash of the input string concatenated with the index. For part 2, stretch the hash by rehashing it 2016 additional times.
2. **Triplet and Quintuplet Detection**: For each generated hash, scan for the first occurrence of any triplet (three identical consecutive characters). Additionally, check the entire hash for any quintuplets (five identical consecutive characters).
3. **Key Validation**: When a triplet is found, store its index and character. If a quintuplet of the same character is found in a subsequent hash (within 1000 indices of the triplet's index), mark the triplet's index as a valid key.
4. **Efficiency Optimization**: 
   - **Triplet Storage**: Use a dictionary to store triplets by their character, allowing quick lookups when a quintuplet is found.
   - **Cleanup**: Regularly remove outdated triplets (those older than the current index minus 1000) to keep storage efficient.
   - **Early Termination**: Continue processing until 64 valid keys are found and no more valid keys can be found within the next 1000 indices of the last valid key.

### Solution Code

from hashlib import md5
import sys
from collections import defaultdict, deque

def solve(data, stretch):
    triplets_by_char = defaultdict(deque)
    valid_keys = set()
    index = 0

    while len(valid_keys) < 64 or index < (max(valid_keys) + 1000 if valid_keys else 0):
        for c in list(triplets_by_char.keys()):
            q = triplets_by_char[c]
            while q and q[0] < index - 1000:
                q.popleft()
            if not q:
                del triplets_by_char[c]

        h = data + str(index)
        hex_ = md5(h.encode()).hexdigest()
        for _ in range(stretch):
            hex_ = md5(hex_.encode()).hexdigest()

        quintuplet_chars = set()
        for j in range(len(hex_)-4):
            if hex_[j] == hex_[j+1] == hex_[j+2] == hex_[j+3] == hex_[j+4]:
                quintuplet_chars.add(hex_[j])

        found_triplet = False
        for j in range(len(hex_)-2):
            if hex_[j] == hex_[j+1] == hex_[j+2]:
                c = hex_[j]
                if not found_triplet:
                    triplets_by_char[c].append(index)
                    found_triplet = True
                if c in quintuplet_chars and c in triplets_by_char:
                    valid_keys.update(triplets_by_char[c])
                    del triplets_by_char[c]
        index += 1

    return sorted(valid_keys)[63]

def part1(data):
    return solve(data, 0)

def part2(data):
    return solve(data, 2016)

if __name__ == '__main__':
    inout_strings = sys.argv[1]
    with open(inout_strings, 'r') as file:
        data = file.read().strip()
    p1 = part1(data)
    p2 = part2(data)
    sys.stdout.write(f"{p1} {p2}")


### Explanation
1. **Hash Generation**: The solution processes each index by appending it to the input string and generating an MD5 hash. For part 2, each hash is stretched by rehashing 2016 times.
2. **Triplet and Quintuplet Detection**: The algorithm scans each hash for triplets (three consecutive identical characters) and quintuplets (five consecutive identical characters). The first triplet encountered per hash is stored along with its index.
3. **Key Validation**: When a quintuplet is detected, all previously stored triplets of the same character (within the last 1000 indices) are marked as valid keys. This ensures that each triplet is validated as soon as a matching quintuplet is found.
4. **Efficiency**: The solution efficiently manages storage by removing outdated triplets (those older than 1000 indices) and uses dictionaries and deques for quick lookups and updates, optimizing both time and space complexity. The loop terminates once 64 valid keys are found and no further keys can be validated within the next 1000 indices of the last valid key.