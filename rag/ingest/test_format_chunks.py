import json
from format_trials_chunks import format_trial_chunks  

# Load parsed JSON
with open("../../data/parsed_trials.json", "r", encoding="utf-8") as f:
    parsed_trials = json.load(f)

# Pick one trial to inspect
trial = parsed_trials[0]
chunks = format_trial_chunks(trial)

# Print formatted chunks
print(f"🧩 Trial NCT ID: {trial['nct_id']}")
print(f"📍 Condition: {trial['condition']}")
print(f"🧵 Total formatted sections: {len(chunks)}\n")

for i, (chunk_text, metadata) in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk_text)
    print("📎 Metadata:", metadata)
    print("\n" + "="*80 + "\n")