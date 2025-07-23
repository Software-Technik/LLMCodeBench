To solve this problem, we need to determine the number of ways a given design string can be constructed using a predefined list of units. The solution involves dynamic programming to efficiently check and count the valid constructions.

### Approach
1. **Problem Analysis**:
   - **Part 1**: Check if a design string can be segmented into a sequence of units from the given list. The solution uses dynamic programming to verify if at least one valid segmentation exists.
   - **Part 2**: Count the number of distinct ways to segment the design string into units from the list. This also employs dynamic programming but focuses on counting all valid segmentations.

2. **Dynamic Programming Setup**:
   - **Part 1**: A boolean array `dp` is used where `dp[i]` is `True` if the prefix of the design string up to the `i-th` character can be segmented into units. The array is initialized with `dp[0] = True` (indicating the empty string can always be segmented).
   - **Part 2**: An integer array `dp` is used where `dp[i]` stores the number of ways to segment the prefix up to the `i-th` character. Here, `dp[0] = 1` (one way to segment the empty string).

3. **Processing Each Design**:
   - For each character in the design string, iterate through all units. For each unit, check if the substring ending at the current character matches the unit and if the prefix before this substring can be segmented (using the `dp` array). 
   - **Part 1**: If a valid segmentation is found for the current position, set `dp[i+1]` to `True` and break early (since only one valid segmentation is needed).
   - **Part 2**: For each valid segmentation found, accumulate the count of segmentations by adding the value from `dp` at the start of the current unit.

4. **Result Calculation**:
   - **Part 1**: The result is the count of design strings where `dp[n]` is `True` (entire string can be segmented).
   - **Part 2**: The result is the sum of `dp[n]` values for all design strings (total ways to segment all strings).

### Solution Code

import sys

def part1(lines):
    units = lines[0].split(", ")
    designs = lines[2:]
    units_with_len = [(u, len(u)) for u in units]
    
    count = 0
    for d in designs:
        n = len(d)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for u, L in units_with_len:
                if i+1 < L:
                    continue
                start = i - L + 1
                if d[start:i+1] == u and dp[start]:
                    dp[i+1] = True
                    break
        if dp[n]:
            count += 1
    return count

def part2(lines):
    units = lines[0].split(", ")
    designs = lines[2:]
    units_with_len = [(u, len(u)) for u in units]
    
    total = 0
    for d in designs:
        n = len(d)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            for u, L in units_with_len:
                if i+1 < L:
                    continue
                start = i - L + 1
                if d[start:i+1] == u:
                    dp[i+1] += dp[start]
        total += dp[n]
    return total

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")

print(part1(lines), part2(lines))


### Explanation
- **Part 1**:
  - For each design string, a dynamic programming array `dp` tracks if prefixes of the string can be segmented into units. The array is built by checking each unit against substrings ending at the current character. If a unit matches and the preceding prefix is valid, `dp` is updated. The result is the count of design strings where the entire string is valid.

- **Part 2**:
  - Similar to Part 1, but the dynamic programming array `dp` now counts the number of valid segmentations for each prefix. For each matching unit, the count of valid segmentations is incremented by the count from the start of the unit. The result sums the valid segmentations for all design strings.

This approach efficiently checks and counts segmentations using dynamic programming, ensuring optimal performance and correctness.