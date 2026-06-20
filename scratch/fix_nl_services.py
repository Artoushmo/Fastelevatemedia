import re

filepath = "/Users/v/Desktop/Fastelevate 06-01/nl/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix the CSS overlay styles
old_css = """.image-hover-card-container .overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, var(--color-card-overlay-1) 0%, var(--color-card-overlay-2) 100%);
      opacity: 0.3;
      z-index: 10;
      transition: opacity 600ms ease;
    }
    .image-hover-card-container:hover .overlay {
      opacity: 0.5;
    }"""

new_css = """.image-hover-card-container .overlay {
      position: absolute;
      inset: 0;
      background: rgba(76, 114, 169, 0.72);
      opacity: 0;
      z-index: 10;
      transition: opacity 400ms ease;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .image-hover-card-container:hover .overlay {
      opacity: 1;
    }
    .image-hover-card-container .overlay-label {
      color: #fff;
      font-weight: 800;
      font-size: 1.35rem;
      text-align: center;
      padding: 0 1rem;
      opacity: 0;
      transform: translateY(6px);
      transition: opacity 350ms ease, transform 350ms ease;
      text-shadow: 0 2px 8px rgba(0,0,0,0.3);
      letter-spacing: 0.01em;
    }
    .image-hover-card-container:hover .overlay-label {
      opacity: 1;
      transform: translateY(0);
    }"""

content = content.replace(old_css, new_css)

# 2. Fix section header spacing
content = content.replace(
    'class="py-24 bg-white px-6 md:px-12 lg:px-24 border-t border-gray-200">',
    'class="py-12 bg-white px-6 md:px-12 lg:px-24 border-t border-gray-200">',
    1  # only first occurrence (the services section)
)
content = content.replace(
    '<div class="text-center mb-16 max-w-3xl mx-auto">',
    '<div class="text-center mb-8 max-w-3xl mx-auto">',
    1
)
content = content.replace(
    'class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">',
    'class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">',
    1
)

# 3. Fix all 6 cards: aspect ratio, overlay label, spacing
card_fixes = [
    # (old_overlay, new_overlay, old_aspect, new_aspect, old_py, new_py, old_mb, new_mb, old_pt, new_pt, label)
    ('<div class="overlay"></div>\n            <img alt="Evenementenfotografie"',
     '<div class="overlay"><span class="overlay-label">Evenementenfotografie</span></div>\n            <img alt="Evenementenfotografie"'),
    ('<div class="overlay"></div>\n            <img alt="Videoproductie"',
     '<div class="overlay"><span class="overlay-label">Zakelijke Videoproductie</span></div>\n            <img alt="Videoproductie"'),
    ('<div class="overlay"></div>\n            <img alt="Professionele portretfoto\'s"',
     '<div class="overlay"><span class="overlay-label">Professionele Portretfoto\'s</span></div>\n            <img alt="Professionele portretfoto\'s"'),
    ('<div class="overlay"></div>\n            <img alt="Zakelijke interviews"',
     '<div class="overlay"><span class="overlay-label">Zakelijke Interviews</span></div>\n            <img alt="Zakelijke interviews"'),
    ('<div class="overlay"></div>\n            <img alt="Drone video"',
     '<div class="overlay"><span class="overlay-label">Dronevideo &amp; Luchtfotografie</span></div>\n            <img alt="Drone video"'),
    ('<div class="overlay"></div>\n            <img alt="Uw evenement naar een hoger niveau"',
     '<div class="overlay"><span class="overlay-label">Uw Evenement Naar Een Hoger Niveau</span></div>\n            <img alt="Uw evenement naar een hoger niveau"'),
]

for old, new in card_fixes:
    content = content.replace(old, new)

# 4. Fix aspect ratios
content = content.replace('image-hover-card-container aspect-[3/2]', 'image-hover-card-container aspect-[16/9]')

# 5. Fix spacing inside cards
content = content.replace('<div class="py-6">', '<div class="py-3">')
content = content.replace('<div class="pt-2"><span class="text-primary font-bold inline-flex items-center gap-2">Meer lezen',
                          '<div class="pt-1"><span class="text-primary font-bold inline-flex items-center gap-2">Meer lezen')
content = content.replace('class="text-headline-md mb-3 text-[#121111]', 'class="text-headline-md mb-1 text-[#121111]')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("NL index.html updated successfully.")
