import os, re

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: bullet list item
# ─────────────────────────────────────────────────────────────────────────────
def li(text):
    return f"""            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">{text}</p>
            </li>"""

def ul(items):
    return '          <ul class="space-y-3 mb-8">\n' + "\n".join(li(i) for i in items) + "\n          </ul>"

def section(num, title, *body_parts):
    parts = [f'          <hr class="border-gray-200 my-8"/>',
             f'          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">{num}. {title}</h3>']
    for p in body_parts:
        parts.append(p)
    return "\n".join(parts)

def para(text, extra_cls="mb-8"):
    return f'          <p class="text-sm text-gray-700 leading-relaxed {extra_cls}">{text}</p>'

def h4(text):
    return f'          <h4 class="text-base font-bold text-[#121111] mt-6 mb-3">{text}</h4>'

# ─────────────────────────────────────────────────────────────────────────────
# ENGLISH TERMS CONTENT
# ─────────────────────────────────────────────────────────────────────────────
en_intro = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Terms &amp; Conditions</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Last updated: June 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Introduction</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            These Terms &amp; Conditions govern the use of the Fast Elevate Media website and the provision of services by Fast Elevate Media.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            By using our website, requesting a quotation, engaging our services, or entering into an agreement with Fast Elevate Media, you agree to these Terms &amp; Conditions.
          </p>"""

en_s2 = section(2, "Company Information",
    para("""<strong>Fast Elevate Media</strong><br/>
            Chamber of Commerce (KVK): 56193203<br/>
            VAT Number: NL002247193B30<br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>"""))

en_s3 = section(3, "Services",
    para("Fast Elevate Media provides creative and media services, including but not limited to:", "mb-4"),
    ul(["Photography","Videography","Corporate event coverage","Drone photography and videography",
        "Interviews and testimonials","Social media content creation","Editing and post-production",
        "Creative production services","Marketing and promotional content"]))

en_s4 = section(4, "Quotations and Agreements",
    para("All quotations are non-binding unless explicitly stated otherwise. Quotations remain valid for 30 calendar days from the date of issue unless otherwise specified.", "mb-4"),
    para("An agreement is established when:", "mb-4"),
    ul(["The client accepts a quotation in writing;",
        "The client confirms a booking by email, message, or other written communication;",
        "Fast Elevate Media commences work at the client\u2019s request."]),
    para("Any changes to the agreed scope may result in additional charges."))

en_s5 = section(5, "Deposits, Pricing and Payment",
    para("Unless otherwise stated, all prices are exclusive of VAT.", "mb-4"),
    para("A non-refundable deposit of 50% of the quoted amount is required to secure a booking and reserve production dates. Production dates are not considered confirmed until the deposit has been received.", "mb-4"),
    para("The remaining balance shall be invoiced upon completion of the assignment unless otherwise agreed in writing. Invoices must be paid within 14 calendar days of the invoice date.", "mb-4"),
    para("Fast Elevate Media reserves the right to:", "mb-4"),
    ul(["Suspend ongoing work;","Postpone delivery;","Withhold deliverables;"]),
    para("until outstanding invoices have been paid in full. Statutory interest and collection costs may be charged on overdue invoices."))

en_s6 = section(6, "Additional Work",
    para("Any work requested outside the agreed scope may be considered additional work and invoiced separately. This may include:", "mb-4"),
    ul(["Additional shooting hours","Additional editing","Additional deliverables",
        "Additional revisions","Additional travel","Additional production requirements"]))

en_s7 = section(7, "Delivery Times",
    para("Fast Elevate Media\u2019s standard delivery target for the first draft of most video productions is within three (3) business days after completion of the assignment, subject to the agreed project scope, complexity, and timely receipt of all required client materials.", "mb-4"),
    para("Accelerated delivery options may be available for an additional fee, including:", "mb-4"),
    '          <ul class="space-y-3 mb-6">\n' +
        "\n".join(li(i) for i in ["48-hour delivery","24-hour delivery","Same-day delivery","Custom delivery schedules"]) +
    "\n          </ul>",
    para("Fast Elevate Media shall make reasonable efforts to meet agreed deadlines but shall not be liable for delays resulting from circumstances beyond its reasonable control. This includes, but is not limited to:", "mb-4"),
    ul(["Late client feedback","Delayed approvals","Missing information","Missing branding materials",
        "Missing logos","Missing graphics","Delayed client-supplied assets","Technical issues","Force majeure events"]))

en_s8 = section(8, "Revisions and Acceptance of Deliverables",
    para("Unless otherwise agreed in writing, projects include up to two revision rounds. Additional revisions may be charged separately. Requests that substantially alter the original scope may be treated as a new project and invoiced accordingly.", "mb-4"),
    para("Unless the Client reports material defects within fourteen (14) calendar days after delivery, the delivered work shall be deemed accepted. Minor subjective differences in style, colour grading, editing, framing or creative interpretation shall not constitute defects."))

en_s9 = section(9, "Client Responsibilities",
    para("The client is responsible for:", "mb-4"),
    ul(["Providing accurate information",
        "Providing project schedules",
        "Providing event details",
        "Obtaining all necessary permissions",
        "Ensuring venue access",
        "Providing branding assets where required",
        "Providing timely feedback and approvals"]),
    para("For assignments extending beyond six consecutive working hours or taking place during standard meal times, the client shall provide reasonable meals and refreshments for Fast Elevate Media personnel and contracted freelancers working on-site.", "mb-4"),
    para("Fast Elevate Media shall not be liable for delays or issues resulting from incomplete, inaccurate, or delayed information provided by the client.", "mb-4"),
    para("Deliverables should be reviewed by the Client as soon as reasonably possible after delivery. Any material defects or deviations from the agreed project brief should be reported within fourteen (14) calendar days of delivery. Unless such defects are reported within this period, the delivered work shall be deemed accepted.", "mb-4"),
    para("Creative services are inherently subjective. Minor differences in editing style, colour grading, framing, pacing or creative interpretation shall not be considered defects, provided the delivered work substantially complies with the agreed project brief."))

en_s10 = section(10, "Client Materials",
    para("The client warrants that all materials supplied to Fast Elevate Media may legally be used for the requested project. This includes:", "mb-4"),
    ul(["Logos","Brand assets","Images","Videos","Music","Documents","Third-party content"]),
    para("The client indemnifies Fast Elevate Media against any claims arising from the unlawful use of supplied materials."))

en_s11 = section(11, "Intellectual Property",
    para("Unless otherwise agreed in writing, all copyrights and intellectual property rights in content created by Fast Elevate Media remain the exclusive property of Fast Elevate Media. No copyright transfer shall occur unless expressly agreed in writing."))

en_s12 = section(12, "Licence to Use Deliverables",
    para("Upon full payment, the client receives a non-exclusive licence to use the delivered content for the agreed purpose.", "mb-4"),
    para("The client may not, unless explicitly agreed in writing:", "mb-4"),
    ul(["Resell the content","Transfer rights to third parties","Claim authorship","Alter copyright notices"]))

en_s13 = section(13, "RAW Files and Source Materials",
    para("Unless otherwise agreed in writing, Fast Elevate Media is not obligated to provide:", "mb-4"),
    ul(["RAW photographs","Unedited video footage","Editing project files","Timelines",
        "Source files","Working files","Production assets"]),
    para("Fast Elevate Media retains ownership of all source materials."))

en_s14 = section(14, "AI-Assisted Production",
    para("Fast Elevate Media may use artificial intelligence (\u201cAI\u201d) assisted technologies as part of its creative and administrative workflow. Such tools may be used for purposes including, but not limited to:", "mb-4"),
    ul(["Language refinement and proofreading","Transcription and subtitle generation",
        "Audio enhancement and noise reduction","Image enhancement","Object removal",
        "Background extensions or generative editing","Video editing assistance","Workflow optimisation"]),
    para("AI technologies are used solely as supportive production tools. All creative decisions, quality control, editing decisions and final deliverables remain subject to human review and approval by Fast Elevate Media.", "mb-4"),
    para("Where AI-assisted editing substantially alters the nature of the agreed deliverable beyond standard post-production practices, this will only be performed where appropriate for the project or agreed with the Client.", "mb-4"),
    para("AI-assisted tools shall never replace professional judgement, creative direction, or final editorial approval."))

en_s15 = section(15, "Portfolio and Promotional Use",
    para("Unless otherwise agreed in writing, Fast Elevate Media reserves the right to use content created during assignments for:", "mb-4"),
    ul(["Portfolio purposes","Website publication","Social media","Marketing materials",
        "Promotional campaigns","Award submissions","Business development activities"]),
    para("This includes the right to display completed work on Fast Elevate Media\u2019s website, social media channels, presentations and showreels.", "mb-4"),
    para("This clause applies only to content created by Fast Elevate Media. Materials submitted through contact forms or supplied by prospective clients shall never be used for promotional purposes without explicit written permission.", "mb-4"),
    para("Where confidentiality agreements, non-disclosure agreements, or written restrictions apply, Fast Elevate Media shall respect such restrictions.", "mb-4"),
    para("Fast Elevate Media shall never use Client-submitted materials or AI-generated working files originating from Client materials for portfolio or promotional purposes unless explicit written permission has been obtained."))

en_s16 = section(16, "Confidential Information",
    para("Fast Elevate Media shall treat all confidential information received from the Client with appropriate care.", "mb-4"),
    para("Project documentation, presentations, schedules, internal communications, event details, business information, and other confidential materials supplied by the Client shall not be disclosed to third parties except:", "mb-4"),
    '          <ul class="space-y-3 mb-6">\n' +
        "\n".join(li(i) for i in [
            "where necessary for the execution of the agreed services;",
            "where disclosure is required by applicable law; or",
            "where the Client has provided prior written consent."]) +
    "\n          </ul>",
    para("Fast Elevate Media shall ensure that any employees, freelancers, or subcontractors engaged in the performance of the services are subject to appropriate confidentiality obligations."))

en_s17 = section(17, "Drone Operations",
    para("Drone operations are subject to:", "mb-4"),
    ul(["Weather conditions","Airspace restrictions","Local regulations",
        "Government restrictions","Safety considerations"]),
    para("Fast Elevate Media cannot guarantee that drone footage can be obtained at every location. Where drone operations are prohibited, restricted, or deemed unsafe, alternative filming methods may be used where possible."))

en_s18 = section(18, "Cancellation Policy",
    para("Unless otherwise agreed in writing, cancellations are subject to the following fees:", "mb-4"),
    ul(["More than 30 days before the assignment: no cancellation fee",
        "Between 14 and 30 days before the assignment: 50% of the agreed project fee",
        "Less than 14 days before the assignment: 100% of the agreed project fee"]),
    para("Deposits are non-refundable except where cancellation results directly from Fast Elevate Media\u2019s inability to perform the agreed services. Any non-refundable expenses already incurred shall remain payable by the client."))

en_s19 = section(19, "Force Majeure",
    para("Fast Elevate Media shall not be liable for failure or delay in performing its obligations due to circumstances beyond its reasonable control. Such circumstances include, but are not limited to:", "mb-4"),
    ul(["Illness","Injury","Extreme weather","Natural disasters","Travel disruptions",
        "Technical failures","Internet outages","Government restrictions","Venue closures"]))

en_s20 = section(20, "Limitation of Liability",
    para("Fast Elevate Media shall not be liable for indirect, incidental, special, or consequential damages.", "mb-4"),
    para("To the maximum extent permitted by law, Fast Elevate Media\u2019s total liability shall be limited to the total amount invoiced for the relevant assignment.", "mb-4"),
    para("Nothing in these Terms excludes liability where such exclusion is prohibited by applicable law."))

en_s21 = section(21, "Website Use",
    para("The content on this website is provided for general informational purposes only. Fast Elevate Media reserves the right to modify, suspend, or discontinue any aspect of the website at any time without prior notice.", "mb-4"),
    para("Users may not use the website in any unlawful manner or in any way that interferes with its operation.", "mb-4"),
    para("The content on this website may not be copied, reproduced, distributed or otherwise used without prior written permission from Fast Elevate Media unless permitted by applicable law."))

en_s22 = section(22, "External Links",
    para("This website may contain links to third-party websites. Fast Elevate Media accepts no responsibility for the content, privacy practices, or policies of third-party websites."))

en_s23 = section(23, "Privacy, Cookies and AI Processing",
    para("The collection and processing of personal data are governed by our <a href=\"./privacy.html\" class=\"text-primary underline hover:text-primary/80 transition-colors\">Privacy Policy</a> and <a href=\"./cookies.html\" class=\"text-primary underline hover:text-primary/80 transition-colors\">Cookie Policy</a>.", "mb-4"),
    para("Where AI-assisted software is used during editing or production workflows involving Client materials, Fast Elevate Media shall take reasonable measures to ensure that personal data is processed in accordance with applicable privacy legislation, including the General Data Protection Regulation (GDPR).", "mb-4"),
    para("AI tools are used solely to support creative production and administrative efficiency and do not replace human review or decision-making.", "mb-4"),
    para("Visitors may review or modify their cookie preferences at any time through the cookie settings available on the website."))

en_s24 = section(24, "Right of Withdrawal",
    para("Where the Client is a consumer within the meaning of applicable law, statutory rights of withdrawal may apply.", "mb-4"),
    para("However, the statutory right of withdrawal may expire where:", "mb-4"),
    '          <ul class="space-y-3 mb-6">\n' +
        "\n".join(li(i) for i in [
            "the Client expressly requests Fast Elevate Media to commence the performance of the services during the withdrawal period; and",
            "acknowledges that the right of withdrawal may be lost once the services have been fully performed."]) +
    "\n          </ul>",
    para("Custom photography, videography, editing, creative productions and other personalised services are generally exempt from return or exchange once work has commenced."))

en_s25 = section(25, "Governing Law",
    para("These Terms &amp; Conditions shall be governed by and interpreted in accordance with the laws of the Netherlands.", "mb-4"),
    para("Any disputes arising under these Terms shall be submitted to the competent courts of Amsterdam, The Netherlands."))

en_s26 = section(26, "Contact Information",
    para("""<strong>Fast Elevate Media</strong><br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a><br/>
            Website: <a href="https://fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">www.fastelevatemedia.com</a>"""))

terms_en_full = "\n".join([en_intro, en_s2, en_s3, en_s4, en_s5, en_s6, en_s7, en_s8, en_s9,
                            en_s10, en_s11, en_s12, en_s13, en_s14, en_s15, en_s16, en_s17,
                            en_s18, en_s19, en_s20, en_s21, en_s22, en_s23, en_s24, en_s25, en_s26])

# ─────────────────────────────────────────────────────────────────────────────
# DUTCH TERMS CONTENT
# ─────────────────────────────────────────────────────────────────────────────
def nli(text):
    return f"""            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">{text}</p>
            </li>"""

def nul(items):
    return '          <ul class="space-y-3 mb-8">\n' + "\n".join(nli(i) for i in items) + "\n          </ul>"

def nsection(num, title, *body_parts):
    parts = [f'          <hr class="border-gray-200 my-8"/>',
             f'          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">{num}. {title}</h3>']
    for p in body_parts:
        parts.append(p)
    return "\n".join(parts)

def npara(text, extra_cls="mb-8"):
    return f'          <p class="text-sm text-gray-700 leading-relaxed {extra_cls}">{text}</p>'

nl_intro = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Algemene Voorwaarden</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Laatst bijgewerkt: juni 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Inleiding</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Deze Algemene Voorwaarden zijn van toepassing op het gebruik van de website van Fast Elevate Media en de levering van diensten door Fast Elevate Media.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Door onze website te gebruiken, een offerte aan te vragen, gebruik te maken van onze diensten of een overeenkomst aan te gaan met Fast Elevate Media, gaat u akkoord met deze Algemene Voorwaarden.
          </p>"""

