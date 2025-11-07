"""
load_trials.py

Runs the full pipeline to fetch, parse, and store pediatric brain tumor clinical trials
from ClinicalTrials.gov into a local SQLite database.
"""

from ingest.fetch_trials import fetch_trials
from ingest.parse_trials import parse_trials
from ingest.ingest_trials import insert_trials
from db.db_setup import init_db

# Step 1: Initialize DB schema
init_db()

# Step 2: Fetch raw trial data
data = fetch_trials()

# Step 3: Parse into clean records
trials = parse_trials(data)

# Step 4: Insert into SQLite
insert_trials(trials)

print(f" Loaded {len(trials)} trials into the database.")