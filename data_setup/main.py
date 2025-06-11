import subprocess
import sys

INPUT_CRAWLER_PATH = "./input_crawler.py"
SOLUTION_GENERATOR_PATH = "./solution_generator.py"
SOLUTION_COMMITER_PATH = "./solution_commiter.py"


def run_input_crawler():
    print("Running input crawler...")

    subprocess.run([sys.executable, INPUT_CRAWLER_PATH])

    print("--- finished input crawler ---")


def run_solution_generator():
    print("Running solution generator...")

    subprocess.run([sys.executable, SOLUTION_GENERATOR_PATH])

    print("--- finished solution generator ---")


def run_solution_comitter():
    print("Running solution commiter...")

    subprocess.run([sys.executable, SOLUTION_COMMITER_PATH])

    print("--- finished solution comitter ---")


def main():
    # run_input_crawler()
    # run_solution_generator()
    run_solution_comitter()


if __name__ == "__main__":
    main()
