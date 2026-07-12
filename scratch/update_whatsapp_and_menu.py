import os
import re

workspace_dir = "/Users/v/Desktop/Fastelevate 06-01"

# Find all HTML files
html_files = []
for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

print(f"Found {len(html_files)} HTML files to update.")

# 1. Broken mobile menu patterns
en_menu_broken = """          <li>
            <a href="./corporate-event-photography.html" class="hover:text-primary transition-colors block">
          <li>
            <a href="./services.html" class="text-blue-400 font-bold hover:text-primary transition-colors block border-b border-white/5 pb-2 mb-1">Service Overview</a>
          </li>Corporate Event Photography</a>
          </li>"""

en_menu_fixed = """          <li>
            <a href="./services.html" class="text-blue-400 font-bold hover:text-primary transition-colors block border-b border-white/5 pb-2 mb-1">Service Overview</a>
          </li>
          <li>
            <a href="./corporate-event-photography.html" class="hover:text-primary transition-colors block">Corporate Event Photography</a>
          </li>"""

nl_menu_broken = """          <li>
            <a href="./corporate-event-photography.html" class="hover:text-primary transition-colors block">
          <li>
            <a href="./services.html" class="text-blue-400 font-bold hover:text-primary transition-colors block border-b border-white/5 pb-2 mb-1">Service Overzicht</a>
          </li>Corporate Event Fotografie</a>
          </li>"""

nl_menu_fixed = """          <li>
            <a href="./services.html" class="text-blue-400 font-bold hover:text-primary transition-colors block border-b border-white/5 pb-2 mb-1">Service Overzicht</a>
          </li>
          <li>
            <a href="./corporate-event-photography.html" class="hover:text-primary transition-colors block">Corporate Event Fotografie</a>
          </li>"""

# 2. Phone number patterns
# Matches:
# +31624821770
# +31 6 24821770
# +31 6 2482 1770
# +316 2482 1770
# 31624821770
# 24821770 (maybe, but let's be careful and use the prefix)
phone_regex = re.compile(r'(\+?31\s?6\s?2482\s?1770)')

def replace_phone(match, content_around):
    matched_str = match.group(1)
    # Check if this match is inside an href (tel: or phone=) by looking at surrounding text
    # A simple way is to find the index of the match and check the 30 chars before it.
    start_idx = content_around.find(matched_str)
    prefix = content_around[max(0, start_idx-50):start_idx]
    
    if "tel:" in prefix or "phone=" in prefix or "wa.me/" in prefix:
        # Compact format for URLs
        if matched_str.startswith('+'):
            return "+31628460837"
        elif matched_str.startswith('31'):
            return "31628460837"
        else:
            return "31628460837"
    else:
        # User display format
        return "+316 2846 0837"

# Iterate and apply updates
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    
    # Apply menu fixes
    if en_menu_broken in content:
        content = content.replace(en_menu_broken, en_menu_fixed)
        print(f"Fixed English mobile menu in {os.path.basename(filepath)}")
    elif nl_menu_broken in content:
        content = content.replace(nl_menu_broken, nl_menu_fixed)
        print(f"Fixed Dutch mobile menu in {os.path.basename(filepath)}")
    else:
        # Let's check for subfolder variant where href could be '../services.html' or similar
        # E.g. in some Dutch files, wait, they all use `./corporate-event-photography.html` as seen in grep.
        pass
        
    # Replace phone numbers
    # We do a custom search-and-replace using index to know context
    offset = 0
    while True:
        match = phone_regex.search(content, offset)
        if not match:
            break
        
        start = match.start()
        end = match.end()
        matched_str = match.group(1)
        
        # Get context (30 chars before the match)
        prefix = content[max(0, start-40):start]
        
        if "tel:" in prefix or "phone=" in prefix or "wa.me/" in prefix:
            if matched_str.startswith('+'):
                repl = "+31628460837"
            else:
                repl = "31628460837"
        else:
            repl = "+316 2846 0837"
            
        content = content[:start] + repl + content[end:]
        offset = start + len(repl)
        
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved changes to {os.path.basename(filepath)}")

print("All replacements done!")
