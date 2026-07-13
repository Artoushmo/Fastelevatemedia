/**
 * Vibe Connector v1.2
 * Connects static websites to the Vibe portal via Supabase.
 */

const VIBE_CONFIG = {
  // 1) Fill these from your Supabase project settings.
  supabaseUrl: "https://rqvmjtdgwaizlgnfhptn.supabase.co",
  supabaseKey: "sb_publishable_K6cCt8Ywqnzy3-YD0qV9JA_QZzdm5YO",

  // 2) Fill this with the site id from the Vibe portal.
  siteId: "1bd48132-1f8a-401a-8699-7e529491c30b",

  // 3) Optional analytics hooks (leave empty when unused).
  analytics: {
    ga4MeasurementId: "",
    gtmId: "",
    metaPixelId: "",
    linkedInPartnerId: "",
    plausibleDomain: "",
  },
};

const hasConfiguredSupabase =
  /^https?:\/\//i.test(String(VIBE_CONFIG.supabaseUrl || "").trim()) &&
  String(VIBE_CONFIG.supabaseKey || "").trim().length > 20;
const hasConfiguredSiteId = !/^0{8}-0{4}-0{4}-0{4}-0{12}$/i.test(String(VIBE_CONFIG.siteId || "").trim());
const isConnectorConfigured = hasConfiguredSupabase && hasConfiguredSiteId;

let vibeClient = null;
if (isConnectorConfigured) {
  try {
    vibeClient = supabase.createClient(VIBE_CONFIG.supabaseUrl, VIBE_CONFIG.supabaseKey);
  } catch (err) {
    console.warn("[Vibe] Supabase init failed, connector running in editor-only mode.", err);
  }
}
const IS_EDITOR_MODE = window.self !== window.top;
const PARENT_ORIGIN = (() => {
  try {
    return document.referrer ? new URL(document.referrer).origin : "*";
  } catch {
    return "*";
  }
})();

const HTML_TEXT_SELECTOR = "h1,h2,h3,h4,h5,h6,p,span,li,a,button,label,small,strong,em,blockquote,figcaption";

const sendEditorEvent = (payload) => {
  if (!IS_EDITOR_MODE) return;
  window.parent.postMessage(payload, PARENT_ORIGIN);
};

const normalizeAnalytics = (raw) => ({
  ga4MeasurementId: String(raw?.ga4MeasurementId || "").trim(),
  gtmId: String(raw?.gtmId || "").trim(),
  metaPixelId: String(raw?.metaPixelId || "").trim(),
  linkedInPartnerId: String(raw?.linkedInPartnerId || "").trim(),
  plausibleDomain: String(raw?.plausibleDomain || "").trim(),
});

const getCurrentPageSlug = () => {
  let pathname = (window.location.pathname || "").trim();
  pathname = pathname.replace(/\/+$/g, "");

  if (
    !pathname || 
    pathname === "/" || 
    pathname === "/nl" || 
    pathname.endsWith("/index.html") || 
    pathname.endsWith("/index") ||
    pathname === "index.html"
  ) {
    return "home";
  }
  
  const segments = pathname.split("/").filter(Boolean);
  let lastSegment = segments[segments.length - 1] || "home";
  return (lastSegment.replace(/\.html$/i, "") || "home").toLowerCase();
};

const normalizeImageValue = (value) => {
  if (typeof value === "string") return value;
  if (value && typeof value === "object" && typeof value.url === "string") return value.url;
  return "";
};

const normalizeTextValue = (value) => {
  if (value == null) return "";
  return String(value).replace(/\s+/g, " ").trim();
};

const slugify = (value) =>
  String(value || "")
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "");

const getNodeText = (node) => {
  if (node instanceof HTMLInputElement || node instanceof HTMLTextAreaElement) {
    return node.value;
  }
  return node.textContent || "";
};