nl_s2  = nsection(2, "Bedrijfsinformatie",
    npara("""<strong>Fast Elevate Media</strong><br/>
            Kamer van Koophandel (KVK): 56193203<br/>
            BTW-nummer: NL002247193B30<br/>
            Amsterdam, Nederland<br/>
            E-mail: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>"""))

nl_s3  = nsection(3, "Diensten",
    npara("Fast Elevate Media levert creatieve en mediadiensten, inclusief maar niet beperkt tot:", "mb-4"),
    nul(["Fotografie","Videografie","Verslaglegging van bedrijfsevenementen","Dronefotografie en -videografie",
         "Interviews en testimonials","Creatie van social media content","Montage en postproductie",
         "Creatieve productiediensten","Marketing en promotionele content"]))

nl_s4  = nsection(4, "Offertes en Overeenkomsten",
    npara("Alle offertes zijn vrijblijvend, tenzij uitdrukkelijk anders vermeld. Offertes blijven geldig gedurende 30 kalenderdagen na de datum van uitgifte, tenzij anders aangegeven.", "mb-4"),
    npara("Een overeenkomst komt tot stand wanneer:", "mb-4"),
    nul(["De klant een offerte schriftelijk accepteert;",
         "De klant een boeking bevestigt via e-mail, bericht of andere schriftelijke communicatie;",
         "Fast Elevate Media op verzoek van de klant begint met de werkzaamheden."]),
    npara("Eventuele wijzigingen in de overeengekomen omvang kunnen leiden tot extra kosten."))

