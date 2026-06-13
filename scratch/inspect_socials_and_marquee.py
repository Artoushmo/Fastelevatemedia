import os
import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

# 1. Print socials from a few files to check layout
def inspect_socials():
    files = ["index.html", "faq.html", "about.html", "nl/index.html", "nl/faq.html", "nl/about.html"]
    for f in files:
        path = os.path.join(workspace, f)
        if not os.path.exists(path):
            print(f"File not found: {f}")
            continue
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"\n--- Socials in {f} ---")
        # Try to find a snippet containing footer socials
        # Commonly around target="_blank" and href containing x.com or linkedin
        match = re.search(r'(<!-- Socials and Logo -->|<!-- Social Icons -->|<div class="flex gap-4">.*?(https?://(x\.com|twitter|linkedin|instagram)|href="#").*?</div>)', content, re.DOTALL | re.IGNORECASE)
        if match:
            # Print around the match
            start = max(0, match.start() - 100)
            end = min(len(content), match.end() + 200)
            print(content[start:end])
        else:
            print("No simple regex match, printing last 1000 characters:")
            print(content[-1000:])

def inspect_marquee():
    files = ["index.html", "services.html"]
    for f in files:
        path = os.path.join(workspace, f)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"\n--- Marquee in {f} ---")
        match = re.search(r'(@keyframes scroll\s*\{.*?\})', content, re.DOTALL)
        if match:
            print("Keyframe:", match.group(1))
        match2 = re.search(r'(\.logo-carousel\s*\{.*?\})', content, re.DOTALL)
        if match2:
            print("Class logo-carousel:", match2.group(1))

inspect_socials()
inspect_marquee()
