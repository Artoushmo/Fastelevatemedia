import os
import glob

workspace = "/Users/v/Desktop/Fastelevate 06-01"
images_dir = os.path.join(workspace, "images")
favicon_src = os.path.join(images_dir, "FEM Favicon.jpg")
favicon_jpg = os.path.join(images_dir, "favicon.jpg")

# Try to use PIL to create favicon.ico
ico_path = os.path.join(workspace, "favicon.ico")
try:
    from PIL import Image
    if os.path.exists(favicon_src):
        img = Image.open(favicon_src)
        img.save(ico_path, format='ICO', sizes=[(32, 32), (64, 64)])
        print("Created favicon.ico using PIL")
except Exception as e:
    print(f"PIL not available or failed: {e}. Just copying the file.")
    import shutil
    if os.path.exists(favicon_src):
        shutil.copy2(favicon_src, ico_path)

# Also copy to favicon.jpg for standard use
import shutil
if os.path.exists(favicon_src):
    shutil.copy2(favicon_src, favicon_jpg)

# HTML files to update
html_files = glob.glob(os.path.join(workspace, "*.html")) + glob.glob(os.path.join(workspace, "nl", "*.html"))

for file_path in html_files:
    is_nl = "nl/" in file_path.replace("\\", "/") or "nl\\" in file_path
    
    # Determine the relative path
    rel_path = "../images/favicon.jpg" if is_nl else "./images/favicon.jpg"
    root_ico = "../favicon.ico" if is_nl else "./favicon.ico"
    
    favicon_tags = f"""
  <link rel="icon" type="image/jpeg" href="{rel_path}">
  <link rel="apple-touch-icon" href="{rel_path}">
  <link rel="shortcut icon" href="{root_ico}">
"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "rel=\"icon\"" not in content and "rel=\"apple-touch-icon\"" not in content:
        # Insert before </head>
        updated_content = content.replace("</head>", favicon_tags + "</head>")
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Added favicon to {os.path.basename(file_path)}")
    else:
        print(f"Favicon already exists in {os.path.basename(file_path)}")

print("Done updating favicons!")
