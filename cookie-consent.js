/**
 * Fast Elevate Media — Cookie Consent System
 * GDPR-compliant two-layer consent banner.
 *
 * Layer 1: Banner with Accept All / Reject Non-Essential / Cookie Settings
 * Layer 2: Granular settings panel (Strictly Necessary, Analytics, Advertising)
 *
 * Google Analytics 4 and Google Ads Conversion Tracking are ONLY loaded
 * after explicit consent. No tracking fires on page load before consent.
 *
 * Replace the placeholder IDs below with your real tracking IDs:
 *   GA4_MEASUREMENT_ID  — e.g. "G-XXXXXXXXXX"
 *   GADS_CONVERSION_ID  — e.g. "AW-XXXXXXXXXX"
 */

(function () {
  'use strict';

  // ─── CONFIG — Replace with real tracking IDs ────────────────────────────────
  var GA4_ID  = 'G-XXXXXXXXXX';   // Replace with your Google Analytics 4 ID
  var GADS_ID = 'AW-XXXXXXXXXX';  // Replace with your Google Ads Conversion ID
  // ────────────────────────────────────────────────────────────────────────────

  var STORAGE_KEY = 'fem_cookie_consent';
  var COOKIE_POLICY_URL = (window.location.pathname.indexOf('/nl/') === 0)
    ? './cookies.html'
    : (window.location.pathname.indexOf('/nl') === 0 && window.location.pathname.length <= 4)
      ? './cookies.html'
      : './cookies.html';

  // Detect language for bilingual labels
  var isNL = window.location.pathname.indexOf('/nl') === 0 ||
             document.documentElement.lang === 'nl';

  var labels = {
    en: {
      bannerTitle:     'We value your privacy',
      bannerText:      'We use cookies and similar technologies to improve website functionality, analyze website traffic, and measure the effectiveness of our advertising campaigns. You can accept all cookies, reject non-essential cookies, or customize your preferences.',
      acceptAll:       'Accept All',
      rejectNon:       'Reject Non-Essential',
      settings:        'Cookie Settings',
      settingsTitle:   'Cookie Settings',
      settingsIntro:   'Manage your cookie preferences below. Strictly necessary cookies are always active and cannot be disabled.',
      alwaysActive:    'Always Active',
      savePrefs:       'Save Preferences',
      necessary:       'Strictly Necessary Cookies',
      necessaryDesc:   'Required for website functionality and security. These cannot be disabled.',
      analytics:       'Analytics Cookies',
      analyticsDesc:   'Help us understand how visitors interact with our website through anonymous statistics.',
      analyticsEx:     'Example: Google Analytics 4',
      advertising:     'Advertising Cookies',
      advertisingDesc: 'Used to measure advertising performance and understand how visitors interact with our campaigns.',
      advertisingEx:   'Example: Google Ads Conversion Tracking',
      policyLink:      'Cookie Policy',
    },
    nl: {
      bannerTitle:     'Wij respecteren uw privacy',
      bannerText:      'Wij gebruiken cookies en vergelijkbare technologieën om de websitewerking te verbeteren, websiteverkeer te analyseren en de effectiviteit van onze advertentiecampagnes te meten. U kunt alle cookies accepteren, niet-essentiële cookies weigeren of uw voorkeuren aanpassen.',
      acceptAll:       'Alle accepteren',
      rejectNon:       'Niet-essentieel weigeren',
      settings:        'Cookie-instellingen',
      settingsTitle:   'Cookie-instellingen',
      settingsIntro:   'Beheer uw cookievoorkeuren hieronder. Strikt noodzakelijke cookies zijn altijd actief en kunnen niet worden uitgeschakeld.',
      alwaysActive:    'Altijd actief',
      savePrefs:       'Voorkeuren opslaan',
      necessary:       'Strikt Noodzakelijke Cookies',
      necessaryDesc:   'Vereist voor de werking en veiligheid van de website. Deze kunnen niet worden uitgeschakeld.',
      analytics:       'Analytics Cookies',
      analyticsDesc:   'Helpen ons te begrijpen hoe bezoekers omgaan met onze website via anonieme statistieken.',
      analyticsEx:     'Voorbeeld: Google Analytics 4',
      advertising:     'Advertising Cookies',
      advertisingDesc: 'Worden gebruikt om advertentieprestaties te meten en te begrijpen hoe bezoekers omgaan met onze campagnes.',
      advertisingEx:   'Voorbeeld: Google Ads Conversion Tracking',
      policyLink:      'Cookiebeleid',
    }
  };

  var t = isNL ? labels.nl : labels.en;

  // ─── Consent storage helpers ─────────────────────────────────────────────────
  function getConsent() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)); } catch (e) { return null; }
  }

  function saveConsent(analytics, advertising) {
    var consent = { analytics: !!analytics, advertising: !!advertising, timestamp: Date.now() };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(consent));
    return consent;
  }

  // ─── Load Google tracking scripts ────────────────────────────────────────────
  function loadGA4() {
    if (document.getElementById('fem-ga4-script')) return;
    var s = document.createElement('script');
    s.id = 'fem-ga4-script';
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA4_ID, { anonymize_ip: true });
  }

  function loadGAds() {
    if (document.getElementById('fem-gads-script')) return;
    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('config', GADS_ID);
    gtag('event', 'conversion', { send_to: GADS_ID });
  }

  function applyConsent(consent) {
    if (consent.analytics)    loadGA4();
    if (consent.advertising)  loadGAds();
  }

  // ─── CSS styles ──────────────────────────────────────────────────────────────
  var css = `
    #fem-cookie-overlay {
      position: fixed; inset: 0; z-index: 99998;
      background: rgba(0,0,0,0.25);
      display: flex; align-items: flex-end; justify-content: center;
      padding: 0;
      font-family: 'Lexend', 'Inter', sans-serif;
      animation: fem-fade-in 0.2s ease;
    }
    @keyframes fem-fade-in { from { opacity: 0; } to { opacity: 1; } }

    #fem-cookie-banner {
      background: #1c1c1e;
      width: 100%;
      max-width: 100%;
      border-radius: 0;
      padding: 14px 28px;
      box-shadow: 0 -4px 24px rgba(0,0,0,0.3);
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      animation: fem-slide-up 0.25s cubic-bezier(0.25,0.46,0.45,0.94);
    }
    @keyframes fem-slide-up { from { transform: translateY(100%); } to { transform: translateY(0); } }

    #fem-cookie-banner .fem-banner-text {
      flex: 1; min-width: 220px;
    }
    #fem-cookie-banner h2 {
      font-size: 0.78rem; font-weight: 800; color: #ffffff; margin: 0 0 2px;
      letter-spacing: 0.01em;
    }
    #fem-cookie-banner p {
      font-size: 0.68rem; color: rgba(255,255,255,0.65); line-height: 1.5; margin: 0;
    }
    #fem-cookie-banner .fem-policy-link {
      color: #7da8e0; text-decoration: underline; font-size: 0.68rem;
    }
    #fem-cookie-banner .fem-btn-row {
      display: flex; flex-wrap: nowrap; gap: 8px; align-items: center; flex-shrink: 0;
    }
    .fem-btn-accept {
      background: #4C72A9; color: white; border: none; cursor: pointer;
      font-family: inherit; font-weight: 700; font-size: 0.68rem;
      text-transform: uppercase; letter-spacing: 0.06em;
      padding: 8px 18px; border-radius: 999px;
      transition: background 0.2s, transform 0.15s;
      white-space: nowrap;
    }
    .fem-btn-accept:hover { background: #3b5c8f; transform: scale(1.03); }
    .fem-btn-reject {
      background: transparent; color: rgba(255,255,255,0.8);
      border: 1.5px solid rgba(255,255,255,0.25); cursor: pointer;
      font-family: inherit; font-weight: 700; font-size: 0.68rem;
      text-transform: uppercase; letter-spacing: 0.06em;
      padding: 8px 18px; border-radius: 999px;
      transition: border-color 0.2s, transform 0.15s;
      white-space: nowrap;
    }
    .fem-btn-reject:hover { border-color: rgba(255,255,255,0.6); transform: scale(1.02); }
    .fem-btn-settings {
      background: transparent; color: rgba(255,255,255,0.5);
      border: none; cursor: pointer;
      font-family: inherit; font-weight: 600; font-size: 0.65rem;
      text-decoration: underline; padding: 6px 2px;
      transition: color 0.2s;
      white-space: nowrap;
    }
    .fem-btn-settings:hover { color: rgba(255,255,255,0.9); }

    /* Settings panel */
    #fem-cookie-settings-panel {
      position: fixed; inset: 0; z-index: 99999;
      display: flex; align-items: center; justify-content: center;
      padding: 16px;
      font-family: 'Lexend', 'Inter', sans-serif;
      background: rgba(0,0,0,0.55);
      animation: fem-fade-in 0.2s ease;
    }
    #fem-cookie-settings-box {
      background: #fff; border-radius: 20px;
      width: 100%; max-width: 500px;
      max-height: 90vh; overflow-y: auto;
      padding: 28px 24px 20px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.25);
      animation: fem-scale-in 0.25s cubic-bezier(0.34,1.56,0.64,1);
    }
    @keyframes fem-scale-in { from { transform: scale(0.93); opacity: 0; } to { transform: scale(1); opacity: 1; } }
    #fem-cookie-settings-box h2 {
      font-size: 1.05rem; font-weight: 800; color: #121111; margin: 0 0 6px;
    }
    #fem-cookie-settings-box p.fem-intro {
      font-size: 0.73rem; color: #555; line-height: 1.6; margin: 0 0 16px;
    }
    .fem-cookie-row {
      border: 1.5px solid #e5e7eb; border-radius: 12px;
      padding: 13px 15px; margin-bottom: 10px;
    }
    .fem-cookie-row-header {
      display: flex; align-items: center; justify-content: space-between; gap: 12px;
      margin-bottom: 6px;
    }
    .fem-cookie-row-header strong {
      font-size: 0.80rem; font-weight: 700; color: #121111;
    }
    .fem-cookie-row p {
      font-size: 0.71rem; color: #666; line-height: 1.5; margin: 0 0 3px;
    }
    .fem-cookie-row .fem-example {
      font-size: 0.66rem; color: #9ca3af; margin: 0;
    }
    .fem-badge-always {
      font-size: 0.62rem; font-weight: 700; color: #4C72A9;
      background: #e8eef8; padding: 3px 9px; border-radius: 999px;
      white-space: nowrap;
    }
    /* Toggle switch */
    .fem-toggle { position: relative; display: inline-block; width: 40px; height: 22px; flex-shrink: 0; }
    .fem-toggle input { opacity: 0; width: 0; height: 0; }
    .fem-toggle-slider {
      position: absolute; cursor: pointer; inset: 0;
      background: #d1d5db; border-radius: 999px;
      transition: background 0.25s;
    }
    .fem-toggle-slider:before {
      content: ''; position: absolute;
      height: 16px; width: 16px; left: 3px; bottom: 3px;
      background: white; border-radius: 50%;
      transition: transform 0.25s;
      box-shadow: 0 1px 4px rgba(0,0,0,0.2);
    }
    .fem-toggle input:checked + .fem-toggle-slider { background: #4C72A9; }
    .fem-toggle input:checked + .fem-toggle-slider:before { transform: translateX(18px); }
    .fem-settings-footer {
      display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-end;
      margin-top: 16px; padding-top: 14px;
      border-top: 1px solid #e5e7eb;
    }
    .fem-btn-save {
      background: #4C72A9; color: white; border: none; cursor: pointer;
      font-family: inherit; font-weight: 700; font-size: 0.68rem;
      text-transform: uppercase; letter-spacing: 0.06em;
      padding: 9px 20px; border-radius: 999px;
      transition: background 0.2s, transform 0.15s;
    }
    .fem-btn-save:hover { background: #3b5c8f; transform: scale(1.03); }
    .fem-btn-save-all {
      background: transparent; color: #121111;
      border: 1.5px solid #d1d5db; cursor: pointer;
      font-family: inherit; font-weight: 700; font-size: 0.68rem;
      text-transform: uppercase; letter-spacing: 0.06em;
      padding: 9px 20px; border-radius: 999px;
      transition: border-color 0.2s, transform 0.15s;
    }
    .fem-btn-save-all:hover { border-color: #4C72A9; transform: scale(1.02); }

    @media (max-width: 640px) {
      #fem-cookie-banner { padding: 12px 16px; gap: 10px; }
      #fem-cookie-banner .fem-btn-row { flex-wrap: wrap; width: 100%; }
      .fem-btn-accept, .fem-btn-reject { flex: 1; text-align: center; }
      #fem-cookie-settings-box { padding: 20px 14px 16px; }
    }
  `;

  // ─── Inject CSS ───────────────────────────────────────────────────────────────
  function injectCSS() {
    var style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
  }

  // ─── Close and remove overlay ─────────────────────────────────────────────────
  function removeOverlay() {
    var overlay = document.getElementById('fem-cookie-overlay');
    if (overlay) {
      overlay.style.opacity = '0';
      overlay.style.transition = 'opacity 0.2s';
      setTimeout(function () { if (overlay.parentNode) overlay.parentNode.removeChild(overlay); }, 210);
    }
  }

  function removeSettingsPanel() {
    var panel = document.getElementById('fem-cookie-settings-panel');
    if (panel) {
      panel.style.opacity = '0';
      panel.style.transition = 'opacity 0.2s';
      setTimeout(function () { if (panel.parentNode) panel.parentNode.removeChild(panel); }, 210);
    }
  }



  // ─── Settings panel ───────────────────────────────────────────────────────────
  function buildSettingsPanel(fromBanner) {
    var existing = document.getElementById('fem-cookie-settings-panel');
    if (existing) return;

    var saved = getConsent() || {};

    var panel = document.createElement('div');
    panel.id = 'fem-cookie-settings-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'true');
    panel.setAttribute('aria-label', t.settingsTitle);

    panel.innerHTML = `
      <div id="fem-cookie-settings-box" role="document">
        <h2>${t.settingsTitle}</h2>
        <p class="fem-intro">${t.settingsIntro} <a href="${COOKIE_POLICY_URL}" class="fem-policy-link" style="color:#4C72A9;text-decoration:underline;">${t.policyLink}</a></p>

        <!-- Strictly Necessary -->
        <div class="fem-cookie-row">
          <div class="fem-cookie-row-header">
            <strong>${t.necessary}</strong>
            <span class="fem-badge-always">${t.alwaysActive}</span>
          </div>
          <p>${t.necessaryDesc}</p>
        </div>

        <!-- Analytics -->
        <div class="fem-cookie-row">
          <div class="fem-cookie-row-header">
            <strong>${t.analytics}</strong>
            <label class="fem-toggle" aria-label="${t.analytics}">
              <input type="checkbox" id="fem-toggle-analytics" ${saved.analytics ? 'checked' : ''} />
              <span class="fem-toggle-slider"></span>
            </label>
          </div>
          <p>${t.analyticsDesc}</p>
          <p class="fem-example">${t.analyticsEx}</p>
        </div>

        <!-- Advertising -->
        <div class="fem-cookie-row">
          <div class="fem-cookie-row-header">
            <strong>${t.advertising}</strong>
            <label class="fem-toggle" aria-label="${t.advertising}">
              <input type="checkbox" id="fem-toggle-advertising" ${saved.advertising ? 'checked' : ''} />
              <span class="fem-toggle-slider"></span>
            </label>
          </div>
          <p>${t.advertisingDesc}</p>
          <p class="fem-example">${t.advertisingEx}</p>
        </div>

        <div class="fem-settings-footer">
          <button class="fem-btn-save-all" id="fem-settings-accept-all">${t.acceptAll}</button>
          <button class="fem-btn-save" id="fem-settings-save">${t.savePrefs}</button>
        </div>
      </div>
    `;

    document.body.appendChild(panel);

    // Close on overlay click
    panel.addEventListener('click', function (e) {
      if (e.target === panel) {
        removeSettingsPanel();
        if (fromBanner && !getConsent()) {
          // reshow banner if they close without saving and no prior consent
        } else {

        }
      }
    });

    document.getElementById('fem-settings-accept-all').addEventListener('click', function () {
      var consent = saveConsent(true, true);
      applyConsent(consent);
      removeSettingsPanel();
      removeOverlay();
    });

    document.getElementById('fem-settings-save').addEventListener('click', function () {
      var analytics    = document.getElementById('fem-toggle-analytics').checked;
      var advertising  = document.getElementById('fem-toggle-advertising').checked;
      var consent = saveConsent(analytics, advertising);
      applyConsent(consent);
      removeSettingsPanel();
      removeOverlay();
    });
  }

  // ─── Main Banner ──────────────────────────────────────────────────────────────
  function buildBanner() {
    var overlay = document.createElement('div');
    overlay.id = 'fem-cookie-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', t.bannerTitle);

    overlay.innerHTML = `
      <div id="fem-cookie-banner">
        <div class="fem-banner-text">
          <h2>${t.bannerTitle}</h2>
          <p>${t.bannerText} <a href="${COOKIE_POLICY_URL}" class="fem-policy-link">${t.policyLink}</a></p>
        </div>
        <div class="fem-btn-row">
          <button class="fem-btn-accept" id="fem-btn-accept-all">${t.acceptAll}</button>
          <button class="fem-btn-reject" id="fem-btn-reject">${t.rejectNon}</button>
          <button class="fem-btn-settings" id="fem-btn-open-settings">${t.settings}</button>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    document.getElementById('fem-btn-accept-all').addEventListener('click', function () {
      var consent = saveConsent(true, true);
      applyConsent(consent);
      removeOverlay();
    });

    document.getElementById('fem-btn-reject').addEventListener('click', function () {
      saveConsent(false, false);
      removeOverlay();
    });

    document.getElementById('fem-btn-open-settings').addEventListener('click', function () {
      buildSettingsPanel(true);
    });
  }

  // ─── Public API — called by "Modify Cookie Settings" buttons ─────────────────
  window.openCookieSettings = function () {
    buildSettingsPanel(false);
  };

  // ─── Init ─────────────────────────────────────────────────────────────────────
  function init() {
    injectCSS();

    var saved = getConsent();
    if (saved) {
      // Consent already given — apply and show reopener
      applyConsent(saved);

    } else {
      // No consent yet — show banner
      buildBanner();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
