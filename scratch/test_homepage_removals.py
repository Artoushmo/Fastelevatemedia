import re

workspace = "/Users/v/Desktop/Fastelevate 06-01"

with open(f"{workspace}/nl/index.html", "r", encoding="utf-8") as f:
    content = f.read()

original_len = len(content)

# 1. Logo slider bottom divider removal
content, count1 = re.subn(
    r'<!-- Bottom Shape Divider \(transitions from white to Testimonials dark bg #121111\) -->\s*<div class="absolute bottom-0 left-0 w-full overflow-hidden leading-\[0\] z-20">\s*<svg class="relative block w-full h-\[150px\]".*?</svg>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

# 2. Testimonials section removal
content, count2 = re.subn(
    r'<!-- 7\. Testimonials Slider Section -->\s*<section class="py-32 bg-\[#1c1b1b\] px-6 overflow-hidden">.*?</section>',
    '',
    content,
    flags=re.DOTALL
)

# 3. Content section top divider removal
content, count3 = re.subn(
    r'<!-- Top Shape Divider \(transitions from Testimonials dark bg #121111\) -->\s*<div class="absolute top-0 left-0 w-full overflow-hidden leading-\[0\] z-20 transform -translate-y-\[1px\]">\s*<svg class="relative block w-full h-\[150px\]".*?</svg>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

# 4. Results section removal
content, count4 = re.subn(
    r'<!-- 9\. Results Section -->\s*<section class="py-32 relative bg-\[#4C72A9\] text-white overflow-hidden">.*?</section>',
    '',
    content,
    flags=re.DOTALL
)

# 5. Counter JS removal
content, count5 = re.subn(
    r'// Counter Animation.*?ScrollTrigger\.create\(\{.*?onEnter:\s*\(\)\s*=>\s*updateCount\(\)\s*\}\);\s*\}\);',
    '',
    content,
    flags=re.DOTALL
)

# 6. Testimonial track JS removal
content, count6 = re.subn(
    r'// Testimonial Track Autoplay & Drag Simulation.*?translateX\(-\$\{offset\}%\).*?\}, 5000\);',
    '',
    content,
    flags=re.DOTALL
)

print(f"Results of removal regex checks for nl/index.html:")
print(f"1. Logo slider divider removed: {count1}")
print(f"2. Testimonials section removed: {count2}")
print(f"3. Content section divider removed: {count3}")
print(f"4. Results section removed: {count4}")
print(f"5. Counter JS removed: {count5}")
print(f"6. Testimonials JS removed: {count6}")
print(f"Old size: {original_len}, New size: {len(content)}")
