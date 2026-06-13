import os
import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

# Find all html files
html_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith(".html") and not "node_modules" in root:
            html_files.append(os.path.join(root, f))

def find_socials_block(content):
    # Find all <div class="flex gap-4"> blocks (up to the next </div>)
    # Since there are no nested divs inside the socials block, we can use a simple regex.
    pattern = re.compile(r'(<div class="flex gap-4">.*?</div>)', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(content)
    for m in matches:
        # Check if this block contains references to twitter/x/linkedin/instagram or their SVG paths
        m_lower = m.lower()
        if (
            "linkedin" in m_lower or 
            "instagram" in m_lower or 
            "twitter" in m_lower or 
            "x.com" in m_lower or
            "m18.244" in m_lower or # Twitter SVG path start
            "m19 0h-14" in m_lower or # LinkedIn SVG path start
            "m20.447" in m_lower or # LinkedIn SVG path 2 start
            "m12 2.163" in m_lower # Instagram SVG path start
        ):
            return m
    return None

unmatched = []
for path in html_files:
    rel_path = os.path.relpath(path, workspace)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    block = find_socials_block(content)
    if block:
        print(f"FOUND socials block in {rel_path} ({len(block)} chars)")
    else:
        unmatched.append(rel_path)

print(f"\nUnmatched files: {unmatched}")
if not unmatched:
    print("SUCCESS: Socials block found in all 32 files!")
