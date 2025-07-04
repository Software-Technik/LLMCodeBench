import sys
import subprocess
import time
import psutil
import sqlite3
from pathlib import Path
import os

TIMEOUT_SECONDS = 120
DB_PATH = "results.db"


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def evaluate_code(path, input_file_path):
    start_time = time.time()
    proc = subprocess.Popen(
        [sys.executable, str(path), str(input_file_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    p = psutil.Process(proc.pid)
    used_max_mem = 0

    try:
        while proc.poll() is None:
            try:
                mem = p.memory_info().rss
                if mem > used_max_mem:
                    used_max_mem = mem
            except psutil.NoSuchProcess:
                break
            if time.time() - start_time > TIMEOUT_SECONDS:
                proc.kill()
                raise TimeoutError("Timeout: Process took more than 2 minutes.")
            time.sleep(0.01)

        end_time = time.time()

        stdout, stderr = proc.communicate(timeout=1)
        run_time_ms = (end_time - start_time) * 1000
        used_max_mem_kb = used_max_mem / 1024

        output = stdout.decode("utf-8").strip()
        error_output = stderr.decode("utf-8").strip()

        return run_time_ms, used_max_mem_kb, output, error_output

    except TimeoutError as te:
        proc.kill()
        return TIMEOUT_SECONDS * 1000, used_max_mem / 1024, "", str(te)
    except Exception as e:
        proc.kill()
        return TIMEOUT_SECONDS * 1000, used_max_mem / 1024, "", f"Exception: {e}"


def evaluate_code_multiple_times(path, input_data, runs=3):
    run_times = []
    mem_usages = []
    output = None
    error_happened = False
    error_message = ""
    print(f"Testing file {path}")
    for i in range(runs):
        print("run #" + str(i))
        run_time_ms, used_max_mem_kb, out, error_output = evaluate_code(
            path, input_data
        )
        run_times.append(run_time_ms)
        mem_usages.append(used_max_mem_kb)
        if error_output:
            print(f"Error in {path}:\n{error_output}\n")
            error_happened = True
            error_message = error_output
            break

        if i == 0:
            output = out
    avg_run_time = sum(run_times) / len(run_times)
    avg_mem_usage = sum(mem_usages) / len(mem_usages)
    if error_happened:
        return f"{avg_run_time:.1f}", f"{avg_mem_usage:.1f}", "ERROR", error_message
    else:
        return f"{avg_run_time:.1f}", f"{avg_mem_usage:.0f}", output, ""


def find_python_files(root_dir):
    root = Path(root_dir)
    return list(root.rglob("*.py"))


def get_input_and_solution_paths(py_file):
    parent = Path(py_file).parent
    input_path = parent / "input"
    solution_path = parent / "solution"

    if not input_path.exists() or not solution_path.exists():
        parent = parent.parent
        input_path = parent / "input"
        solution_path = parent / "solution"
    return input_path, solution_path


def init_db(db_path=DB_PATH):
    if os.path.exists(db_path):
        os.remove(db_path)  # Clean start
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE results (
            filename TEXT PRIMARY KEY,
            runtime_ms REAL,
            peak_mem_kb REAL,
            output TEXT,
            expected_solution TEXT,
            correct TEXT,
            error_message TEXT
        )
    """)
    conn.commit()
    return conn


def insert_result(conn, row):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO results (
            filename, runtime_ms, peak_mem_kb, output,
            expected_solution, correct, error_message
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, row)
    conn.commit()


def main():
    print("Starting evaluation")
    conn = init_db()
    for file_path in find_python_files("../project_root"):
        input_path, solution_path = get_input_and_solution_paths(file_path)
        if not input_path.exists() or not solution_path.exists():
            print(f"Input or solution missing for {file_path}, skipping...")
            continue

        expected_solution = read_file(solution_path)

        run_time, avg_mem_usage, output, error_message = evaluate_code_multiple_times(
            file_path, input_path, runs=3
        )

        correct = output == expected_solution and not error_message

        row = [
            str(file_path).split("../project_root/")[1],
            float(run_time),
            float(avg_mem_usage),
            output,
            expected_solution,
            "YES" if correct else "NO",
            error_message,
        ]
        insert_result(conn, row)

    conn.close()
    print(f"finished, results stored in {DB_PATH}")


if __name__ == "__main__":
    main()
