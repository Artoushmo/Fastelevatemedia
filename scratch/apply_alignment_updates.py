import os

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

alignment_pages = [
    "corporate-event-photography.html",
    "corporate-video-production.html",
    "corporate-interviews-testimonials.html",
    "professional-headshots-corporate-portraits.html",
    "drone-video-aerial-photography.html",
    "services.html"
]

def update_alignment(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    target = "grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center"
    replacement = "grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-start"

    content = content.replace(target, replacement)

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
        if entry in alignment_pages:
            filepath = os.path.join(base_dir, entry)
            if update_alignment(filepath):
                count += 1
                
    # Process files in nl/
    nl_dir = os.path.join(base_dir, "nl")
    if os.path.exists(nl_dir):
        for entry in os.listdir(nl_dir):
            if entry in alignment_pages:
                filepath = os.path.join(nl_dir, entry)
                if update_alignment(filepath):
                    count += 1

    print(f"Alignment updates completed. Total files modified: {count}")

if __name__ == "__main__":
    main()
