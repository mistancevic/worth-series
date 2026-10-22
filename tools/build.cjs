// Build a book's PDF from its pages: each page one sheet at its print size, fonts embedded, no margins.
//   node tools/build.cjs worthy-numbers   →  books/worthy-numbers/releases/worthy-numbers-<version>.pdf
// Run check first. A released file is never overwritten: raise "version" in book.json for a new one.
const fs = require("node:fs"), path = require("node:path");
const { book, FACES, pageBody, launch } = require("./common.cjs");
(async () => {
  const b = book(process.argv[2] || "worthy-numbers"), { width, height } = b.meta.size;
  const file = path.join(b.dir, "releases", `${b.meta.slug}-${b.meta.version}.pdf`);
  if (fs.existsSync(file) && !process.argv.includes("--draft")) { console.log(`${path.relative(process.cwd(), file)} exists: raise the version in book.json, or add --draft`); process.exit(1); }
  const target = process.argv.includes("--draft") ? path.join(b.dir, "releases", `${b.meta.slug}-draft.pdf`) : file;
  const html = `<!doctype html><html><head><meta charset="utf-8"><title>${b.meta.title}</title><style>${FACES}@page{size:${width}px ${height}px;margin:0}html,body{margin:0}.pg{width:${width}px;height:${height}px;overflow:hidden;break-after:page}.pg:last-child{break-after:auto}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}</style></head><body>` +
    b.meta.pages.map((n) => `<div class="pg">${pageBody(b, n)}</div>`).join("") + "</body></html>";
  const br = await launch(), page = await br.newPage();
  await page.setContent(html); await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: target, width: `${width}px`, height: `${height}px`, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await br.close();
  console.log(`${path.relative(process.cwd(), target)}: ${b.meta.pages.length} pages, ${Math.round(fs.statSync(target).size / 1024)} KB`);
})();
