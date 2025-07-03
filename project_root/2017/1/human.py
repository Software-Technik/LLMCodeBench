import sys

def solve(digits, jump):
    size = len(digits)
    result = 0
    for i, n in enumerate(digits):
        if n == digits[(i + jump) % size]:
            result += n
    return result

# Lecture du fichier et conversion des données
input_strings = sys.argv[1]
with open(input_strings) as f:
    digits = [int(digit) for digit in f.read().strip()]

# Calcul des résultats
print(solve(digits, 1))
print(solve(digits, len(digits) // 2))