import subprocess
import sys
import argparse

INPUT_CRAWLER_PATH = "./input_crawler.py"
CODE_SYNTAX_CHECKER_PATH = "./code_syntax_checker.py"
SOLUTION_GENERATOR_PATH = "./solution_generator.py"
SOLUTION_COMMITER_PATH = "./solution_commiter.py"
LLM_CONTROLLER_PATH = "./llm_controller.py"
LLM_ERROR_FIXER_PATH = "./llm_error_fixer.py"

LLM_NUMBER_OF_RETRIES = 3


def run_input_crawler():
    print("Running input crawler...")

    subprocess.run([sys.executable, INPUT_CRAWLER_PATH])

    print("--- finished input crawler ---")


def run_solution_generator():
    print("Generating solution files")

    subprocess.run([sys.executable, SOLUTION_GENERATOR_PATH])

    print("--- finished solution generation ---")


def run_solution_comitter():
    print("Running solution commiter...")

    subprocess.run([sys.executable, SOLUTION_COMMITER_PATH])

    print("--- finished solution comitter ---")


def llm_gen_and_validate(args):
    print("Running llm generator...")

    flags = []
    if args.ollama:
        flags.append("--ollama")
    if args.openai:
        flags.append("--openai")
    if args.deepseek:
        flags.append("--deepseek")

    subprocess.run([sys.executable, LLM_CONTROLLER_PATH] + flags)

    print("--- finished llm generator ---")
    print("Checking llm solutions for syntax error...")
    subprocess.run([sys.executable, CODE_SYNTAX_CHECKER_PATH, "--all"])

    for i in range(LLM_NUMBER_OF_RETRIES):
        print(f"--- Retry {i+1}/{LLM_NUMBER_OF_RETRIES} ---")
        subprocess.run([sys.executable, LLM_ERROR_FIXER_PATH] + flags)
        print("Rechecking...")
        subprocess.run([sys.executable, CODE_SYNTAX_CHECKER_PATH])


def main(args):
    if args.init:
        run_input_crawler()
        run_solution_generator()
        run_solution_comitter()
    
    llm_gen_and_validate(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--ollama", action="store_true")
    parser.add_argument("--openai", action="store_true")
    parser.add_argument("--deepseek", action="store_true")
    args = parser.parse_args()

    main(args)
