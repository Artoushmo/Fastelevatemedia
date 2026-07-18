import json

with open("content.json", "r", encoding="utf-8") as f:
    d = json.load(f)

# The section we need to fix
media = d.get("nl", {}).get("home", {}).get("Mediaoplossingen", {})

# Keys to remove
keys_to_remove = [
    "auto_text_div_1_a_0",
    "auto_text_div_1_a_0_div_0_div_0_div_0_span_0",
    "auto_text_div_1_a_1",
    "auto_text_div_1_a_1_div_0_div_0_div_0_span_0",
    "auto_text_div_1_a_2",
    "auto_text_div_1_a_2_div_0_div_0_div_0_span_0",
    "auto_text_div_1_a_3",
    "auto_text_div_1_a_3_div_0_div_0_div_0_span_0",
    "auto_text_div_1_a_4",
    "auto_text_div_1_a_4_div_0_div_0_div_0_span_0",
    "auto_text_div_1_a_5",
    "auto_text_div_1_a_5_div_0_div_0_div_0_span_0",
]

removed_count = 0
for k in keys_to_remove:
    if k in media:
        del media[k]
        removed_count += 1

if removed_count > 0:
    with open("content.json", "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"Removed {removed_count} problematic auto_text keys from Mediaoplossingen.")
else:
    print("No keys found to remove.")