nl_s5  = nsection(5, "Aanbetalingen, Tarieven en Betaling",
    npara("Tenzij anders vermeld, zijn alle prijzen exclusief btw.", "mb-4"),
    npara("Een niet-restitueerbare aanbetaling van 50% van het geoffreerde bedrag is vereist om een boeking te garanderen en productiedata te reserveren. Productiedata worden pas als bevestigd beschouwd wanneer de aanbetaling is ontvangen.", "mb-4"),
    npara("Het resterende saldo wordt gefactureerd na afronding van de opdracht, tenzij schriftelijk anders overeengekomen. Facturen dienen binnen 14 kalenderdagen na factuurdatum te worden voldaan.", "mb-4"),
    npara("Fast Elevate Media behoudt zich het recht voor om:", "mb-4"),
    nul(["Lopende werkzaamheden op te schorten;","De levering uit te stellen;","Opleveringen achter te houden;"]),
    npara("totdat openstaande facturen volledig zijn voldaan. Wettelijke rente en incassokosten kunnen in rekening worden gebracht bij achterstallige facturen."))

nl_s6  = nsection(6, "Meerwerk",
    npara("Alle werkzaamheden die buiten de overeengekomen omvang worden aangevraagd, kunnen als meerwerk worden beschouwd en afzonderlijk worden gefactureerd. Dit kan omvatten:", "mb-4"),
    nul(["Extra opname-uren","Extra montagewerk","Extra op te leveren bestanden",
         "Extra revisierondes","Extra reiskosten","Extra productie-eisen"]))

