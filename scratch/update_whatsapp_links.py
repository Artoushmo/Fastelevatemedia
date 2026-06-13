import os
import re

target_url = "https://api.whatsapp.com/send/?phone=31624821770&text&type=phone_number&app_absent=0"

# Find all HTML files in the workspace
workspace_dir = "/Users/v/Desktop/Fastelevate 06-01"
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

print(f"Found {len(html_files)} HTML files.")

# Regex to find different variants of WhatsApp URLs:
# Matches:
# - https://wa.me/xxxxxx
# - https://wa.me/#
# - https://wa.me
# - https://api.whatsapp.com/send/...
# - https://api.whatsapp.com/send?...
whatsapp_regex = re.compile(r'https?://(?:wa\.me|api\.whatsapp\.com/send)/?[a-zA-Z0-9_#?&=\-\+\.]*')

updated_count = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = whatsapp_regex.findall(content)
    if matches:
        # Perform substitution
        new_content = whatsapp_regex.sub(target_url, content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath} - replaced {len(matches)} links.")
        updated_count += len(matches)

print(f"Completed updating {updated_count} WhatsApp links across files.")
