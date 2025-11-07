import sqlite3

def init_db(db_name = "db/clinical_trials.db"):
    conn = sqlite3.Connection(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATe TABLE IF NOT EXISTS trials (
            nct_id TEXT PRIMARY KEY,
            brief_title TEXT,
            status TEXT,
            condition TEXT,
            min_age TEXT,
            max_age TEXT,
            location_name TEXT,
            city TEXT,
            state TEXT,
            country TEXT,
            latitude REAL,
            longitude REAL
                   )

""")
    conn.commit()
    conn.close()