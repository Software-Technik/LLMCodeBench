import sys
import subprocess
import time
import csv
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
import os
from tqdm import tqdm
from natsort import natsorted
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

load_dotenv()
openai_client = OpenAI()
deepseek_client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com"
)
ollama_client = OpenAI(base_url="http://localhost:11434/v1")
ollama_model = (
    os.environ["OLLAMA_MODEL"] if "OLLAMA_MODEL" in os.environ else "devtral:24b"
)

PROMPT = """
You are an expert Python developer specializing in algorithmic optimization. Your task is to refine existing Python code that solves a problem from Advent of Code. The goal of your refinement is to:
- Improve runtime performance
- Reduce memory usage
- Preserve the correctness of the original solution
Constraints:
The refined code must produce exactly the same output as the original when given the same input.
The code must be valid Python, runnable without errors.
Do not remove or simplify test cases or input parsing unless they are clearly redundant or inefficient.
Avoid use of external libraries unless already used in the original code.
Please provide only the optimized version of the code, without any additional comments or explanations. The code should be ready to run as a standalone script.
NEVER EVER respond with anything but the code, no explanation, no leading info, JUST THE CODE.
"""

def enhance_code_openai(code, model, reasoning=False, reasoning_effort="medium"):
    if reasoning:
        openai_response = openai_client.responses.create(
            model=model,
            instructions=PROMPT,
            reasoning={"effort": reasoning_effort},
            input=code,
        )
        return openai_response.output_text
    else:
        openai_response = openai_client.responses.create(
            model=model,
            instructions=PROMPT,
            input=code,
        )
        return openai_response.output_text

def enhance_code_deepseek(code, model):
    deepseek_response = deepseek_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": code},
        ],
        stream=False,
    )
    return deepseek_response.choices[0].message.content

def enhance_code_ollama(code, model):
    ollama_response = ollama_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": code},
        ],
        stream=False,
    )
    return ollama_response.choices[0].message.content

def find_human_python_files(root_dir):
    root = Path(root_dir)
    return list(root.rglob("human.py"))

def save_code(code, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

def sanatize_code(code):
    # remove ```python and ``` from the code
    code = code.replace("```python", "").replace("```", "")
    return code.strip()

def enhance_and_save_code_openai(code, file_path, model, reasoning=False, reasoning_effort="medium"):
    enhanced_code = enhance_code_openai(code, model, reasoning, reasoning_effort)
    enhanced_code = sanatize_code(enhanced_code)
    save_code(enhanced_code, file_path)

def enhance_and_save_code_deepseek(code, file_path, model):
    enhanced_code = enhance_code_deepseek(code, model)
    enhanced_code = sanatize_code(enhanced_code)
    save_code(enhanced_code, file_path)

def enhance_and_save_code_ollama(code, file_path, model):
    enhanced_code = enhance_code_ollama(code, model)
    enhanced_code = sanatize_code(enhanced_code)
    save_code(enhanced_code, file_path)

def load_checkpoint():
    try:
        with open("checkpoint.txt", "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0

def save_checkpoint(index):
    with open("checkpoint.txt", "w") as f:
        f.write(str(index))

def enhance_full_file(file_path, args):
    with open(file_path, "r", encoding="utf-8") as f:
        human_code = f.read()

    if args.openai:
        tqdm.write("Enhancing " + str(file_path) + " using OpenAI model: gpt-4o")
        enhance_and_save_code_openai(
            human_code, str(file_path.parent) + "/OpenAI/4o.py", "gpt-4o"
        )

        tqdm.write("Enhancing " + str(file_path) + " using OpenAI model: o4-mini, effort low")
        enhance_and_save_code_openai(
            human_code, str(file_path.parent) + "/OpenAI/o4-low.py", "o4-mini", True, "low"
        )

        tqdm.write("Enhancing " + str(file_path) + " using OpenAI model: o4-mini, effort medium")
        enhance_and_save_code_openai(
            human_code, str(file_path.parent) + "/OpenAI/o4-medium.py", "o4-mini", True, "medium"
        )

        tqdm.write("Enhancing " + str(file_path) + " using OpenAI model: o4-mini, effort high")
        enhance_and_save_code_openai(
            human_code, str(file_path.parent) + "/OpenAI/o4-high.py", "o4-mini", True, "high"
        )

    if args.deepseek:
        tqdm.write("Enhancing " + str(file_path) + " using Deepseek model: V3")
        enhance_and_save_code_deepseek(
            human_code, str(file_path.parent) + "/DeepSeek/V3.py", "deepseek-chat"
        )

        tqdm.write("Enhancing " + str(file_path) + " using Deepseek model: R1")
        enhance_and_save_code_deepseek(
            human_code, str(file_path.parent) + "/DeepSeek/R1.py", "deepseek-reasoner"
        )

    if args.ollama:
        tqdm.write("Enhancing " + str(file_path) + " using Ollama model: " + ollama_model)
        enhance_and_save_code_ollama(
            human_code, str(file_path.parent) + "/Ollama/ollama.py", ollama_model
        )

def process_file(file_path, args):
    print("Args received:", args)
    print("args.ollama =", args.ollama)
    try:
        enhance_full_file(file_path, args)
        return (file_path, None)
    except Exception as e:
        return (file_path, e)

def main(args):
    files = natsorted(find_human_python_files("../project_root"), key=str)
    start_index = load_checkpoint()
    files = files[start_index:]

    if os.path.exists("error_log.txt"):
        os.remove("error_log.txt")

    max_workers = 5  # Passe das ggf. an deine API-Limits an!
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_file, f, args): f for f in files}
        for i, future in enumerate(tqdm(as_completed(futures), total=len(futures), desc="Processing files", unit="file")):
            file_path, error = future.result()
            if error:
                tqdm.write(f"Error processing {file_path}: {error}")
                with open("error_log.txt", "a") as error_file:
                    error_file.write(f"Error processing {file_path}: {error}\n")
            # Checkpoint nach jedem File
            save_checkpoint(start_index + i + 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--openai", action="store_true")
    parser.add_argument("--deepseek", action="store_true")
    parser.add_argument("--ollama", action="store_true")
    args = parser.parse_args()

    main(args)

