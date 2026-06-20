import os

base = "/Users/v/Desktop/Fastelevate 06-01"

# Hero pages: use the main v2 video
hero_files = [
    (os.path.join(base, "index.html"),    "./Banner Video FEM.MP4",    "./Banner video FEM v2 .mp4"),
    (os.path.join(base, "nl/index.html"), "../Banner Video FEM.MP4",   "../Banner video FEM v2 .mp4"),
]

# About pages: use the about-specific v2 video
about_files = [
    (os.path.join(base, "about.html"),    "./Banner Video FEM.MP4",    "./Banner video FEM v2 about page.mp4"),
    (os.path.join(base, "nl/about.html"), "../Banner Video FEM.MP4",   "../Banner video FEM v2 about page.mp4"),
]

all_files = hero_files + about_files

total = 0
for filepath, old_src, new_src in all_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(old_src)
    if count:
        content = content.replace(old_src, new_src)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  {os.path.relpath(filepath, base)}: replaced {count}x '{old_src}' → '{new_src}'")
        total += count
    else:
        print(f"  {os.path.relpath(filepath, base)}: no match for '{old_src}'")

print(f"\nDone. {total} replacements made.")