nl_s7  = nsection(7, "Levertijden",
    npara("De standaard levertijd van Fast Elevate Media voor de eerste versie van de meeste videoproducties is binnen drie (3) werkdagen na afronding van de opdracht, onder voorbehoud van de overeengekomen projectomvang, complexiteit en tijdige ontvangst van al het vereiste materiaal van de klant.", "mb-4"),
    npara("Versnelde leveringsopties kunnen beschikbaar zijn tegen een meerprijs, waaronder:", "mb-4"),
    '          <ul class="space-y-3 mb-6">\n' +
        "\n".join(nli(i) for i in ["48-uurs levering","24-uurs levering","Same-day levering (dezelfde dag)","Aangepaste leveringsschema\u2019s"]) +
    "\n          </ul>",
    npara("Fast Elevate Media spant zich redelijkerwijs in om de overeengekomen termijnen te halen, maar is niet aansprakelijk voor vertragingen als gevolg van omstandigheden buiten haar redelijke controle. Dit omvat, maar is niet beperkt tot:", "mb-4"),
    nul(["Late feedback van de klant","Vertraagde goedkeuringen","Ontbrekende informatie",
         "Ontbrekende huisstijlmaterialen","Ontbrekende logo\u2019s","Ontbrekende graphics",
         "Vertraging bij door de klant geleverde materialen","Technische storingen","Overmachtsituaties"]))

