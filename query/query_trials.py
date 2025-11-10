import sqlite3

def find_trials(age = None, location = None, db_name = "db/clinical_trials.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = 'SELECT * FROM trials WHERE 1=1'
    params = []

    if condition:
        query += " AND condition LIKE ?"
        params.append(f"%{condition}%")
    
    if location:
        query += " AND (city LIKE ? OR state LIKE ? OR country LIKE ?)"
        params.extend([f"%{location}%"] * 3)

    if age:
        query += " AND (min_age IS NULL OR CAST(REPLACE(min_age, 'Years', '') AS INTEGER) <= ?)"
        query += " AND (max_age IS NULL OR CAST(REPLACE(max_age, 'Years', '') AS INTEGER) >= ?)"
        params.extend([age, age])

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

