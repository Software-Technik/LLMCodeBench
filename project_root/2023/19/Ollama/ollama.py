import re
import sys

def part1(text: str) -> int:
    workflows_txt, parts_txt = text.split("\n\n", maxsplit=1)
    workflows = {}
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{")
        workflows[name] = conditions[:-1].split(",")

    parts = []
    pattern = re.compile(r"([a-z]+)=([0-9]+)")
    for part in parts_txt.splitlines():
        part_dict = {}
        for category, value in pattern.findall(part):
            part_dict[category] = int(value)
        parts.append(part_dict)

    total = 0
    for part in parts:
        current_workflow = "in"
        while current_workflow not in ["A", "R"]:
            for rule in workflows[current_workflow]:
                if "<" in rule:
                    category, value = rule.split("<")
                    value, workflow = value.split(":")
                    if part[category] < int(value):
                        current_workflow = workflow
                        break
                elif ">" in rule:
                    category, value = rule.split(">")
                    value, workflow = value.split(":")
                    if part[category] > int(value):
                        current_workflow = workflow
                        break
                else:
                    current_workflow = rule
                    break
        if current_workflow == "A":
            total += sum(part.values())
    return total

def traverse(workflow, workflows, ranges: dict[str, list[tuple[int, int]]], results):
    if workflow == "A":
        results.append(ranges)
        return
    elif workflow == "R":
        return

    rules = workflows[workflow]
    for rule in rules:
        if "<" in rule:
            category, value = rule.split("<")
            value, next_workflow = value.split(":")
            value = int(value)

            new_ranges_c = []
            new_current_ranges_c = []
            for a, b in ranges[category]:
                if b < value:
                    new_ranges_c.append((a, b))
                elif a < value:
                    new_ranges_c.append((a, value - 1))
                    new_current_ranges_c.append((value, b))
                else:
                    new_current_ranges_c.append((a, b))

            new_ranges = ranges.copy()
            new_ranges[category] = new_ranges_c
            traverse(next_workflow, workflows, new_ranges, results)
            ranges[category] = new_current_ranges_c
        elif ">" in rule:
            category, value = rule.split(">")
            value, next_workflow = value.split(":")
            value = int(value)

            new_ranges_c = []
            new_current_ranges_c = []
            for a, b in ranges[category]:
                if a > value:
                    new_ranges_c.append((a, b))
                elif b > value:
                    new_ranges_c.append((value + 1, b))
                    new_current_ranges_c.append((a, value))
                else:
                    new_current_ranges_c.append((a, b))

            new_ranges = ranges.copy()
            new_ranges[category] = new_ranges_c
            traverse(next_workflow, workflows, new_ranges, results)
            ranges[category] = new_current_ranges_c
        else:
            traverse(rule, workflows, ranges, results)

def part2(text: str) -> int:
    workflows_txt, _ = text.split("\n\n", maxsplit=1)
    workflows = {}
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{")
        workflows[name] = conditions[:-1].split(",")

    results = []
    ranges = {
        "x": [(1, 4000)],
        "m": [(1, 4000)],
        "a": [(1, 4000)],
        "s": [(1, 4000)]
    }
    traverse("in", workflows, ranges, results)

    total = 0
    for result in results:
        subtotal = 1
        for _, subranges in result.items():
            n = sum(b - a + 1 for a, b in subranges)
            subtotal *= n
        total += subtotal
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")