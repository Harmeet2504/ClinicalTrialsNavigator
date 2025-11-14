def format_trial_chunks(trial):
    chunks = []
    base_metadata = {
        "nct_id": trial.get("nct_id"),
        "condition": trial.get("condition"),
        "status": trial.get("status"),
        "location": trial.get("location_name"),
        "min_age": trial.get("min_age"),
        "max_age": trial.get("max_age")
    }

    #Custom helper function to get chunks of fields with longer texts
    def make_chunk(title, content):
        if content:
            return f"{title}:\n{content.strip()}"
        return None

    fields = [
        ("Brief Summary", trial.get("brief_summary")),
        ("Eligibility Criteria", trial.get("eligibility")),
        ("Detailed Description", trial.get("detailed_description")),
        ("Treatment Arms", trial.get("arm_descriptions")),
        ("Outcome Measures", trial.get("outcome_descriptions"))
    ]

    # For each chunk, adding metadata for the purpose of filtering when queried
    for title, content in fields:
        chunk_text = make_chunk(title, content)
        if chunk_text:
            chunks.append((chunk_text, base_metadata))

    return chunks