const getNodeImageUrl = (node) => {
  if (node instanceof HTMLImageElement) {
    return node.currentSrc || node.src || "";
  }

  const nestedImage = node.querySelector("img");
  if (nestedImage instanceof HTMLImageElement) {
    return nestedImage.currentSrc || nestedImage.src || "";
  }

  const styleAttr = node.getAttribute("style") || "";
  const bgMatch = styleAttr.match(/background(?:-image)?\s*:\s*url\((['"]?)([^'")]+)\1\)/i);
  return bgMatch?.[2] || "";
};

const getNodePathKey = (sectionElement, node) => {
  const chunks = [];
  let current = node;

  while (current && current !== sectionElement && current.parentElement) {
    const tag = current.tagName.toLowerCase();
    const siblings = Array.from(current.parentElement.children).filter(
      (sibling) => sibling.tagName === current.tagName
    );
    const index = Math.max(0, siblings.indexOf(current));
    chunks.push(`${tag}_${index}`);
    current = current.parentElement;
  }

  return chunks.reverse().join("__") || "root";
};

const ensureDetachedContainerSections = () => {
  const detachedContainers = Array.from(document.querySelectorAll("[data-vibe-list],[data-vibe-gallery]"));
  detachedContainers.forEach((node) => {
    if (node.closest("[data-vibe-section]")) return;

    const listField = node.getAttribute("data-vibe-list");
    const galleryField = node.getAttribute("data-vibe-gallery");
    const suffix = slugify(listField || galleryField || "content");
    const sectionName = suffix ? `Detached ${suffix}` : "Detached Content";
    node.setAttribute("data-vibe-section", sectionName);
  });
};

const ensureSectionElements = () => {
  ensureDetachedContainerSections();
  const explicit = Array.from(document.querySelectorAll("[data-vibe-section]"));
  if (explicit.length > 0) return explicit;

  const fallback = document.querySelector("main") || document.body;
  if (!fallback) return [];
  if (!fallback.getAttribute("data-vibe-section")) {
    fallback.setAttribute("data-vibe-section", "Main");
  }

  return [fallback];
};

const shouldSkipAutoTextNode = (sectionElement, node) => {
  if (!(node instanceof HTMLElement)) return true;
  if (node.hasAttribute("data-vibe-field")) return true;
  if (node.closest("script,style,noscript")) return true;

  const insideSpecial = node.closest("[data-vibe-gallery],[data-vibe-list],[data-vibe-image]");
  if (insideSpecial && insideSpecial !== sectionElement && !insideSpecial.contains(sectionElement)) {
    return true;
  }

  const raw = normalizeTextValue(getNodeText(node));
  if (!raw || raw.length < 2) return true;
  if (raw.length > 500) return true;

  const hasSemanticChildren = Array.from(node.children).some((child) => {
    const tag = child.tagName.toLowerCase();
    return ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "a", "span"].includes(tag);
  });

  return hasSemanticChildren;
};

const parseListItemsFromDom = (listNode) => {
  const children = Array.from(listNode.children);
  if (children.length === 0) return [];

  const items = [];

  children.forEach((child) => {
    const iframe = child.querySelector("iframe");
    const link = child.querySelector("a[href]");
    const heading = child.querySelector("h1,h2,h3,h4,h5,h6");
    const textParagraphs = Array.from(child.querySelectorAll("p")).map((node) => normalizeTextValue(node.textContent));

    const url = (iframe?.getAttribute("src") || link?.getAttribute("href") || "").trim();
    const title = normalizeTextValue(heading?.textContent || "");
    const subtitle = textParagraphs[0] || "";

    const yearMatch = (child.textContent || "").match(/\b(19|20)\d{2}\b/);
    const year = yearMatch ? yearMatch[0] : "";

    if (!url && !title && !subtitle && !year) return;

    items.push({
      title,
      subtitle,
      year,
      url,
      type: iframe ? "video" : "link",
    });
  });

  return items;
};

const discoverSectionSchema = (sectionElement, sectionIndex) => {
  const sectionType = sectionElement.getAttribute("data-vibe-section") || `Section ${sectionIndex + 1}`;
  const content = {};

  sectionElement.querySelectorAll("[data-vibe-field]").forEach((node) => {
    const key = node.getAttribute("data-vibe-field");
    if (!key) return;
    content[key] = normalizeTextValue(getNodeText(node));
  });

  sectionElement.querySelectorAll("[data-vibe-image]").forEach((node) => {
    const key = node.getAttribute("data-vibe-image");
    if (!key) return;
    const url = getNodeImageUrl(node);
    if (url) content[key] = url;
  });

  sectionElement.querySelectorAll("[data-vibe-gallery]").forEach((node) => {
    const key = node.getAttribute("data-vibe-gallery");
    if (!key) return;

    const galleryItems = Array.from(node.querySelectorAll("img"))
      .map((imageNode) => {
        const url = imageNode.currentSrc || imageNode.src || "";
        if (!url) return null;
        return {
          url,
          alt: imageNode.alt || "",
        };
      })
      .filter(Boolean);

    if (galleryItems.length > 0) {
      content[key] = galleryItems;
    }
  });

  sectionElement.querySelectorAll("[data-vibe-list]").forEach((node) => {
    const key = node.getAttribute("data-vibe-list");
    if (!key) return;
    const listItems = parseListItemsFromDom(node);
    if (listItems.length > 0) {
      content[key] = listItems;
    }
  });

  const autoTextNodes = Array.from(sectionElement.querySelectorAll(HTML_TEXT_SELECTOR));
  autoTextNodes.forEach((node) => {
    if (shouldSkipAutoTextNode(sectionElement, node)) return;

    let fieldKey = node.getAttribute("data-vibe-field");
    if (!fieldKey) {
      fieldKey = `auto_text_${slugify(getNodePathKey(sectionElement, node))}`;
      node.setAttribute("data-vibe-field", fieldKey);
    }

    if (content[fieldKey] == null) {
      content[fieldKey] = normalizeTextValue(getNodeText(node));
    }
  });

  const autoImageNodes = Array.from(sectionElement.querySelectorAll("img"));
  autoImageNodes.forEach((node) => {
    if (!(node instanceof HTMLElement)) return;
    if (node.closest("[data-vibe-gallery]")) return;

    let fieldKey = node.getAttribute("data-vibe-image");
    if (!fieldKey) {
      fieldKey = `auto_image_${slugify(getNodePathKey(sectionElement, node))}`;
      node.setAttribute("data-vibe-image", fieldKey);
    }

    if (content[fieldKey] == null) {
      const imageUrl = getNodeImageUrl(node);
      if (imageUrl) {
        content[fieldKey] = imageUrl;
      }
    }
  });

  return {
    sectionType,
    sortOrder: sectionIndex + 1,
    content,
  };
};

const collectPageSchema = () => {
  const pageSlug = getCurrentPageSlug();
  const sectionElements = ensureSectionElements();

  const sections = sectionElements.map((sectionElement, index) =>
    discoverSectionSchema(sectionElement, index)
  );

  return {
    pageSlug,
    sections,
  };
};

const emitPageSchema = () => {
  if (!IS_EDITOR_MODE) return;
  const payload = collectPageSchema();
  sendEditorEvent({
    type: "VIBE_PAGE_SCHEMA",
    pageSlug: payload.pageSlug,
    sections: payload.sections,
  });
};

const bindEditorForSchema = (schemaPayload) => {
  if (!IS_EDITOR_MODE) return;
  (schemaPayload?.sections || []).forEach((section) => {
    const sectionType = String(section?.sectionType || "").trim();
    if (!sectionType) return;
    const elements = document.querySelectorAll(`[data-vibe-section="${sectionType}"]`);
    elements.forEach((element) => {
      const provisionalId = `__schema__${slugify(sectionType) || "section"}`;
      ensureEditorBindings(
        {
          id: provisionalId,
          section_type: sectionType,
        },
        element
      );
    });
  });
};

const setTextValue = (node, value) => {
  if (value == null) return;
  if (node instanceof HTMLInputElement || node instanceof HTMLTextAreaElement) {
    node.value = String(value);
    return;
  }
  node.innerHTML = String(value);
};

const setImageValue = (node, value) => {
  const url = normalizeImageValue(value);
  if (!url) return;

  if (node instanceof HTMLImageElement) {
    node.src = url;
    return;
  }

  const nestedImage = node.querySelector("img");
  if (nestedImage instanceof HTMLImageElement) {
    nestedImage.src = url;
    return;
  }

  node.style.backgroundImage = `url("${url}")`;
};

const renderGenericGallery = (galleryEl, galleryData) => {
  galleryEl.innerHTML = "";
  galleryData.forEach((imageItem) => {
    const imageUrl = normalizeImageValue(imageItem);
    if (!imageUrl) return;

    const alt = typeof imageItem === "object" && imageItem ? imageItem.alt || "" : "";
    const item = document.createElement("div");
    item.className = "gallery-item cursor-pointer aspect-[4/5] overflow-hidden bg-gray-100 reveal-on-scroll active";
    item.innerHTML = `<img src="${imageUrl}" alt="${alt}" class="w-full h-full object-cover">`;
    item.onclick = () => {
      if (typeof openLightbox === "function") openLightbox(imageUrl);
    };
    galleryEl.appendChild(item);
  });
};

const renderHeroSlideshow = (galleryNode, galleryData) => {
  if (!Array.isArray(galleryData) || galleryData.length === 0) return;

  const existingSlides = Array.from(galleryNode.querySelectorAll(".hero-slide"));

  // Keep existing slide nodes so inline slideshow timers that captured these nodes keep working.
  if (existingSlides.length > 0) {
    existingSlides.forEach((slide, index) => {
      const item = galleryData[index];
      if (!item) {
        slide.style.display = "none";
        slide.classList.remove("active");
        return;
      }

      const imageUrl = normalizeImageValue(item);
      const alt = typeof item === "object" && item ? item.alt || "" : "";
      slide.style.display = "";
      if (imageUrl) slide.src = imageUrl;
      slide.alt = alt;
    });

    const hasActiveVisible = existingSlides.some(
      (slide) => slide.classList.contains("active") && slide.style.display !== "none"
    );
    if (!hasActiveVisible) {
      const firstVisible = existingSlides.find((slide) => slide.style.display !== "none");
      if (firstVisible) firstVisible.classList.add("active");
    }
    return;
  }

  galleryNode.innerHTML = galleryData
    .map((imageItem, index) => {
      const imageUrl = normalizeImageValue(imageItem);
      const alt = typeof imageItem === "object" && imageItem ? imageItem.alt || "" : "";
      return `<img src="${imageUrl}" alt="${alt}" class="hero-slide ${index === 0 ? "active" : ""}">`;
    })
    .join("");
};

const renderGenericList = (listNode, listData) => {
  listNode.innerHTML = "";

  listData.forEach((item) => {
    const sectionItem = document.createElement("section");
    sectionItem.className = "space-y-8 reveal-on-scroll active";

    if (item?.type === "video" || (item?.url && String(item.url).includes("youtube"))) {
      sectionItem.innerHTML = `
        <div class="video-container shadow-2xl overflow-hidden rounded-xl bg-black">
          <iframe src="${item.url || ""}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div class="flex justify-between items-end border-b border-gray-100 pb-8">
          <div>
            <h2 class="font-display font-bold text-3xl uppercase tracking-tight">${item.title || "Untitled Video"}</h2>
            <p class="text-gray-400 uppercase text-xs tracking-widest mt-2">${item.subtitle || "Production"}</p>
          </div>
          <span class="text-sm font-medium text-brand-accent">${item.year || "2024"}</span>
        </div>
      `;
    } else {
      sectionItem.innerHTML = `
        <div class="p-8 bg-slate-50 rounded-xl border border-gray-100">
          <h2 class="font-display font-bold text-2xl uppercase">${item?.title || "Untitled"}</h2>
          <p class="mt-2 text-gray-500">${item?.description || ""}</p>
          <a href="${item?.url || "#"}" target="_blank" class="inline-block mt-4 text-sm font-bold uppercase tracking-widest text-brand-dark hover:text-blue-600 transition-colors">View Link -></a>
        </div>
      `;
    }

    listNode.appendChild(sectionItem);
  });
};

const sendTextUpdate = (section, fieldName, nextValue) => {
  sendEditorEvent({
    type: "VIBE_TEXT_UPDATE",
    sectionId: section.id,
    pageSlug: getCurrentPageSlug(),
    sectionType: section.section_type,
    field: fieldName,
    value: nextValue,
  });
};

const ensureEditorBindings = (section, sectionElement) => {
  if (!IS_EDITOR_MODE) return;

  sectionElement.querySelectorAll("[data-vibe-field]").forEach((fieldNode) => {
    const fieldName = fieldNode.getAttribute("data-vibe-field");
    if (!fieldName || fieldNode.hasAttribute("data-vibe-bound-edit")) return;

    if (!(fieldNode instanceof HTMLInputElement) && !(fieldNode instanceof HTMLTextAreaElement)) {
      fieldNode.setAttribute("contenteditable", "true");
      if (fieldNode instanceof HTMLAnchorElement) {
        fieldNode.addEventListener("click", (event) => event.preventDefault());
      }
    }

    let inputDebounce = null;
    const readValue = () =>
      fieldNode instanceof HTMLInputElement || fieldNode instanceof HTMLTextAreaElement
        ? fieldNode.value
        : fieldNode.textContent || "";
    const emitUpdate = () => {
      sendTextUpdate(section, fieldName, readValue());
    };

    fieldNode.addEventListener("blur", emitUpdate);
    fieldNode.addEventListener("input", () => {
      if (inputDebounce) {
        window.clearTimeout(inputDebounce);
      }
      inputDebounce = window.setTimeout(() => {
        emitUpdate();
      }, 350);
    });

    fieldNode.setAttribute("data-vibe-bound-edit", "1");
  });

  sectionElement.querySelectorAll("[data-vibe-image]").forEach((imageNode) => {
    const fieldName = imageNode.getAttribute("data-vibe-image");
    if (!fieldName || imageNode.hasAttribute("data-vibe-bound-edit")) return;

    imageNode.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      sendEditorEvent({
        type: "VIBE_IMAGE_CLICK",
        sectionId: section.id,
        pageSlug: getCurrentPageSlug(),
        sectionType: section.section_type,
        field: fieldName,
      });
    });

    imageNode.setAttribute("data-vibe-bound-edit", "1");
  });

  sectionElement.querySelectorAll("[data-vibe-gallery]").forEach((galleryNode) => {
    const fieldName = galleryNode.getAttribute("data-vibe-gallery");
    if (!fieldName || galleryNode.hasAttribute("data-vibe-bound-edit")) return;

    galleryNode.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      sendEditorEvent({
        type: "VIBE_GALLERY_CLICK",
        sectionId: section.id,
        pageSlug: getCurrentPageSlug(),
        sectionType: section.section_type,
        field: fieldName,
      });
    });

    galleryNode.setAttribute("data-vibe-bound-edit", "1");
  });

  sectionElement.querySelectorAll("[data-vibe-list]").forEach((listNode) => {
    const fieldName = listNode.getAttribute("data-vibe-list");
    if (!fieldName || listNode.hasAttribute("data-vibe-bound-edit")) return;

    listNode.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      sendEditorEvent({
        type: "VIBE_LIST_CLICK",
        sectionId: section.id,
        pageSlug: getCurrentPageSlug(),
        sectionType: section.section_type,
        field: fieldName,
      });
    });

    listNode.setAttribute("data-vibe-bound-edit", "1");
  });
};

