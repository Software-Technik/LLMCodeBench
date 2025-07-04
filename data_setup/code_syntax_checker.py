import subprocess
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

ERROR_LOG = "./logs/execution_errors.txt"
PROJECT_ROOT = "../project_root"


def find_non_human_py_files(root_dir):
    root = Path(root_dir)
    return [p for p in root.rglob("*.py") if p.name != "human.py"]


def parse_error_log():
    if not Path(ERROR_LOG).exists():
        return []
    files = set()
    with open(ERROR_LOG, "r") as f:
        for line in f:
            if ":" in line:
                file_path = line.split(":", 1)[0].strip()
                files.add(file_path)
    return list(files)


def check_py_file(py_file):
    input_path = py_file.parent.parent / "input"
    rel_path = py_file.relative_to(PROJECT_ROOT)
    if not input_path.exists():
        return (str(rel_path), f"{rel_path}: input file missing")

    try:
        result = subprocess.run(
            [sys.executable, str(py_file), str(input_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception as e:
        return (str(rel_path), f"{rel_path}: Exception: {e}")

    if result.returncode != 0:
        last_error = (
            result.stderr.strip().splitlines()[-1] if result.stderr else "Unknown error"
        )
        return (str(rel_path), f"{rel_path}: {last_error}")

    print(f"No error in {rel_path}")
    return (str(rel_path), None)


def check_files(py_files, max_workers=4):
    errors = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(check_py_file, py_file) for py_file in py_files]
        for future in as_completed(futures):
            rel_path, error_msg = future.result()
            if error_msg:
                print(error_msg)
                errors.append((rel_path, error_msg))

    errors.sort()
    os.makedirs(os.path.dirname(ERROR_LOG), exist_ok=True)
    with open(ERROR_LOG, "w", encoding="utf-8") as f:
        for _, msg in errors:
            f.write(msg + "\n")


if __name__ == "__main__":
    check_all = "--all" in sys.argv
    if check_all:
        py_files = find_non_human_py_files(PROJECT_ROOT)
    else:
        error_files = parse_error_log()
        if not error_files:
            print("No erors found in llm code")
            sys.exit(0)
        py_files = [Path(PROJECT_ROOT) / f for f in error_files]
    check_files(py_files, max_workers=4)
