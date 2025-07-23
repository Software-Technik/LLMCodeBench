To solve this problem, we need to generate a disk of a specific size by expanding an initial string of bits according to a specific rule and then compute a checksum for the generated disk. The expansion rule involves repeatedly appending a `0` followed by the inverted and reversed version of the current data until the disk reaches the desired size. The checksum is computed by repeatedly reducing the data by comparing adjacent bits in non-overlapping pairs until the length of the data is odd.

### Approach
1. **Disk Generation (fill_disk):** 
   - Initialize a bytearray of the desired disk size with zeros.
   - Copy the initial data into the beginning of the bytearray.
   - Expand the data iteratively: for each iteration, append a `0` followed by the inverted and reversed version of the current data. This is done by setting `data[n] = 0` and then for each subsequent position `j` (from 1 to the minimum of the current length or remaining space), set `data[n+j] = 1 - data[n-j]`.
   - The loop continues until the disk size is reached.

2. **Checksum Calculation (create_checksum):**
   - The checksum is computed by repeatedly reducing the data. While the length of the data is even, process the data in non-overlapping pairs:
     - For each pair of bits, set the result to `1` if the bits are equal, otherwise `0`.
     - The reduced data is stored in the beginning of the same bytearray, and the length is halved after each reduction.
   - The process stops when the length of the data becomes odd, and the remaining data is converted to a string and returned as the checksum.

### Solution Code

import sys

DISK_1 = 272
DISK_2 = 35651584

def fill_disk(initial, disk_size):
    data = bytearray(disk_size)
    n0 = len(initial)
    for i in range(n0):
        data[i] = initial[i]
    n = n0
    while n < disk_size:
        data[n] = 0
        max_j = min(n, disk_size - n - 1)
        for j in range(1, max_j + 1):
            data[n + j] = 1 - data[n - j]
        n = 2 * n + 1
    return data

def create_checksum(data):
    n = len(data)
    while n % 2 == 0:
        j = 0
        for i in range(0, n, 2):
            if data[i] == data[i + 1]:
                data[j] = 1
            else:
                data[j] = 0
            j += 1
        n = j
    return ''.join(str(x) for x in data[:n])

def part1(data):
    initial = [int(x) for x in data]
    disk = fill_disk(initial, DISK_1)
    return create_checksum(disk)

def part2(data):
    initial = [int(x) for x in data]
    disk = fill_disk(initial, DISK_2)
    return create_checksum(disk)

if __name__ == '__main__':
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        data_str = f.read().strip()
    p1 = part1(data_str)
    p2 = part2(data_str)
    sys.stdout.write(f"{p1} {p2}")


### Explanation
1. **Disk Generation (fill_disk):**
   - The function starts by creating a bytearray of the specified disk size, initialized to zeros.
   - The initial data is copied into the beginning of this bytearray.
   - The data is expanded iteratively: a `0` is appended, followed by the inverted and reversed version of the current data. This is done efficiently by leveraging the symmetry in the expansion rule, where each new bit is derived from existing bits without additional storage.

2. **Checksum Calculation (create_checksum):**
   - The checksum is computed in-place by processing the data in passes. Each pass reduces the data by half by comparing non-overlapping pairs of bits. If the bits in a pair are equal, the result is `1`; otherwise, it's `0`.
   - The reduction continues until the length of the data is odd. The final result is the concatenation of the remaining bits converted to a string.

3. **Efficiency:**
   - The disk generation runs in linear time relative to the disk size, as each bit is computed in constant time during expansion.
   - The checksum calculation also runs in linear time relative to the disk size, as each reduction pass processes the current data length, and the total work across all passes is proportional to the initial disk size.
   - Memory usage is optimized by using a single bytearray for both disk generation and checksum calculation, reducing overhead from multiple allocations.