import os

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

# 1. privacy.html (English)
privacy_en_filepath = os.path.join(base_dir, "privacy.html")
privacy_en_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Privacy Policy</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Last updated: June 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Introduction</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            Fast Elevate Media ("Fast Elevate Media", "we", "us", or "our") respects your privacy and is committed to protecting your personal data in accordance with the General Data Protection Regulation (GDPR) and other applicable privacy laws.
            This Privacy Policy explains how we collect, use, store, and protect personal information when you visit our website, contact us, request a quotation, or engage our services.
            By using our website, you agree to the terms of this Privacy Policy.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. Company Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Fast Elevate Media</strong><br/>
            KVK Number: 56193203<br/>
            VAT Number: NL002247193B30<br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. Personal Data We Collect</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">We may collect and process the following personal data:</p>
          
          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Information You Provide</h4>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Full name</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Email address</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Telephone number</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Company name</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Subject of inquiry</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Message content</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Event location</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Project details</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Event schedules and briefs</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Any files, images, photographs, documents, or supporting materials uploaded through our contact forms</p>
            </li>
          </ul>

          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Information Collected Automatically</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">When visiting our website, we may collect:</p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">IP address</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Browser type</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Device information</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Operating system</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Pages visited</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Referring website</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Time spent on pages</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Website interaction data</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            This information may be collected through cookies and analytics technologies where consent has been provided.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Purposes of Processing</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">We process personal data for the following purposes:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Responding to inquiries</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Preparing quotations and proposals</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Communicating regarding potential projects</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Delivering photography, videography, creative, and media services</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Managing customer relationships</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Scheduling projects and events</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Maintaining business administration</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Complying with legal obligations</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Improving our website and services</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Measuring website performance</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Measuring advertising effectiveness</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Following up on requests, quotations, and ongoing business discussions</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Legal Basis for Processing</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">We process personal data based on one or more of the following legal grounds:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Contractual Necessity:</strong> To prepare quotations, negotiate agreements, and perform services requested by clients.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Legitimate Interest:</strong> To communicate with prospective and existing clients, improve our services, maintain business operations, and follow up on requests or quotations.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Consent:</strong> Where required by law, including for analytics, advertising technologies, and certain cookies.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Legal Obligation:</strong> To comply with tax, accounting, and other legal requirements.</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Contact Forms and Uploaded Files</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            When you submit information through our contact forms, we process the information solely for the purpose of evaluating, discussing, preparing, and executing potential projects.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Files submitted through contact forms may include:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Event schedules</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Briefings</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Production documents</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Images</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Photographs</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Project documentation</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media will not use materials submitted through contact forms for promotional, portfolio, or marketing purposes without prior written permission.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Business Communications</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            If you contact us or request a quotation, we may contact you by email, telephone, or WhatsApp Business regarding: your inquiry, your quotation request, project-related communication, follow-up questions, service availability, or business opportunities related to your request. These communications are considered part of our legitimate business relationship and are not considered newsletter marketing communications.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. Analytics and Advertising Technologies</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            To improve our website and measure marketing performance, Fast Elevate Media may use:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Analytics 4</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Tag Manager</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Ads Conversion Tracking</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            These technologies help us understand website traffic, visitor behaviour, popular pages, campaign performance, and lead generation effectiveness.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Where legally required, these technologies will only be activated after obtaining your consent through our cookie banner. You may withdraw or modify your cookie preferences at any time.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Sharing of Personal Data</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            We do not sell personal data. We may share personal data with trusted service providers who support our business operations, including:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Website hosting providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Email service providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Analytics providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Cloud storage providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">IT service providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Accounting and administration providers</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Such providers may only process data on our behalf and under appropriate contractual safeguards.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">10. International Data Transfers</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Certain service providers may process data outside the European Economic Area (EEA). Where this occurs, we ensure appropriate safeguards are implemented in accordance with GDPR requirements, including the use of approved contractual mechanisms where applicable.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">11. Data Retention</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            We retain personal data only as long as necessary for the purposes described in this Privacy Policy. Typical retention periods include:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Contact inquiries: up to 12 months</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Quotations and project discussions: up to 24 months</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Contracts and financial records: 7 years or longer where required by law</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Data may be retained longer where necessary to establish, exercise, or defend legal claims.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">12. Security Measures</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            We take reasonable technical and organisational measures to protect personal data against loss, misuse, unauthorised access, disclosure, alteration, or destruction. However, no internet transmission or storage system can be guaranteed to be completely secure.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">13. Your Rights</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Under the GDPR, you have the right to: access your personal data, correct inaccurate information, request deletion of your data, restrict processing, object to processing, withdraw consent, or request data portability.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Requests may be submitted to: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">14. Complaints</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            If you believe that your personal data has been processed unlawfully, you have the right to lodge a complaint with the relevant supervisory authority. Examples include:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Autoriteit Persoonsgegevens (Netherlands)</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Gegevensbeschermingsautoriteit (Belgium)</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">15. Changes to This Privacy Policy</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media may update this Privacy Policy from time to time. Any updates will be published on this page together with the revised date.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">16. Contact</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">For questions regarding this Privacy Policy or the processing of personal data, please contact:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