const applySectionContent = (section) => {
  const sectionElements = document.querySelectorAll(`[data-vibe-section="${section.section_type}"]`);

  sectionElements.forEach((sectionElement) => {
    discoverSectionSchema(sectionElement, 0);

    sectionElement.querySelectorAll("[data-vibe-field]").forEach((fieldNode) => {
      const fieldName = fieldNode.getAttribute("data-vibe-field");
      if (!fieldName) return;
      if (section.content?.[fieldName] != null) {
        setTextValue(fieldNode, section.content[fieldName]);
      }
    });

    sectionElement.querySelectorAll("[data-vibe-image]").forEach((imageNode) => {
      const fieldName = imageNode.getAttribute("data-vibe-image");
      if (!fieldName) return;
      if (section.content?.[fieldName] != null) {
        setImageValue(imageNode, section.content[fieldName]);
      }
    });

    sectionElement.querySelectorAll("[data-vibe-gallery]").forEach((galleryNode) => {
      const fieldName = galleryNode.getAttribute("data-vibe-gallery");
      if (!fieldName) return;

      const galleryData = section.content?.[fieldName];
      if (Array.isArray(galleryData)) {
        if (galleryNode.classList.contains("hero-slideshow")) {
          renderHeroSlideshow(galleryNode, galleryData);
        } else {
          renderGenericGallery(galleryNode, galleryData);
        }
      }
    });

    sectionElement.querySelectorAll("[data-vibe-list]").forEach((listNode) => {
      const fieldName = listNode.getAttribute("data-vibe-list");
      if (!fieldName) return;
      const listData = section.content?.[fieldName];
      if (Array.isArray(listData)) {
        renderGenericList(listNode, listData);
      }
    });

    ensureEditorBindings(section, sectionElement);
  });
};

