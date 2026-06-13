import os
import re

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

video_pages = [
    "corporate-video-production.html",
    "corporate-interviews-testimonials.html",
    "drone-video-aerial-photography.html"
]

def update_video_tags(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # We want to find each <video class="gallery-video ... > ... </video> block
    # Using re.DOTALL to match newlines
    pattern = re.compile(r'(<video class="gallery-video[^>]*>)(.*?)(</video>)', re.DOTALL)

    def replace_video_block(match):
        video_open_tag = match.group(1)
        inner_content = match.group(2)
        video_close_tag = match.group(3)

        # 1. Update preload="metadata" to preload="auto"
        if 'preload="metadata"' in video_open_tag:
            video_open_tag = video_open_tag.replace('preload="metadata"', 'preload="auto"')
        elif 'preload' not in video_open_tag:
            # If preload is not specified, add preload="auto" before the closing bracket
            video_open_tag = video_open_tag[:-1] + ' preload="auto">'

        # 2. Update <source src="..." to include #t=0.1
        # Match src="url"
        src_pattern = re.compile(r'src="([^"]+)"')
        def replace_source_src(src_match):
            url = src_match.group(1)
            if not url.endswith('#t=0.1') and not url.endswith('#t=0.001'):
                # Avoid appending #t=0.1 if it's already there or if there is another fragment
                if '#' in url:
                    return f'src="{url}"'
                return f'src="{url}#t=0.1"'
            return src_match.group(0)

        inner_content = src_pattern.sub(replace_source_src, inner_content)

        return video_open_tag + inner_content + video_close_tag

    new_content = pattern.sub(replace_video_block, content)

    if new_content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
        return True
    return False

def main():
    count = 0
    # Process files in root
    for entry in os.listdir(base_dir):
        if entry in video_pages:
            filepath = os.path.join(base_dir, entry)
            if update_video_tags(filepath):
                count += 1
                
    # Process files in nl/
    nl_dir = os.path.join(base_dir, "nl")
    if os.path.exists(nl_dir):
        for entry in os.listdir(nl_dir):
            if entry in video_pages:
                filepath = os.path.join(nl_dir, entry)
                if update_video_tags(filepath):
                    count += 1

    print(f"Video updates completed. Total files modified: {count}")

if __name__ == "__main__":
    main()
