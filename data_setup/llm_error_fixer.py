import os
from dotenv import load_dotenv
load_dotenv()

PROJECT_ROOT = "../project_root"
ERROR_LOG = "./logs/execution_errors.txt"

from llm_controller import (
    enhance_and_save_code_openai,
    enhance_and_save_code_deepseek,
    enhance_and_save_code_ollama,
)


def get_model_and_func_from_path(path):
    if "/OpenAI/" in path:
        if "4o.py" in path:
            return enhance_and_save_code_openai, "gpt-4o"
        elif "o4-low.py" in path:
            return enhance_and_save_code_openai, "o4-mini", True, "low"
        elif "o4-medium.py" in path:
            return enhance_and_save_code_openai, "o4-mini", True, "medium"
        elif "o4-high.py" in path:
            return enhance_and_save_code_openai, "o4-mini", True, "high"
    elif "/DeepSeek/" in path:
        if "V3.py" in path:
            return enhance_and_save_code_deepseek, "deepseek-chat"
        elif "R1.py" in path:
            return enhance_and_save_code_deepseek, "deepseek-reasoner"
    elif "/Ollama/" in path:
        return enhance_and_save_code_ollama, os.environ.get("OLLAMA_MODEL")
    return None


def get_human_code_path(llm_file_path):
    parts = llm_file_path.split(os.sep)
    return os.path.join(PROJECT_ROOT, *parts[:-2], "human.py")


def parse_error_log():
    if not os.path.exists(ERROR_LOG):
        return []
    files = set()
    with open(ERROR_LOG, "r") as f:
        for line in f:
            if ":" in line:
                file_path = line.split(":", 1)[0].strip()
                files.add(file_path)
    return list(files)


def regenerate_file(llm_file_path):
    abs_llm_path = os.path.join(PROJECT_ROOT, llm_file_path)
    human_code_path = get_human_code_path(llm_file_path)
    if not os.path.exists(human_code_path):
        print(f"Human code not found: {human_code_path}")
        return

    with open(human_code_path, "r", encoding="utf-8") as f:
        human_code = f.read()

    model_info = get_model_and_func_from_path(llm_file_path)
    if model_info is None:
        print(f"Unknown model for file: {llm_file_path}")
        return

    if model_info[0] == enhance_and_save_code_openai:
        if len(model_info) == 2:
            enhance_and_save_code_openai(human_code, abs_llm_path, model_info[1])
        else:
            enhance_and_save_code_openai(
                human_code, abs_llm_path, model_info[1], model_info[2], model_info[3]
            )
    elif model_info[0] == enhance_and_save_code_deepseek:
        enhance_and_save_code_deepseek(human_code, abs_llm_path, model_info[1])
    elif model_info[0] == enhance_and_save_code_ollama:
        enhance_and_save_code_ollama(human_code, abs_llm_path, model_info[1])


def main():
    error_files = parse_error_log()
    if not error_files:
        print("No errors found in all llm files")
        return

    print(f"{len(error_files)} files are being regenerated...")
    for rel_path in error_files:
        print(f"Regenerating: {rel_path}")
        regenerate_file(rel_path)


if __name__ == "__main__":
    main()
