import json
import os
import shutil

workspace = "/Users/v/Desktop/Fastelevate 06-01"
images_dir = os.path.join(workspace, "images")
gallery_dir = os.path.join(images_dir, "FEM Gallery photo's tijdelijk", "Low Res Pictures", "1. Gallery Photography")

# Source files (from the gallery)
src_handshake = os.path.join(gallery_dir, "Joshua_Statie179.jpg")
src_keynote = os.path.join(gallery_dir, "Joshua_Statie176.jpg")

# Target cache-busting files
dest_prosus1 = os.path.join(images_dir, "gallery-prosus-1.jpg")
dest_prosus2 = os.path.join(images_dir, "gallery-prosus-2.jpg")

# Copy the files
if os.path.exists(src_handshake):
    shutil.copy2(src_handshake, dest_prosus1)
    print(f"Copied handshake to {dest_prosus1}")

if os.path.exists(src_keynote):
    shutil.copy2(src_keynote, dest_prosus2)
    print(f"Copied keynote to {dest_prosus2}")

# Replace references in files
files_to_update = [
    "content.json",
    "corporate-event-photography.html",
    "nl/corporate-event-photography.html"
]

for filename in files_to_update:
    file_path = os.path.join(workspace, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content_str = f.read()
        
        # Replace the true Prosus photos
        updated_str = content_str.replace("NZ3_4808-Verbeterd-NR.jpg", "gallery-prosus-1.jpg")
        updated_str = updated_str.replace("NZ3_5157-Verbeterd-NR.jpg", "gallery-prosus-2.jpg")
        
        if updated_str != content_str:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_str)
            print(f"Updated references in {filename}!")
        else:
            print(f"No changes needed in {filename}")
    else:
        print(f"WARNING: File {filename} not found!")

print("Prosus photos replaced with cache-busting names successfully!")
