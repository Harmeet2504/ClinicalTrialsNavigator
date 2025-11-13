import requests
from datetime import datetime, timedelta

def fetch_trials(condition="Pediatric Brain Tumor", months_back=12, page_size=100):
    url = "https://clinicaltrials.gov/api/v2/studies"
    headers = {"accept": "application/json"}

    # Calculate date range
    min_date = (datetime.today() - timedelta(days=30 * months_back)).strftime("%Y-%m-%d")
    query_term = f"AREA[Condition]{condition} AND AREA[LastUpdatePostDate]RANGE[{min_date},MAX]"

    all_trials = []
    next_token = None
    page = 1

    while True:
        params = {
            "query.term": query_term,
            "pageSize": page_size
        }
        if next_token:
            params["pageToken"] = next_token

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            studies = data.get("studies", [])
            all_trials.extend(studies)
            print(f" Page {page}: Fetched {len(studies)} trials (Total so far: {len(all_trials)})")

            next_token = data.get("nextPageToken")
            if not next_token:
                print("All pages fetched.")
                break

            page += 1

        except requests.exceptions.RequestException as e:
            print("Error fetching trials:", e)
            break

    return all_trials