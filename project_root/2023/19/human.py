import re
import sys
from copy import deepcopy

def part1(text: str) -> int:
    workflows_txt, parts_txt = text.split("\n\n", maxsplit=1)
    workflows = {}
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{", maxsplit=1)  # }
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

def traverse(
    workflow,
    workflows,
    ranges: dict[str, list[tuple[int, int]]],
    results: list[dict[str, list[tuple[int, int]]]],
):
    if workflow == "A":
        results.append(ranges)
        return
    if workflow == "R":
        return

    for rule in workflows[workflow]:
        if "<" in rule:
            category, value = rule.split("<")
            value, workflow = value.split(":")
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

            new_ranges = deepcopy(ranges)
            new_ranges[category] = new_ranges_c
            traverse(workflow, workflows, new_ranges, results)
            ranges[category] = new_current_ranges_c
        elif ">" in rule:
            category, value = rule.split(">")
            value, workflow = value.split(":")
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

            new_ranges = deepcopy(ranges)
            new_ranges[category] = new_ranges_c
            traverse(workflow, workflows, new_ranges, results)
            ranges[category] = new_current_ranges_c
        else:
            workflow = rule
            traverse(workflow, workflows, ranges, results)


def part2(text: str) -> int:
    workflows_txt, _ = text.split("\n\n", maxsplit=1)
    workflows = {}
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{", maxsplit=1)  # }
        workflows[name] = conditions[:-1].split(",")

    results: list[dict[str, list[tuple[int, int]]]] = []
    ranges: dict[str, list[tuple[int, int]]] = {
        "x": [(1, 4000)],
        "m": [(1, 4000)],
        "a": [(1, 4000)],
        "s": [(1, 4000)],
    }
    traverse("in", workflows, ranges, results)

    total = 0
    for result in results:
        subtotal = 1
        for _, subranges in result.items():
            n = 0
            for a, b in subranges:
                n += b - a + 1
            subtotal *= n
        total += subtotal
    return total


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")