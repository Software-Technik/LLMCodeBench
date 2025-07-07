import sys,re

words_to_digits = {
    "one":"1","two":"2","three":"3","four":"4","five":"5",
    "six":"6","seven":"7","eight":"8","nine":"9"
}

PAT = re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")

def part1(text):
    total=0
    for line in text.splitlines():
        for c in line:
            if c.isdigit():
                f=int(c);break
        for c in reversed(line):
            if c.isdigit():
                l=int(c);break
        total+=f*10+l
    return total

def part2(text):
    total=0
    for line in text.splitlines():
        m=PAT.findall(line)
        a=m[0];b=m[-1]
        fa=a if a.isdigit() else words_to_digits[a]
        la=b if b.isdigit() else words_to_digits[b]
        total+=int(fa)*10+int(la)
    return total

data=sys.stdin.read() if len(sys.argv)==1 else open(sys.argv[1]).read()
sys.stdout.write(f"{part1(data)} {part2(data)}")