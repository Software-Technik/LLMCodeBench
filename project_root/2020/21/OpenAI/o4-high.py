import sys
from collections import Counter

ingredient_counts = Counter()
allergen_candidates = {}
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        left, right = line.split(' (contains ')
        ingredients = left.split()
        allergens = right[:-1].split(', ')
        for ing in ingredients:
            ingredient_counts[ing] += 1
        ingset = set(ingredients)
        for allergen in allergens:
            if allergen in allergen_candidates:
                allergen_candidates[allergen] &= ingset
            else:
                allergen_candidates[allergen] = set(ingset)

solved = {}
while len(solved) < len(allergen_candidates):
    for allergen, candidates in allergen_candidates.items():
        if len(candidates) == 1 and allergen not in solved:
            ing = next(iter(candidates))
            solved[allergen] = ing
            for other in allergen_candidates:
                if other != allergen:
                    allergen_candidates[other].discard(ing)
            break

dangerous = set(solved.values())
safe_count = sum(c for ing, c in ingredient_counts.items() if ing not in dangerous)
canonical = ','.join(solved[allergen] for allergen in sorted(solved))
print(safe_count, canonical)