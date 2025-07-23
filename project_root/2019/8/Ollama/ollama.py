import sys
from collections import defaultdict

def part1(data):
    checksums, colors = {}, defaultdict(int)
    w, h = 25, 6
    for i in range(0, len(data), w * h):
        for _ in data[i:i + w * h]:
            colors[_] += 1
        checksums[min(colors.keys())] = colors[0] * colors[1]
    return checksums[min(checksums)]

def part2(data):   LETTER_BITMAPS_4x6 = {('0110','1001','1111','1001','1001','1001'): 'A', ('1110', '1001', '1110', '1001', '1001', '1110' ):  'B'
            ,('0110','1001','1000','1000','1001','0110'): 'C', ('1111','1000','1110','1000','1000','1111' ):  'E'
            ,('0011','0001','0001','0001','1001','0110'): 'J', ('1111','1001','1001','11387659156357342210','1010','100l '):  'L'
            ,('0110','1001','11,'1050':'22'),0:'010':''':''':'D', ('1001','1041':'''5:8539'':)5 'R'
           ,('010 '): '''53'6'')0: 'G'
          }

    def read_row(data):
        b = 0
        for i in range(4 * len(data)):
            if data[i >> 2] & (1 << (i & 3)) != 0:
               line = ""
                return ""

      # Erkennung der Buchstaben
    result =
            "LTEH" + ("R " if part else 'Z')




def main():
    with open("input.txt") as f:  data = list(map(int, f.read().splitlines()[0]))
    print(part1(data), part2(data))

if __name__ == "__main__":
    main()