import os
import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

# Find all html files
html_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith(".html") and not "node_modules" in root:
            html_files.append(os.path.join(root, f))

print(f"Total HTML files to scan for CSS variable updates: {len(html_files)}")

# 1. Update card overlay color variable in all HTML files
# Replace --color-card-overlay-2: #5D0E9E; or #5d0e9e with #4C72A9
overlay_pattern1 = re.compile(r'--color-card-overlay-2:\s*#5D0E9E\b', re.IGNORECASE)
overlay_pattern2 = re.compile(r'--color-card-overlay-2:\s*#5d0e9e\b', re.IGNORECASE)

for path in html_files:
    rel_path = os.path.relpath(path, workspace)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Replace overlay color variable
    content, c1 = overlay_pattern1.subn('--color-card-overlay-2: #4C72A9', content)
    content, c2 = overlay_pattern2.subn('--color-card-overlay-2: #4C72A9', content)
    
    if c1 + c2 > 0:
        print(f"Updated --color-card-overlay-2 to brand blue (#4C72A9) in {rel_path}")
        
    # Write changes if anything changed
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

# 2. Homepage Updates (index.html & nl/index.html)
homepages = ["index.html", "nl/index.html"]
for f_name in homepages:
    path = os.path.join(workspace, f_name)
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # 2.1 Logo slider bottom divider removal
    content, count1 = re.subn(
        r'<!-- Bottom Shape Divider \(transitions from white to Testimonials dark bg #121111\) -->\s*<div class="absolute bottom-0 left-0 w-full overflow-hidden leading-\[0\] z-20">\s*<svg class="relative block w-full h-\[150px\]".*?</svg>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2.2 Testimonials section removal
    content, count2 = re.subn(
        r'<!-- 7\. Testimonials Slider Section -->\s*<section class="py-32 bg-\[#1c1b1b\] px-6 overflow-hidden">.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2.3 Content section top divider removal
    content, count3 = re.subn(
        r'<!-- Top Shape Divider \(transitions from Testimonials dark bg #121111\) -->\s*<div class="absolute top-0 left-0 w-full overflow-hidden leading-\[0\] z-20 transform -translate-y-\[1px\]">\s*<svg class="relative block w-full h-\[150px\]".*?</svg>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2.4 Results section removal
    content, count4 = re.subn(
        r'<!-- 9\. Results Section -->\s*<section class="py-32 relative bg-\[#4C72A9\] text-white overflow-hidden">.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2.5 Counter JS removal
    content, count5 = re.subn(
        r'// Counter Animation.*?ScrollTrigger\.create\(\{.*?onEnter:\s*\(\)\s*=>\s*updateCount\(\)\s*\}\);\s*\}\);',
        '',
        content,
        flags=re.DOTALL
    )

    # 2.6 Testimonial track JS removal
    content, count6 = re.subn(
        r'// Testimonial Track Autoplay & Drag Simulation.*?translateX\(-\$\{offset\}%\).*?\}, 5000\);',
        '',
        content,
        flags=re.DOTALL
    )
    
    print(f"\nHomepage removals in {f_name}:")
    print(f"  Divider 1 removed: {count1}")
    print(f"  Testimonials section removed: {count2}")
    print(f"  Divider 2 removed: {count3}")
    print(f"  Results section removed: {count4}")
    print(f"  Counter JS removed: {count5}")
    print(f"  Testimonial JS removed: {count6}")
    
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved removals to {f_name}")

# 3. About Page Updates (about.html & nl/about.html)
# English version
path_about = os.path.join(workspace, "about.html")
if os.path.exists(path_about):
    with open(path_about, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # 3.1 Remove Google Rating details card
    rating_regex = r'<!-- Rating details -->\s*<div class="flex items-center gap-2 bg-white/5 rounded-2xl py-3 px-5 border border-white/5">.*?/5 on Google\s*</span>\s*</div>'
    content, count_r = re.subn(rating_regex, '', content, flags=re.DOTALL)
    
    # 3.2 Remove Meet Our Champions Section
    champions_regex = r'<!-- 3\.5\. Meet Our Champions Section -->\s*<section class="py-24 bg-\[#121111\] text-white px-6 md:px-12 lg:px-24">.*?</section>'
    content, count_c = re.subn(champions_regex, '', content, flags=re.DOTALL)
    
    # 3.3 Change grid layout
    grid_regex = r'<!-- Team Members Grid -->\s*<div class="grid grid-cols-1 md:grid-cols-3 gap-8">'
    new_grid = '<!-- Team Members Grid -->\n      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">'
    content, count_g = re.subn(grid_regex, new_grid, content)
    
    # 3.4 Append Laurien & Artoush cards
    laurien_card = """

        <!-- Member 4 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Laurien" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="./images/laurien.png"/>
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]">Laurien</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider">Executive Assistant - Fast Elevate Media</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed">
              Laurien is the Executive Assistant at Fast Elevate Media, responsible for orchestrating daily operations, managing client communications, and ensuring seamless project logistics. With a strong background in corporate administration and event coordination, she keeps production timelines on track and maintains clear communication from initial booking to final delivery. Her organized and detail-oriented approach ensures that our team of creatives and client partners can collaborate efficiently and effectively on every production.
            </p>
          </div>
        </div>

        <!-- Member 5 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Artoush" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="./images/artoush.png"/>
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]">Artoush</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider">Web & App Developer - Fast Elevate Media</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed">
              Artoush is a Web and App Developer at Fast Elevate Media, specialising in building high-performance, responsive digital interfaces and custom media delivery solutions. Combining technical precision with an eye for modern UI/UX design, he ensures that our clients' visual assets are integrated seamlessly into premium, fast-loading digital environments. Artoush focuses on developing clean, structured code that optimizes media playback, interactive layouts, and user engagement across web and mobile platforms.
            </p>
          </div>
        </div>"""
        
    joshua_card_end = r'(<!-- Member 3 -->.*?</div>\s*</div>)(\s*</div>\s*</div>\s*</section>)'
    
    # We replace Joshua's block with Joshua's block + Laurien + Artoush + the grid/section end
    match = re.search(joshua_card_end, content, re.DOTALL)
    if match:
        content = content.replace(match.group(0), match.group(1) + laurien_card + match.group(2))
        print("\nUpdated about.html:")
        print(f"  Google rating card removed: {count_r}")
        print(f"  Champions section removed: {count_c}")
        print(f"  Grid layout updated: {count_g}")
        print("  Laurien and Artoush team cards added successfully!")
    else:
        print("WARNING: Could not append team members in about.html")
        
    if content != original:
        with open(path_about, "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved updates to about.html")

# Dutch version
path_about_nl = os.path.join(workspace, "nl/about.html")
if os.path.exists(path_about_nl):
    with open(path_about_nl, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    
    # 3.1 Remove Google Rating details card (NL version: "op Google")
    rating_regex_nl = r'<!-- Rating details -->\s*<div class="flex items-center gap-2 bg-white/5 rounded-2xl py-3 px-5 border border-white/5">.*?/5 op Google\s*</span>\s*</div>'
    content, count_r = re.subn(rating_regex_nl, '', content, flags=re.DOTALL)
    
    # 3.2 Remove Meet Our Champions Section
    content, count_c = re.subn(champions_regex, '', content, flags=re.DOTALL)
    
    # 3.3 Change grid layout
    content, count_g = re.subn(grid_regex, new_grid, content)
    
    # 3.4 Append Laurien & Artoush cards (with relative src `../images/`)
    laurien_card_nl = """

        <!-- Member 4 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Laurien" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="../images/laurien.png"/>
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]">Laurien</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider">Executive Assistant - Fast Elevate Media</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed">
              Laurien is de Executive Assistant bij Fast Elevate Media, verantwoordelijk voor het structureren van de dagelijkse operaties, het beheren van klantcommunicatie en het waarborgen van naadloze projectlogistiek. Met een sterke achtergrond in zakelijke administratie en evenementencoördinatie houdt zij productietijdlijnen op schema en zorgt zij voor duidelijke communicatie van de eerste boeking tot de uiteindelijke oplevering. Haar georganiseerde en detailgerichte aanpak zorgt ervoor dat ons team van creatieven en klantpartners efficiënt en effectief kunnen samenwerken aan elke productie.
            </p>
          </div>
        </div>

        <!-- Member 5 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Artoush" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="../images/artoush.png"/>
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]">Artoush</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider">Web & App Developer - Fast Elevate Media</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed">
              Artoush is Web- en App-ontwikkelaar bij Fast Elevate Media, gespecialiseerd in het bouwen van hoogwaardige, responsieve digitale interfaces en op maat gemaakte oplossingen voor mediadistributie. Door technische precisie te combineren met oog voor modern UI/UX-ontwerp, zorgt hij ervoor dat de visuele assets van onze klanten naadloos worden geïntegreerd in premium, snel ladende digitale omgevingen. Artoush richt zich op het ontwikkelen van schone, gestructureerde code die de afspeelkwaliteit van media, interactieve lay-outs en gebruikersbetrokkenheid op web- en mobiele platforms optimaliseert.
            </p>
          </div>
        </div>"""
        
    match = re.search(joshua_card_end, content, re.DOTALL)
    if match:
        content = content.replace(match.group(0), match.group(1) + laurien_card_nl + match.group(2))
        print("\nUpdated nl/about.html:")
        print(f"  Google rating card removed: {count_r}")
        print(f"  Champions section removed: {count_c}")
        print(f"  Grid layout updated: {count_g}")
        print("  Laurien and Artoush team cards added successfully!")
    else:
        print("WARNING: Could not append team members in nl/about.html")
        
    if content != original:
        with open(path_about_nl, "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved updates to nl/about.html")

print("\nAll updates executed!")
