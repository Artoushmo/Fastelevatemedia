import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

# English file test
with open(f"{workspace}/about.html", "r", encoding="utf-8") as f:
    content_en = f.read()

print("--- Testing about.html ---")
# 1. Rating details block removal
# Using specific ending with "on Google"
pattern_rating_en = r'<!-- Rating details -->\s*<div class="flex items-center gap-2 bg-white/5 rounded-2xl py-3 px-5 border border-white/5">.*?on Google\s*</strong>/5 on Google\s*</span>\s*</div>'
# Let's check exactly what the text in about.html is:
# Rated <strong class="text-white font-bold">4.9</strong>/5 on Google
# So it has `Rated <strong class="text-white font-bold">4.9</strong>/5 on Google\s*</span>\s*</div>`
# Let's write a simple match that stops at `on Google\s*</span>\s*</div>` or `op Google\s*</span>\s*</div>`.
rating_en_regex = r'<!-- Rating details -->\s*<div class="flex items-center gap-2 bg-white/5 rounded-2xl py-3 px-5 border border-white/5">.*?/5 on Google\s*</span>\s*</div>'
content_en, count1 = re.subn(rating_en_regex, '', content_en, flags=re.DOTALL)
print(f"1. Rating details removed: {count1}")

# 2. Champions section removal
champions_regex = r'<!-- 3\.5\. Meet Our Champions Section -->\s*<section class="py-24 bg-\[#121111\] text-white px-6 md:px-12 lg:px-24">.*?</section>'
content_en, count2 = re.subn(champions_regex, '', content_en, flags=re.DOTALL)
print(f"2. Champions section removed: {count2}")

# 3. Grid columns change
grid_regex = r'<!-- Team Members Grid -->\s*<div class="grid grid-cols-1 md:grid-cols-3 gap-8">'
content_en, count3 = re.subn(grid_regex, '<!-- Team Members Grid -->\n      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">', content_en)
print(f"3. Grid cols changed: {count3}")

# 4. Check if we can find Joshua card end to append Laurien and Artoush
# Joshua is Member 3. Let's find the closing tag of Joshua card.
# The card for Joshua is:
#         <!-- Member 3 -->
#         <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
#           ...
#         </div>
# Immediately followed by `</div>` (which ends the Team Members Grid).
# We can find this by matching:
# `<!-- Member 3 -->.*?</div>\s*</div>\s*</div>\s*</section>`
# Wait, let's write a specific pattern for the end of Joshua card.
joshua_card_end = r'(<!-- Member 3 -->.*?</div>\s*</div>)\s*(</div>\s*</div>\s*</section>)'
# Let's check if this matches.
# Group 1 is Member 3 block up to the card closing </div>.
# Group 2 is the grid closing </div>, container closing </div>, and section closing </section>.
# If we replace this with:
# Group 1 + Laurien and Artoush + Group 2, it will insert them perfectly!
# Let's test this in Python.

match_joshua = re.search(joshua_card_end, content_en, re.DOTALL)
if match_joshua:
    print("4. Joshua card end matched!")
    # Let's print the match length and some preview
    print(f"Group 1 length: {len(match_joshua.group(1))}")
    print(f"Group 2: {match_joshua.group(2)}")
else:
    print("4. Joshua card end NOT matched!")

print("\n--- Testing nl/about.html ---")
with open(f"{workspace}/nl/about.html", "r", encoding="utf-8") as f:
    content_nl = f.read()

rating_nl_regex = r'<!-- Rating details -->\s*<div class="flex items-center gap-2 bg-white/5 rounded-2xl py-3 px-5 border border-white/5">.*?/5 op Google\s*</span>\s*</div>'
content_nl, count1_nl = re.subn(rating_nl_regex, '', content_nl, flags=re.DOTALL)
print(f"1. Rating details removed: {count1_nl}")

content_nl, count2_nl = re.subn(champions_regex, '', content_nl, flags=re.DOTALL)
print(f"2. Champions section removed: {count2_nl}")

content_nl, count3_nl = re.subn(grid_regex, '<!-- Team Members Grid -->\n      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">', content_nl)
print(f"3. Grid cols changed: {count3_nl}")

match_joshua_nl = re.search(joshua_card_end, content_nl, re.DOTALL)
if match_joshua_nl:
    print("4. Joshua card end matched!")
else:
    print("4. Joshua card end NOT matched!")
