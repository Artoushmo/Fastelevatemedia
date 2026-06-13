import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

card_pattern = re.compile(
    r'<div class="flex flex-col justify-between h-full group">(.*?)<div class="pt-2">\s*<a class="text-primary font-bold inline-flex items-center gap-2 group/link" href="([^"]*?)">\s*(.*?)\s*<span class="group-hover/link:translate-x-2 transition-transform">→</span>\s*</a>\s*</div>\s*</div>',
    re.DOTALL | re.IGNORECASE
)

with open(f"{workspace}/index.html", "r", encoding="utf-8") as f:
    content = f.read()

matches = card_pattern.findall(content)
print(f"Matches in index.html: {len(matches)}")
for i, m in enumerate(matches):
    print(f"\nMatch {i+1}:")
    print(f"Link: {m[1]}")
    print(f"Text: {m[2].strip()}")

with open(f"{workspace}/nl/index.html", "r", encoding="utf-8") as f:
    content_nl = f.read()

matches_nl = card_pattern.findall(content_nl)
print(f"Matches in nl/index.html: {len(matches_nl)}")
for i, m in enumerate(matches_nl):
    print(f"\nMatch {i+1}:")
    print(f"Link: {m[1]}")
    print(f"Text: {m[2].strip()}")
