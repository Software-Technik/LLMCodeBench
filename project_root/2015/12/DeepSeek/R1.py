To solve this problem, we need to process a JSON-like string to sum all the numbers in the string while excluding any numbers within objects that contain a property with the value "red". The solution involves two main parts: summing all numbers in the string (part1) and summing numbers after removing objects that contain "red" as a value (part2).

### Approach
1. **Part1: Summing All Numbers** 
   - Use a regular expression to find all numbers (including negative numbers) in the input string.
   - Convert these numbers to integers and sum them.

2. **Part2: Handling Objects with "red" Values**
   - **Precompute String Boundaries**: Identify which characters in the string are inside quotes (to avoid mistaking "red" inside strings as actual values).
   - **Brace Matching**: Track the positions of matching braces (`{}` and `[]`) to identify the start and end of objects and arrays.
   - **Innermost Object Tracking**: For each position in the string, determine the innermost object that contains it (if any).
   - **Identify "red" Values**: Locate occurrences of the pattern `:"red"` that are not inside strings and mark the innermost containing object for removal.
   - **Remove Marked Objects**: Construct a new string by excluding the marked objects and then apply part1 to sum the remaining numbers.

### Solution Code

import sys
import re

def part1(data):
    nums = re.findall(r"-?\d+", data[0])
    return sum(int(i) for i in nums)

def part2(data):
    doc = data[0]
    n = len(doc)
    is_string = [False] * n
    in_str = False
    escape = False
    for i, c in enumerate(doc):
        if not in_str:
            if c == '"':
                in_str = True
                is_string[i] = True
            else:
                is_string[i] = False
        else:
            if escape:
                escape = False
                is_string[i] = True
            else:
                if c == '\\':
                    escape = True
                    is_string[i] = True
                elif c == '"':
                    in_str = False
                    is_string[i] = True
                else:
                    is_string[i] = True
    
    stack = []
    matches = {}
    open_objects = []
    innermost_object_start = [-1] * n
    for i, c in enumerate(doc):
        if c == '{' or c == '[':
            stack.append(i)
            if c == '{':
                open_objects.append(i)
        elif c == '}' or c == ']':
            if stack:
                start_index = stack.pop()
                if (c == '}' and doc[start_index] == '{') or (c == ']' and doc[start_index] == '['):
                    matches[start_index] = i
                    if doc[start_index] == '{' and open_objects:
                        open_objects.pop()
        if open_objects:
            innermost_object_start[i] = open_objects[-1]
        else:
            innermost_object_start[i] = -1

    occurrences = []
    for i in range(n-5):
        if doc[i:i+6] == ':"red"':
            if not is_string[i] and all(is_string[i+j] for j in range(1,6)):
                occurrences.append(i)
    
    remove_set = set()
    for i in occurrences:
        if innermost_object_start[i] != -1:
            obj_start = innermost_object_start[i]
            if obj_start in matches:
                remove_set.add((obj_start, matches[obj_start]))
    
    remove_list = sorted(remove_set, key=lambda x: x[0])
    new_doc_parts = []
    last_index = 0
    for (start, end) in remove_list:
        new_doc_parts.append(doc[last_index:start])
        last_index = end + 1
    new_doc_parts.append(doc[last_index:])
    new_doc = ''.join(new_doc_parts)
    return part1([new_doc])

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")


### Explanation
1. **Part1**:
   - The function `part1` uses a regular expression to find all numbers (including negative numbers) in the input string. These numbers are converted to integers and summed.

2. **Part2**:
   - **String Identification**: The `is_string` array marks characters inside quotes, handling escaped quotes correctly.
   - **Brace Matching**: The `matches` dictionary records the positions of matching braces. The `open_objects` stack tracks the start indices of objects (`{}`), and `innermost_object_start` records the innermost object containing each character.
   - **Finding "red" Values**: The code scans for the pattern `:"red"` that is not inside strings. Valid occurrences are those where the colon is outside any string, and the subsequent characters (including quotes) are inside a string.
   - **Object Removal**: For each valid "red" value, the innermost containing object is marked for removal. The new string is constructed by excluding these objects, and `part1` is called on the resulting string to compute the sum of the remaining numbers.

This approach efficiently processes the input by leveraging careful tracking of string boundaries and object structures to ensure correct handling of nested objects and arrays. The solution optimizes performance by minimizing repeated scans and using precomputed data structures.