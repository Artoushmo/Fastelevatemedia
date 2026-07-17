import os
import shutil

base_dir = "/Users/v/Desktop/Fastelevate 06-01"
images_dir = os.path.join(base_dir, "images")

# 1. Vervang Kores foto
dest_kores = os.path.join(images_dir, "kores-developer-fast-elevate-media.jpg")
src_kores = os.path.join(images_dir, "Kores.jpeg")

if os.path.exists(src_kores):
    shutil.copy2(src_kores, dest_kores)
    print("Kores foto succesvol overschreven.")
else:
    print(f"Kores.jpeg niet gevonden in {images_dir}")

# 2. HTML toevoeging voor Julian
julian_en = """        <!-- Member 6 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Julian" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="./images/Julian.jpg" data-vibe-field="image_5">
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]" data-vibe-field="subtitle_6">Julian</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider" data-vibe-field="text_11">Videographer - Fast Elevate Network</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed" data-vibe-field="text_12">
              Julian is a videographer with a passion for visual storytelling, specialising in cinematic edits, interviews and branded content. With a strong eye for detail and narrative, he transforms every project into a compelling story that connects with its audience. From capturing authentic interviews to crafting polished final edits, Julian focuses on creating videos that are both engaging and impactful.<br><br>As part of Fast Elevate Media, Julian collaborates on corporate productions, brand campaigns and commercial projects, delivering high-quality video content that combines creativity, professionalism and a story-driven approach.
            </p>
          </div>
        </div>"""

julian_nl = """        <!-- Member 6 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Julian" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="../images/Julian.jpg" data-vibe-field="image_5">
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]" data-vibe-field="subtitle_6">Julian</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider" data-vibe-field="text_11">Videograaf - Fast Elevate Network</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed" data-vibe-field="text_12">
              Julian is een videograaf met een passie voor visuele storytelling, gespecialiseerd in cinematografische montages, interviews en branded content. Met een scherp oog voor detail en narratief transformeert hij elk project in een meeslepend verhaal dat verbinding maakt met het publiek. Van het vastleggen van authentieke interviews tot het creëren van gepolijste eindmontages, Julian richt zich op het maken van video's die zowel boeiend als impactvol zijn.<br><br>Als onderdeel van Fast Elevate Media werkt Julian samen aan zakelijke producties, merkcampagnes en commerciële projecten, waarbij hij hoogwaardige videocontent levert die creativiteit, professionaliteit en een verhaalgestuurde aanpak combineert.
            </p>
          </div>
        </div>"""

# Aanpassen EN page
about_en_path = os.path.join(base_dir, "about.html")
with open(about_en_path, "r", encoding="utf-8") as f:
    about_en = f.read()

# We zoeken naar de sluiting van Member 5
target_en = """        <!-- Member 5 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Joshua" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="./images/SP9_20.jpg" data-vibe-field="image_4">
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]" data-vibe-field="subtitle_5">Joshua</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider" data-vibe-field="text_9">Photo/Videographer - Fast Elevate Media Network</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed" data-vibe-field="text_10">
              Joshua is an Amsterdam-based photographer and videographer specialising in corporate events, conferences, brand imagery and professional headshots. Known for his dynamic shooting style and ability to capture authentic moments, he focuses on creating visual content that reflects the energy and professionalism of each production.<br><br>Joshua regularly collaborates with Fast Elevate Media on corporate productions across the Netherlands, bringing a focused and professional approach to capturing key moments at every event.
            </p>
          </div>
        </div>"""

if target_en in about_en:
    about_en = about_en.replace(target_en, target_en + "\n\n" + julian_en)
    with open(about_en_path, "w", encoding="utf-8") as f:
        f.write(about_en)
    print("Julian succesvol toegevoegd aan about.html.")
else:
    print("Fout: Kon Member 5 sectie niet vinden in about.html.")

# Aanpassen NL page
about_nl_path = os.path.join(base_dir, "nl/about.html")
with open(about_nl_path, "r", encoding="utf-8") as f:
    about_nl = f.read()

target_nl = """        <!-- Member 5 -->
        <div class="flex flex-col bg-gray-50 border border-gray-100 rounded-2xl overflow-hidden p-6 gap-6 shadow-sm">
          <img alt="Joshua" class="w-full aspect-[4/3] object-cover rounded-xl shadow-md" src="../images/SP9_20.jpg" data-vibe-field="image_4">
          <div class="space-y-1">
            <h4 class="text-lg font-bold text-[#121111]" data-vibe-field="subtitle_5">Joshua</h4>
            <p class="text-xs text-primary font-semibold uppercase tracking-wider" data-vibe-field="text_9">Foto-/Videograaf - Fast Elevate Media Netwerk</p>
          </div>
          <div class="border-t border-gray-200/60 pt-4">
            <p class="text-sm text-gray-600 leading-relaxed" data-vibe-field="text_10">
              Joshua is een in Amsterdam gevestigde fotograaf en videograaf die gespecialiseerd is in zakelijke evenementen, congressen, merkimago en professionele portretfoto's. Bekend om zijn dynamische opnamestijl en het vermogen om authentieke momenten vast te leggen, richt hij zich op het creëren van visuele content die de energie en professionaliteit van elke productie weerspiegelt.<br><br>Joshua werkt regelmatig samen met Fast Elevate Media aan zakelijke producties in heel Nederland, waarbij hij een gerichte en professionele aanpak brengt om de belangrijkste momenten van elk evenement vast te leggen.
            </p>
          </div>
        </div>"""

if target_nl in about_nl:
    about_nl = about_nl.replace(target_nl, target_nl + "\n\n" + julian_nl)
    with open(about_nl_path, "w", encoding="utf-8") as f:
        f.write(about_nl)
    print("Julian succesvol toegevoegd aan nl/about.html.")
else:
    print("Fout: Kon Member 5 sectie niet vinden in nl/about.html.")
