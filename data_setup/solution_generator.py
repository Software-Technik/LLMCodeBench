import subprocess
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

def find_human_py_files(root_dir):
    root = Path(root_dir)
    return list(root.rglob("human.py"))

def write_solution_file(solution_path, output):
    with open(solution_path, "w", encoding="utf-8") as f:
        f.write(output.strip() + "\n")

def get_year_day_from_path(human_py):
    return f"{human_py.parts[-3]}/{human_py.parts[-2]}"

def process_human_py(human_py):
    input_path = human_py.parent / "input"
    solution_path = human_py.parent / "solution"
    year_day = get_year_day_from_path(human_py)

    if not input_path.exists():
        return (year_day, f"{year_day}: Input file missing")

    try:
        result = subprocess.run(
            [sys.executable, str(human_py), str(input_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
    except Exception as e:
        return (year_day, f"{year_day}: Exception: {e}")

    if result.returncode != 0:
        last_error = result.stderr.strip().splitlines()[-1] if result.stderr else "Unknown error"
        return (year_day, f"{year_day}: {last_error}")

    output = result.stdout.strip()
    write_solution_file(solution_path, output)
    print(f"Solution written for {year_day}")
    return (year_day, None)  # None bedeutet: kein Fehler

def generate_solutions_parallel(root_dir, max_workers=4):
    human_files = find_human_py_files(root_dir)
    errors = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_human_py, human_py) for human_py in human_files]
        for future in as_completed(futures):
            year_day, error_msg = future.result()
            if error_msg:
                print(error_msg)
                errors.append((year_day, error_msg))

    errors.sort()
    with open("./logs/solution_errors.txt", "w", encoding="utf-8") as f:
        for _, msg in errors:
            f.write(msg + "\n")

if __name__ == "__main__":
    generate_solutions_parallel("../project_root", max_workers=4)
