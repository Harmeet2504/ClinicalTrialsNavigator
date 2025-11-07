# ingest/parse_trials.py

def parse_trials(data):
    """
    Function to extract clean trial records from the raw API response
    """
    trials = []

    for study in data.get("studies", []):
        protocol = study.get("protocolSection", {})
        id_module = protocol.get("identificationModule", {})
        status_module = protocol.get("statusModule", {})
        eligibility = protocol.get("eligibilityModule", {})
        conditions = protocol.get("conditionsModule", {})
        locations = protocol.get("contactsLocationsModule", {}).get("locations", [])

        loc = locations[0] if locations else {}
        geo = loc.get("geoPoint", {}) if isinstance(loc, dict) else {}

        trial_record = {
            "nct_id": id_module.get("nctId"),
            "brief_title": id_module.get("briefTitle"),
            "status": status_module.get("overallStatus"),
            "condition": ", ".join(conditions.get("conditions", [])),
            "min_age": eligibility.get("minimumAge"),
            "max_age": eligibility.get("maximumAge"),
            "location_name": loc.get("facility") if isinstance(loc, dict) else None,
            "city": loc.get("city") if isinstance(loc, dict) else None,
            "state": loc.get("state") if isinstance(loc, dict) else None,
            "country": loc.get("country") if isinstance(loc, dict) else None,
            "latitude": geo.get("lat"),
            "longitude": geo.get("lon")
        }

        trials.append(trial_record)

    return trials