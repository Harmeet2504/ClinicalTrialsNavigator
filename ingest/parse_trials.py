import json

def parse_trial(study):
    ps = study.get("protocolSection", {})
    id_mod = ps.get("identificationModule", {})
    status_mod = ps.get("statusModule", {})
    desc_mod = ps.get("descriptionModule", {})
    cond_mod = ps.get("conditionsModule", {})
    elig_mod = ps.get("eligibilityModule", {})
    loc_mod = ps.get("contactsLocationsModule", {})
    arms_mod = ps.get("armsInterventionsModule", {})
    outcomes_mod = ps.get("outcomesModule", {})
    refs_mod = ps.get("referencesModule", {})

    # Location (first site only)
    loc = loc_mod.get("locations", [{}])[0]
    geo = loc.get("geoPoint", {})

    # Interventions
    interventions = arms_mod.get("interventions", [])
    intervention_names = [i.get("name", "") for i in interventions]
    intervention_descriptions = [i.get("description", "") for i in interventions]

    # Arm groups
    arm_groups = arms_mod.get("armGroups", [])
    arm_labels = [a.get("label", "") for a in arm_groups]
    arm_descriptions = [a.get("description", "") for a in arm_groups]

    # Outcomes
    primary_outcomes = outcomes_mod.get("primaryOutcomes", [])
    outcome_measures = [o.get("measure", "") for o in primary_outcomes]
    outcome_descriptions = [o.get("description", "") for o in primary_outcomes]
    outcome_timeframes = [o.get("timeFrame", "") for o in primary_outcomes]

    # References
    references = refs_mod.get("references", [])
    pubmed_ids = [r.get("pmid", "") for r in references]
    citations = [r.get("citation", "") for r in references]

    return {
        "nct_id": id_mod.get("nctId", ""),
        "brief_title": id_mod.get("briefTitle", ""),
        "status": status_mod.get("overallStatus", ""),
        "why_stopped": status_mod.get("whyStopped", ""),
        "start_date": status_mod.get("startDateStruct", {}).get("date", ""),
        "completion_date": status_mod.get("completionDateStruct", {}).get("date", ""),
        "condition": ", ".join(cond_mod.get("conditions", [])),
        "keywords": ", ".join(cond_mod.get("keywords", [])),
        "brief_summary": desc_mod.get("briefSummary", ""),
        "detailed_description": desc_mod.get("detailedDescription", ""),
        "eligibility": elig_mod.get("eligibilityCriteria", ""),
        "min_age": elig_mod.get("minimumAge", ""),
        "max_age": elig_mod.get("maximumAge", ""),
        "sex": elig_mod.get("sex", ""),
        "healthy_volunteers": elig_mod.get("healthyVolunteers", False),
        "location_name": loc.get("facility", ""),
        "city": loc.get("city", ""),
        "state": loc.get("state", ""),
        "country": loc.get("country", ""),
        "latitude": geo.get("lat", ""),
        "longitude": geo.get("lon", ""),
        "intervention_names": ", ".join(intervention_names),
        "intervention_descriptions": "\n\n".join(intervention_descriptions),
        "arm_labels": ", ".join(arm_labels),
        "arm_descriptions": "\n\n".join(arm_descriptions),
        "outcome_measures": ", ".join(outcome_measures),
        "outcome_descriptions": "\n\n".join(outcome_descriptions),
        "outcome_timeframes": ", ".join(outcome_timeframes),
        "pubmed_ids": ", ".join(pubmed_ids),
        "citations": "\n\n".join(citations)
    }

def parse_trials(raw_trials):
    return [parse_trial(study) for study in raw_trials]