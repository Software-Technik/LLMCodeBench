import sys,re

words_to_digits={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
token_pattern=re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")

def part1(text):
    total=0
    for line in text.splitlines():
        first=next(c for c in line if c.isdigit())
        last=next(c for c in reversed(line) if c.isdigit())
        total+=int(first+last)
    return total

def part2(text):
    total=0
    for line in text.splitlines():
        matches=token_pattern.findall(line)
        fd=matches[0]; ld=matches[-1]
        total+=int(words_to_digits.get(fd,fd)+words_to_digits.get(ld,ld))
    return total

data=open(sys.argv[1]).read()
sys.stdout.write(f"{part1(data)} {part2(data)}")