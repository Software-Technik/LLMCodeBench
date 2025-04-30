import requests
import os

# Advent of Code session cookie
session_cookie = '53616c7465645f5fed002aea8dff635d19946653e8e36bc79da907910969b3bc4378ff7d78e73ae266d7d14ff084bb62f6383935c952c5d415bfafc6c9af886b'
cookies = {'session': session_cookie}

base_url = 'https://adventofcode.com/{year}/day/{day}/input'
project_root = 'project_root'

# Verify session cookie by testing a known input
test_url = base_url.format(year=2023, day=1)
test_response = requests.get(test_url, cookies=cookies)

if "Please log in" in test_response.text or test_response.status_code != 200:
    print("Login failed. Please verify the session cookie.")
    exit(1)
else:
    print("Login successful.")

for year in range(14, 25):
    full_year = 2000 + year
    year_url = base_url.format(year=full_year, day=1)
    response = requests.get(year_url, cookies=cookies)

    if response.status_code == 404 or "Please log in" in response.text or (year >= 2025 and response.status_code == 404):
        print(f"Year {full_year} not available or requires login. Skipping.")
        continue

    print(f'Year {full_year}:')

    saved_days = []
    failed_days = []

    for day in range(1, 32):
        url = base_url.format(year=full_year, day=day)
        response = requests.get(url, cookies=cookies)

        if "Please log in" in response.text or response.status_code != 200:
            failed_days.append(day)
            continue

        folder_path = os.path.join(project_root, str(full_year), f'challenge{day:02d}')
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, 'inputs')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text.strip())

        saved_days.append(day)

    print(f'  Days saved: {len(saved_days)}, Days failed: {len(failed_days)}')
    if failed_days:
        print(f'  Failed days: {", ".join(map(str, failed_days))}')
