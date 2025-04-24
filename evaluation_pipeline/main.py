import sys
import subprocess
import time
import psutil


def main():
    start_time = time.time()
    proc = subprocess.Popen(
        [sys.executable, r"../project_root/2015/1/human.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    p = psutil.Process(proc.pid)
    used_max_mem = 0

    while proc.poll() is None:
        try:
            mem = p.memory_info().rss
            if mem > used_max_mem:
                used_max_mem = mem
        except psutil.NoSuchProcess:
            break
        time.sleep(0.01)

    end_time = time.time()
    run_time = end_time - start_time

    print(f"tested code ran for {run_time:.3f} seconds")
    print(f"Max memory usage: {used_max_mem / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    main()