nl_s8  = nsection(8, "Revisies en Acceptatie van Opleveringen",
    npara("Tenzij schriftelijk anders overeengekomen, zijn bij projecten maximaal twee revisierondes inbegrepen. Extra revisies kunnen afzonderlijk in rekening worden gebracht. Aanvragen die de oorspronkelijke omvang wezenlijk wijzigen, kunnen als een nieuw project worden behandeld en als zodanig worden gefactureerd.", "mb-4"),
    npara("Tenzij de klant binnen veertien (14) kalenderdagen na levering wezenlijke gebreken meldt, wordt het geleverde werk als geaccepteerd beschouwd. Geringe subjectieve verschillen in stijl, kleurcorrectie, montage, kadrering of creatieve interpretatie vormen geen gebreken."))

nl_s9  = nsection(9, "Verantwoordelijkheden van de Klant",
    npara("De klant is verantwoordelijk voor:", "mb-4"),
    nul(["Het verstrekken van nauwkeurige informatie",
         "Het verstrekken van projectplanningen",
         "Het verstrekken van details van het evenement",
         "Het verkrijgen van alle benodigde toestemmingen",
         "Het garanderen van toegang tot de locatie",
         "Het verstrekken van merkmaterialen waar nodig",
         "Het geven van tijdige feedback en goedkeuringen"]),
    npara("Voor opdrachten die langer duren dan zes opeenvolgende werkuren of plaatsvinden tijdens standaard maaltijduren, zorgt de klant voor redelijke maaltijden en verfrissingen voor het personeel en de ingehuurde freelancers van Fast Elevate Media die op locatie werken.", "mb-4"),
    npara("Fast Elevate Media is niet aansprakelijk voor vertragingen of problemen die voortvloeien uit onvolledige, onjuiste of vertraagde informatie die door de klant is verstrekt.", "mb-4"),
    npara("Opleveringen moeten zo snel als redelijkerwijs mogelijk na levering door de klant worden beoordeeld. Wezenlijke gebreken of afwijkingen van de overeengekomen projectbriefing moeten binnen veertien (14) kalenderdagen na levering worden gemeld. Tenzij dergelijke gebreken binnen deze periode worden gemeld, wordt het geleverde werk als geaccepteerd beschouwd.", "mb-4"),
    npara("Creatieve diensten zijn inherent subjectief. Geringe verschillen in montagestijl, kleurcorrectie, kadrering, tempo of creatieve interpretatie worden niet als gebreken beschouwd, mits het geleverde werk substantieel voldoet aan de overeengekomen projectbriefing."))

nl_s10 = nsection(10, "Materialen van de Klant",
    npara("De klant garandeert dat alle aan Fast Elevate Media geleverde materialen legaal mogen worden gebruikt voor het aangevraagde project. Dit omvat:", "mb-4"),
    nul(["Logo\u2019s","Merkelementen","Afbeeldingen","Video\u2019s","Muziek","Documenten","Inhoud van derden"]),
    npara("De klant vrijwaart Fast Elevate Media tegen alle claims die voortvloeien uit het onrechtmatig gebruik van de geleverde materialen."))

nl_s11 = nsection(11, "Intellectueel Eigendom",
    npara("Tenzij schriftelijk anders overeengekomen, blijven alle auteursrechten en intellectuele eigendomsrechten op de door Fast Elevate Media gecre\u00eberde inhoud het exclusieve eigendom van Fast Elevate Media. Er vindt geen overdracht van auteursrechten plaats, tenzij uitdrukkelijk schriftelijk overeengekomen."))

