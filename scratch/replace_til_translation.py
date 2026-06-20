import os

workspace_nl = "/Users/v/Desktop/Fastelevate 06-01/nl"

replacements = {
    # Project translations
    "Til uw project naar een hoger niveau": "Breng uw project naar een hoger niveau",
    "til uw project naar een hoger niveau": "breng uw project naar een hoger niveau",
    "Til Uw Project Naar Een Hoger Niveau": "Breng uw project naar een hoger niveau",
    "Til uw project naar een hoger niveau": "Breng uw project naar een hoger niveau",
    
    # Event translations
    "Til Je Evenement naar een Hoger Niveau": "Breng uw evenement naar een hoger niveau",
    "Til Uw Evenement naar een Hoger Niveau": "Breng uw evenement naar een hoger niveau",
    "Til uw Evenement naar een Hoger Niveau": "Breng uw evenement naar een hoger niveau",
    "Til Je Evenement naar een hoger niveau": "Breng uw evenement naar een hoger niveau",
    "Til Uw Evenement naar een hoger niveau": "Breng uw evenement naar een hoger niveau",
    "Til Je evenement naar een Hoger Niveau": "Breng uw evenement naar een hoger niveau",
    "Til Je evenement naar een hoger niveau": "Breng uw evenement naar een hoger niveau",
    "Til je evenement naar een hoger niveau": "Breng uw evenement naar een hoger niveau",
    "Til Je Evenement Naar Een Hoger Niveau": "Breng uw evenement naar een hoger niveau",
    "Til Uw Evenement Naar Een Hoger Niveau": "Breng uw evenement naar een hoger niveau",
    "Til Je Evenement": "Breng uw evenement naar een hoger niveau", # Fallback for partial links
    "Til Uw Evenement": "Breng uw evenement naar een hoger niveau"
}

# Scan files and do replacement
for root, dirs, files in os.walk(workspace_nl):
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            modified = False
            # Perform direct string replacements
            for old, new in replacements.items():
                if old in content:
                    content = content.replace(old, new)
                    modified = True
                    print(f"Replaced '{old}' with '{new}' in {f}")
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)

print("Bulk replacement complete.")
