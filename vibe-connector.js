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

  /**
   * Een #t=-fragment dat voorbij het einde van de clip ligt levert het zwarte
   * eindframe op als stilstaand beeld. De bedoeling van zo'n fragment is juist
   * om een intro over te slaan, dus vallen we terug op een frame vroeg in de
   * clip. Zonder dit toont een te korte clip een zwarte tegel.
   */
  function fixOutOfRangeSeek(node, url) {
    var fragment = /#t=(\d+(?:\.\d+)?)/.exec(url);
    if (!fragment) return;
    var wanted = parseFloat(fragment[1]);

    var correct = function () {
      if (!isFinite(node.duration) || node.duration === 0) return;
      if (wanted < node.duration) return;
      node.currentTime = Math.min(1, node.duration / 4);
    };

    if (node.readyState >= 1) {
      correct();
      return;
    }
    var onMeta = function () {
      node.removeEventListener("loadedmetadata", onMeta);
      correct();
    };
    node.addEventListener("loadedmetadata", onMeta);
  }

  function setVideo(node, url) {
    if (!url) return;
    var source = node.querySelector("source");
    var current = source ? source.getAttribute("src") : node.getAttribute("src");

    if (current !== url) {
      if (source) source.setAttribute("src", url);
      else node.setAttribute("src", url);
      // Zonder load() blijft de speler op de oude bron hangen.
      if (typeof node.load === "function") node.load();
    }

    fixOutOfRangeSeek(node, url);
  }

  function mediaElementOf(child) {
    if (child.tagName === "IMG" || child.tagName === "VIDEO") return child;
    return child.querySelector("img, video");
  }

  /**
   * Zorgt dat een tegel het juiste mediatype toont. Alleen het blad-element
   * (img of video) wordt verwisseld; de tegel zelf — met al zijn classes,
   * verhoudingen en overlays — blijft ongemoeid. Dat is precies hoe de site
   * het zelf ook doet: dezelfde wrapper, een ander mediabeeld erin.
   */
  /**
   * Classes die naar het mediatype verwijzen mogen niet meeverhuizen. Sites
   * zoeken elementen op zulke classes op — een <img> met `gallery-video` krijgt
   * dan `.play()` aangeroepen, wat een fout geeft. Opmaakclasses blijven wel.
   */
  function stripTypeClasses(className, wantVideo) {
    return String(className || "")
      .split(/\s+/)
      .filter(Boolean)
      .filter(function (token) {
        return wantVideo ? !/(img|image|photo|foto)/i.test(token) : !/video/i.test(token);
      })
      .join(" ");
  }

  function ensureMediaType(child, wantVideo) {
    var current = mediaElementOf(child);
    if (!current) return null;
    var wantTag = wantVideo ? "VIDEO" : "IMG";
    if (current.tagName === wantTag) return current;

    var replacement = document.createElement(wantVideo ? "video" : "img");
    replacement.className = stripTypeClasses(current.className, wantVideo);
    if (wantVideo) {
      replacement.muted = true;
      replacement.loop = true;
      replacement.playsInline = true;
      replacement.setAttribute("preload", "auto");
      replacement.appendChild(document.createElement("source"));
    }
    current.replaceWith(replacement);
    return replacement;
  }

  function normalizeGalleryItem(item) {
    if (typeof item === "string") return { url: item };
    return item && typeof item === "object" ? item : null;
  }

  /**
   * Galleries: het aantal tegels volgt content.json, maar de opmaak komt uit
   * de bestaande tegels. Foto- en videotegels hebben elk hun eigen sjabloon,
   * zodat de klant beide types kan toevoegen zonder dat classes,
   * verhoudingen of hover-effecten veranderen.
   */
  /**
   * Kiest de tegel die als sjabloon dient voor nieuwe items: de vorm die het
   * vaakst voorkomt. Niet simpelweg de eerste — galerijen openen vaak met een
   * bewust bredere tegel (md:col-span-2), en die klonen zou elke toegevoegde
   * foto dubbelbreed maken.
   */
  function pickTemplate(children, wantVideo) {
    var counts = {};
    var byClass = {};
    var best = null;

    children.forEach(function (child) {
      var media = mediaElementOf(child);
      if (!media) return;
      if ((media.tagName === "VIDEO") !== wantVideo) return;
      var key = child.className || "";
      counts[key] = (counts[key] || 0) + 1;
      if (!byClass[key]) byClass[key] = child;
      if (!best || counts[key] > counts[best]) best = key;
    });

    return best === null ? null : byClass[best].cloneNode(true);
  }

  function setGallery(container, rawItems) {
    if (!Array.isArray(rawItems)) return false;
    // Tegels zonder beeld én zonder clip hebben niets te tonen; ze zouden als
    // leeg grijs vlak op de site verschijnen. Ze blijven wel in content.json
    // staan, zodat de klant ze in de editor kan afmaken.
    var items = rawItems
      .map(normalizeGalleryItem)
      .filter(function (item) {
        return item && (item.url || item.clip);
      });
    if (!items.length || !container.firstElementChild) return false;

    // Sjablonen kiezen vóór er iets gewijzigd wordt.
    var children = Array.prototype.slice.call(container.children);
    var photoTemplate = pickTemplate(children, false);
    var videoTemplate = pickTemplate(children, true);
    var fallback = photoTemplate || videoTemplate;
    if (!fallback) return false;

    while (container.children.length > items.length) {
      container.removeChild(container.lastElementChild);
    }
    var grew = false;
    while (container.children.length < items.length) {
      container.appendChild(fallback.cloneNode(true));
      grew = true;
    }

    Array.prototype.forEach.call(container.children, function (child, index) {
      var item = items[index];
      var wantVideo = Boolean(item.clip);

      // Wisselt de tegel van type, begin dan van het juiste sjabloon zodat
      // ook overlay-iconen (vergrootglas versus play-knop) kloppen.
      var current = mediaElementOf(child);
      var isVideoNow = Boolean(current && current.tagName === "VIDEO");
      if (wantVideo !== isVideoNow) {
        var source = wantVideo ? videoTemplate : photoTemplate;
        if (source) {
          var fresh = source.cloneNode(true);
          // Deze plek in het raster houdt zijn eigen vorm — een bredere
          // openingstegel blijft breed; alleen het mediatype verandert.
          if (child.className) fresh.className = child.className;
          child.replaceWith(fresh);
          child = fresh;
        }
      }

      var media = ensureMediaType(child, wantVideo);
      if (media) {
        if (wantVideo) {
          setVideo(media, item.clip);
          if (item.url) media.poster = item.url;
        } else if (item.url) {
          media.src = item.url;
          // Een eigen alt-tekst wint; anders dient het bijschrift als
          // beschrijving voor schermlezers en zoekmachines.
          var altText = item.alt || item.caption;
          if (altText) media.alt = altText;
        }
      }

      // De lightbox van de site leest deze attributen; meelopen houdt hem
      // kloppend, ook voor pas toegevoegde tegels.
      if (child.hasAttribute("data-img-url") || item.url) {
        if (item.url) child.setAttribute("data-img-url", item.url);
      }
      child.setAttribute("data-video-url", item.videoUrl || "");
      var caption = item.caption || item.alt;
      if (caption) child.setAttribute("data-caption", caption);
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

      // Tegels die een Vimeo/YouTube-video openen via een data-attribuut.
      sectionEl.querySelectorAll("[data-vibe-videolink]").forEach(function (node) {
        if (!ownedBy(node, sectionEl)) return;
        var url = fields[node.getAttribute("data-vibe-videolink")];
        if (url != null) node.setAttribute("data-video-url", url);
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
    ".sbp-editor [data-vibe-video],.sbp-editor [data-vibe-embed]," +
    ".sbp-editor [data-vibe-videolink]{cursor:pointer}" +
    ".sbp-editor [data-vibe-field]:hover,.sbp-editor [data-vibe-gallery]:hover," +
    ".sbp-editor [data-vibe-video]:hover,.sbp-editor [data-vibe-embed]:hover," +
    ".sbp-editor [data-vibe-videolink]:hover" +
    "{outline:2px dashed #93c5fd;outline-offset:2px}";

  // Cookiebanners van de site zelf horen niet in de weg te zitten tijdens het
  // bewerken — vooral niet als de toestemming van de klant niet blijft hangen
  // in een cross-origin preview-iframe (browsers isoleren opslag daar vaak
  // per herkomst) en de banner dus telkens terugkomt. Puur zichtbaarheid: de
  // regels gelden alleen binnen .sbp-editor, dus nooit voor echte bezoekers.
  var COOKIE_BANNER_STYLE =
    '.sbp-editor [id*="cookie-banner" i],.sbp-editor [id*="cookie-consent" i],' +
    '.sbp-editor [id*="cookie-overlay" i],.sbp-editor [id*="cookiebanner" i],' +
    '.sbp-editor [id*="cookieconsent" i],.sbp-editor [class*="cookie-banner" i],' +
    '.sbp-editor [class*="cookie-consent" i],.sbp-editor [class*="cookiebanner" i],' +
    '.sbp-editor [class*="cookieconsent" i]{display:none !important}';

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
        '[data-vibe-link="' + esc + '"],[data-vibe-videolink="' + esc + '"]'
    );
    if (!node) return;
    node.setAttribute("data-sbp-hl", "1");
    node.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  var TAGGED_SELECTOR =
    "[data-vibe-field],[data-vibe-gallery],[data-vibe-video],[data-vibe-embed],[data-vibe-videolink]";

  /**
   * Zoekt het bewerkbare element op de klikpositie zelf, niet alleen bij de
   * voorouders van het geklikte element. Een hover-overlay of een omhullende
   * link die visueel boven een getagde foto ligt is vaak geen voorouder van
   * die foto in de DOM — closest() zou hem dan mislopen. elementsFromPoint
   * doorloopt de hele stapel elementen op die plek, dus vindt de foto er wél
   * onder, ook al ligt er iets overheen.
   */
  function findTaggedAtPoint(x, y) {
    var stack =
      typeof document.elementsFromPoint === "function" ? document.elementsFromPoint(x, y) : [];
    for (var i = 0; i < stack.length; i++) {
      var el = stack[i];
      var match = el.matches && el.matches(TAGGED_SELECTOR) ? el : el.closest(TAGGED_SELECTOR);
      if (match) return match;
    }
    return null;
  }

  function initEditorBridge() {
    if (!IS_EDITOR_MODE) return;

    document.documentElement.classList.add("sbp-editor");
    var style = document.createElement("style");
    style.textContent = EDITOR_STYLE + COOKIE_BANNER_STYLE;
    document.head.appendChild(style);

    // In bewerkmodus mag niets in de preview ooit wegnavigeren — de klant
    // wisselt van pagina uitsluitend via de paginakiezer in het portaal.
    // Een klik onderschept daarom altijd eerst de standaardactie van links en
    // knoppen; is er een bewerkbaar element op die plek, dan springt het
    // portaal ernaartoe. Zonder match gebeurt er verder niets — de klik is
    // simpelweg onschadelijk gemaakt.
    document.addEventListener(
      "click",
      function (event) {
        var link = event.target.closest("a[href], button[type='submit'], form");
        if (link) {
          event.preventDefault();
        }

        var node = findTaggedAtPoint(event.clientX, event.clientY);
        if (!node) return;

        event.preventDefault();
        event.stopPropagation();
        var field =
          node.getAttribute("data-vibe-field") ||
          node.getAttribute("data-vibe-gallery") ||
          node.getAttribute("data-vibe-video") ||
          node.getAttribute("data-vibe-embed") ||
          node.getAttribute("data-vibe-videolink");
        post({ type: "SBP_FIELD_CLICK", section: sectionNameOf(node), field: field });
      },
      true
    );

    // Sommige sites navigeren via JavaScript in plaats van een <a href> (bv.
    // window.location.href in een klik-handler). Die weg is met click-events
    // niet af te vangen; deze twee vangnetten dekken de rest af zonder de
    // normale werking van de site elders te raken.
    window.addEventListener(
      "submit",
      function (event) {
        event.preventDefault();
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
