import os
import shutil

base_dir = "/Users/v/Desktop/Fastelevate 06-01"
images_dir = os.path.join(base_dir, "images")
low_res_dir = os.path.join(images_dir, "FEM Gallery photo's tijdelijk", "Low Res Pictures")
gallery_dir = os.path.join(low_res_dir, "1. Gallery Photography")

# Overschrijf abnamro-scaled-1.jpg met Joshua_Statie176.jpg
dest = os.path.join(images_dir, "abnamro-scaled-1.jpg")
src = os.path.join(gallery_dir, "Joshua_Statie176.jpg")

if os.path.exists(src):
    shutil.copy2(src, dest)
    print(f"Overschreven: abnamro-scaled-1.jpg met Joshua_Statie176.jpg")
else:
    print(f"FOUT: Bronbestand bestaat niet: {src}")
