import os

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

service_files = [
    "corporate-event-photography.html",
    "corporate-video-production.html",
    "corporate-interviews-testimonials.html",
    "professional-headshots-corporate-portraits.html"
]

def update_html_file(filepath, is_service_page):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Revert switcher text
    content = content.replace("EN (US)", "EN")
    content = content.replace("NL (Dutch)", "NL")

    # 2. Add shrink-0 and flex-shrink:0; to all flag SVGs
    target_svg = 'class="w-5 h-3.5 rounded-sm object-cover" width="20" height="14" style="width:20px; height:14px; display:inline-block; vertical-align:middle;"'
    replacement_svg = 'class="w-5 h-3.5 rounded-sm object-cover shrink-0" width="20" height="14" style="width:20px; height:14px; display:inline-block; vertical-align:middle; flex-shrink:0;"'
    content = content.replace(target_svg, replacement_svg)

    # 3. Compact bottom images on service pages
    if is_service_page:
        content = content.replace("h-[22rem] md:h-[26rem]", "h-[18rem] md:h-[20rem]")

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filepath}")
        return True
    return False

def main():
    count = 0
    # Process files in root
    for entry in os.listdir(base_dir):
        if entry.endswith(".html"):
            filepath = os.path.join(base_dir, entry)
            is_service = entry in service_files
            if update_html_file(filepath, is_service):
                count += 1
                
    # Process files in nl/
    nl_dir = os.path.join(base_dir, "nl")
    if os.path.exists(nl_dir):
        for entry in os.listdir(nl_dir):
            if entry.endswith(".html"):
                filepath = os.path.join(nl_dir, entry)
                is_service = entry in service_files
                if update_html_file(filepath, is_service):
                    count += 1

    print(f"Updates completed. Total files modified: {count}")

if __name__ == "__main__":
    main()
