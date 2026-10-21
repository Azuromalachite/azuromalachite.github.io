// Browser checks against Jekyll output. External requests are blocked.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve('_site');
const server = http.createServer((req, res) => {
  let file = path.join(root, decodeURIComponent(new URL(req.url, 'http://localhost').pathname));
  if (!file.startsWith(root + path.sep) && file !== root) { res.writeHead(403).end(); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file)) { res.writeHead(404).end(); return; }
  res.setHeader('Content-Type', { '.css': 'text/css', '.js': 'text/javascript', '.html': 'text/html' }[path.extname(file)] || 'application/octet-stream');
  res.end(fs.readFileSync(file));
});
(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const origin = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.route('**/*', route => {
      const url = new URL(route.request().url());
      if (url.origin === origin) return route.continue();
      // Theme assets use the production absolute URL; serve the built copy locally.
      if (url.hostname === 'azuromalachite.github.io') return route.continue({ url: origin + url.pathname + url.search });
      return route.abort();
    });
    await page.goto(origin);
    for (const width of [320, 390, 600, 612, 860, 900, 1100, 1101, 1440, 1766]) {
      await page.setViewportSize({ width, height: 1000 });
      const metrics = await page.evaluate(() => ({
        edges: [...document.querySelectorAll('.section-heading h2, .practice-row h3, .work > div')].map(el => el.getBoundingClientRect().left),
        overflow: document.documentElement.scrollWidth > innerWidth
      }));
      assert.equal(metrics.edges.length, 9);
      assert.ok(Math.max(...metrics.edges) - Math.min(...metrics.edges) < 1, `${width}px: rail drift ${metrics.edges}`);
      assert.equal(metrics.overflow, false, `${width}px: horizontal overflow`);
      console.log(`${width}px: heading, practice and publication content share one rail`);
    }
    for (const route of ['/', '/research/', '/natural-history/', '/art-biodesign/', '/teaching/', '/cv/', '/publications/']) {
      await page.goto(origin + route);
      assert.equal(await page.locator('script[src*="mathjax"], script[src*="polyfill"]').count(), 0, route);
      assert.ok(await page.locator('footer a[href$="/publications/"]').count(), `Missing footer route: ${route}`);
      assert.equal(await page.locator('nav a[href$="/publications/"]').count(), 0, route);
      assert.equal(await page.locator('link[media="print"]').count(), 1, route);
    }
    assert.equal(await page.locator('.print-authors:visible').count(), 0);
    assert.ok((await page.locator('body').evaluate(el => getComputedStyle(el).fontFamily)).includes('sans-serif'), 'Theme CSS must load before print checks');
    // Print copies avoid browser differences when printing closed details, without JS.
    await page.emulateMedia({ media: 'print' });
    assert.equal(await page.locator('.print-authors:visible').count(), 5);
    assert.equal(await page.locator('.publication-authors:visible, .sidebar:visible, .masthead:visible, .page__footer:visible').count(), 0);
    for (const link of await page.locator('a[href^="https://doi.org/"]').all()) {
      const doi = await link.evaluate(el => ({ href: el.href, printed: getComputedStyle(el, '::after').content }));
      assert.ok(doi.printed.includes(doi.href), `DOI missing in print: ${doi.href}`);
    }
    fs.mkdirSync('local/layout-check', { recursive: true });
    await page.pdf({ path: 'local/layout-check/publications.pdf', format: 'A4', preferCSSPageSize: true });
    await page.screenshot({ path: 'local/layout-check/publications-print.png', fullPage: true });
    await page.emulateMedia({ media: 'screen' });
    await page.goto(origin);
    for (const width of [390, 612, 1440, 1766]) {
      await page.setViewportSize({ width, height: 1000 });
      await page.screenshot({ path: `local/layout-check/home-${width}.png`, fullPage: true });
    }
    console.log('Print authors, visible DOIs, footer routes, MathJax gating and navigation passed.');
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; }).finally(() => server.close());