nl_s12 = nsection(12, "Licentie voor het Gebruik van Opleveringen",
    npara("Na volledige betaling ontvangt de klant een niet-exclusieve licentie om de geleverde inhoud te gebruiken voor het overeengekomen doel.", "mb-4"),
    npara("Het is de klant niet toegestaan, tenzij uitdrukkelijk schriftelijk overeengekomen:", "mb-4"),
    nul(["De inhoud door te verkopen","Rechten over te dragen aan derden","Het auteurschap te claimen","Auteursrechtvermeldingen te wijzigen"]))

nl_s13 = nsection(13, "RAW-bestanden en Bronmateriaal",
    npara("Tenzij schriftelijk anders overeengekomen, is Fast Elevate Media niet verplicht om de volgende bestanden te leveren:", "mb-4"),
    nul(["RAW-foto\u2019s","Onbewerkte videobeelden","Montageprojectbestanden","Tijdlijnen",
         "Bronbestanden","Werkbestanden","Productie-assets"]),
    npara("Fast Elevate Media behoudt het eigendom van al het bronmateriaal."))

nl_s14 = nsection(14, "AI-ondersteunde Productie",
    npara("Fast Elevate Media kan gebruikmaken van kunstmatige intelligentie (\u201cAI\u201d) ondersteunde technologie\u00ebn als onderdeel van haar creatieve en administratieve workflow. Dergelijke tools kunnen worden gebruikt voor doeleinden inclusief, maar niet beperkt tot:", "mb-4"),
    nul(["Taalverfijning en proeflezen","Transcriptie en het genereren van ondertiteling",
         "Audioverbetering en ruisonderdrukking","Beeldverbetering","Het verwijderen van objecten",
         "Achtergronduitbreidingen of generatieve bewerking","Video-editing-assistentie","Workflowoptimalisatie"]),
    npara("AI-technologie\u00ebn worden uitsluitend gebruikt als ondersteunende productietools. Alle creatieve beslissingen, kwaliteitscontrole, montagebeslissingen en uiteindelijke opleveringen blijven onderworpen aan menselijke beoordeling en goedkeuring door Fast Elevate Media.", "mb-4"),
    npara("Waar AI-ondersteunde montage het karakter van de overeengekomen oplevering wezenlijk verandert buiten de standaard postproductiepraktijken, zal dit alleen worden uitgevoerd wanneer dit passend is voor het project of is overeengekomen met de klant.", "mb-4"),
    npara("AI-ondersteunde tools zullen nooit professioneel oordeel, creatieve sturing of definitieve redactionele goedkeuring vervangen."))

nl_s15 = nsection(15, "Portfolio en Promotioneel Gebruik",
    npara("Tenzij schriftelijk anders overeengekomen, behoudt Fast Elevate Media zich het recht voor om de tijdens opdrachten gecre\u00eberde inhoud te gebruiken voor:", "mb-4"),
    nul(["Portfoliodoeleinden","Publicatie op de website","Social media","Marketingmateriaal",
         "Promotiecampagnes","Prijsinzendingen","Zakelijke ontwikkelingsactiviteiten"]),
    npara("Dit omvat het recht om voltooid werk te tonen op de website, social media kanalen, presentaties en showreels van Fast Elevate Media.", "mb-4"),
    npara("Deze clausule is alleen van toepassing op door Fast Elevate Media gecre\u00eberde inhoud. Materialen ingediend via contactformulieren of verstrekt door potenti\u00eble klanten zullen nooit worden gebruikt voor promotionele doeleinden zonder expliciete schriftelijke toestemming.", "mb-4"),
    npara("Waar geheimhoudingsovereenkomsten, NDA\u2019s of schriftelijke beperkingen van toepassing zijn, zal Fast Elevate Media deze beperkingen respecteren.", "mb-4"),
    npara("Fast Elevate Media zal door de klant ingediende materialen of AI-gegenereerde werkbestanden die afkomstig zijn van klantmaterialen nooit gebruiken voor portfolio- of promotionele doeleinden, tenzij expliciete schriftelijke toestemming is verkregen."))

nl_s16 = nsection(16, "Vertrouwelijke Informatie",
    npara("Fast Elevate Media zal alle van de klant ontvangen vertrouwelijke informatie met de nodige zorg behandelen.", "mb-4"),
    npara("Projectdocumentatie, presentaties, planningen, interne communicatie, details van evenementen, bedrijfsinformatie en andere door de klant verstrekte vertrouwelijke materialen worden niet aan derden bekendgemaakt, behalve:", "mb-4"),
    '          <ul class="space-y-3 mb-6">\n' +
        "\n".join(nli(i) for i in [
            "waar nodig voor de uitvoering van de overeengekomen diensten;",
            "waar openbaarmaking vereist is door de toepasselijke wetgeving; of",
            "waar de klant voorafgaande schriftelijke toestemming heeft verleend."]) +
    "\n          </ul>",
    npara("Fast Elevate Media zorgt ervoor dat werknemers, freelancers of onderaannemers die bij de uitvoering van de diensten zijn betrokken, onderworpen zijn aan passende vertrouwelijkheidsverplichtingen."))

