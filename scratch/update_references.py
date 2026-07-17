import json
import os

workspace = "/Users/v/Desktop/Fastelevate 06-01"
json_path = os.path.join(workspace, "content.json")

# 1. Update content.json
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # English corporate-event-photography
    if "corporate-event-photography" in data:
        if "CorporateEventsWe" in data["corporate-event-photography"]:
            data["corporate-event-photography"]["CorporateEventsWe"]["image"] = "./images/events-we-cover.jpg"
            print("Updated content.json: corporate-event-photography -> CorporateEventsWe -> image")
            
    # English corporate-video-production
    if "corporate-video-production" in data:
        if "CorporateEventsWe" in data["corporate-video-production"]:
            data["corporate-video-production"]["CorporateEventsWe"]["image"] = "./images/events-we-cover.jpg"
            print("Updated content.json: corporate-video-production -> CorporateEventsWe -> image")
            
    # English elevate-your-event
    if "elevate-your-event" in data:
        if "TailoredCorporateEvent" in data["elevate-your-event"]:
            data["elevate-your-event"]["TailoredCorporateEvent"]["image_2"] = "./images/events-we-cover.jpg"
            print("Updated content.json: elevate-your-event -> TailoredCorporateEvent -> image_2")
        if "ExploreOurCorporate" in data["elevate-your-event"]:
            data["elevate-your-event"]["ExploreOurCorporate"]["image_2"] = "./images/events-we-cover.jpg"
            print("Updated content.json: elevate-your-event -> ExploreOurCorporate -> image_2")
            
    # Dutch (nl) sections
    if "nl" in data:
        nl_data = data["nl"]
        if "corporate-event-photography" in nl_data:
            if "CorporateEventsWe" in nl_data["corporate-event-photography"]:
                nl_data["corporate-event-photography"]["CorporateEventsWe"]["image"] = "../images/events-we-cover.jpg"
                print("Updated content.json: nl -> corporate-event-photography -> CorporateEventsWe -> image")
        if "corporate-video-production" in nl_data:
            if "CorporateEventsWe" in nl_data["corporate-video-production"]:
                nl_data["corporate-video-production"]["CorporateEventsWe"]["image"] = "../images/events-we-cover.jpg"
                print("Updated content.json: nl -> corporate-video-production -> CorporateEventsWe -> image")
        if "elevate-your-event" in nl_data:
            if "ZakelijkeEvenementenmediaproductieOp" in nl_data["elevate-your-event"]:
                nl_data["elevate-your-event"]["ZakelijkeEvenementenmediaproductieOp"]["image_2"] = "../images/events-we-cover.jpg"
                print("Updated content.json: nl -> elevate-your-event -> ZakelijkeEvenementenmediaproductieOp -> image_2")
            if "OntdekOnzeFotografie" in nl_data["elevate-your-event"]:
                nl_data["elevate-your-event"]["OntdekOnzeFotografie"]["image_2"] = "../images/events-we-cover.jpg"
                print("Updated content.json: nl -> elevate-your-event -> OntdekOnzeFotografie -> image_2")
                
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("content.json successfully updated!")
else:
    print("ERROR: content.json not found!")

# 2. Update HTML Files
html_replacements = [
    # English HTMLs
    ("corporate-event-photography.html", './images/zaal.jpg', './images/events-we-cover.jpg'),
    ("corporate-video-production.html", './images/zaal.jpg', './images/events-we-cover.jpg'),
    ("elevate-your-event.html", './images/zaal.jpg', './images/events-we-cover.jpg'),
    # Dutch HTMLs
    ("nl/corporate-event-photography.html", '../images/zaal.jpg', '../images/events-we-cover.jpg'),
    ("nl/corporate-video-production.html", '../images/zaal.jpg', '../images/events-we-cover.jpg'),
    ("nl/elevate-your-event.html", '../images/zaal.jpg', '../images/events-we-cover.jpg'),
]

for filename, old_src, new_src in html_replacements:
    file_path = os.path.join(workspace, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace occurrences of zaal.jpg with events-we-cover.jpg in non-homepage pages
        # Be careful not to replace it if it's not matching the path exactly
        new_content = content.replace(old_src, new_src)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated HTML file: {filename}")
        else:
            print(f"No changes made to {filename}")
    else:
        print(f"WARNING: File {filename} not found!")

print("All HTML and JSON reference updates completed!")
