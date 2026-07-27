/**
 * Snap Build Portal — Site Connector
 *
 * Zet de inhoud uit /content.json op de pagina en praat met de Visuele Editor
 * in het portaal. Kernregel: dit script raakt NOOIT de opmaak aan. Het zet
 * uitsluitend waarden op bestaande elementen (tekst, src, href, alt) en bouwt
 * nooit containers opnieuw op. Galleries groeien of krimpen door het eerste
 * bestaande item als sjabloon te klonen, zodat alle classes behouden blijven.
 *
 * De tags in de HTML komen van scripts/scan-site.mjs:
 *   data-vibe-section="Naam"   sectie
 *   data-vibe-field="veld"     tekst of afbeelding
 *   data-vibe-video="veld"     <video>-bron
 *   data-vibe-embed="veld"     iframe-embed (YouTube/Vimeo)
 *   data-vibe-link="veld"      href van een link
 *   data-vibe-gallery="veld"   gallery/portfolio-container
 */
(function () {
  "use strict";

  var CONTENT_URL = "/content.json";
  var GLOBAL_KEY = "__global";
  var META_KEY = "__meta";

  var params = new URLSearchParams(window.location.search);
  var IS_EDITOR_MODE = params.get("vibeEditor") === "1" || params.get("sbpEditor") === "1";
  var PARENT_ORIGIN = params.get("vibeOrigin") || params.get("sbpOrigin") || "*";

  // --- Pagina en taal bepalen --------------------------------------------

  function currentLang() {
    var match = window.location.pathname.match(/\/([a-z]{2})\//);
    if (match) return match[1];
    var htmlLang = (document.documentElement.getAttribute("lang") || "").slice(0, 2).toLowerCase();
    return htmlLang || "en";
  }

  function currentSlug() {
    var pathname = (window.location.pathname || "").replace(/\/+$/, "");
    var file = pathname.split("/").pop() || "";
    if (!file || file === "index.html" || /^[a-z]{2}$/.test(file)) return "home";
    return file.replace(/\.html$/i, "").toLowerCase();
  }

  // --- Waarden toepassen -------------------------------------------------

  function setText(node, value) {
    if (value == null) return;
    if (node instanceof HTMLInputElement || node instanceof HTMLTextAreaElement) {
      node.value = String(value);
      return;
    }
    node.innerHTML = String(value);
  }

  function setImage(node, value) {
    var url = typeof value === "string" ? value : value && value.url;
    if (!url) return;
    if (node instanceof HTMLImageElement) {
      node.src = url;
      return;
    }
    var nested = node.querySelector && node.querySelector("img");
    if (nested) {
      nested.src = url;
      return;
    }
    node.style.backgroundImage = 'url("' + url + '")';
  }

  function setVideo(node, url) {
    if (!url) return;
    var source = node.querySelector("source");
    if (source) {
      if (source.getAttribute("src") === url) return;
      source.setAttribute("src", url);
    } else {
      if (node.getAttribute("src") === url) return;
      node.setAttribute("src", url);
    }
    // Zonder load() blijft de speler op de oude bron hangen.
    if (typeof node.load === "function") node.load();
  }

  /**
   * Galleries: het aantal items volgt content.json, maar de opmaak komt uit
   * het bestaande eerste item. Zo kan de klant foto's toevoegen of weghalen
   * zonder dat classes, verhoudingen of hover-effecten veranderen.
   */
  function setGallery(container, items) {
    if (!Array.isArray(items) || items.length === 0) return false;
    var first = container.firstElementChild;
    if (!first) return false;

    var template = first.cloneNode(true);

    while (container.children.length > items.length) {
      container.removeChild(container.lastElementChild);
    }
    var grew = false;
    while (container.children.length < items.length) {
      container.appendChild(template.cloneNode(true));
      grew = true;
    }

    Array.prototype.forEach.call(container.children, function (child, index) {
      var item = items[index];
      var url = typeof item === "string" ? item : item && item.url;
      var alt = item && typeof item === "object" ? item.alt || "" : "";
      if (!url) return;

      var img = child.tagName === "IMG" ? child : child.querySelector("img");
      if (img) {
        img.src = url;
        if (alt) img.alt = alt;
      }
      // Lightboxes lezen de bron vaak van het item zelf; meelopen houdt ze kloppend.
      if (child.hasAttribute && child.hasAttribute("data-img-url")) {
        child.setAttribute("data-img-url", url);
      }
      if (alt && child.hasAttribute && child.hasAttribute("data-caption")) {
        child.setAttribute("data-caption", alt);
      }
    });

    return grew;
  }

  function applyMeta(meta) {
    if (!meta) return;
    if (meta.title) document.title = meta.title;
    if (meta.description) {
      var tag = document.querySelector('meta[name="description"]');
      if (!tag) {
        tag = document.createElement("meta");
        tag.setAttribute("name", "description");
        document.head.appendChild(tag);
      }
      tag.setAttribute("content", meta.description);
    }
  }

  // Hoort dit element bij déze sectie, of bij een geneste sectie?
  function ownedBy(node, sectionEl) {
    return node.closest("[data-vibe-section]") === sectionEl;
  }

  function applySection(name, fields) {
    if (!name || !fields) return false;
    var sections = document.querySelectorAll('[data-vibe-section="' + CSS.escape(name) + '"]');
    var galleryGrew = false;

    Array.prototype.forEach.call(sections, function (sectionEl) {
      sectionEl.querySelectorAll("[data-vibe-field]").forEach(function (node) {
        if (!ownedBy(node, sectionEl)) return;
        var field = node.getAttribute("data-vibe-field");
        var value = fields[field];
        if (value == null) return;

        if (node.tagName === "IMG") {
          setImage(node, value);
          var alt = fields[field + "_alt"];
          if (alt) node.alt = alt;
        } else {
          setText(node, value);
        }
      });

      sectionEl.querySelectorAll("[data-vibe-video]").forEach(function (node) {
        if (!ownedBy(node, sectionEl)) return;
        setVideo(node, fields[node.getAttribute("data-vibe-video")]);
      });

      sectionEl.querySelectorAll("[data-vibe-embed]").forEach(function (node) {
        if (!ownedBy(node, sectionEl)) return;
        var url = fields[node.getAttribute("data-vibe-embed")];
        if (url && node.getAttribute("src") !== url) node.setAttribute("src", url);
      });

      sectionEl.querySelectorAll("[data-vibe-link]").forEach(function (node) {
        if (!ownedBy(node, sectionEl)) return;
        var href = fields[node.getAttribute("data-vibe-link")];
        if (href) node.setAttribute("href", href);
      });

      sectionEl.querySelectorAll("[data-vibe-gallery]").forEach(function (node) {
        if (!ownedBy(node, sectionEl)) return;
        if (setGallery(node, fields[node.getAttribute("data-vibe-gallery")])) galleryGrew = true;
      });
    });

    return galleryGrew;
  }

  function applyPage(data) {
    var lang = currentLang();
    var slug = currentSlug();
    var langData = data[lang];
    if (!langData) {
      var firstLang = Object.keys(data).filter(function (k) { return k !== "__config"; })[0];
      langData = data[firstLang] || {};
    }
    var page = langData[slug] || {};
    var globals = langData[GLOBAL_KEY] || {};

    // Globale secties (header/footer) eerst; een pagina-eigen variant wint daarna.
    var merged = {};
    Object.keys(globals).forEach(function (k) { merged[k] = globals[k]; });
    Object.keys(page).forEach(function (k) { merged[k] = page[k]; });

    var galleryGrew = false;
    Object.keys(merged).forEach(function (name) {
      if (name === META_KEY) return;
      if (applySection(name, merged[name])) galleryGrew = true;
    });

    applyMeta(merged[META_KEY]);

    // Gekloonde gallery-items hebben nog geen klik-handlers van de site zelf.
    // Via dit event kan de site ze opnieuw binden.
    document.dispatchEvent(
      new CustomEvent("sbp:content-applied", {
        detail: { lang: lang, slug: slug, galleryGrew: galleryGrew },
      })
    );
  }

  // --- Analytics ---------------------------------------------------------

  function injectScriptOnce(key, src, onload) {
    if (document.querySelector('script[data-sbp-analytics="' + key + '"]')) {
      if (typeof onload === "function") onload();
      return;
    }
    var script = document.createElement("script");
    script.async = true;
    script.src = src;
    script.setAttribute("data-sbp-analytics", key);
    if (typeof onload === "function") script.onload = onload;
    document.head.appendChild(script);
  }

  function initAnalytics(config) {
    var a = config || {};
    var ga4 = String(a.ga4MeasurementId || "").trim();
    var gtm = String(a.gtmId || "").trim();
    var pixel = String(a.metaPixelId || "").trim();
    var linkedIn = String(a.linkedInPartnerId || "").trim();
    var plausible = String(a.plausibleDomain || "").trim();

    if (ga4) {
      window.dataLayer = window.dataLayer || [];
      window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
      injectScriptOnce("ga4", "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(ga4), function () {
        window.gtag("js", new Date());
        window.gtag("config", ga4);
      });
    }
    if (gtm) {
      injectScriptOnce("gtm", "https://www.googletagmanager.com/gtm.js?id=" + encodeURIComponent(gtm));
    }
    if (pixel) {
      injectScriptOnce("meta-pixel", "https://connect.facebook.net/en_US/fbevents.js", function () {
        if (typeof window.fbq === "function") return;
        window.fbq = function () {
          window.fbq.callMethod
            ? window.fbq.callMethod.apply(window.fbq, arguments)
            : window.fbq.queue.push(arguments);
        };
        window.fbq.queue = [];
        window.fbq("init", pixel);
        window.fbq("track", "PageView");
      });
    }
    if (linkedIn) {
      window._linkedin_partner_id = linkedIn;
      window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
      if (window._linkedin_data_partner_ids.indexOf(linkedIn) === -1) {
        window._linkedin_data_partner_ids.push(linkedIn);
      }
      injectScriptOnce("linkedin", "https://snap.licdn.com/li.lms-analytics/insight.min.js");
    }
    if (plausible && !document.querySelector('script[data-domain][src*="plausible.io/js/script"]')) {
      var script = document.createElement("script");
      script.defer = true;
      script.src = "https://plausible.io/js/script.js";
      script.setAttribute("data-domain", plausible);
      script.setAttribute("data-sbp-analytics", "plausible");
      document.head.appendChild(script);
    }
  }

  // --- Brug naar de Visuele Editor ---------------------------------------

  var EDITOR_STYLE =
    "[data-sbp-hl]{outline:2px solid #2563eb !important;outline-offset:2px;border-radius:3px}" +
    ".sbp-editor [data-vibe-field],.sbp-editor [data-vibe-gallery]," +
    ".sbp-editor [data-vibe-video],.sbp-editor [data-vibe-embed]{cursor:pointer}" +
    ".sbp-editor [data-vibe-field]:hover,.sbp-editor [data-vibe-gallery]:hover," +
    ".sbp-editor [data-vibe-video]:hover,.sbp-editor [data-vibe-embed]:hover" +
    "{outline:2px dashed #93c5fd;outline-offset:2px}";

  function post(payload) {
    if (!IS_EDITOR_MODE) return;
    window.parent.postMessage(payload, PARENT_ORIGIN);
  }

  function sectionNameOf(node) {
    var owner = node.closest("[data-vibe-section]");
    return owner ? owner.getAttribute("data-vibe-section") : null;
  }

  function highlight(sectionName, field) {
    document.querySelectorAll("[data-sbp-hl]").forEach(function (n) {
      n.removeAttribute("data-sbp-hl");
    });
    if (!sectionName || !field) return;
    var section = document.querySelector('[data-vibe-section="' + CSS.escape(sectionName) + '"]');
    if (!section) return;
    var esc = CSS.escape(field);
    var node = section.querySelector(
      '[data-vibe-field="' + esc + '"],[data-vibe-gallery="' + esc + '"],' +
        '[data-vibe-video="' + esc + '"],[data-vibe-embed="' + esc + '"],' +
        '[data-vibe-link="' + esc + '"]'
    );
    if (!node) return;
    node.setAttribute("data-sbp-hl", "1");
    node.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  function initEditorBridge() {
    if (!IS_EDITOR_MODE) return;

    document.documentElement.classList.add("sbp-editor");
    var style = document.createElement("style");
    style.textContent = EDITOR_STYLE;
    document.head.appendChild(style);

    // Klik in de preview → het portaal springt naar het bijbehorende veld.
    document.addEventListener(
      "click",
      function (event) {
        var node = event.target.closest(
          "[data-vibe-field],[data-vibe-gallery],[data-vibe-video],[data-vibe-embed]"
        );
        if (!node) return;
        event.preventDefault();
        event.stopPropagation();
        var field =
          node.getAttribute("data-vibe-field") ||
          node.getAttribute("data-vibe-gallery") ||
          node.getAttribute("data-vibe-video") ||
          node.getAttribute("data-vibe-embed");
        post({ type: "SBP_FIELD_CLICK", section: sectionNameOf(node), field: field });
      },
      true
    );

    window.addEventListener("message", function (event) {
      if (event.source !== window.parent) return;
      if (PARENT_ORIGIN !== "*" && event.origin !== PARENT_ORIGIN) return;
      var msg = event.data;
      if (!msg || typeof msg !== "object") return;

      if (msg.type === "SBP_APPLY_SECTION") {
        // Live voorbeeld terwijl er getypt wordt, nog zonder opslaan.
        applySection(msg.section, msg.fields || {});
      } else if (msg.type === "SBP_HIGHLIGHT") {
        highlight(msg.section, msg.field);
      } else if (msg.type === "SBP_RELOAD") {
        window.location.reload();
      }
    });
  }

  // --- Start -------------------------------------------------------------

  async function init() {
    initEditorBridge();

    var data = null;
    try {
      var res = await fetch(CONTENT_URL + "?t=" + Date.now(), { cache: "no-store" });
      if (res.ok) data = await res.json();
    } catch (err) {
      console.warn("[SBP] content.json niet geladen:", err);
    }
    if (!data) return;

    initAnalytics(data.__config && data.__config.analytics);

    try {
      applyPage(data);
    } catch (err) {
      console.error("[SBP] Fout bij toepassen van content:", err);
    }

    post({ type: "SBP_READY", lang: currentLang(), slug: currentSlug() });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