nl_s17 = nsection(17, "Drone-operaties",
    npara("Drone-operaties zijn afhankelijk van:", "mb-4"),
    nul(["Weersomstandigheden","Luchtruimbeperkingen","Lokale regelgeving",
         "Overheidsbeperkingen","Veiligheidsoverwegingen"]),
    npara("Fast Elevate Media kan niet garanderen dat er op elke locatie dronebeelden kunnen worden gemaakt. Waar drone-operaties verboden, beperkt of onveilig worden geacht, kunnen waar mogelijk alternatieve opnamemethoden worden gebruikt."))

nl_s18 = nsection(18, "Annuleringsvoorwaarden",
    npara("Tenzij schriftelijk anders overeengekomen, gelden bij annulering de volgende kosten:", "mb-4"),
    nul(["Meer dan 30 dagen voor de opdracht: geen annuleringskosten",
         "Tussen 14 en 30 dagen voor de opdracht: 50% van het overeengekomen projecttarief",
         "Minder dan 14 dagen voor de opdracht: 100% van het overeengekomen projecttarief"]),
    npara("Aanbetalingen worden niet gerestitueerd, behalve wanneer de annulering het directe gevolg is van het onvermogen van Fast Elevate Media om de overeengekomen diensten uit te voeren. Reeds gemaakte niet-restitueerbare kosten blijven verschuldigd door de klant."))

nl_s19 = nsection(19, "Overmacht",
    npara("Fast Elevate Media is niet aansprakelijk voor het niet of vertraagd nakomen van haar verplichtingen als gevolg van omstandigheden buiten haar redelijke controle. Dergelijke omstandigheden omvatten, maar zijn niet beperkt tot:", "mb-4"),
    nul(["Ziekte","Letsel","Extreem weer","Natuurrampen","Reisonderbrekingen",
         "Technische storingen","Internetuitval","Overheidsbeperkingen","Sluiting van locaties"]))

nl_s20 = nsection(20, "Beperking van Aansprakelijkheid",
    npara("Fast Elevate Media is niet aansprakelijk voor indirecte, incidentele, bijzondere of gevolgschade.", "mb-4"),
    npara("Voor zover maximaal toegestaan door de wet is de totale aansprakelijkheid van Fast Elevate Media beperkt tot het totale bedrag dat voor de desbetreffende opdracht is gefactureerd.", "mb-4"),
    npara("Niets in deze Voorwaarden sluit aansprakelijkheid uit waar een dergelijke uitsluiting door de toepasselijke wetgeving is verboden."))

nl_s21 = nsection(21, "Gebruik van de Website",
    npara("De inhoud op deze website wordt uitsluitend ter algemene informatie verstrekt. Fast Elevate Media behoudt zich het recht voor om elk aspect van de website op elk moment zonder voorafgaande kennisgeving te wijzigen, op te schorten of stop te zetten.", "mb-4"),
    npara("Gebruikers mogen de website niet gebruiken op een onwettige manier of op een manier die de werking ervan verstoort.", "mb-4"),
    npara("De inhoud op deze website mag niet worden gekopieerd, gereproduceerd, gedistribueerd of anderszins worden gebruikt zonder voorafgaande schriftelijke toestemming van Fast Elevate Media, tenzij toegestaan door de toepasselijke wetgeving."))

nl_s22 = nsection(22, "Externe Links",
    npara("Deze website kan links bevatten naar websites van derden. Fast Elevate Media aanvaardt geen verantwoordelijkheid voor de inhoud, het privacybeleid of het cookiebeleid van websites van derden."))

nl_s23 = nsection(23, "Privacy, Cookies en AI-verwerking",
    npara("Het verzamelen en verwerken van persoonlijke gegevens wordt beheerst door ons <a href=\"./privacy.html\" class=\"text-primary underline hover:text-primary/80 transition-colors\">Privacybeleid</a> en <a href=\"./cookies.html\" class=\"text-primary underline hover:text-primary/80 transition-colors\">Cookiebeleid</a>.", "mb-4"),
    npara("Waar AI-ondersteunde software wordt gebruikt tijdens montage- of productieworkflows waarbij klantmaterialen betrokken zijn, neemt Fast Elevate Media redelijke maatregelen om ervoor te zorgen dat persoonlijke gegevens worden verwerkt in overeenstemming met de toepasselijke privacywetgeving, inclusief de Algemene Verordening Gegevensbescherming (AVG).", "mb-4"),
    npara("AI-tools worden uitsluitend gebruikt ter ondersteuning van creatieve productie en administratieve effici\u00ebntie en vervangen geen menselijke beoordeling of besluitvorming.", "mb-4"),
    npara("Bezoekers kunnen hun cookievoorkeuren op elk moment bekijken of wijzigen via de cookie-instellingen die beschikbaar zijn op de website."))

