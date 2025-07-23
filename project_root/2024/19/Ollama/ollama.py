import sys

def part1(input):
    units, _, *designs = input.split('\n')
    units = set(units.split(', '))

    def is_possible(design):
        for i in range(len(design)):
            if design[:i + 1] in units:
                return True
            sub_problem_solved = False
            for unit in units:
                if len(unit) <= i and design[i - len(unit) + 1:i + 1] == unit:
                    sub_problem_solved |= is_possible(design[:i - len(unit) + 1])
        return sub_problem_solved

    return sum(is_possible(design) for design in designs)

def part2(input):
    units, _, *designs = input.split('\n')
    units = set(units.split(', '))

    @lru_cache(None)
    def is_possible_ways(design):
        if not design: return 1
        ways = sum(design.startswith(unit) and is_possible_ways(design[len(unit):]) for unit in units)
        return ways

    return sum(is_possible_ways(design) for design in designs)

input_path = sys.argv[1]
with open(input_path) as fin:
     input_str = fin.read().strip()