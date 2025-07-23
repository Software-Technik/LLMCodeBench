import re
import sys

def part1(text: str) -> int:
    workflows_txt, parts_txt = text.split("\n\n", maxsplit=1)
    workflows = {}
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{", maxsplit=1)
        rules = conditions[:-1].split(",")
        compiled_rules = []
        for rule in rules:
            if '<' in rule:
                cat, rest = rule.split('<', 1)
                val, target = rest.split(':', 1)
                compiled_rules.append(('<', cat, int(val), target))
            elif '>' in rule:
                cat, rest = rule.split('>', 1)
                val, target = rest.split(':', 1)
                compiled_rules.append(('>', cat, int(val), target))
            else:
                compiled_rules.append(('always', None, None, rule))
        workflows[name] = compiled_rules

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
                op, cat, val, target = rule
                if op == '<':
                    if part[cat] < val:
                        current_workflow = target
                        break
                elif op == '>':
                    if part[cat] > val:
                        current_workflow = target
                        break
                else:
                    current_workflow = target
                    break
        if current_workflow == "A":
            total += sum(part.values())
    return total

def traverse(workflow, workflows, ranges, results):
    if workflow == "A":
        results.append(ranges)
        return
    if workflow == "R":
        return

    for rule in workflows[workflow]:
        op, cat, val, target = rule
        if op == '<':
            new_ranges_c = []
            new_current_ranges_c = []
            for a, b in ranges[cat]:
                if b < val:
                    new_ranges_c.append((a, b))
                elif a < val:
                    new_ranges_c.append((a, val - 1))
                    new_current_ranges_c.append((val, b))
                else:
                    new_current_ranges_c.append((a, b))
            if new_ranges_c:
                new_ranges = ranges.copy()
                new_ranges[cat] = new_ranges_c
                traverse(target, workflows, new_ranges, results)
            ranges[cat] = new_current_ranges_c
            if not new_current_ranges_c:
                break
        elif op == '>':
            new_ranges_c = []
            new_current_ranges_c = []
            for a, b in ranges[cat]:
                if a > val:
                    new_ranges_c.append((a, b))
                elif b > val:
                    new_ranges_c.append((val + 1, b))
                    new_current_ranges_c.append((a, val))
                else:
                    new_current_ranges_c.append((a, b))
            if new_ranges_c:
                new_ranges = ranges.copy()
                new_ranges[cat] = new_ranges_c
                traverse(target, workflows, new_ranges, results)
            ranges[cat] = new_current_ranges_c
            if not new_current_ranges_c:
                break
        else:
            traverse(target, workflows, ranges, results)
            break

def part2(text: str) -> int:
    workflows_txt, _ = text.split("\n\n", maxsplit=1)
    workflows = {}
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{", maxsplit=1)
        rules = conditions[:-1].split(",")
        compiled_rules = []
        for rule in rules:
            if '<' in rule:
                cat, rest = rule.split('<', 1)
                val, target = rest.split(':', 1)
                compiled_rules.append(('<', cat, int(val), target))
            elif '>' in rule:
                cat, rest = rule.split('>', 1)
                val, target = rest.split(':', 1)
                compiled_rules.append(('>', cat, int(val), target))
            else:
                compiled_rules.append(('always', None, None, rule))
        workflows[name] = compiled_rules

    results = []
    ranges = {
        "x": [(1, 4000)],
        "m": [(1, 4000)],
        "a": [(1, 4000)],
        "s": [(1, 4000)],
    }
    traverse("in", workflows, ranges, results)

    total = 0
    for result in results:
        subtotal = 1
        for subranges in result.values():
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