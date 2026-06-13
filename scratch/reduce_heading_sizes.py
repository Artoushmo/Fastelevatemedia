import os
import re

workspace_dir = "/Users/v/Desktop/Fastelevate 06-01"

# Service pages only (EN + NL) — not homepage, about, contact, etc.
service_pages = [
    "corporate-event-photography.html",
    "corporate-video-production.html",
    "professional-headshots-corporate-portraits.html",
    "corporate-interviews-testimonials.html",
    "drone-video-aerial-photography.html",
    "elevate-your-event.html",
    "nl/corporate-event-photography.html",
    "nl/corporate-video-production.html",
    "nl/professional-headshots-corporate-portraits.html",
    "nl/corporate-interviews-testimonials.html",
    "nl/drone-video-aerial-photography.html",
    "nl/elevate-your-event.html",
]

# Size step-downs (one Tailwind size smaller each):
# h1 hero titles:   text-4xl md:text-6xl  →  text-3xl md:text-5xl
# section h2:       text-3xl md:text-5xl  →  text-2xl md:text-4xl
# section h2 small: text-3xl md:text-4xl  →  text-2xl md:text-3xl
# subtitle text:    text-4xl md:text-5xl  →  text-3xl md:text-4xl
# inline h2:        text-4xl md:text-5xl  →  text-3xl md:text-4xl

replacements = [
    # H1 hero page title
    ('text-4xl md:text-6xl font-black text-white leading-tight',
     'text-3xl md:text-5xl font-black text-white leading-tight'),

    # Large section h2 (most common on service pages)
    ('text-3xl md:text-5xl font-black text-[#121111] leading-tight',
     'text-2xl md:text-4xl font-black text-[#121111] leading-tight'),
    ('text-3xl md:text-5xl font-black text-[#121111]',
     'text-2xl md:text-4xl font-black text-[#121111]'),
    ('text-3xl md:text-5xl font-extrabold text-[#121111] leading-tight',
     'text-2xl md:text-4xl font-extrabold text-[#121111] leading-tight'),
    ('text-3xl md:text-5xl font-black text-white leading-tight',
     'text-2xl md:text-4xl font-black text-white leading-tight'),

    # Medium h2 (e.g. 3xl/4xl combos)
    ('text-3xl md:text-4xl font-extrabold text-[#121111] leading-tight',
     'text-2xl md:text-3xl font-extrabold text-[#121111] leading-tight'),
    ('text-3xl md:text-4xl font-black text-[#121111] leading-tight',
     'text-2xl md:text-3xl font-black text-[#121111] leading-tight'),

    # h2 in dark/CTA sections
    ('text-3xl md:text-4xl font-extrabold text-white leading-tight',
     'text-2xl md:text-3xl font-extrabold text-white leading-tight'),

    # h3 pull-quote style
    ('text-2xl md:text-4xl font-extrabold text-white leading-relaxed',
     'text-xl md:text-3xl font-extrabold text-white leading-relaxed'),
    ('text-2xl md:text-4xl font-extrabold tracking-tight',
     'text-xl md:text-3xl font-extrabold tracking-tight'),

    # Subtitle label texts under h1 (small badge)
    # No change needed — these are already xs/sm
]

total = 0
for rel_path in service_pages:
    filepath = os.path.join(workspace_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"  MISSING: {rel_path}")
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    count = sum(1 for a, b in zip(original.split('\n'), content.split('\n')) if a != b)
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Updated {rel_path}: ~{count} line(s) changed")
        total += 1
    else:
        print(f"  No changes: {rel_path}")

print(f"\nDone. Updated {total} files.")
