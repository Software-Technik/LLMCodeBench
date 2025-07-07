import re
import sys

def part1(text: str) -> int:
    workflows_txt, parts_txt = text.split("\n\n", maxsplit=1)
    workflows = {}
    
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{", maxsplit=1)
        workflows[name] = conditions[:-1].split(",")  # }
    
    parts = [dict((m[0], int(m[1])) for m in re.findall(r"([a-z]+)=([0-9]+)", part)) 
             for part in parts_txt.splitlines()]

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

def traverse(workflow, workflows, ranges, results):
    if workflow == "A":
        results.append(ranges.copy())
        return
    if workflow == "R":
        return

    for rule in workflows[workflow]:
        if "<" in rule or ">" in rule:
            category, value = (rule.split("<") if "<" in rule else rule.split(">"))
            value, workflow = value.split(":")
            value = int(value)

            new_ranges_c = []
            new_current_ranges_c = []
            if "<" in rule:
                for a, b in ranges[category]:
                    if b < value:
                        new_ranges_c.append((a, b))
                    elif a < value:
                        new_ranges_c.append((a, value - 1))
                        new_current_ranges_c.append((value, b))
                    else:
                        new_current_ranges_c.append((a, b))
            else:
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
            traverse(workflow, workflows, new_ranges, results)
            ranges[category] = new_current_ranges_c
        else:
            workflow = rule
            traverse(workflow, workflows, ranges, results)

def part2(text: str) -> int:
    workflows_txt, _ = text.split("\n\n", maxsplit=1)
    workflows = {}
    
    for workflow in workflows_txt.splitlines():
        name, conditions = workflow.split("{", maxsplit=1)
        workflows[name] = conditions[:-1].split(",")  # }
    
    results = []
    ranges = {k: [(1, 4000)] for k in "xmas"}
    traverse("in", workflows, ranges, results)

    total = 0
    for result in results:
        subtotal = 1
        for subranges in result.values():
            subtotal *= sum(b - a + 1 for a, b in subranges)
        total += subtotal
    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")