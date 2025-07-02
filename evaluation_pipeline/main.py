
import sys
import subprocess
import time
import psutil
import csv
from pathlib import Path
import os

TIMEOUT_SECONDS = 120


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


def write_result_row(row, write_header=False):
    header = [
        "Filename",
        "Runtime in ms",
        "Peak Memory Usage in kb",
        "Output",
        "Expected Solution",
        "Correct",
        "Error Message",
    ]
    file_exists = os.path.exists("./results.csv")
    with open("./results.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if write_header and not file_exists:
            writer.writerow(header)
        if row:  # Nur schreiben, wenn row nicht leer ist
            writer.writerow(row)


def main():
    print("Starting evaluation")
    results_csv_path = "./results.csv"
    # Datei am Anfang löschen, damit sie immer frisch ist
    if os.path.exists(results_csv_path):
        os.remove(results_csv_path)
    # Schreibe Header
    write_result_row([], write_header=True)
    for file_path in find_python_files("../project_root/2015"):
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
            run_time,
            avg_mem_usage,
            output,
            expected_solution,
            "YES" if correct else "NO",
            error_message,
        ]
        write_result_row(row)


def sort_csv_by_filename(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        header = reader[0]
        rows = reader[1:]

    def sort_key(row):
        filename = row[0]
        parts = filename.split("/")
        year = int(parts[0])
        day = int(parts[1])
        rest = "/".join(parts[2:])
        return (year, day, rest)

    rows.sort(key=sort_key)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    main()
    sort_csv_by_filename("./results.csv")
    print("finished, results stored in ./results.csv")

