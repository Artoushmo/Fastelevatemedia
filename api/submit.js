const ALLOWED_ORIGINS = new Set([
  'https://www.fastelevatemedia.com',
  'https://fastelevatemedia.com'
]);

export default async function handler(req, res) {
  const origin = req.headers.origin || '';
  const referer = req.headers.referer || '';

  if (ALLOWED_ORIGINS.has(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  }
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Accept');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, message: 'Method Not Allowed' });
  }

  // Block cross-site abuse if an Origin or Referer header is present and not from fastelevatemedia.com
  const isAllowedOrigin = !origin || ALLOWED_ORIGINS.has(origin);
  const isAllowedReferer = !referer || Array.from(ALLOWED_ORIGINS).some((o) => referer.startsWith(o));
  if (!isAllowedOrigin || !isAllowedReferer) {
    return res.status(403).json({ success: false, message: 'Forbidden' });
  }

  const rawBody = req.body && typeof req.body === 'object' ? req.body : {};

  // Honeypot anti-bot check: if _honey is filled, silently drop spam
  if (rawBody._honey && String(rawBody._honey).trim() !== '') {
    return res.status(200).json({ success: 'true', message: 'Submission received' });
  }

  // Sanitize and bound payload fields
  const cleanBody = {};
  const keys = Object.keys(rawBody).slice(0, 40);
  for (const key of keys) {
    const cleanKey = String(key).slice(0, 64).replace(/[^\w\s\-_.]/g, '');
    if (!cleanKey) continue;
    const val = rawBody[key];
    if (val === null || val === undefined) continue;
    cleanBody[cleanKey] = String(val).slice(0, 4000);
  }

  try {
    const response = await fetch('https://formsubmit.co/ajax/info@fastelevatemedia.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Origin': 'https://www.fastelevatemedia.com',
        'Referer': 'https://www.fastelevatemedia.com/contact.html'
      },
      body: JSON.stringify(cleanBody)
    });

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ success: false, message: 'Submission failed. Please try again later.' });
  }
}

