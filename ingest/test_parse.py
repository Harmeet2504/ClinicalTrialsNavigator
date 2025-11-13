from fetch_trials import fetch_trials
from parse_trials import parse_trials
import json

raw_trials = fetch_trials()
parsed = parse_trials(raw_trials)

print(f"Parsed {len(parsed)} trials.")
print(json.dumps(parsed[0], indent=2))