# 2. nl/privacy.html (Dutch)
privacy_nl_filepath = os.path.join(base_dir, "nl/privacy.html")
privacy_nl_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Privacybeleid</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Laatst bijgewerkt: juni 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Inleiding</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            Fast Elevate Media ("Fast Elevate Media", "we", "ons" of "onze") respecteert uw privacy en zet zich in om uw persoonlijke gegevens te beschermen in overeenstemming met de Algemene Verordening Gegevensbescherming (AVG/GDPR) en andere toepasselijke privacywetgeving.
            Dit Privacybeleid legt uit hoe we persoonlijke gegevens verzamelen, gebruiken, opslaan en beveiligen wanneer u onze website bezoekt, contact met ons opneemt, een offerte aanvraagt of gebruikmaakt van onze diensten.
            Door onze website te gebruiken, gaat u akkoord met de voorwaarden van dit Privacybeleid.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. Bedrijfsinformatie</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Fast Elevate Media</strong><br/>
            KVK-nummer: 56193203<br/>
            BTW-nummer: NL002247193B30<br/>
            Amsterdam, Nederland<br/>
            E-mail: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. Persoonlijke Gegevens Die We Verzamelen</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">We kunnen de volgende persoonlijke gegevens verzamelen en verwerken:</p>
          
          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Informatie Die U Verstrekt</h4>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Volledige naam</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">E-mailadres</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Telefoonnummer</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Bedrijfsnaam</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Onderwerp van aanvraag</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Inhoud van het bericht</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Locatie van het evenement</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Projectdetails</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Evenementschema's en briefings</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Bestanden, afbeeldingen, foto's, documenten of ondersteunend materiaal geüpload via onze contactformulieren</p>
            </li>
          </ul>

          <h4 class="text-base font-bold text-[#121111] mt-6 mb-2">Informatie Die Automatisch Wordt Verzameld</h4>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Bij het bezoeken van onze website kunnen we het volgende verzamelen:</p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">IP-adres</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Browser type</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Apparaatinformatie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Besturingssysteem</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Bezochte pagina's</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Verwijzende website</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Tijd doorgebracht op pagina's</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Website-interactiegegevens</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            Deze informatie kan worden verzameld via cookies en analysetechnologieën waarvoor toestemming is verleend.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Doeleinden van de Verwerking</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Wij verwerken persoonlijke gegevens voor de volgende doeleinden:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Beantwoorden van vragen en verzoeken</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Opstellen van offertes en voorstellen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Communiceren over potentiële projecten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Leveren van fotografie, videografie, creatieve en mediadiensten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Beheren van klantrelaties</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Plannen van projecten en evenementen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Onderhouden van de bedrijfsadministratie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Voldoen aan wettelijke verplichtingen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Verbeteren van onze website en diensten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Meten van websiteprestaties</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Meten van advertentie-effectiviteit</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Opvolgen van aanvragen, offertes en lopende zakelijke besprekingen</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Juridische Grondslag voor de Verwerking</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Wij verwerken persoonlijke gegevens op basis van een of meer van de volgende rechtsgronden:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Contractuele Noodzaak:</strong> Om offertes op te stellen, over overeenkomsten te onderhandelen en door klanten gevraagde diensten uit te voeren.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Gerechtvaardigd Belang:</strong> Om te communiceren met potentiële en bestaande klanten, onze diensten te verbeteren, bedrijfsactiviteiten te onderhouden en aanvragen of offertes op te volgen.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Toestemming:</strong> Waar wettelijk vereist, inclusief voor analytics, advertentietechnologieën en bepaalde cookies.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Wettelijke Verplichting:</strong> Om te voldoen aan belasting-, boekhoudkundige en andere wettelijke vereisten.</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Contactformulieren en Geüploade Bestanden</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Wanneer u informatie indient via onze contactformulieren, verwerken we deze informatie uitsluitend om potentiële projecten te beoordelen, te bespreken, voor te bereiden en uit te voeren.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Bestanden ingediend via contactformulieren kunnen zijn:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Evenementschema's</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Briefings</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Productiedocumenten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Afbeeldingen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Foto's</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Projectdocumentatie</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media zal materiaal ingediend via contactformulieren niet gebruiken voor promotie-, portfolio- of marketingdoeleinden zonder voorafgaande schriftelijke toestemming.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Zakelijke Communicatie</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            Als u contact met ons opneemt of een offerte aanvraagt, kunnen we contact met u opnemen via e-mail, telefoon of WhatsApp Business met betrekking tot: uw aanvraag, uw offerteverzoek, projectgerelateerde communicatie, vervolgvragen, beschikbaarheid van diensten of zakelijke mogelijkheden met betrekking tot uw verzoek. Deze communicatie wordt beschouwd als onderdeel van onze legitieme zakelijke relatie en wordt niet beschouwd als nieuwsbrief-marketing.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. Analytics en Advertentietechnologieën</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Om onze website te verbeteren en marketingprestaties te meten, kan Fast Elevate Media gebruikmaken van:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Analytics 4</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Tag Manager</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Google Ads Conversion Tracking</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Deze technologieën helpen ons websiteverkeer, gebruikersgedrag, populaire pagina's, campagne-prestaties en effectiviteit van leadgeneratie te begrijpen.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Waar wettelijk vereist, worden deze technologieën pas geactiveerd na het verkrijgen van uw toestemming via onze cookiebanner. U kunt uw cookievoorkeuren op elk moment intrekken of wijzigen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Delen van Persoonlijke Gegevens</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Wij verkopen geen persoonlijke gegevens. We kunnen persoonlijke gegevens delen met vertrouwde serviceproviders die onze bedrijfsactiviteiten ondersteunen, waaronder:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Website hosting providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">E-mail service providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Analytics providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Cloud opslag providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">IT service providers</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Boekhoudings- en administratieproviders</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Dergelijke providers mogen gegevens alleen namens ons en onder passende contractuele waarborgen verwerken.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">10. Internationale Gegevensoverdrachten</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Bepaalde serviceproviders kunnen gegevens buiten de Europese Economische Ruimte (EER) verwerken. Wanneer dit gebeurt, zorgen we ervoor dat passende waarborgen worden geïmplementeerd in overeenstemming met de AVG-vereisten, waaronder het gebruik van goedgekeurde contractuele mechanismen waar van toepassing.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">11. Gegevensretentie</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            We bewaren persoonlijke gegevens alleen zo lang als nodig is voor de doeleinden beschreven in dit Privacybeleid. Typische bewaartermijnen zijn:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Contactaanvragen: tot 12 maanden</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Offertes en projectbesprekingen: tot 24 maanden</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Contracten en financiële administratie: 7 jaar of langer indien wettelijk vereist</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Gegevens kunnen langer worden bewaard wanneer dit nodig is om rechtsvorderingen in te stellen, uit te oefenen of te onderbouwen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">12. Beveiligingsmaatregelen</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Wij nemen passende technische en organisatorische maatregelen om persoonlijke gegevens te beschermen tegen verlies, misbruik, ongeoorloofde toegang, openbaarmaking, wijziging of vernietiging. Geen enkele transmissie over het internet of opslagsysteem kan echter als 100% veilig worden gegarandeerd.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">13. Uw Rechten</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Onder de AVG heeft u het recht om: uw persoonlijke gegevens in te zien, onjuiste informatie te corrigeren, verzoek tot verwijdering van uw gegevens in te dienen, de verwerking te beperken, bezwaar te maken tegen verwerking, uw toestemming in te trekken of verzoek te doen tot gegevensoverdraagbaarheid.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Verzoeken kunnen worden ingediend bij: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">14. Klachten</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Als u van mening bent dat uw persoonlijke gegevens onrechtmatig zijn verwerkt, heeft u het recht om een klacht in te dienen bij de relevante toezichthoudende autoriteit. Voorbeelden zijn:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Autoriteit Persoonsgegevens (Nederland)</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Gegevensbeschermingsautoriteit (België)</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">15. Wijzigingen in dit Privacybeleid</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media kan dit Privacybeleid van tijd tot tijd bijwerken. Eventuele updates worden op deze pagina gepubliceerd samen met de herziene datum.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">16. Contact</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Voor vragen over dit Privacybeleid of de verwerking van persoonlijke gegevens kunt u contact opnemen met:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Amsterdam, Nederland<br/>
            E-mail: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

