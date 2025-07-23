To solve this problem, we need to optimize two functions that calculate the difference between the number of characters in the code representation of strings and their in-memory representation (part1) and the difference when re-encoding the strings with additional escaping (part2). The goal is to improve runtime performance and reduce memory usage while preserving correctness.

### Approach
1. **Part1 Optimization**:
   - **Original Approach**: The original code processed each string by removing outer quotes, replacing escape sequences (backslash and quote), and then handling hexadecimal escape sequences using regex and string replacements. This involved multiple passes over the string and building intermediate strings.
   - **Optimized Approach**: We use a single-pass state machine to traverse each string (without the outer quotes) and count the in-memory characters. For each character:
     - If it's a backslash, check the next character(s) to determine the escape sequence (backslash, quote, or hex value). Adjust the count and skip the appropriate number of characters.
     - Otherwise, count the character as-is.
   - This avoids building intermediate strings and reduces the number of passes over each string.

2. **Part2 Optimization**:
   - **Original Approach**: The original code constructed a new string by escaping each backslash and quote, then added the length of the new string plus two for the outer quotes.
   - **Optimized Approach**: Instead of building the new string, we directly compute its length by iterating over each character in the original string. For each character:
     - If it's a backslash or quote, add 2 to the new length (since these are escaped as "\\\\" or "\\\"").
     - Otherwise, add 1.
   - Add 2 for the new outer quotes. This avoids constructing the new string, saving memory and time.

### Solution Code

import sys

def part1(data):
    hex_digits = "0123456789abcdef"
    code_len = 0
    memory_size = 0
    for line in data:
        s = line
        code_len += len(s)
        s = s[1:-1]
        count = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '\\':
                if i+1 < n:
                    if s[i+1] in ['\\', '"']:
                        count += 1
                        i += 2
                    elif s[i+1] == 'x' and i+3 < n and s[i+2] in hex_digits and s[i+3] in hex_digits:
                        count += 1
                        i += 4
                    else:
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 1
            else:
                count += 1
                i += 1
        memory_size += count
    return code_len - memory_size

def part2(data):
    code_len = 0
    new_code_len = 0
    for line in data:
        code_len += len(line)
        new_len = 2
        for c in line:
            if c in ['\\', '"']:
                new_len += 2
            else:
                new_len += 1
        new_code_len += new_len
    return new_code_len - code_len

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")


### Explanation
- **Part1**:
  - For each string, we first remove the outer quotes.
  - We then traverse the string character by character. When encountering a backslash, we check the subsequent characters to identify escape sequences (backslash, quote, or hex value). Based on the sequence, we adjust the in-memory character count and skip the appropriate number of characters in the string.
  - The difference between the original code length and the in-memory count gives the result for part1.

- **Part2**:
  - For each string, we calculate the new length by considering each character in the original string. Backslashes and quotes contribute 2 characters each in the new encoding (due to escaping), while other characters contribute 1.
  - We add 2 for the new outer quotes. The difference between the new total length and the original code length gives the result for part2.

This approach efficiently processes the strings with minimal passes and without constructing intermediate strings, optimizing both runtime and memory usage.