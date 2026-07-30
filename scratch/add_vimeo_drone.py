import urllib.request
import json
import re
import os

urls = [
    "https://vimeo.com/1214376229?share=copy&fl=sv&fe=ci",
    "https://vimeo.com/1214376261?fl=tl&fe=ec",
    "https://vimeo.com/1214376263?share=copy&fl=sv&fe=ci",
    "https://vimeo.com/1214376227?share=copy&fl=sv&fe=ci",
    "https://vimeo.com/1214376228?share=copy&fl=sv&fe=ci",
    "https://vimeo.com/1214376232?share=copy&fl=sv&fe=ci"
]

html_to_append = ""

for url in urls:
    api_url = f"https://vimeo.com/api/oembed.json?url={urllib.parse.quote(url)}"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            title = data.get("title", "Drone Video").replace('"', '&quot;')
            thumbnail = data.get("thumbnail_url", "")
            # We want a high-res thumbnail. Vimeo provides smaller ones by default, we can strip the width modifier.
            # e.g., https://i.vimeocdn.com/video/1234_295x166
            thumbnail = re.sub(r'_\d+x\d+', '', thumbnail)
            
            clean_url = url.split("?")[0]
            
            html_to_append += f"""
        <div class="gallery-item relative group overflow-hidden rounded-2xl border-4 border-white shadow-md cursor-pointer aspect-[3/2]" data-video-url="{clean_url}" data-caption="{title}">
          <img class="w-full h-full object-cover" src="{thumbnail}" alt="{title}">
          <div class="absolute inset-0 bg-black/30 group-hover:bg-black/40 transition-colors flex items-center justify-center z-10">
            <span class="w-14 h-14 rounded-full bg-white/20 text-white flex items-center justify-center backdrop-blur-sm group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6 fill-current translate-x-[2px]" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M8 5v14l11-7z"></path>
              </svg>
            </span>
          </div>
        </div>
"""
    except Exception as e:
        print(f"Error fetching {url}: {e}")

files_to_update = [
    "/Users/v/Desktop/Fastelevate 06-01/drone-video-aerial-photography.html",
    "/Users/v/Desktop/Fastelevate 06-01/nl/drone-video-aerial-photography.html"
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We need to find the end of the gallery-grid div.
    # The grid has id="gallery-grid".
    # Let's find `<div class="grid ... id="gallery-grid">` and then append our HTML before its closing tag.
    # A simple way since we know the structure:
    # Look for the section after it: `<!-- 4. Why Corporate Clients Choose Us -->`
    # The structure is:
    #       </div>
    #     </div>
    #   </section>
    # 
    #   <!-- 4. Why Corporate Clients Choose Us -->
    
    parts = content.split('<!-- 4. Why')
    if len(parts) == 2:
        # We need to insert right before `      </div>\n    </div>\n  </section>`
        # Let's find `      </div>\n    </div>\n  </section>` at the end of parts[0]
        match = re.search(r'(\s*</div>\s*</div>\s*</section>\s*)$', parts[0])
        if match:
            new_part0 = parts[0][:match.start()] + html_to_append + match.group(1)
            new_content = new_part0 + '<!-- 4. Why' + parts[1]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Could not find closing tags in {filepath}")
    else:
        print(f"Could not find section 4 marker in {filepath}")