// Cache for loaded JSON content to avoid duplicate fetches
let cachedJsonContent = null;

async function loadJsonContent() {
  try {
    const res = await fetch("/content.json?t=" + Date.now());
    if (!res.ok) throw new Error("Status " + res.status);
    cachedJsonContent = await res.json();
    return cachedJsonContent;
  } catch (err) {
    console.warn("[Vibe] Failed to load content.json:", err);
    return null;
  }
}

async function fetchLiveAnalyticsConfig() {
  try {
    const data = await loadJsonContent();
    const merged = {
      ...(VIBE_CONFIG.analytics || {}),
      ...(data?.__config?.analytics || {}),
    };
    return normalizeAnalytics(merged);
  } catch (err) {
    console.warn("[Vibe] Analytics config unexpected error:", err);
    return normalizeAnalytics(VIBE_CONFIG.analytics || {});
  }
}

async function initVibeContent() {
  const pageSlug = getCurrentPageSlug();
  ensureSectionElements();
  const discoveredSchema = collectPageSchema();
  bindEditorForSchema(discoveredSchema);

  // Detect page language based on URL path or document attribute
  const lang = (typeof window !== "undefined" && (window.location.pathname.includes("/nl/") || document.documentElement.lang === "nl")) ? "nl" : "en";

  try {
    const fullData = await loadJsonContent();
    if (!fullData) return;
    const pageData = fullData[lang]?.[pageSlug] || {};
    
    Object.entries(pageData).forEach(([sectionType, content]) => {
      applySectionContent({
        section_type: sectionType,
        content: content
      });
    });
  } catch (err) {
    console.error("[Vibe] Error applying content from JSON:", err);
  }
}

