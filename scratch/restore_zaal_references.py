import json
import os

workspace = "/Users/v/Desktop/Fastelevate 06-01"
json_path = os.path.join(workspace, "content.json")

# 1. Restore content.json
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # en -> corporate-event-photography -> CorporateEventsWe -> image
    try:
        data["en"]["corporate-event-photography"]["CorporateEventsWe"]["image"] = "./images/zaal.jpg"
        print("Restored: en -> corporate-event-photography -> CorporateEventsWe -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # en -> corporate-video-production -> CorporateEventsWe -> image
    try:
        data["en"]["corporate-video-production"]["CorporateEventsWe"]["image"] = "./images/zaal.jpg"
        print("Restored: en -> corporate-video-production -> CorporateEventsWe -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # en -> elevate-your-event -> TailoredCorporateEvent -> image_2
    try:
        data["en"]["elevate-your-event"]["TailoredCorporateEvent"]["image_2"] = "./images/zaal.jpg"
        print("Restored: en -> elevate-your-event -> TailoredCorporateEvent -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    # en -> elevate-your-event -> ExploreOurCorporate -> image_2
    try:
        data["en"]["elevate-your-event"]["ExploreOurCorporate"]["image_2"] = "./images/zaal.jpg"
        print("Restored: en -> elevate-your-event -> ExploreOurCorporate -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> corporate-event-photography -> SoortenEvenementenDie -> image
    try:
        data["nl"]["corporate-event-photography"]["SoortenEvenementenDie"]["image"] = "../images/zaal.jpg"
        print("Restored: nl -> corporate-event-photography -> SoortenEvenementenDie -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> corporate-video-production -> ZakelijkeEvenementenDie -> image
    try:
        data["nl"]["corporate-video-production"]["ZakelijkeEvenementenDie"]["image"] = "../images/zaal.jpg"
        print("Restored: nl -> corporate-video-production -> ZakelijkeEvenementenDie -> image")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> elevate-your-event -> ZakelijkeEvenementenmediaproductieOp -> image_2
    try:
        data["nl"]["elevate-your-event"]["ZakelijkeEvenementenmediaproductieOp"]["image_2"] = "../images/zaal.jpg"
        print("Restored: nl -> elevate-your-event -> ZakelijkeEvenementenmediaproductieOp -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    # nl -> elevate-your-event -> OntdekOnzeFotografie -> image_2
    try:
        data["nl"]["elevate-your-event"]["OntdekOnzeFotografie"]["image_2"] = "../images/zaal.jpg"
        print("Restored: nl -> elevate-your-event -> OntdekOnzeFotografie -> image_2")
    except KeyError as e:
        print(f"KeyError: {e}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("content.json successfully restored!")
else:
    print("ERROR: content.json not found!")

# 2. Restore HTML Files
html_replacements = [
    # English HTMLs
    ("corporate-event-photography.html", './images/events-we-cover.jpg', './images/zaal.jpg'),
    ("corporate-video-production.html", './images/events-we-cover.jpg', './images/zaal.jpg'),
    ("elevate-your-event.html", './images/events-we-cover.jpg', './images/zaal.jpg'),
    # Dutch HTMLs
    ("nl/corporate-event-photography.html", '../images/events-we-cover.jpg', '../images/zaal.jpg'),
    ("nl/corporate-video-production.html", '../images/events-we-cover.jpg', '../images/zaal.jpg'),
    ("nl/elevate-your-event.html", '../images/events-we-cover.jpg', '../images/zaal.jpg'),
]

for filename, old_src, new_src in html_replacements:
    file_path = os.path.join(workspace, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(old_src, new_src)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Restored HTML file: {filename}")
        else:
            print(f"No changes made to {filename}")
    else:
        print(f"WARNING: File {filename} not found!")

print("All reference restorations completed!")
