import os

# Files to update
base_dir = "/Users/v/Desktop/Fastelevate 06-01"

# 1. privacy.html (English) replacement
privacy_en_filepath = os.path.join(base_dir, "privacy.html")
privacy_en_target = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-4">Who we are</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            <strong>Suggested text:</strong> Our website address is: <a href="https://fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">https://fastelevatemedia.com</a>.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">Comments</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Suggested text:</strong> When visitors leave comments on the site, we collect the data shown in the comments form, as well as the visitor's IP address and browser user agent string to help detect spam.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            An anonymized string created from your email address (also called a hash) may be provided to the Gravatar service if you use it. The Gravatar service privacy policy is available here: <a href="https://automattic.com/privacy/" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">https://automattic.com/privacy/</a>. After approval of your comment, your profile picture is visible to the public in the context of your comment.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">Media</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            <strong>Suggested text:</strong> If you upload images to the website, you should avoid uploading images with embedded location data (EXIF GPS) included. Visitors to the website can download and extract any location data from images on the website.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">Cookies</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Suggested text:</strong> If you leave a comment on our site, you may opt in to saving your name, email address, and website in cookies. These are for your convenience so that you do not have to fill in your details again when you leave another comment. These cookies will last for one year.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            If you visit our login page, we will set a temporary cookie to determine if your browser accepts cookies. This cookie contains no personal data and is discarded when you close your browser.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            When you log in, we will also set up several cookies to save your login information and your screen display choices. Login cookies last for two days, and screen options cookies last for one year. If you select "Remember Me", your login will persist for two weeks. If you log out of your account, the login cookies will be removed.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            If you edit or publish an article, an additional cookie will be saved in your browser. This cookie includes no personal data and simply indicates the post ID of the article you just edited. It expires after one day.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">Embedded content from other websites</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Suggested text:</strong> Articles on this site may include embedded content (e.g. videos, images, articles, etc.). Embedded content from other websites behaves in the exact same way as if the visitor has visited the other website.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            These websites may collect data about you, use cookies, embed additional third-party tracking, and monitor your interaction with that embedded content, including tracking your interaction if you have an account and are logged in to that website.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">Who we share your data with</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            <strong>Suggested text:</strong> If you request a password reset, your IP address will be included in the reset email.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">How long we retain your data</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Suggested text:</strong> If you leave a comment, the comment and its metadata are retained indefinitely. This is so we can recognize and approve any follow-up comments automatically instead of holding them for moderation.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            For users that register on our website (if any), we also store the personal information they provide in their user profile. All users can see, edit, or delete their personal information at any time (except they cannot change their username). Website administrators can also see and edit that information.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">What rights you have over your data</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            <strong>Suggested text:</strong> If you have an account on this site, or have left comments, you can request to receive an exported file of the personal data we hold about you, including any data you have provided to us. You can also request that we erase any personal data we hold about you. This does not include any data we are obliged to keep for administrative, legal, or security purposes.
          </p>

          <hr class="border-gray-200 my-8"/>
          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-10 mb-4">Where your data is sent</h2>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            <strong>Suggested text:</strong> Visitor comments may be checked through an automated spam detection service.
          </p>"""

privacy_en_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Privacy Policy</h2>
          <p class="text-sm text-gray-500 font-semibold mb-4"><strong>Last updated: June 2026</strong></p>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            At <strong>Fast Elevate Media</strong>, we respect your privacy and are committed to protecting your personal data in accordance with the General Data Protection Regulation (GDPR) and other applicable privacy laws. This Privacy Policy explains how we collect, use, store, and protect your personal information when you visit <a href="https://fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">fastelevatemedia.com</a>, contact us, request a quotation, or engage our services.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Company Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam, The Netherlands<br/>
            KVK Number: 56193203<br/>
            VAT Number: NL002247193B30<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. Personal Data We Collect</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">We may collect and process the following personal data:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Information You Provide:</strong> Contact details (such as full name, email address, telephone number, company name), subject of inquiry, message content, event location, project details, event schedules, and any files or materials uploaded through our forms.</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed"><strong>Information Collected Automatically:</strong> When visiting our website, we may collect IP addresses, browser types, device information, operating systems, and pages visited.</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. How We Use Your Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">We use the collected information for various purposes, including to:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Provide, operate, and maintain our website and services</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Process your inquiries and communicate with you</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Send you updates, newsletters, and promotional materials (subject to your consent)</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Improve and optimize our website and user experience</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Comply with legal obligations</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Sharing Your Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media does not sell, trade, or rent your personal identification information to others. We may share information with trusted third-party service providers who assist us in operating our website or conducting our business, so long as those parties agree to keep this information confidential.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Data Security</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            We implement appropriate technical and organizational security measures to protect your personal data against unauthorized access, alteration, disclosure, or destruction.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Your Rights</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Under the GDPR and other applicable data protection legislation, you have the right to:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Access, correct, or erase your personal data</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Restrict or object to the processing of your data</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Withdraw consent at any time for consent-based activities</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Request data portability</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            To exercise any of these rights, please contact us using the details below.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Changes to This Privacy Policy</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            We reserve the right to update or change our Privacy Policy at any time. Any changes will be posted on this page with an updated revision date.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. Contact Us</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">If you have any questions or comments about this Privacy Policy, please contact us at:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam, The Netherlands<br/>
            KVK Number: 56193203<br/>
            VAT Number: NL002247193B30<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

# Read, update and write privacy.html
with open(privacy_en_filepath, "r", encoding="utf-8") as f:
    privacy_en_content = f.read()

if privacy_en_target in privacy_en_content:
    privacy_en_content = privacy_en_content.replace(privacy_en_target, privacy_en_replacement)
    with open(privacy_en_filepath, "w", encoding="utf-8") as f:
        f.write(privacy_en_content)
    print("Updated privacy.html (English) successfully.")
else:
    # Try direct replacements for who we are section
    print("English privacy.html target block not found exactly. Attempting fallback replacement.")
    # Fallback to replace between Who we are and Where your data is sent
    # Or just replace the whole section
    start_tag = '<!-- LEFT: Privacy Policy Content -->'
    end_tag = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
    if start_tag in privacy_en_content and end_tag in privacy_en_content:
        start_idx = privacy_en_content.find(start_tag) + len(start_tag)
        end_idx = privacy_en_content.find(end_tag)
        inner_content = privacy_en_content[start_idx:end_idx]
        
        # Build the exact wrapper content
        new_inner = "\n        <div class=\"flex-1 min-w-0 prose prose-sm max-w-none text-[#121111]\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + privacy_en_replacement + "\n        </div>\n        "
        privacy_en_content = privacy_en_content[:start_idx] + new_inner + privacy_en_content[end_idx:]
        with open(privacy_en_filepath, "w", encoding="utf-8") as f:
            f.write(privacy_en_content)
        print("Updated privacy.html via fallback successfully.")

# 2. nl/privacy.html (Dutch) replacement
privacy_nl_filepath = os.path.join(base_dir, "nl/privacy.html")
privacy_nl_target = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Neem contact met ons op</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Als u vragen of opmerkingen heeft over dit Privacybeleid, neem dan contact met ons op via:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

privacy_nl_replacement = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Neem contact met ons op</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Als u vragen of opmerkingen heeft over dit Privacybeleid, neem dan contact met ons op via:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            KVK-nummer: 56193203<br/>
            BTW-nummer: NL002247193B30<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

with open(privacy_nl_filepath, "r", encoding="utf-8") as f:
    privacy_nl_content = f.read()

if privacy_nl_target in privacy_nl_content:
    privacy_nl_content = privacy_nl_content.replace(privacy_nl_target, privacy_nl_replacement)
    with open(privacy_nl_filepath, "w", encoding="utf-8") as f:
        f.write(privacy_nl_content)
    print("Updated nl/privacy.html successfully.")
else:
    print("Target in nl/privacy.html not found.")

# 3. terms.html (English) replacement
terms_en_filepath = os.path.join(base_dir, "terms.html")
terms_en_target = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Contact Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">If you have any questions about these Terms and Conditions, please contact us at:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

terms_en_replacement = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Contact Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">If you have any questions about these Terms and Conditions, please contact us at:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            KVK Number: 56193203<br/>
            VAT Number: NL002247193B30<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

with open(terms_en_filepath, "r", encoding="utf-8") as f:
    terms_en_content = f.read()

if terms_en_target in terms_en_content:
    terms_en_content = terms_en_content.replace(terms_en_target, terms_en_replacement)
    with open(terms_en_filepath, "w", encoding="utf-8") as f:
        f.write(terms_en_content)
    print("Updated terms.html successfully.")
else:
    print("Target in terms.html not found.")

# 4. nl/terms.html (Dutch) replacement
terms_nl_filepath = os.path.join(base_dir, "nl/terms.html")
terms_nl_target = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Contactgegevens</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Als u vragen heeft over deze Algemene voorwaarden, neem dan contact met ons op via:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

terms_nl_replacement = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Contactgegevens</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Als u vragen heeft over deze Algemene voorwaarden, neem dan contact met ons op via:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            KVK-nummer: 56193203<br/>
            BTW-nummer: NL002247193B30<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

with open(terms_nl_filepath, "r", encoding="utf-8") as f:
    terms_nl_content = f.read()

if terms_nl_target in terms_nl_content:
    terms_nl_content = terms_nl_content.replace(terms_nl_target, terms_nl_replacement)
    with open(terms_nl_filepath, "w", encoding="utf-8") as f:
        f.write(terms_nl_content)
    print("Updated nl/terms.html successfully.")
else:
    print("Target in nl/terms.html not found.")

# 5. cookies.html (English) replacement
cookies_en_filepath = os.path.join(base_dir, "cookies.html")
cookies_en_target = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Contact</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">If you have any questions about our use of cookies, please contact us at:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

cookies_en_replacement = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Contact</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">If you have any questions about our use of cookies, please contact us at:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            KVK Number: 56193203<br/>
            VAT Number: NL002247193B30<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

with open(cookies_en_filepath, "r", encoding="utf-8") as f:
    cookies_en_content = f.read()

if cookies_en_target in cookies_en_content:
    cookies_en_content = cookies_en_content.replace(cookies_en_target, cookies_en_replacement)
    with open(cookies_en_filepath, "w", encoding="utf-8") as f:
        f.write(cookies_en_content)
    print("Updated cookies.html successfully.")
else:
    print("Target in cookies.html not found.")

# 6. nl/cookies.html (Dutch) replacement
cookies_nl_filepath = os.path.join(base_dir, "nl/cookies.html")
cookies_nl_target = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Contact</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Als u vragen heeft over ons gebruik van cookies, neem dan contact met ons op via:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

cookies_nl_replacement = """          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Contact</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-2">Als u vragen heeft over ons gebruik van cookies, neem dan contact met ons op via:</p>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Wittenburgerkade 70, 1018LK Amsterdam<br/>
            KVK-nummer: 56193203<br/>
            BTW-nummer: NL002247193B30<br/>
            <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>"""

with open(cookies_nl_filepath, "r", encoding="utf-8") as f:
    cookies_nl_content = f.read()

if cookies_nl_target in cookies_nl_content:
    cookies_nl_content = cookies_nl_content.replace(cookies_nl_target, cookies_nl_replacement)
    with open(cookies_nl_filepath, "w", encoding="utf-8") as f:
        f.write(cookies_nl_content)
    print("Updated nl/cookies.html successfully.")
else:
    print("Target in nl/cookies.html not found.")

print("All legal pages updated locally.")
