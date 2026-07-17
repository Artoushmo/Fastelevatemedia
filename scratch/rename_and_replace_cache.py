import json
import os
import shutil

workspace = "/Users/v/Desktop/Fastelevate 06-01"
images_dir = os.path.join(workspace, "images")
gallery_dir = os.path.join(images_dir, "FEM Gallery photo's tijdelijk", "Low Res Pictures", "1. Gallery Photography")

# Source files
src_handshake = os.path.join(gallery_dir, "Joshua_Statie179.jpg")
src_keynote = os.path.join(gallery_dir, "Joshua_Statie176.jpg")

# Target files
dest_handshake = os.path.join(images_dir, "gallery-handshake-new.jpg")
dest_keynote = os.path.join(images_dir, "gallery-keynote-new.jpg")

# Copy the files
if os.path.exists(src_handshake):
    shutil.copy2(src_handshake, dest_handshake)
    print(f"Copied handshake to {dest_handshake}")
else:
    print(f"ERROR: Source handshake not found: {src_handshake}")

if os.path.exists(src_keynote):
    shutil.copy2(src_keynote, dest_keynote)
    print(f"Copied keynote to {dest_keynote}")
else:
    print(f"ERROR: Source keynote not found: {src_keynote}")

# Update content.json
json_path = os.path.join(workspace, "content.json")
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        content_str = f.read()
    
    # Replace references
    updated_str = content_str.replace("DSC_4998-Verbeterd-NR.jpg", "gallery-handshake-new.jpg")
    updated_str = updated_str.replace("DSC_9147.jpg", "gallery-keynote-new.jpg")
    
    if updated_str != content_str:
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(updated_str)
        print("Updated content.json references!")
    else:
        print("No changes needed in content.json")

# Update HTML files
html_files = [
    "corporate-event-photography.html",
    "corporate-video-production.html",
    "nl/corporate-event-photography.html",
    "nl/corporate-video-production.html"
]

for filename in html_files:
    file_path = os.path.join(workspace, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content_str = f.read()
        
        updated_str = content_str.replace("DSC_4998-Verbeterd-NR.jpg", "gallery-handshake-new.jpg")
        updated_str = updated_str.replace("DSC_9147.jpg", "gallery-keynote-new.jpg")
        
        if updated_str != content_str:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_str)
            print(f"Updated HTML file: {filename}")
        else:
            print(f"No changes needed in {filename}")
    else:
        print(f"WARNING: File {filename} not found!")

print("Cache bypass replacement completed successfully!")
