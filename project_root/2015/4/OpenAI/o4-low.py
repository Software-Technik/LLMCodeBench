import sys, hashlib

def find_num(key_bytes, zero_bytes, check_nibble):
    i = 1
    while True:
        m = hashlib.md5()
        m.update(key_bytes)
        m.update(str(i).encode())
        d = m.digest()
        if d[:zero_bytes] == b'\0' * zero_bytes and (not check_nibble or d[zero_bytes] < 16):
            return i
        i += 1

def main():
    key = open(sys.argv[1]).read().strip()
    key_bytes = key.encode()
    part1 = find_num(key_bytes, 2, True)
    part2 = find_num(key_bytes, 3, False)
    print(part1)
    print(part2)

if __name__ == "__main__":
    main()