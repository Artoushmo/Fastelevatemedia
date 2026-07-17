import re

files = [
    "/Users/v/Desktop/Fastelevate 06-01/pricing.html",
    "/Users/v/Desktop/Fastelevate 06-01/nl/pricing.html"
]

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Pattern 1: standard packages - lightning note inside features div (4 spaces indent for closing div stack)
    # Move the lightning note OUT of the inner content div, and make it a direct child of the card flex container
    # Also change text-xs to text-sm

    # Find all occurrences of the lightning section that is inside the features space-y-4 div
    # and move it outside the two closing divs (</div></div>) to be a direct card child

    # The pattern to find:
    # (whitespace)<div class="mt-6 pt-4 border-t border-white/5 flex items-start gap-2.5 text-xs text-[#f3bf51]">
    #   <span>⚡ ...</span>
    # </div>
    # </div>   <- closes space-y-4
    # </div>   <- closes inner content div

    # Standard single-line lightning note inside space-y-4 (inside inner div)
    pattern_standard = re.compile(
        r'([ \t]+)<div class="mt-6 pt-4 border-t border-white/5 flex items-start gap-2\.5 text-xs text-\[#f3bf51\]">\n'
        r'([ \t]+)<span>(⚡[^<]*)</span>\n'
        r'([ \t]+)</div>\n'
        r'([ \t]+)</div>\n'   # closes space-y-4
        r'([ \t]+)</div>\n'   # closes inner content <div>
        r'([ \t]+)</div>\n'   # closes .pricing-card
    )

    def replace_standard(m):
        card_indent = m.group(7)  # indent of closing pricing-card div
        inner_indent = m.group(1)  # indent of lightning div (2 levels inside)
        # The lightning note goes at the level of inner content div (one level inside card)
        lightning_indent = card_indent + "  "
        text = m.group(3)
        return (
            f"{m.group(5)}</div>\n"   # close space-y-4
            f"{m.group(6)}</div>\n"   # close inner content div
            f"{lightning_indent}<div class=\"mt-6 pt-4 border-t border-white/5 flex items-start gap-2.5 text-sm text-[#f3bf51]\">\n"
            f"{lightning_indent}  <span>{text}</span>\n"
            f"{lightning_indent}</div>\n"
            f"{card_indent}</div>\n"  # close pricing-card
        )

    content_new = pattern_standard.sub(replace_standard, content)

    # Pattern 2: Elevate Your Event style - has flex-col gap-3 wrapper AND extra <p> tag
    # <div class="mt-6 pt-4 border-t border-white/5 flex flex-col gap-3">
    #   <div class="flex items-start gap-2.5 text-xs">
    #     <span class="...">⚡</span>
    #     <span class="...">text</span>
    #   </div>
    #   <p class="...">Let's build...</p>
    # </div>
    pattern_elevate = re.compile(
        r'([ \t]+)<div class="mt-6 pt-4 border-t border-white/5 flex flex-col gap-3">\n'
        r'([ \t]+)<div class="flex items-start gap-2\.5 text-xs">\n'
        r'([ \t]+)<span class="text-\[#f3bf51\] text-lg mr-1">⚡</span>\n'
        r'([ \t]+)<span class="text-\[#f3bf51\]">([^<]*)</span>\n'
        r'([ \t]+)</div>\n'
        r'([ \t]+)(<p class="[^"]*" data-vibe-field="text_8">[^<]*</p>)\n'
        r'([ \t]+)</div>\n'
        r'([ \t]+)</div>\n'   # closes inner content div
        r'([ \t]+)</div>\n'   # closes .pricing-card
    )

    def replace_elevate(m):
        card_indent = m.group(11)
        lightning_indent = card_indent + "  "
        text = m.group(5)
        p_tag = m.group(8)
        return (
            f"{m.group(9)}</div>\n"   # close inner content div
            f"{lightning_indent}<div class=\"mt-6 pt-4 border-t border-white/5 flex flex-col gap-3\">\n"
            f"{lightning_indent}  <div class=\"flex items-start gap-2.5 text-sm text-[#f3bf51]\">\n"
            f"{lightning_indent}    <span>⚡ {text}</span>\n"
            f"{lightning_indent}  </div>\n"
            f"{lightning_indent}  {p_tag}\n"
            f"{lightning_indent}</div>\n"
            f"{card_indent}</div>\n"
        )

    content_new = pattern_elevate.sub(replace_elevate, content_new)

    if content_new != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content_new)
        print(f"✅ Bijgewerkt: {path}")
    else:
        print(f"⚠️  Geen wijzigingen in: {path} — pattern matcht mogelijk niet")
