import os
import re

OLD_URL = "https://www.linkedin.com/company/fastelevatemedia"
NEW_URL = "https://www.linkedin.com/company/fast-elevate-media/"

workspace_dir = "/Users/v/Desktop/Fastelevate 06-01"
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    # skip hidden and scratch dirs
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scratch']
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

print(f"Found {len(html_files)} HTML files.")
total = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(OLD_URL)
    if count:
        new_content = content.replace(OLD_URL, NEW_URL)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Updated {os.path.relpath(filepath, workspace_dir)}: {count} link(s)")
        total += count

print(f"\nDone. Replaced {total} LinkedIn links in total.")
