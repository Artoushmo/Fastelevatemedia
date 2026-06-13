import os
from html.parser import HTMLParser

class HTMLSanityChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
        self.links = []
        self.images = []
        self.videos = []

    def handle_starttag(self, tag, attrs):
        self_closing = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']
        attrs_dict = dict(attrs)
        if tag not in self_closing:
            self.tags.append(tag)
        
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(attrs_dict['href'])
        if tag == 'img' and 'src' in attrs_dict:
            self.images.append(attrs_dict['src'])
        if tag == 'source' and 'src' in attrs_dict:
            self.videos.append(attrs_dict['src'])
        if 'data-video-url' in attrs_dict:
            self.videos.append(attrs_dict['data-video-url'])

    def handle_endtag(self, tag):
        self_closing = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']
        if tag in self_closing:
            return
        if not self.tags:
            self.errors.append(f"Unexpected closing tag: </{tag}>")
            return
        last_open = self.tags.pop()
        if last_open != tag:
            self.errors.append(f"Mismatched closing tag: </{tag}>. Expected </{last_open}>.")

    def check_file(self, filepath):
        self.tags = []
        self.errors = []
        self.links = []
        self.images = []
        self.videos = []
        
        if not os.path.exists(filepath):
            print(f"Error: {filepath} does not exist.")
            return False
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        try:
            self.feed(html_content)
        except Exception as e:
            self.errors.append(f"Parser error: {str(e)}")
        
        if self.tags:
            self.errors.append(f"Unclosed tags at end of file: {self.tags}")
            
        basename = os.path.basename(filepath)
        dirname = os.path.basename(os.path.dirname(filepath))
        display_name = f"{dirname}/{basename}" if dirname != "Fastelevate 06-01" else basename
        
        if self.errors:
            print(f"File: {display_name} -> FAILED")
            for err in self.errors[:5]:
                print(f"  - {err}")
            if len(self.errors) > 5:
                print(f"  - ... and {len(self.errors) - 5} more errors.")
            return False
            
        # Verify local links
        dead_links = 0
        for link in set(self.links):
            if (link.startswith("./") or link.endswith(".html")) and not link.startswith("#"):
                clean_link = link.split("#")[0]
                local_path = os.path.join(os.path.dirname(filepath), clean_link)
                if not os.path.exists(local_path):
                    print(f"  - WARNING: Dead local link: {link} (path: {local_path})")
                    dead_links += 1
        
        print(f"File: {display_name} -> PASSED (Checked {len(self.links)} links, {dead_links} dead warnings)")
        return True

checker = HTMLSanityChecker()
workspace = "/Users/v/Desktop/Fastelevate 06-01"

html_files = []
for root, dirs, files in os.walk(workspace):
    for f in files:
        if f.endswith(".html") and not "node_modules" in root:
            html_files.append(os.path.join(root, f))

print(f"Running sanity check on {len(html_files)} HTML files...")
all_passed = True
for f in sorted(html_files):
    if not checker.check_file(f):
        all_passed = False

if all_passed:
    print("\nAll HTML files are structurally sound and verified!")
else:
    print("\nSome HTML files have validation issues!")
