import requests
from datetime import datetime, timedelta

def fetch_trials(
    condition="Pediatric Brain Tumor",
    page_size=20,
    months_back=12 
):
    url = "https://clinicaltrials.gov/api/v2/studies"
    headers = {
        "accept": "application/json"
    }

    # Calculate dynamic date (For fetching recent trials avoiding noise and preserve legacy trials)
    min_date = (datetime.today() - timedelta(days=30 * months_back)).strftime("%Y-%m-%d")
    query_term = f"AREA[Condition]{condition} AND AREA[LastUpdatePostDate]RANGE[{min_date},MAX]"

    params = {
        "query.term": query_term,
        "pageSize": page_size
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching trials:", e)
        return {}

