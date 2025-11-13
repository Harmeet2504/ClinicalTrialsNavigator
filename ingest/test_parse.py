from fetch_trials import fetch_trials
from parse_trials import parse_trials
import json

#Fetch and parse
raw_trials = fetch_trials()
parsed = parse_trials(raw_trials)

#Uncomment to investigate the output
# print(f"Parsed {len(parsed)} trials.")
# print(json.dumps(parsed[0], indent=2))

# Save to JSON
with open("../data/parsed_trials.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, indent=2, ensure_ascii=False)

print(f"Saved {len(parsed)} trials to data/parsed_trials.json")