nl_s24 = nsection(24, "Herroepingsrecht",
    npara("Wanneer de klant een consument is in de zin van de toepasselijke wetgeving, kunnen wettelijke herroepingsrechten van toepassing zijn.", "mb-4"),
    npara("Het wettelijke herroepingsrecht kan echter vervallen wanneer:", "mb-4"),
    '          <ul class="space-y-3 mb-6">\n' +
        "\n".join(nli(i) for i in [
            "de klant Fast Elevate Media uitdrukkelijk verzoekt om te beginnen met de uitvoering van de diensten tijdens de herroepingstermijn; en",
            "erkent dat het herroepingsrecht verloren kan gaan zodra de diensten volledig zijn uitgevoerd."]) +
    "\n          </ul>",
    npara("Maatwerkfotografie, videografie, montage, creatieve producties en andere gepersonaliseerde diensten zijn over het algemeen uitgesloten van herroeping of ruil zodra de werkzaamheden zijn begonnen."))

nl_s25 = nsection(25, "Toepasselijk Recht",
    npara("Deze Algemene Voorwaarden worden beheerst door en ge\u00efnterpreteerd in overeenstemming met de Nederlandse wetgeving.", "mb-4"),
    npara("Alle geschillen die voortvloeien uit deze Voorwaarden worden voorgelegd aan de bevoegde rechter in Amsterdam, Nederland."))

nl_s26 = nsection(26, "Contactgegevens",
    npara("""<strong>Fast Elevate Media</strong><br/>
            Amsterdam, Nederland<br/>
            E-mail: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a><br/>
            Website: <a href="https://fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">www.fastelevatemedia.com</a>"""))

terms_nl_full = "\n".join([nl_intro, nl_s2, nl_s3, nl_s4, nl_s5, nl_s6, nl_s7, nl_s8, nl_s9,
                            nl_s10, nl_s11, nl_s12, nl_s13, nl_s14, nl_s15, nl_s16, nl_s17,
                            nl_s18, nl_s19, nl_s20, nl_s21, nl_s22, nl_s23, nl_s24, nl_s25, nl_s26])

# ─────────────────────────────────────────────────────────────────────────────
# APPLY TO terms.html and nl/terms.html
# ─────────────────────────────────────────────────────────────────────────────
def replace_content(filepath, content_html, is_nl=False):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    start_tag = '<!-- LEFT: Terms Content -->'
    end_tag   = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
    if start_tag not in raw or end_tag not in raw:
        print(f"WARNING: markers not found in {filepath}")
        return
    start_idx = raw.find(start_tag) + len(start_tag)
    end_idx   = raw.find(end_tag)
    new_block = "\n        <div class=\"flex-1 min-w-0\" style=\"font-family:'Lexend',sans-serif;\">\n" \
                + content_html + "\n        </div>\n        "
    raw = raw[:start_idx] + new_block + raw[end_idx:]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(raw)
    print(f"Overwrote {filepath} successfully.")

replace_content(os.path.join(base_dir, "terms.html"),    terms_en_full, is_nl=False)
replace_content(os.path.join(base_dir, "nl/terms.html"), terms_nl_full, is_nl=True)

# ─────────────────────────────────────────────────────────────────────────────
# INJECT cookie-consent.js into ALL HTML files (if not already present)
# ─────────────────────────────────────────────────────────────────────────────
import glob

html_files_root = glob.glob(os.path.join(base_dir, "*.html"))
html_files_nl   = glob.glob(os.path.join(base_dir, "nl", "*.html"))
all_html = html_files_root + html_files_nl

CONSENT_TAG = 'cookie-consent.js'
injected = 0
already  = 0

for path in sorted(all_html):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if CONSENT_TAG in content:
        already += 1
        continue

    # Determine relative path depth
    if os.path.dirname(path).endswith('/nl'):
        script_src = '../cookie-consent.js'
    else:
        script_src = './cookie-consent.js'

    snippet = f'\n  <!-- Cookie Consent System -->\n  <script src="{script_src}" defer></script>'

    # Insert just before </body>
    if '</body>' in content:
        content = content.replace('</body>', snippet + '\n</body>', 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        injected += 1
    else:
        print(f"  WARNING: no </body> tag found in {os.path.basename(path)}")

print(f"\ncookie-consent.js injected into {injected} files. Already present in {already} files.")
