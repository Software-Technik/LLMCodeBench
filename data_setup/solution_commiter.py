import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# -------------------- CONFIGURATION --------------------
ROOT = "../project_root"
env_path = os.path.join(os.path.dirname(__file__), ".config-env")
load_dotenv(dotenv_path=env_path)
SESSION_COOKIE = os.getenv("SESSION_COOKIE")
# -------------------------------------------------------

def extract_answer(output, level):
    parts = output.strip().split()
    if len(parts) >= level:
        return parts[level - 1]
    return None

def submit_solution(year, day, level, answer, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    cookies = {"session": session_cookie}
    data = {"level": str(level), "answer": str(answer).strip()}
    headers = {"User-Agent": "adventofcode-auto-submitter by your_username"}

    response = requests.post(url, data=data, cookies=cookies, headers=headers)
    print(f"Submission for {year}/{day} part {level}: {answer}")
    if "That's the right answer!" in response.text:
        result = "Correct answer."
    elif "That's not the right answer." in response.text:
        result = "Incorrect answer."
    elif "You gave an answer too recently" in response.text:
        result = "Rate limit active. Please wait before submitting again."
    elif "Did you already complete it" in response.text:
        result = "Already completed."
    else:
        result = "Unrecognized server response."

    print(f"Result: {result}\n")
    return result

def main():
    root = Path(ROOT)
    solution_files = list(root.rglob("solution"))

    for solution_file in sorted(solution_files):
        try:
            year = int(solution_file.parts[-3])
            day = int(solution_file.parts[-2])
        except Exception:
            print(f"Skipping {solution_file}: could not extract year/day")
            continue

        with open(solution_file, "r", encoding="utf-8") as f:
            output = f.read().strip()

        for level in [1, 2]:
            answer = extract_answer(output, level)
            if answer is not None:
                submit_solution(year, day, level, answer, SESSION_COOKIE)
            else:
                print(f"No answer for {year}/{day} part {level}")

if __name__ == "__main__":
    main()
