import requests
import os
from dotenv import load_dotenv

# Advent of Code session cookie

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)
session_cookie = os.getenv("SESSION_COOKIE")
cookies = {"session": session_cookie}

base_url = "https://adventofcode.com/{year}/day/{day}/input"
project_root = "../project_root"

# Verify session cookie by testing a known input
test_url = base_url.format(year=2023, day=1)
test_response = requests.get(test_url, cookies=cookies)

if "Please log in" in test_response.text or test_response.status_code != 200:
    print("Login failed. Please verify the session cookie.")
    exit(1)
else:
    print("Login successful.")

for year in range(15, 25):
    full_year = 2000 + year
    year_url = base_url.format(year=full_year, day=1)
    response = requests.get(year_url, cookies=cookies)

    if (
        response.status_code == 404
        or "Please log in" in response.text
        or (year >= 2025 and response.status_code == 404)
    ):
        print(f"Year {full_year} not available or requires login. Skipping.")
        continue

    print(f"Year {full_year}:")

    saved_days = []
    failed_days = []

    for day in range(1, 25):
        url = base_url.format(year=full_year, day=day)
        response = requests.get(url, cookies=cookies)

        if "Please log in" in response.text or response.status_code != 200:
            failed_days.append(day)
            continue

        folder_path = os.path.join(project_root, str(full_year), f"{day}")
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, "input")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text.strip())

        saved_days.append(day)

    print(f"  Days saved: {len(saved_days)}, Days failed: {len(failed_days)}")
    if failed_days:
        print(f'  Failed days: {", ".join(map(str, failed_days))}')
