# ingest/ingest_trials.py

import sqlite3

def insert_trials(trials, db_name="db/clinical_trials.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for trial in trials:
        cursor.execute("""
            INSERT OR REPLACE INTO trials (
                nct_id, brief_title, status, condition, min_age, max_age,
                location_name, city, state, country, latitude, longitude
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(trial.values()))

    conn.commit()
    conn.close()