const acceptsEditorMessage = (event) => {
  if (!IS_EDITOR_MODE) return false;
  if (event.source !== window.parent) return false;
  if (PARENT_ORIGIN !== "*" && event.origin !== PARENT_ORIGIN) return false;
  if (!event.data || typeof event.data !== "object") return false;
  return true;
};

const initEditorMessageBridge = () => {
  if (!IS_EDITOR_MODE) return;

  window.addEventListener("message", (event) => {
    if (!acceptsEditorMessage(event)) return;
    if (event.data.type === "VIBE_REQUEST_SCHEMA") {
      emitPageSchema();
    }
  });
};

const PORTFOLIO_CATEGORY_FALLBACKS = {
  events: "images/events/event-1.png",
  portraits: "images/portraits/portrait-1.png",
  products: "images/products/product-1.png",
};

const getProjectCover = (project) => {
  const media = Array.isArray(project?.project_media) ? [...project.project_media] : [];
  media.sort((a, b) => (a?.position ?? a?.sort_order ?? 0) - (b?.position ?? b?.sort_order ?? 0));
  const firstWithUrl = media.find((item) => item?.file_url || item?.url);
  return (firstWithUrl?.file_url || firstWithUrl?.url || "").trim();
};

const renderPortfolio = (projects, container, category) => {
  const validProjects = (projects || [])
    .map((project) => ({ ...project, __cover: getProjectCover(project) }))
    .filter((project) => Boolean(project.__cover));

  if (validProjects.length === 0) {
    return false;
  }

  const fallback = PORTFOLIO_CATEGORY_FALLBACKS[String(category || "").toLowerCase()] || "images/products/product-1.png";
  container.innerHTML = "";
  validProjects.forEach((project) => {
    const cover = project.__cover;

    const item = document.createElement("div");
    item.className = "gallery-item cursor-pointer aspect-[4/5] overflow-hidden bg-gray-100 reveal-on-scroll active";
    item.innerHTML = `
      <img src="${cover}" alt="${project?.title || "Project"}" class="w-full h-full object-cover" onerror="this.onerror=null;this.src='${fallback}'">
      <div class="portfolio-overlay">
        <h3 class="text-white font-bold p-4">${project?.title || "Untitled project"}</h3>
      </div>
    `;
    item.onclick = () => {
      if (typeof openLightbox === "function") openLightbox(cover || fallback);
    };
    container.appendChild(item);
  });

  return true;
};

