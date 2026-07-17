import os
import shutil

base_dir = "/Users/v/Desktop/Fastelevate 06-01"
images_dir = os.path.join(base_dir, "images")
low_res_dir = os.path.join(images_dir, "FEM Gallery photo's tijdelijk", "Low Res Pictures")
intro_dir = os.path.join(low_res_dir, "2. Photography page intro")
gallery_dir = os.path.join(low_res_dir, "1. Gallery Photography")

# Mapping of old file to new file
replacements = {
    # Task 1: Elevate Your Event homepage tile
    os.path.join(images_dir, "Elevate-Website-FEM.jpg"): os.path.join(low_res_dir, "Elevate your event.jpg"),
    
    # Task 2: Staggered section "Powerful Content, Global Reach"
    os.path.join(images_dir, "zaal.jpg"): os.path.join(low_res_dir, "Powerful Content.jpg"),
    os.path.join(images_dir, "drone-skyline.jpg"): os.path.join(low_res_dir, "Global Reach.jpg"),
    
    # Task 3: Corporate Photography Page intro photos
    os.path.join(images_dir, "Photography-page-1.jpg"): os.path.join(intro_dir, "Photography page 1.jpg"),
    os.path.join(images_dir, "Photography-page-2.jpg"): os.path.join(intro_dir, "Photography page 2.jpg"),
    os.path.join(images_dir, "Photography-pag-3.jpg"): os.path.join(intro_dir, "Photography page 3.jpg"),
    
    # Task 4: Old gallery photos (with red crosses)
    os.path.join(images_dir, "DSC_4326-Verbeterd-NR-2.jpg"): os.path.join(gallery_dir, "20250603_GBG_12.jpg"),
    os.path.join(images_dir, "DSC_4998-Verbeterd-NR.jpg"): os.path.join(gallery_dir, "20250603_GBG_20.jpg"),
    os.path.join(images_dir, "2025-10-30-Architect-at-Work-by-Daan-Jeurens-Websized-21.jpg"): os.path.join(gallery_dir, "20250603_GBG_31.jpg"),
    os.path.join(images_dir, "DSC_1964.jpg"): os.path.join(gallery_dir, "Joshua_Statie174.jpg"),
    os.path.join(images_dir, "gallery-handshake-new.jpg"): os.path.join(gallery_dir, "Joshua_Statie179.jpg"),
    os.path.join(images_dir, "gallery-keynote-new.jpg"): os.path.join(gallery_dir, "Joshua_Statie176.jpg"),
}

for dest, src in replacements.items():
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"Overschreven: {os.path.basename(dest)} met {os.path.basename(src)}")
    else:
        print(f"FOUT: Bronbestand bestaat niet: {src}")

print("Alle foto-vervangingen zijn succesvol uitgevoerd!")
