import re
import time
import subprocess
import requests
import os

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pathlib import Path
from requests.adapters import HTTPAdapter
from urllib3.util import (
    Retry,
)  # -------------------- CONFIGURATION --------------------

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

SESSION_COOKIE = os.getenv("SESSION_COOKIE")
ROOT = "../project_root"
# -------------------------------------------------------


# Setup a requests.Session with retry/backoff logic for transient errors
def create_session_with_retries(total_retries=5, backoff_factor=1):
    session = requests.Session()
    retry_strategy = Retry(
        total=total_retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


session = create_session_with_retries()


def extract_answer(output, level):
    parts = output.strip().split()
    return parts[level - 1] if len(parts) >= level else None


def submit_solution(year, day, level, answer):
    post_url = f"https://adventofcode.com/{year}/day/{day}/answer"
    cookies = {"session": SESSION_COOKIE}
    data = {"level": str(level), "answer": answer.strip()}
    headers = {"User-Agent": "adventofcode-auto-submitter by your_username"}

    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        resp = session.post(post_url, data=data, cookies=cookies, headers=headers)
        text = resp.text

        if "That's the right answer!" in text:
            print(f"Day {day} Part {level}: Correct answer.")
            break
        if "That's not the right answer." in text:
            print(f"Day {day} Part {level}: Incorrect answer.")
            break

        # Check for rate-limit message
        if ("You gave an answer too recently" in text) or ("please wait" in text):
            # Extract wait time (minutes or seconds)
            m_min = re.search(r"wait (\d+) minute", text)
            m_sec = re.search(r"wait (\d+) second", text)
            wait_time = 10  # default
            if m_min:
                wait_time = int(m_min.group(1)) * 60
            elif m_sec:
                wait_time = int(m_sec.group(1))
            # Cap maximum wait to avoid excessive delays
            wait_time = min(wait_time, 10 * 60)
            print(
                f"Rate limit hit on Day {day} Part {level}. Attempt {attempt}/{max_attempts}, waiting {wait_time} seconds."
            )
            time.sleep(wait_time)
            continue

        if "Did you already complete it" in text:
            print(f"Day {day} Part {level}: Already completed.")
            break

        print(f"Day {day} Part {level}: Unrecognized response.")
        break

    # Verify submission by scraping result page
    check_url = f"https://adventofcode.com/{year}/day/{day}"
    check_resp = session.get(check_url, cookies=cookies, headers=headers)
    if check_resp.status_code == 200:
        soup = BeautifulSoup(check_resp.text, "html.parser")
        for p in soup.find_all("p"):
            if "Your puzzle answer was" in p.text:
                if answer in p.text:
                    print(f"Recorded solution matches submitted answer: {answer}")
                else:
                    print(f"Mismatch! Page text: {p.text.strip()}")
                break
    else:
        print(f"Verification failed with status code: {check_resp.status_code}")


def main():
    root = Path(ROOT)
    solution_files = list(root.rglob("solution"))

    for sol in sorted(solution_files):
        try:
            year = int(sol.parts[-3])
            day = int(sol.parts[-2])
        except ValueError:
            print(f"Skipping {sol}: cannot determine year/day")
            continue

        output = sol.read_text(encoding="utf-8").strip()
        for level in (1, 2):
            answer = extract_answer(output, level)
            if answer:
                submit_solution(year, day, level, answer)
            else:
                print(f"No answer found for {year}/{day} part {level}")


if __name__ == "__main__":
    main()
