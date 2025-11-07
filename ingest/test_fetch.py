import json
from .fetch_trials import fetch_trials

# Fetch trials updated in the last 12 months
data = fetch_trials(condition="Pediatric Brain Tumor", page_size=5, months_back=12)

# Print summary
print(f"\n Retrieved {len(data.get('studies', []))} trials.\n")

# Optional: Pretty-print the first trial
if data.get("studies"):
    print(json.dumps(data["studies"][0], indent=2))
else:
    print("No trials found.")