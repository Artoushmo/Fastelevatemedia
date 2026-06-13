import os
import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

# Find all html files
html_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith(".html") and not "node_modules" in root:
            html_files.append(os.path.join(root, f))

print(f"Total HTML files to process: {len(html_files)}")

# 1. Social Media Links Replacement
# Templates for LinkedIn and Instagram
linkedin_svg = """<svg class="{size} fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.779-1.75-1.75s.784-1.75 1.75-1.75 1.75.779 1.75 1.75-.784 1.75-1.75 1.75zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
              </svg>"""

instagram_svg = """<svg class="{size} fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
              </svg>"""

def update_socials(content, rel_path):
    # Find socials block
    pattern = re.compile(r'(<div class="flex gap-4">.*?</div>)', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(content)
    socials_block = None
    for m in matches:
        m_lower = m.lower()
        if (
            "linkedin" in m_lower or 
            "instagram" in m_lower or 
            "twitter" in m_lower or 
            "x.com" in m_lower or
            "m18.244" in m_lower or 
            "m19 0h-14" in m_lower or 
            "m20.447" in m_lower or 
            "m12 2.163" in m_lower
        ):
            socials_block = m
            break
            
    if not socials_block:
        print(f"WARNING: Socials block not found in {rel_path}")
        return content

    # Detect icon size
    size_class = "w-4 h-4"
    if "w-5 h-5" in socials_block:
        size_class = "w-5 h-5"
    
    # Generate new socials block
    new_block = f"""<div class="flex gap-4">
            <!-- LinkedIn Icon -->
            <a href="https://www.linkedin.com/company/fastelevatemedia" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition-colors" aria-label="LinkedIn">
              {linkedin_svg.format(size=size_class)}
            </a>
            <!-- Instagram Icon -->
            <a href="https://www.instagram.com/fastelevatemedia" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition-colors" aria-label="Instagram">
              {instagram_svg.format(size=size_class)}
            </a>
          </div>"""
          
    return content.replace(socials_block, new_block)

# 2. Keyframe Rename helper
def update_keyframe(content, rel_path):
    if "logo-carousel" in content:
        # Rename @keyframes scroll -> @keyframes logo-marquee
        content = re.sub(r'@keyframes\s+scroll\b', '@keyframes logo-marquee', content)
        # Rename animation: scroll ... -> animation: logo-marquee ...
        content = re.sub(r'animation:\s*scroll\s+([\w\s\-]+);', r'animation: logo-marquee \1;', content)
        print(f"Updated marquee keyframe in {rel_path}")
    return content

# Process each file
for path in html_files:
    rel_path = os.path.relpath(path, workspace)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Apply Socials update
    content = update_socials(content, rel_path)
    
    # Apply Keyframe update
    content = update_keyframe(content, rel_path)
    
    # Apply About Page updates
    if rel_path == "about.html":
        old_text = "Joshua Statie is an Amsterdam-based"
        new_text = "Joshua is an Amsterdam-based"
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(f"Updated Joshua's bio in {rel_path}")
        else:
            print(f"WARNING: Bio text not found in {rel_path}")
            
    elif rel_path == "nl/about.html":
        old_text = "Joshua Statie is een in Amsterdam gevestigde"
        new_text = "Joshua is een in Amsterdam gevestigde"
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(f"Updated Joshua's bio in {rel_path}")
        else:
            print(f"WARNING: Bio text not found in {rel_path}")
            
    # Apply Homepage subtle pricing link updates
    if rel_path == "index.html":
        old_para = "<p>We work fast and efficiently, without compromising on quality or experience. Our goal is simple: to bring your ideas to life and deliver high-quality visual content that truly reflects your vision, delivered with speed and precision.</p>"
        new_para = "<p>We work fast and efficiently, without compromising on quality or experience. Our goal is simple: to bring your ideas to life and deliver high-quality visual content that truly reflects your vision, delivered with speed and precision. Learn more about our transparent <a href=\"./pricing.html\" class=\"text-blue-400 hover:text-blue-300 underline font-semibold transition-colors\">pricing and packages</a>.</p>"
        if old_para in content:
            content = content.replace(old_para, new_para)
            print(f"Added subtle pricing link in {rel_path}")
        else:
            print(f"WARNING: Subtle pricing target paragraph not found in {rel_path}")
            
    elif rel_path == "nl/index.html":
        old_para = "<p>We werken snel en efficiënt, zonder concessies te doen aan kwaliteit of beleving. Ons doel is simpel: uw ideeën tot leven brengen en hoogwaardige visuele content leveren die uw visie weerspiegelt, geleverd met snelheid en precisie.</p>"
        new_para = "<p>We werken snel en efficiënt, zonder concessies te doen aan kwaliteit of beleving. Ons doel is simpel: uw ideeën tot leven brengen en hoogwaardige visuele content leveren die uw visie weerspiegelt, geleverd met snelheid en precisie. Bekijk ook onze transparante <a href=\"./pricing.html\" class=\"text-blue-400 hover:text-blue-300 underline font-semibold transition-colors\">tarieven en pakketten</a>.</p>"
        if old_para in content:
            content = content.replace(old_para, new_para)
            print(f"Added subtle pricing link in {rel_path}")
        else:
            print(f"WARNING: Subtle pricing target paragraph not found in {rel_path}")

    # Apply Homepage Media Solutions cards clickability
    if rel_path in ["index.html", "nl/index.html"]:
        card_pattern = re.compile(
            r'<div class="flex flex-col justify-between h-full group">(.*?)<div class="pt-2">\s*<a class="text-primary font-bold inline-flex items-center gap-2 group/link" href="([^"]*?)">\s*(.*?)\s*<span class="group-hover/link:translate-x-2 transition-transform">→</span>\s*</a>\s*</div>\s*</div>',
            re.DOTALL | re.IGNORECASE
        )
        
        def card_replacement(match):
            inner = match.group(1)
            link = match.group(2)
            btn_text = match.group(3).strip()
            
            # Animate the h3 title color on group hover
            # Replace text-[#121111] font-bold with text-[#121111] font-bold group-hover:text-primary transition-colors
            inner = inner.replace(
                'text-[#121111] font-bold', 
                'text-[#121111] font-bold group-hover:text-primary transition-colors'
            )
            
            # Form the new card wrapper
            replacement = f'<a href="{link}" class="flex flex-col justify-between h-full group block text-left">'
            replacement += inner
            replacement += f'<div class="pt-2"><span class="text-primary font-bold inline-flex items-center gap-2">{btn_text} <span class="group-hover:translate-x-2 transition-transform">→</span></span></div>'
            replacement += '</a>'
            return replacement
            
        modified_content = card_pattern.sub(card_replacement, content)
        if modified_content != content:
            content = modified_content
            print(f"Wrapped Media Solutions cards with clickability in {rel_path}")
        else:
            print(f"WARNING: Media Solutions cards pattern not matched in {rel_path}")

    # Write changes if anything changed
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved changes to {rel_path}")

print("\nUpdates completed!")
