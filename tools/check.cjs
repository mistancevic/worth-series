// Check a book before a release: every page drawn at its print size with the real fonts, anything past the page edge
// reported, and a picture of each page saved to books/<slug>/check/.   node tools/check.cjs worthy-numbers
const fs = require("node:fs"), path = require("node:path");
const { book, FACES, pageBody, launch } = require("./common.cjs");
(async () => {
  const b = book(process.argv[2] || "worthy-numbers"), { width, height } = b.meta.size, out = path.join(b.dir, "check");
  fs.mkdirSync(out, { recursive: true });
  const br = await launch(), page = await br.newPage({ viewport: { width, height }, deviceScaleFactor: 2 });
  let bad = 0;
  for (const name of b.meta.pages) {
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${FACES} body{margin:0}</style></head><body>${pageBody(b, name)}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate(() => {
      const root = document.body.firstElementChild, box = root.getBoundingClientRect(), padB = parseFloat(getComputedStyle(root).paddingBottom);
      root.style.overflow = "visible"; let worst = 0, who = "";
      root.querySelectorAll("*").forEach((e) => { const rb = e.getBoundingClientRect(); const over = rb.bottom - (box.bottom - padB); if (rb.height && over > worst) { worst = over; who = (e.textContent || e.tagName).trim().slice(0, 60); } });
      root.style.overflow = "hidden"; return { worst: Math.round(worst), who };
    });
    await page.screenshot({ path: path.join(out, `${name}.png`), clip: { x: 0, y: 0, width, height } });
    if (r.worst > 0) bad++;
    console.log(name.padEnd(16), r.worst > 0 ? `past the bottom by ${r.worst}px: "${r.who}"` : "fits");
  }
  await br.close();
  console.log(bad ? `${bad} page(s) to fix` : "every page fits");
  process.exit(bad ? 1 : 0);
})();
