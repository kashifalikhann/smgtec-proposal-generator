export async function handler(event) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method not allowed' };
  }

  try {
    const { url } = JSON.parse(event.body);

    if (!url) return jsonResponse(400, { error: 'URL is required' });

    try { new URL(url); } catch {
      return jsonResponse(400, { error: 'Invalid URL' });
    }

    const FIRECRAWL_API_KEY = process.env.FIRECRAWL_API_KEY;
    if (!FIRECRAWL_API_KEY) {
      return jsonResponse(500, { error: 'Firecrawl not configured' });
    }

    const response = await fetch('https://api.firecrawl.dev/v1/scrape', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + FIRECRAWL_API_KEY
      },
      body: JSON.stringify({
        url: url,
        formats: ['markdown'],
        onlyMainContent: true
      })
    });

    if (!response.ok) {
      const errText = await response.text();
      return jsonResponse(response.status, { error: 'Firecrawl error: ' + errText });
    }

    const data = await response.json();
    const markdown = data.data && data.data.markdown ? data.data.markdown : '';
    const parsed = parseScrapedContent(markdown, url);

    return jsonResponse(200, { success: true, markdown: markdown, parsed: parsed });

  } catch (error) {
    return jsonResponse(500, { error: error.message });
  }
}

function jsonResponse(statusCode, body) {
  return {
    statusCode: statusCode,
    headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    body: JSON.stringify(body)
  };
}

function parseScrapedContent(md, url) {
  var result = { companyName: '', contactName: '', services: '', language: 'EN', maturity: 'Low', phone: '', location: '', industry: '' };

  var h1Match = md.match(/^#\s+(.+)$/m);
  if (h1Match) result.companyName = h1Match[1].trim().substring(0, 60);

  var spanishWords = ['español', 'servicios', 'empresa', 'Barcelona', 'abogado', 'legal', 'fiscal'];
  var spanishCount = 0;
  for (var i = 0; i < spanishWords.length; i++) {
    if (md.toLowerCase().indexOf(spanishWords[i]) >= 0) spanishCount++;
  }
  if (spanishCount >= 3) result.language = 'ES';

  var keywords = ['immigration', 'tax', 'visa', 'legal', 'tributación', 'inmigración', 'visados', 'abogado', 'empresa', 'seguros', 'derecho', 'asesoría'];
  var found = [];
  for (var j = 0; j < keywords.length; j++) {
    if (md.toLowerCase().indexOf(keywords[j]) >= 0 && found.indexOf(keywords[j]) < 0) {
      found.push(keywords[j]);
    }
  }
  if (found.length > 0) result.services = found.slice(0, 5).join(', ');

  var dirMatch = md.match(/(?:Director|CEO|Founder)[:\s]+([A-Z][a-záéíóúñ]+\s+[A-Z][a-záéíóúñ]+)/i);
  if (dirMatch) result.contactName = dirMatch[1];

  var phoneMatch = md.match(/(?:tel|phone|whatsapp|llame)[:\s]*([\+\d\s\(\)-]{9,20})/i);
  if (phoneMatch) result.phone = phoneMatch[1].trim();

  var locMatch = md.match(/(?:Barcelona|Madrid|Valencia|Sevilla|Bilbao)/i);
  if (locMatch) result.location = locMatch[0];

  if (md.indexOf('WordPress') >= 0 || md.indexOf('wp-content') >= 0) result.maturity = 'Low (WordPress)';
  else if (md.length < 2000) result.maturity = 'Low (basic site)';
  else result.maturity = 'Medium';

  var ml = md.toLowerCase();
  if (ml.indexOf('legal') >= 0 || ml.indexOf('abogado') >= 0 || ml.indexOf('law firm') >= 0) result.industry = 'legal';
  else if (ml.indexOf('health') >= 0 || ml.indexOf('dental') >= 0 || ml.indexOf('clinic') >= 0 || ml.indexOf('médico') >= 0) result.industry = 'healthcare';
  else if (ml.indexOf('finance') >= 0 || ml.indexOf('accounting') >= 0 || ml.indexOf('finanzas') >= 0) result.industry = 'finance';
  else if (ml.indexOf('retail') >= 0 || ml.indexOf('e-commerce') >= 0 || ml.indexOf('shop') >= 0) result.industry = 'retail';
  else if (ml.indexOf('manufacturing') >= 0 || ml.indexOf('industrial') >= 0) result.industry = 'manufacturing';

  return result;
}
