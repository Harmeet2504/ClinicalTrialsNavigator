import json
from fetch_trials import fetch_trials

# Fetch trials updated in the last 12 months
data = fetch_trials()
# print(data.keys())  # Top-level keys (output: dict_keys(['studies', 'nextPageToken']))
#Check total number of records fetched
print("Number of trials fetched:", len(data))
# Preview first trial
if data:
    print(json.dumps(data[0], indent=2))
else:
    print("No trials returned.")


# # Print summary
# print(f"\n Retrieved {len(data.get('studies', []))} trials.\n")

# # Optional: Pretty-print the first trial
# if data.get("studies"):
#     print(json.dumps(data["studies"][0], indent=2))
# else:
#     print("No trials found.")