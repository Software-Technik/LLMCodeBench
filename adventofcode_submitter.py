
import subprocess
import requests
import os

# -------------------- CONFIGURATION --------------------
YEAR = 2024
DAY = 1
LEVEL = 1  # 1 = Part 1, 2 = Part 2

SESSION_COOKIE = '53616c7465645f5f4337485860b99ad0a4a3a72a7bd681cd9d94e5a2c70aa579f494cfc2d2821b1cdcb0363e9ee0d2ff33ebc7e0a1720cd201a3314fc0427a25'
SCRIPT_PATH = f'project_root/{YEAR}/{DAY}/human.py'
# -------------------------------------------------------


def run_solution_script(script_path):
    try:
        result = subprocess.check_output(
            ['python', script_path],
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
        return result
    except subprocess.CalledProcessError as e:
        print("Error while executing the solution script:")
        print(e.output)
        return None

def extract_answer(output, level):
    parts = output.strip().split()
    if len(parts) >= level:
        return parts[level - 1]
    return None

def submit_solution(year, day, level, answer, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    cookies = {'session': session_cookie}
    data = {
        'level': str(level),
        'answer': str(answer).strip()
    }
    headers = {
        'User-Agent': 'adventofcode-auto-submitter by your_username'
    }

    response = requests.post(url, data=data, cookies=cookies, headers=headers)

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

    print(f"Submission result for Day {day} Part {level}: {result}")

def main():
    if not os.path.exists(SCRIPT_PATH):
        print(f"Script not found: {SCRIPT_PATH}")
        return

    output = run_solution_script(SCRIPT_PATH)
    if output is None:
        return

    answer = extract_answer(output, LEVEL)
    if answer is None:
        print(f"Could not extract answer for part {LEVEL}")
        return 

    print(f"Submitting answer: {answer}")
    submit_solution(YEAR, DAY, LEVEL, answer, SESSION_COOKIE)

if __name__ == '__main__':
    main()