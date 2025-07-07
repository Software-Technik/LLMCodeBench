import sys
def next_password(pw):
    pw = [ord(c) for c in pw]
    for i in range(len(pw)-1, -1, -1):
        c = pw[i] + 1
        if c > 122:
            pw[i] = 97; continue
        if c in (105,111,108):
            c += 1
            if c > 122:
                pw[i] = 97; continue
        pw[i] = c; break
    return ''.join(map(chr,pw))
def valid_password(pw):
    n = len(pw); ok = False
    for i in range(n-2):
        a = ord(pw[i])
        if a+1 == ord(pw[i+1]) and a+2 == ord(pw[i+2]):
            ok = True; break
    if not ok or 'i' in pw or 'o' in pw or 'l' in pw: return False
    cnt = 0; i = 0
    while i < n-1:
        if pw[i] == pw[i+1]:
            cnt += 1; i += 2
            if cnt > 1: break
        else:
            i += 1
    return cnt > 1
def part1(s):
    s = next_password(s)
    while not valid_password(s):
        s = next_password(s)
    return s
if __name__ == "__main__":
    s = open(sys.argv[1]).readline().strip()
    p1 = part1(s)
    sys.stdout.write(p1+"\n"+part1(p1)+"\n")