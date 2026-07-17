import json
import os

workspace = "/Users/v/Desktop/Fastelevate 06-01"
json_path = os.path.join(workspace, "content.json")

# 1. Update content.json
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # en -> corporate-event-photography -> CorporateEventsWe -> image
    try:
        data["en"]["corporate-event-photography"]["CorporateEventsWe"]["image"] = "./images/events-we-cover.jpg"
        print("Updated: en -> corporate-event-photography -> CorporateEventsWe -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # en -> corporate-video-production -> CorporateEventsWe -> image
    try:
        data["en"]["corporate-video-production"]["CorporateEventsWe"]["image"] = "./images/events-we-cover.jpg"
        print("Updated: en -> corporate-video-production -> CorporateEventsWe -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # en -> elevate-your-event -> TailoredCorporateEvent -> image_2
    try:
        data["en"]["elevate-your-event"]["TailoredCorporateEvent"]["image_2"] = "./images/events-we-cover.jpg"
        print("Updated: en -> elevate-your-event -> TailoredCorporateEvent -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    # en -> elevate-your-event -> ExploreOurCorporate -> image_2
    try:
        data["en"]["elevate-your-event"]["ExploreOurCorporate"]["image_2"] = "./images/events-we-cover.jpg"
        print("Updated: en -> elevate-your-event -> ExploreOurCorporate -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> corporate-event-photography -> SoortenEvenementenDie -> image
    try:
        data["nl"]["corporate-event-photography"]["SoortenEvenementenDie"]["image"] = "../images/events-we-cover.jpg"
        print("Updated: nl -> corporate-event-photography -> SoortenEvenementenDie -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> corporate-video-production -> ZakelijkeEvenementenDie -> image
    try:
        data["nl"]["corporate-video-production"]["ZakelijkeEvenementenDie"]["image"] = "../images/events-we-cover.jpg"
        print("Updated: nl -> corporate-video-production -> ZakelijkeEvenementenDie -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> elevate-your-event -> ZakelijkeEvenementenmediaproductieOp -> image_2
    try:
        data["nl"]["elevate-your-event"]["ZakelijkeEvenementenmediaproductieOp"]["image_2"] = "../images/events-we-cover.jpg"
        print("Updated: nl -> elevate-your-event -> ZakelijkeEvenementenmediaproductieOp -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> elevate-your-event -> OntdekOnzeFotografie -> image_2
    try:
        data["nl"]["elevate-your-event"]["OntdekOnzeFotografie"]["image_2"] = "../images/events-we-cover.jpg"
        print("Updated: nl -> elevate-your-event -> OntdekOnzeFotografie -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("content.json successfully updated!")
else:
    print("ERROR: content.json not found!")

# Print remaining zaal.jpg occurrences in content.json
print("\nRemaining occurrences of zaal.jpg in content.json:")
def find_paths(d, current_path=[]):
    if isinstance(d, dict):
        for k, v in d.items():
            find_paths(v, current_path + [k])
    elif isinstance(d, list):
        for i, v in enumerate(d):
            find_paths(v, current_path + [i])
    elif isinstance(d, str):
        if "zaal.jpg" in d:
            print(" -> ".join(map(str, current_path)) + f" : {d}")
find_paths(data)
