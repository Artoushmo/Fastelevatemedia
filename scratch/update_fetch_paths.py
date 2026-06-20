import os

files = [
    "/Users/v/Desktop/Fastelevate 06-01/contact.html",
    "/Users/v/Desktop/Fastelevate 06-01/nl/contact.html",
    "/Users/v/Desktop/Fastelevate 06-01/start.html",
    "/Users/v/Desktop/Fastelevate 06-01/nl/start.html"
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace fetch("/") with fetch(window.location.pathname)
        if 'fetch("/", {' in content:
            content = content.replace('fetch("/", {', 'fetch(window.location.pathname, {')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated fetch destination in {os.path.basename(filepath)}")

print("Fetch paths updated successfully.")
