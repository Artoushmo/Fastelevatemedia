import os

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

# 1. cookies.html (English)
cookies_en_filepath = os.path.join(base_dir, "cookies.html")
cookies_en_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Cookie Policy</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Last updated: June 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Introduction</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            This Cookie Policy explains how Fast Elevate Media ("we", "us", or "our") uses cookies and similar technologies when you visit our website. This policy should be read together with our <a href="./privacy.html" class="text-primary underline hover:text-primary/80 transition-colors">Privacy Policy</a>. By continuing to use our website, you may be asked to provide consent for certain categories of cookies through our cookie consent banner.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. What Are Cookies?</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Cookies are small text files stored on your device when you visit a website. Cookies help websites function properly, improve user experience, remember preferences, and provide information about website performance and visitor interactions. Cookies may be placed by Fast Elevate Media or by third-party service providers.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. Types of Cookies We Use</h3>
          
          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Strictly Necessary Cookies</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            These cookies are required for the operation and security of our website. They enable core functionality such as:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Website security</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Cookie preference storage</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Form functionality</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Session management</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Basic website performance</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">These cookies cannot be disabled through the cookie banner.</p>

          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Analytics Cookies</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Analytics cookies help us understand how visitors interact with our website. We use this information to improve content, user experience, and website performance. Examples may include:
          </p>
          <ul class="space-y-3 mb-4">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Analytics 4</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Analytics cookies may collect information such as:</p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Pages visited &amp; time spent on pages</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Navigation behaviour, device type &amp; browser type</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Approximate geographic location</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">Analytics cookies are only activated after your consent has been provided.</p>

          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Advertising Cookies</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Advertising cookies help us measure the effectiveness of advertising campaigns and understand how visitors interact with our marketing activities. Examples may include:
          </p>
          <ul class="space-y-3 mb-4">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Ads Conversion Tracking</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">These cookies may collect information relating to:</p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Advertisement interactions &amp; conversion events</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Campaign performance &amp; website actions following ad clicks</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">Advertising cookies are only activated after your consent has been provided.</p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Google Tag Manager</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media may use Google Tag Manager. Google Tag Manager itself does not typically store personal data or place cookies. Instead, it is used to manage and deploy scripts such as Google Analytics and Google Ads Conversion Tracking. Any technologies deployed through Google Tag Manager remain subject to the consent preferences selected by visitors.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Consent Management</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            When you first visit our website, you will be presented with a cookie consent banner. You may choose to: accept all cookies, reject non-essential cookies, or customize your cookie preferences.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Your choices will be stored and respected in accordance with applicable privacy laws.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            You may modify your preferences at any time by clicking the button below or using the cookie settings widget on our website.
            <br/><br/>
            <button onclick="if(typeof openCookieSettings === 'function') { openCookieSettings(); } else { alert('Cookie Settings are loading or not available on this page.'); }" class="bg-primary hover:bg-primary/95 text-white font-bold text-xs uppercase tracking-wider py-3 px-6 rounded-full transition-all inline-block shadow">
              Modify Cookie Settings
            </button>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Managing Cookies</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Most web browsers allow you to view stored cookies, delete cookies, block cookies, or configure cookie preferences. Please note that disabling certain cookies may affect website functionality and user experience. Browser instructions can typically be found through:
          </p>
          <ul class="space-y-2 mb-8">
            <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Google Chrome</a></li>
            <li><a href="https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Mozilla Firefox</a></li>
            <li><a href="https://support.apple.com/guide/safari/sfri11471/mac" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Safari</a></li>
            <li><a href="https://support.microsoft.com/microsoft-edge/delete-and-manage-cookies-168dab11-0753-043d-7c16-ede5947fc64d" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Microsoft Edge</a></li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Third-Party Services</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media may use third-party services that place cookies or similar technologies on our website. These providers may include: Google Analytics, Google Ads, Google Tag Manager, website hosting providers, or cookie consent providers. These third parties are responsible for their own privacy and cookie practices. We encourage visitors to review the privacy policies of these providers.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. International Data Transfers</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Some third-party service providers may process information outside the European Economic Area (EEA). Where applicable, appropriate safeguards are implemented in accordance with GDPR requirements.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Changes to This Cookie Policy</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media may update this Cookie Policy from time to time. Any changes will be published on this page together with the updated revision date.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">10. Contact Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">For questions regarding this Cookie Policy, please contact:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