async function loadVibePortfolio(category, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  if (!vibeClient || !isConnectorConfigured) return;

  const { data: projects, error } = await vibeClient
    .from("projects")
    .select("id,title,project_media (file_url,url,position,sort_order)")
    .eq("site_id", VIBE_CONFIG.siteId)
    .eq("category", category)
    .eq("status", "Gepubliceerd")
    .order("created_at", { ascending: false });

  if (error) {
    console.error("[Vibe] Error loading portfolio:", error);
    return;
  }

  const rendered = renderPortfolio(projects || [], container, category);
  if (!rendered) {
    console.warn(`[Vibe] No valid project media found for category: ${category}. Keeping static gallery.`);
  }
}

const injectScriptOnce = (key, src, onload) => {
  if (document.querySelector(`script[data-vibe-analytics="${key}"]`)) {
    if (typeof onload === "function") onload();
    return;
  }
  const script = document.createElement("script");
  script.async = true;
  script.src = src;
  script.setAttribute("data-vibe-analytics", key);
  if (typeof onload === "function") script.onload = onload;
  document.head.appendChild(script);
};

const initAnalytics = (analytics) => {
  const safeAnalytics = normalizeAnalytics(analytics || VIBE_CONFIG.analytics || {});
  const ga4 = safeAnalytics.ga4MeasurementId;
  const gtm = safeAnalytics.gtmId;
  const pixel = safeAnalytics.metaPixelId;
  const linkedIn = safeAnalytics.linkedInPartnerId;
  const plausibleDomain = safeAnalytics.plausibleDomain;

  if (ga4) {
    window.dataLayer = window.dataLayer || [];
    window.gtag =
      window.gtag ||
      function gtag() {
        window.dataLayer.push(arguments);
      };
    injectScriptOnce("ga4", `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(ga4)}`, () => {
      window.gtag("js", new Date());
      window.gtag("config", ga4);
    });
  }

  if (gtm) {
    injectScriptOnce("gtm", `https://www.googletagmanager.com/gtm.js?id=${encodeURIComponent(gtm)}`);
  }

  if (pixel) {
    injectScriptOnce("meta-pixel", "https://connect.facebook.net/en_US/fbevents.js", () => {
      if (typeof window.fbq === "function") return;
      window.fbq =
        window.fbq ||
        function fbq() {
          window.fbq.callMethod
            ? window.fbq.callMethod.apply(window.fbq, arguments)
            : window.fbq.queue.push(arguments);
        };
      if (!window.fbq.queue) window.fbq.queue = [];
      window.fbq.loaded = true;
      window.fbq.version = "2.0";
      window.fbq("init", pixel);
      window.fbq("track", "PageView");
    });
  }

  if (linkedIn) {
    window._linkedin_partner_id = linkedIn;
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    if (!window._linkedin_data_partner_ids.includes(linkedIn)) {
      window._linkedin_data_partner_ids.push(linkedIn);
    }
    injectScriptOnce("linkedin", "https://snap.licdn.com/li.lms-analytics/insight.min.js");
  }

  if (plausibleDomain) {
    if (!document.querySelector('script[data-domain][src*="plausible.io/js/script"]')) {
      const script = document.createElement("script");
      script.defer = true;
      script.src = "https://plausible.io/js/script.js";
      script.setAttribute("data-domain", plausibleDomain);
      script.setAttribute("data-vibe-analytics", "plausible");
      document.head.appendChild(script);
    }
  }
};

window.loadVibePortfolio = loadVibePortfolio;

document.addEventListener("DOMContentLoaded", async () => {
  if (IS_EDITOR_MODE) {
    document.documentElement.classList.add("vibe-editor-mode");
  }

  initEditorMessageBridge();

  const liveAnalytics = await fetchLiveAnalyticsConfig();
  initAnalytics(liveAnalytics);

  await initVibeContent();
  emitPageSchema();
});
