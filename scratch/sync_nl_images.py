import json

with open("content.json", "r", encoding="utf-8") as f:
    d = json.load(f)

en_home = d["en"]["home"]
nl_home = d["nl"]["home"]

# Map EN sections to NL sections
mapping = {
    "Intro": "Intro",
    "MediaSolutions": "Mediaoplossingen",
    "About": "About",
    "TimelineSection": "TimelineSection",
    "CompaniesThatTrusted": "BedrijvenDieHun",
    "FastReliableDelivery": "SnelleBetrouwbareLevering"
}

changes_made = 0

for en_sec_name, nl_sec_name in mapping.items():
    en_sec = en_home.get(en_sec_name, {})
    nl_sec = nl_home.get(nl_sec_name, {})
    
    for k, v in en_sec.items():
        if k.startswith("image") and isinstance(v, str) and v.strip() != "":
            # Check if NL is missing it
            nl_val = nl_sec.get(k, "")
            if not nl_val.strip():
                # Fix path for NL
                new_val = v.replace("./images/", "../images/")
                nl_sec[k] = new_val
                changes_made += 1
                print(f"Synced {k} in {nl_sec_name} to {new_val}")

if changes_made > 0:
    with open("content.json", "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"Done! {changes_made} changes made to content.json.")
else:
    print("No missing images found to sync.")