# Write English privacy policy
with open(privacy_en_filepath, "r", encoding="utf-8") as f:
    en_content = f.read()

start_tag = '<!-- LEFT: Privacy Policy Content -->'
end_tag = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag in en_content and end_tag in en_content:
    start_idx = en_content.find(start_tag) + len(start_tag)
    end_idx = en_content.find(end_tag)
    new_inner_en = "\n        <div class=\"flex-1 min-w-0 prose prose-sm max-w-none text-[#121111]\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + privacy_en_replacement + "\n        </div>\n        "
    en_content = en_content[:start_idx] + new_inner_en + en_content[end_idx:]
    with open(privacy_en_filepath, "w", encoding="utf-8") as f:
        f.write(en_content)
    print("Overwrote privacy.html successfully.")

# Write Dutch privacy policy
with open(privacy_nl_filepath, "r", encoding="utf-8") as f:
    nl_content = f.read()

start_tag_nl = '<!-- LEFT: Privacy Content -->'
end_tag_nl = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag_nl in nl_content and end_tag_nl in nl_content:
    start_idx_nl = nl_content.find(start_tag_nl) + len(start_tag_nl)
    end_idx_nl = nl_content.find(end_tag_nl)
    new_inner_nl = "\n        <div class=\"flex-1 min-w-0\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + privacy_nl_replacement + "\n        </div>\n        "
    nl_content = nl_content[:start_idx_nl] + new_inner_nl + nl_content[end_idx_nl:]
    with open(privacy_nl_filepath, "w", encoding="utf-8") as f:
        f.write(nl_content)
    print("Overwrote nl/privacy.html successfully.")