# Write English cookies
with open(cookies_en_filepath, "r", encoding="utf-8") as f:
    en_content = f.read()

start_tag = '<!-- LEFT: Cookie Policy Content -->'
end_tag = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag in en_content and end_tag in en_content:
    start_idx = en_content.find(start_tag) + len(start_tag)
    end_idx = en_content.find(end_tag)
    new_inner_en = "\n        <div class=\"flex-1 min-w-0\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + cookies_en_replacement + "\n        </div>\n        "
    en_content = en_content[:start_idx] + new_inner_en + en_content[end_idx:]
    with open(cookies_en_filepath, "w", encoding="utf-8") as f:
        f.write(en_content)
    print("Overwrote cookies.html successfully.")

# 2. nl/cookies.html (Dutch)
cookies_nl_filepath = os.path.join(base_dir, "nl/cookies.html")
cookies_nl_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Cookiebeleid</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Laatst bijgewerkt: juni 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Inleiding</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            Dit Cookiebeleid legt uit hoe Fast Elevate Media ("we", "ons" of "onze") cookies en vergelijkbare technologieën gebruikt wanneer u onze website bezoekt. Dit beleid moet in samenhang met ons <a href="./privacy.html" class="text-primary underline hover:text-primary/80 transition-colors">Privacybeleid</a> worden gelezen. Door onze website te blijven gebruiken, kan u worden gevraagd om toestemming te geven voor bepaalde categorieën cookies via onze cookie-toestemmingsbanner.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. Wat zijn cookies?</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Cookies zijn kleine tekstbestanden die op uw apparaat worden opgeslagen wanneer u een website bezoekt. Cookies helpen websites om correct te functioneren, de gebruikerservaring te verbeteren, voorkeuren te onthouden en informatie te verstrekken over websiteprestaties en bezoekersinteracties. Cookies kunnen worden geplaatst door Fast Elevate Media of door externe serviceproviders.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. Soorten cookies die we gebruiken</h3>
          
          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Strikt Noodzakelijke Cookies</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Deze cookies zijn vereist voor de werking en veiligheid van onze website. Ze maken kernfunctionaliteiten mogelijk, zoals:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Websitebeveiliging</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Opslag van cookievoorkeuren</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Functionaliteit van formulieren</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Sessiebeheer</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Basisprestaties van de website</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">Deze cookies kunnen niet worden uitgeschakeld via de cookiebanner.</p>

          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Analytics Cookies</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Analytics cookies helpen ons te begrijpen hoe bezoekers omgaan met onze website. We gebruiken deze informatie om de inhoud, de gebruikerservaring en de prestaties van de website te verbeteren. Voorbeelden zijn:
          </p>
          <ul class="space-y-3 mb-4">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Analytics 4</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Analytics cookies kunnen informatie verzamelen zoals:</p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Bezochte pagina's &amp; tijd doorgebracht op pagina's</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Navigatiegedrag, apparaattype &amp; browsertype</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Geschatte geografische locatie</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">Analytics cookies worden pas geactiveerd nadat u toestemming hebt gegeven.</p>

          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Advertising Cookies</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Advertising cookies helpen ons de effectiviteit van advertentiecampagnes te meten en te begrijpen hoe bezoekers omgaan met onze marketingactiviteiten. Voorbeelden zijn:
          </p>
          <ul class="space-y-3 mb-4">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Ads Conversion Tracking</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Deze cookies kunnen informatie verzamelen met betrekking tot:</p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Interacties met advertenties &amp; conversie-gebeurtenissen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Campagneprestaties &amp; acties op de website na klikken op advertenties</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">Advertising cookies worden pas geactiveerd nadat u toestemming hebt gegeven.</p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Google Tag Manager</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media kan gebruikmaken van Google Tag Manager. Google Tag Manager zelf slaat doorgaans geen persoonlijke gegevens op en plaatst geen cookies. In plaats daarvan wordt het gebruikt om scripts zoals Google Analytics en Google Ads Conversion Tracking te beheren en te implementeren. Alle technologieën die via Google Tag Manager worden geïmplementeerd, blijven onderworpen aan de cookie-instellingen die door bezoekers zijn geselecteerd.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Toestemmingsbeheer</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Wanneer u onze website voor het eerst bezoekt, krijgt u een cookie-toestemmingsbanner te zien. U kunt kiezen om: alle cookies te accepteren, niet-essentiële cookies te weigeren of uw cookievoorkeuren aan te passen.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Uw keuzes worden opgeslagen en gerespecteerd in overeenstemming met de toepasselijke privacywetgeving.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            U kunt uw voorkeuren op elk moment wijzigen door op de onderstaande knop te klikken of de cookie-instellingen widget op onze website te openen.
            <br/><br/>
            <button onclick="if(typeof openCookieSettings === 'function') { openCookieSettings(); } else { alert('Cookie-instellingen worden geladen of zijn niet beschikbaar op deze pagina.'); }" class="bg-primary hover:bg-primary/95 text-white font-bold text-xs uppercase tracking-wider py-3 px-6 rounded-full transition-all inline-block shadow">
              Cookie-instellingen aanpassen
            </button>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Cookies beheren</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            De meeste webbrowsers staan u toe om opgeslagen cookies te bekijken, cookies te verwijderen, cookies te blokkeren of cookievoorkeuren te configureren. Houd er rekening mee dat het uitschakelen van bepaalde cookies invloed kan hebben op de functionaliteit en gebruikerservaring van de website. Browser-instructies zijn doorgaans te vinden via:
          </p>
          <ul class="space-y-2 mb-8">
            <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Google Chrome</a></li>
            <li><a href="https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Mozilla Firefox</a></li>
            <li><a href="https://support.apple.com/guide/safari/sfri11471/mac" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Safari</a></li>
            <li><a href="https://support.microsoft.com/microsoft-edge/delete-and-manage-cookies-168dab11-0753-043d-7c16-ede5947fc64d" target="_blank" class="text-primary underline hover:text-primary/80 transition-colors">Microsoft Edge</a></li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Diensten van derden</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media kan gebruikmaken van diensten van derden die cookies of soortgelijke technologieën op onze website plaatsen. Deze providers kunnen zijn: Google Analytics, Google Ads, Google Tag Manager, website-hostingproviders of aanbieders van cookie-toestemming. Deze derden zijn zelf verantwoordelijk voor hun eigen privacy- en cookiebeleid. We moedigen bezoekers aan om het privacybeleid van deze aanbieders te bekijken.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. Internationale gegevensoverdrachten</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Sommige externe serviceproviders kunnen informatie buiten de Europese Economische Ruimte (EER) verwerken. Waar van toepassing worden passende waarborgen geïmplementeerd in overeenstemming met de AVG-vereisten.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Wijzigingen in dit Cookiebeleid</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media kan dit Cookiebeleid van tijd tot tijd bijwerken. Eventuele wijzigingen worden op deze pagina gepubliceerd samen met de bijgewerkte revisiedatum.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">10. Contactgegevens</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Voor vragen over dit Cookiebeleid kunt u contact opnemen met:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Amsterdam, Nederland<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

# Write Dutch cookies
with open(cookies_nl_filepath, "r", encoding="utf-8") as f:
    nl_content = f.read()

start_tag_nl = '<!-- LEFT: Cookie Policy Content -->'
end_tag_nl = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag_nl in nl_content and end_tag_nl in nl_content:
    start_idx_nl = nl_content.find(start_tag_nl) + len(start_tag_nl)
    end_idx_nl = nl_content.find(end_tag_nl)
    new_inner_nl = "\n        <div class=\"flex-1 min-w-0\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + cookies_nl_replacement + "\n        </div>\n        "
    nl_content = nl_content[:start_idx_nl] + new_inner_nl + nl_content[end_idx_nl:]
    with open(cookies_nl_filepath, "w", encoding="utf-8") as f:
        f.write(nl_content)
    print("Overwrote nl/cookies.html successfully.")
