import os
import glob

workspace = "/Users/v/Desktop/Fastelevate 06-01"
html_files = glob.glob(os.path.join(workspace, "*.html")) + glob.glob(os.path.join(workspace, "nl", "*.html"))

desc_en = '<meta name="description" content="Fast Elevate Media is a premium corporate photography and video production agency in Amsterdam. Specializing in corporate events, executive interviews, and drone footage.">'
desc_nl = '<meta name="description" content="Fast Elevate Media is een premium bureau voor bedrijfsfotografie en videoproductie in Amsterdam. Gespecialiseerd in zakelijke evenementen, executive interviews en drone beelden.">'

for file_path in html_files:
    is_nl = "nl/" in file_path.replace("\\", "/") or "nl\\" in file_path
    meta_tag = desc_nl if is_nl else desc_en
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if meta description already exists
    if 'name="description"' not in content:
        # Insert after <title>
        if "<title>" in content:
            parts = content.split("</title>")
            updated_content = parts[0] + "</title>\n  " + meta_tag + parts[1]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Added meta description to {os.path.basename(file_path)}")
    else:
        print(f"Meta description already exists in {os.path.basename(file_path)}")

print("Done updating meta descriptions!")
