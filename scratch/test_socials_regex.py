import os
import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

# Find all html files
html_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith(".html") and not "node_modules" in root:
            html_files.append(os.path.join(root, f))

print(f"Total HTML files found: {len(html_files)}")

# Regex to match the block:
# It starts with `<div class="flex gap-4">`
# and contains some social links and is located inside the footer (usually towards the end of the file).
# Let's search for a `<div class="flex gap-4">` that contains at least one of: x.com, twitter, linkedin, instagram, or the specific comments.
socials_pattern = re.compile(
    r'(<div class="flex gap-4">\s*(?:<!--.*?-->\s*)?<a\s+[^>]*?href="[^"]*?"[^>]*?>.*?</a>\s*(?:<!--.*?-->\s*)?<a\s+[^>]*?href="[^"]*?"[^>]*?>.*?</a>\s*(?:<!--.*?-->\s*)?<a\s+[^>]*?href="[^"]*?"[^>]*?>.*?</a>\s*</div>)',
    re.DOTALL | re.IGNORECASE
)

unmatched = []
for path in html_files:
    rel_path = os.path.relpath(path, workspace)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We find all matches of the pattern
    matches = socials_pattern.findall(content)
    # Filter matches to find the one in the footer (usually the one containing socials)
    footer_socials = None
    for m in matches:
        if "linkedin" in m.lower() or "instagram" in m.lower() or "twitter" in m.lower() or "x/twitter" in m.lower() or "x.com" in m.lower():
            footer_socials = m
            break
            
    if footer_socials:
        print(f"MATCH in {rel_path}:")
        # print first 100 chars and last 100 chars
        print(footer_socials[:100] + " ... " + footer_socials[-100:])
    else:
        unmatched.append(rel_path)

print(f"\nUnmatched files: {unmatched}")
