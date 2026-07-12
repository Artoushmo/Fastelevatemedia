import os

base_dir = "/Users/v/Desktop/Fastelevate 06-01"

# 1. terms.html (English)
terms_en_filepath = os.path.join(base_dir, "terms.html")
terms_en_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Terms &amp; Conditions</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Last updated: June 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Introduction</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            These Terms &amp; Conditions govern the use of the Fast Elevate Media website and the provision of services by Fast Elevate Media.
            By using our website, requesting a quotation, engaging our services, or entering into an agreement with Fast Elevate Media, you agree to these Terms &amp; Conditions.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. Company Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Fast Elevate Media</strong><br/>
            Chamber of Commerce (KVK): 56193203<br/>
            VAT Number: NL002247193B30<br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. Services</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Fast Elevate Media provides creative and media services, including but not limited to:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Photography</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Videography</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Corporate event coverage</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Drone photography and videography</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Interviews and testimonials</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Social media content creation</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Editing and post-production</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Creative production services</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Marketing and promotional content</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Quotations and Agreements</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            All quotations are non-binding unless explicitly stated otherwise. Quotations remain valid for 30 calendar days from the date of issue unless otherwise specified.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            An agreement is established when:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">The client accepts a quotation in writing;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">The client confirms a booking by email, message, or other written communication;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Fast Elevate Media commences work at the client's request.</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Any changes to the agreed scope may result in additional charges.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Deposits, Pricing and Payment</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Unless otherwise stated, all prices are exclusive of VAT.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            A non-refundable deposit of 50% of the quoted amount is required to secure a booking and reserve production dates. Production dates are not considered confirmed until the deposit has been received.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            The remaining balance shall be invoiced upon completion of the assignment unless otherwise agreed in writing. Invoices must be paid within 14 calendar days of the invoice date.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media reserves the right to:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Suspend ongoing work;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Postpone delivery;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Withhold deliverables;</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            until outstanding invoices have been paid in full. Statutory interest and collection costs may be charged on overdue invoices.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Additional Work</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Any work requested outside the agreed scope may be considered additional work and invoiced separately. This may include:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Additional shooting hours</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Additional editing</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Additional deliverables</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Additional revisions</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Additional travel</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Additional production requirements</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Delivery Times</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media's standard delivery target for the first draft of most video productions is within three (3) business days after completion of the assignment, subject to the agreed project scope, complexity, and timely receipt of all required client materials.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Accelerated delivery options may be available for an additional fee, including:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">48-hour delivery</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">24-hour delivery</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Same-day delivery</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Custom delivery schedules</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media shall make reasonable efforts to meet agreed deadlines but shall not be liable for delays resulting from circumstances beyond its reasonable control. This includes, but is not limited to:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Late client feedback or delayed approvals</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Missing information, logos, graphics, or branding materials</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Delayed client-supplied assets</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Technical issues or force majeure events</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. Revisions and Acceptance of Deliverables</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Unless otherwise agreed in writing, projects include up to two revision rounds. Additional revisions may be charged separately. Requests that substantially alter the original scope may be treated as a new project and invoiced accordingly.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Unless the Client reports material defects within fourteen (14) calendar days after delivery, the delivered work shall be deemed accepted. Minor subjective differences in style, colour grading, editing, framing or creative interpretation shall not constitute defects.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Client Responsibilities</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            The client is responsible for:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Providing accurate information, project schedules, and event details</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Obtaining all necessary permissions and ensuring venue access</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Providing branding assets where required and providing timely feedback and approvals</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            For assignments extending beyond six consecutive working hours or taking place during standard meal times, the client shall provide reasonable meals and refreshments for Fast Elevate Media personnel and contracted freelancers working on-site.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media shall not be liable for delays or issues resulting from incomplete, inaccurate, or delayed information provided by the client. Creative services are inherently subjective. Minor differences in editing style, colour grading, framing, pacing or creative interpretation shall not be considered defects, provided the delivered work substantially complies with the agreed project brief.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">10. Client Materials</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            The client warrants that all materials supplied to Fast Elevate Media may legally be used for the requested project. This includes logos, brand assets, images, videos, music, documents, and third-party content.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            The client indemnifies Fast Elevate Media against any claims arising from the unlawful use of supplied materials.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">11. Intellectual Property</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Unless otherwise agreed in writing, all copyrights and intellectual property rights in content created by Fast Elevate Media remain the exclusive property of Fast Elevate Media. No copyright transfer shall occur unless expressly agreed in writing.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">12. Licence to Use Deliverables</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Upon full payment, the client receives a non-exclusive licence to use the delivered content for the agreed purpose.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            The client may not:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Resell the content or transfer rights to third parties;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Claim authorship or alter copyright notices;</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">13. RAW Files and Source Materials</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Unless otherwise agreed in writing, Fast Elevate Media is not obligated to provide RAW photographs, unedited video footage, editing project files, timelines, source files, working files, or production assets. Fast Elevate Media retains ownership of all source materials.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">14. AI-Assisted Production</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media may use artificial intelligence ("AI") assisted technologies as part of its creative and administrative workflow. Such tools may be used for purposes including language refinement, transcription, subtitle generation, audio enhancement, noise reduction, image enhancement, object removal, background extensions, video editing assistance, and workflow optimisation.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            AI technologies are used solely as supportive production tools. All creative decisions, quality control, editing decisions, and final deliverables remain subject to human review and approval by Fast Elevate Media. Where AI-assisted editing substantially alters the nature of the agreed deliverable beyond standard post-production practices, this will only be performed where appropriate for the project or agreed with the Client.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">15. Portfolio and Promotional Use</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Unless otherwise agreed in writing, Fast Elevate Media reserves the right to use content created during assignments for portfolio purposes, website publication, social media, marketing materials, promotional campaigns, award submissions, and business development activities.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            This clause applies only to content created by Fast Elevate Media. Materials submitted through contact forms or supplied by prospective clients shall never be used for promotional purposes without explicit written permission. Fast Elevate Media shall never use Client-submitted materials or AI-generated working files originating from Client materials for portfolio or promotional purposes unless explicit written permission has been obtained.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">16. Confidential Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media shall treat all confidential information received from the Client with appropriate care. Project documentation, presentations, schedules, internal communications, event details, business information, and other confidential materials supplied by the Client shall not be disclosed to third parties except where necessary for the execution of the agreed services, required by applicable law, or where the Client has provided prior written consent.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">17. Drone Operations</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Drone operations are subject to weather conditions, airspace restrictions, local regulations, government restrictions, and safety considerations. Fast Elevate Media cannot guarantee that drone footage can be obtained at every location. Where drone operations are prohibited, restricted, or deemed unsafe, alternative filming methods may be used where possible.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">18. Cancellation Policy</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Unless otherwise agreed in writing, cancellations are subject to the following fees:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">More than 30 days before the assignment: no cancellation fee</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Between 14 and 30 days before the assignment: 50% of the agreed project fee</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Less than 14 days before the assignment: 100% of the agreed project fee</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Deposits are non-refundable except where cancellation results directly from Fast Elevate Media's inability to perform the agreed services. Any non-refundable expenses already incurred shall remain payable by the client.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">19. Force Majeure</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media shall not be liable for failure or delay in performing its obligations due to circumstances beyond its reasonable control, including illness, injury, extreme weather, natural disasters, travel disruptions, technical failures, internet outages, government restrictions, or venue closures.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">20. Limitation of Liability</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media shall not be liable for indirect, incidental, special, or consequential damages. To the maximum extent permitted by law, Fast Elevate Media's total liability shall be limited to the total amount invoiced for the relevant assignment. Nothing in these Terms excludes liability where such exclusion is prohibited by applicable law.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">21. Website Use</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            The content on this website is provided for general informational purposes only. Fast Elevate Media reserves the right to modify, suspend, or discontinue any aspect of the website at any time without prior notice. Users may not use the website in any unlawful manner or in any way that interferes with its operation.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">22. External Links</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            This website may contain links to third-party websites. Fast Elevate Media accepts no responsibility for the content, privacy practices, or policies of third-party websites.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">23. Privacy, Cookies and AI Processing</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            The collection and processing of personal data are governed by our Privacy Policy and Cookie Policy. Where AI-assisted software is used during editing or production workflows involving Client materials, Fast Elevate Media shall take reasonable measures to ensure that personal data is processed in accordance with applicable privacy legislation, including the General Data Protection Regulation (GDPR). AI tools are used solely to support creative production and administrative efficiency and do not replace human review or decision-making.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">24. Right of Withdrawal</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Where the Client is a consumer within the meaning of applicable law, statutory rights of withdrawal may apply. However, the statutory right of withdrawal may expire where the Client expressly requests Fast Elevate Media to commence the performance of the services during the withdrawal period and acknowledges that the right of withdrawal may be lost once the services have been fully performed. Custom photography, videography, editing, creative productions, and other personalised services are generally exempt from return or exchange once work has commenced.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">25. Governing Law</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            These Terms &amp; Conditions shall be governed by and interpreted in accordance with the laws of the Netherlands. Any disputes arising under these Terms shall be submitted to the competent courts of Amsterdam, The Netherlands.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">26. Contact Information</h3>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Amsterdam, The Netherlands<br/>
            Email: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Phone: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a><br/>
            Website: <a href="https://fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">www.fastelevatemedia.com</a>
          </p>"""

# Read and update terms.html
with open(terms_en_filepath, "r", encoding="utf-8") as f:
    terms_en_content = f.read()

start_tag = '<!-- LEFT: Terms Content -->'
end_tag = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag in terms_en_content and end_tag in terms_en_content:
    start_idx = terms_en_content.find(start_tag) + len(start_tag)
    end_idx = terms_en_content.find(end_tag)
    new_inner_en = "\n        <div class=\"flex-1 min-w-0 prose prose-sm max-w-none text-[#121111]\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + terms_en_replacement + "\n        </div>\n        "
    terms_en_content = terms_en_content[:start_idx] + new_inner_en + terms_en_content[end_idx:]
    with open(terms_en_filepath, "w", encoding="utf-8") as f:
        f.write(terms_en_content)
    print("Overwrote terms.html successfully.")

# 2. nl/terms.html (Dutch)
terms_nl_filepath = os.path.join(base_dir, "nl/terms.html")
terms_nl_replacement = """          <h2 class="text-2xl md:text-3xl font-black text-[#121111] mt-0 mb-3">Algemene Voorwaarden</h2>
          <p class="text-sm text-gray-500 font-semibold mb-6"><strong>Laatst bijgewerkt: juni 2026</strong></p>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">1. Inleiding</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-6">
            Deze Algemene Voorwaarden zijn van toepassing op het gebruik van de website van Fast Elevate Media en de levering van diensten door Fast Elevate Media.
            Door onze website te gebruiken, een offerte aan te vragen, gebruik te maken van onze diensten of een overeenkomst aan te gaan met Fast Elevate Media, gaat u akkoord met deze Algemene Voorwaarden.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">2. Bedrijfsinformatie</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            <strong>Fast Elevate Media</strong><br/>
            Kamer van Koophandel (KVK): 56193203<br/>
            BTW-nummer: NL002247193B30<br/>
            Amsterdam, Nederland<br/>
            E-mail: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a>
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">3. Diensten</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">Fast Elevate Media levert creatieve en mediadiensten, inclusief maar niet beperkt tot:</p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Fotografie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Videografie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Verslaglegging van bedrijfsevenementen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Dronefotografie en -videografie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Interviews en testimonials</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Creatie van social media content</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Montage en postproductie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Creatieve productiediensten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Marketing en promotionele content</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">4. Offertes en Overeenkomsten</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Alle offertes zijn vrijblijvend, tenzij uitdrukkelijk anders vermeld. Offertes blijven geldig gedurende 30 kalenderdagen na de datum van uitgifte, tenzij anders aangegeven.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Een overeenkomst komt tot stand wanneer:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">De klant een offerte schriftelijk accepteert;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">De klant een boeking bevestigt via e-mail, bericht of andere schriftelijke communicatie;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Fast Elevate Media op verzoek van de klant begint met de werkzaamheden.</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Eventuele wijzigingen in de overeengekomen omvang kunnen leiden tot extra kosten.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">5. Aanbetalingen, Tarieven en Betaling</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Tenzij anders vermeld, zijn alle prijzen exclusief btw.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Een niet-restitueerbare aanbetaling van 50% van het geoffreerde bedrag is vereist om een boeking te garanderen en productiedata te reserveren. Productiedata worden pas als bevestigd beschouwd wanneer de aanbetaling is ontvangen.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Het resterende saldo wordt gefactureerd na afronding van de opdracht, tenzij schriftelijk anders overeengekomen. Facturen dienen binnen 14 kalenderdagen na factuurdatum te worden voldaan.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media behoudt zich het recht voor om:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Lopende werkzaamheden op te schorten;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">De levering uit te stellen;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Opleveringen achter te houden;</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            totdat openstaande facturen volledig zijn voldaan. Wettelijke rente en incassokosten kunnen in rekening worden gebracht bij achterstallige facturen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">6. Meerwerk</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Alle werkzaamheden die buiten de overeengekomen omvang worden aangevraagd, kunnen als meerwerk worden beschouwd en afzonderlijk worden gefactureerd. Dit kan omvatten:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Extra opname-uren</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Extra montagewerk</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Extra op te leveren bestanden</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Extra revisierondes</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Extra reiskosten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Extra productie-eisen</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">7. Levertijden</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            De standaard levertijd van Fast Elevate Media voor de eerste versie van de meeste videoproducties is binnen drie (3) werkdagen na afronding van de opdracht, onder voorbehoud van de overeengekomen projectomvang, complexiteit en tijdige ontvangst van al het vereiste materiaal van de klant.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Versnelde leveringsopties kunnen beschikbaar zijn tegen een meerprijs, waaronder:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">48-uurs levering</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">24-uurs levering</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Same-day levering (dezelfde dag)</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Aangepaste leveringsschema's</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media spant zich redelijkerwijs in om de overeengekomen termijnen te halen, maar is niet aansprakelijk voor vertragingen die het gevolg zijn van omstandigheden buiten haar redelijke controle. Dit omvat, maar is niet beperkt tot:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Late feedback of vertraagde goedkeuringen van de klant</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Ontbrekende informatie, logo's, graphics of huisstijlmaterialen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Vertraging bij door de klant geleverde materialen</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Technische storingen of overmachtsituaties</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">8. Revisies en Acceptatie van Opleveringen</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Tenzij schriftelijk anders overeengekomen, zijn bij projecten maximaal twee revisierondes inbegrepen. Extra revisies kunnen afzonderlijk in rekening worden gebracht. Aanvragen die de oorspronkelijke omvang wezenlijk wijzigen, kunnen als een nieuw project worden behandeld en als zodanig worden gefactureerd.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Tenzij de klant binnen veertien (14) kalenderdagen na levering wezenlijke gebreken meldt, wordt het geleverde werk als geaccepteerd beschouwd. Geringe subjectieve verschillen in stijl, kleurcorrectie, montage, kadrering of creatieve interpretatie vormen geen gebreken.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">9. Verantwoordelijkheden van de Klant</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            De klant is verantwoordelijk voor:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Het verstrekken van nauwkeurige informatie, projectplanningen en details van het evenement</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Het verkrijgen van alle benodigde toestemmingen en het garanderen van toegang tot de locatie</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Het verstrekken van merkmaterialen waar nodig en het geven van tijdige feedback en goedkeuringen</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Voor opdrachten die langer duren dan zes opeenvolgende werkuren of plaatsvinden tijdens standaard maaltijduren, zorgt de klant voor redelijke maaltijden en verfrissingen voor het personeel en de ingehuurde freelancers van Fast Elevate Media die op locatie werken.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media is niet aansprakelijk voor vertragingen of problemen die voortvloeien uit onvolledige, onjuiste of vertraagde informatie die door de klant is verstrekt. Creatieve diensten zijn inherent subjectief. Geringe verschillen in montagestijl, kleurcorrectie, kadrering, tempo of creatieve interpretatie worden niet als gebreken beschouwd, mits het geleverde werk substantieel voldoet aan de overeengekomen projectbriefing.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">10. Materialen van de Klant</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            De klant garandeert dat alle aan Fast Elevate Media geleverde materialen legaal mogen worden gebruikt voor het aangevraagde project. Dit omvat logo's, merkelementen, afbeeldingen, video's, muziek, documenten en inhoud van derden.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            De klant vrijwaart Fast Elevate Media tegen alle claims die voortvloeien uit het onrechtmatig gebruik van de geleverde materialen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">11. Intellectueel Eigendom</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Tenzij schriftelijk anders overeengekomen, blijven alle auteursrechten en intellectuele eigendomsrechten op de door Fast Elevate Media gecreëerde inhoud het exclusieve eigendom van Fast Elevate Media. Er vindt geen overdracht van auteursrechten plaats, tenzij uitdrukkelijk schriftelijk overeengekomen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">12. Licentie voor het Gebruik van Opleveringen</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Na volledige betaling ontvangt de klant een niet-exclusieve licentie om de geleverde inhoud te gebruiken voor het overeengekomen doel.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Het is de klant niet toegestaan om:
          </p>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">De inhoud door te verkopen of rechten over te dragen aan derden;</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Het auteurschap te claimen of auteursrechtvermeldingen te wijzigen;</p>
            </li>
          </ul>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">13. RAW-bestanden en Bronmateriaal</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Tenzij schriftelijk anders overeengekomen, is Fast Elevate Media niet verplicht om RAW-foto's, onbewerkte videobeelden, montageprojectbestanden, tijdlijnen, bronbestanden, werkbestanden of productie-assets te leveren. Fast Elevate Media behoudt het eigendom van al het bronmateriaal.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">14. AI-ondersteunde Productie</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Fast Elevate Media kan gebruikmaken van kunstmatige intelligentie ("AI") ondersteunde technologieën als onderdeel van haar creatieve en administratieve workflow. Dergelijke tools kunnen worden gebruikt voor doeleinden zoals taalverfijning, transcriptie, het genereren van ondertiteling, audioverbetering, ruisonderdrukking, beeldverbetering, het verwijderen van objecten, achtergronduitbreidingen, video-editing-assistentie en workflowoptimalisatie.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            AI-technologieën worden uitsluitend gebruikt als ondersteunende productietools. Alle creatieve beslissingen, kwaliteitscontrole, montagebeslissingen en uiteindelijke opleveringen blijven onderworpen aan menselijke beoordeling en goedkeuring door Fast Elevate Media. Waar AI-ondersteunde montage het karakter van de overeengekomen oplevering wezenlijk verandert buiten de standaard postproductiepraktijken, zal dit alleen worden uitgevoerd wanneer dit passend is voor het project of is overeengekomen met de klant.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">15. Portfolio en Promotioneel Gebruik</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Tenzij schriftelijk anders overeengekomen, behoudt Fast Elevate Media zich het recht voor om de tijdens opdrachten gecreëerde inhoud te gebruiken voor portfoliodoeleinden, publicatie op de website, social media, marketingmateriaal, promotiecampagnes, prijsinzendingen en zakelijke ontwikkelingsactiviteiten.
          </p>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Deze clausule is alleen van toepassing op door Fast Elevate Media gecreëerde inhoud. Materialen ingediend via contactformulieren of verstrekt door potentiële klanten zullen nooit worden gebruikt voor promotionele doeleinden zonder expliciete schriftelijke toestemming. Fast Elevate Media zal door de klant ingediende materialen of AI-gegenereerde werkbestanden die afkomstig zijn van klantmaterialen nooit gebruiken voor portfolio- of promotionele doeleinden, tenzij expliciete schriftelijke toestemming is verkregen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">16. Vertrouwelijke Informatie</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media zal alle van de klant ontvangen vertrouwelijke informatie met de nodige zorg behandelen. Projectdocumentatie, presentaties, planningen, interne communicatie, details van evenementen, bedrijfsinformatie en andere door de klant verstrekte vertrouwelijke materialen worden niet aan derden bekendgemaakt, behalve waar nodig voor de uitvoering van de overeengekomen diensten, vereist door de toepasselijke wetgeving, of waar de klant voorafgaande schriftelijke toestemming heeft verleend.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">17. Drone-operaties</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Drone-operaties zijn afhankelijk van weersomstandigheden, luchtruimbeperkingen, lokale regelgeving, overheidsbeperkingen en veiligheidsoverwegingen. Fast Elevate Media kan niet garanderen dat er op elke locatie dronebeelden kunnen worden gemaakt. Waar drone-operaties verboden, beperkt of onveilig worden geacht, kunnen waar mogelijk alternatieve opnamemethoden worden gebruikt.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">18. Annuleringsvoorwaarden</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-4">
            Tenzij schriftelijk anders overeengekomen, gelden bij annulering de volgende kosten:
          </p>
          <ul class="space-y-3 mb-6">
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Meer dan 30 dagen voor de opdracht: geen annuleringskosten</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Tussen 14 and 30 dagen voor de opdracht: 50% van het overeengekomen projecttarief</p>
            </li>
            <li class="flex items-start gap-3">
              <span class="mt-1.5 w-2 h-2 rounded-full bg-primary flex-shrink-0"></span>
              <p class="text-sm text-gray-700 leading-relaxed">Minder dan 14 dagen voor de opdracht: 100% van het overeengekomen projecttarief</p>
            </li>
          </ul>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Aanbetalingen worden niet gerestitueerd, behalve wanneer de annulering het directe gevolg is van het onvermogen van Fast Elevate Media om de overeengekomen diensten uit te voeren. Reeds gemaakte niet-restitueerbare kosten blijven verschuldigd door de klant.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">19. Overmacht</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media is niet aansprakelijk voor het niet of vertraagd nakomen van haar verplichtingen als gevolg van omstandigheden buiten haar redelijke controle, waaronder ziekte, letsel, extreem weer, natuurrampen, reisonderbrekingen, technische storingen, internetuitval, overheidsbeperkingen of sluiting van locaties.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">20. Beperking van Aansprakelijkheid</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Fast Elevate Media is niet aansprakelijk voor indirecte, incidentele, bijzondere of gevolgschade. Voor zover maximaal toegestaan door de wet is de totale aansprakelijkheid van Fast Elevate Media beperkt tot het totale bedrag dat voor de desbetreffende opdracht is gefactureerd. Niets in deze Voorwaarden sluit aansprakelijkheid uit waar een dergelijke uitsluiting door de toepasselijke wetgeving is verboden.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">21. Gebruik van de Website</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            De inhoud op deze website wordt uitsluitend ter algemene informatie verstrekt. Fast Elevate Media behoudt zich het recht voor om elk aspect van de website op elk moment zonder voorafgaande kennisgeving te wijzigen, op te schorten of stop te zetten. Gebruikers mogen de website niet gebruiken op een onwettige manier of op een manier die de werking ervan verstoort.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">22. Externe Links</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Deze website kan links bevatten naar websites van derden. Fast Elevate Media aanvaardt geen verantwoordelijkheid voor de inhoud, het privacybeleid of het cookiebeleid van websites van derden.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">23. Privacy, Cookies en AI-verwerking</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Het verzamelen en verwerken van persoonlijke gegevens wordt beheerst door ons Privacybeleid en Cookiebeleid. Waar AI-ondersteunde software wordt gebruikt tijdens montage- of productieworkflows waarbij klantmaterialen betrokken zijn, neemt Fast Elevate Media redelijke maatregelen om ervoor te zorgen dat persoonlijke gegevens worden verwerkt in overeenstemming met de toepasselijke privacywetgeving, waaronder de Algemene Verordening Gegevensbescherming (AVG). AI-tools worden uitsluitend gebruikt ter ondersteuning van creatieve productie en administratieve efficiëntie en vervangen geen menselijke beoordeling of besluitvorming.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">24. Herroepingsrecht</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Wanneer de klant een consument is in de zin van de toepasselijke wetgeving, kunnen wettelijke herroepingsrechten van toepassing zijn. Het wettelijke herroepingsrecht kan echter vervallen wanneer de klant Fast Elevate Media uitdrukkelijk verzoekt om te beginnen met de uitvoering van de diensten tijdens de herroepingstermijn en erkent dat het herroepingsrecht verloren kan gaan zodra de diensten volledig zijn uitgevoerd. Maatwerkfotografie, videografie, montage, creatieve producties en andere gepersonaliseerde diensten zijn over het algemeen uitgesloten van herroeping of ruil zodra de werkzaamheden zijn begonnen.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">25. Toepasselijk Recht</h3>
          <p class="text-sm text-gray-700 leading-relaxed mb-8">
            Deze Algemene Voorwaarden worden beheerst door en geïnterpreteerd in overeenstemming met de Nederlandse wetgeving. Alle geschillen die voortvloeien uit deze Voorwaarden worden voorgelegd aan de bevoegde rechter in Amsterdam, Nederland.
          </p>

          <hr class="border-gray-200 my-8"/>

          <h3 class="text-xl md:text-2xl font-black text-[#121111] mt-8 mb-3">26. Contactgegevens</h3>
          <p class="text-sm text-gray-700 leading-relaxed">
            <strong>Fast Elevate Media</strong><br/>
            Amsterdam, Nederland<br/>
            E-mail: <a href="mailto:info@fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors">info@fastelevatemedia.com</a><br/>
            Telefoon: <a href="tel:+31628460837" class="text-primary underline hover:text-primary/80 transition-colors">+316 2846 0837</a><br/>
            Website: <a href="https://fastelevatemedia.com" class="text-primary underline hover:text-primary/80 transition-colors" target="_blank">www.fastelevatemedia.com</a>
          </p>"""

# Write English terms
with open(terms_en_filepath, "r", encoding="utf-8") as f:
    en_content = f.read()

start_tag = '<!-- LEFT: Terms Content -->'
end_tag = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag in en_content and end_tag in en_content:
    start_idx = en_content.find(start_tag) + len(start_tag)
    end_idx = en_content.find(end_tag)
    new_inner_en = "\n        <div class=\"flex-1 min-w-0 prose prose-sm max-w-none text-[#121111]\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + terms_en_replacement + "\n        </div>\n        "
    en_content = en_content[:start_idx] + new_inner_en + en_content[end_idx:]
    with open(terms_en_filepath, "w", encoding="utf-8") as f:
        f.write(en_content)
    print("Overwrote terms.html successfully.")

# Write Dutch terms
with open(terms_nl_filepath, "r", encoding="utf-8") as f:
    nl_content = f.read()

start_tag_nl = '<!-- LEFT: Terms Content -->'
end_tag_nl = '<!-- RIGHT: Sticky "Got any questions?" Card -->'
if start_tag_nl in nl_content and end_tag_nl in nl_content:
    start_idx_nl = nl_content.find(start_tag_nl) + len(start_tag_nl)
    end_idx_nl = nl_content.find(end_tag_nl)
    new_inner_nl = "\n        <div class=\"flex-1 min-w-0\" style=\"font-family:\'Lexend\',sans-serif;\">\n" + terms_nl_replacement + "\n        </div>\n        "
    nl_content = nl_content[:start_idx_nl] + new_inner_nl + nl_content[end_idx_nl:]
    with open(terms_nl_filepath, "w", encoding="utf-8") as f:
        f.write(nl_content)
    print("Overwrote nl/terms.html successfully.")
