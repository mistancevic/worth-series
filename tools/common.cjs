// Shared by build and check: a book's pages, with its pictures and the series fonts built in, ready for a browser.
const fs = require("node:fs"), path = require("node:path");
const ROOT = path.resolve(__dirname, "..");
const book = (slug) => {
  const dir = path.join(ROOT, "books", slug);
  if (!fs.existsSync(path.join(dir, "book.json"))) throw new Error(`No book at books/${slug}: give a folder name under books/`);
  return { dir, meta: JSON.parse(fs.readFileSync(path.join(dir, "book.json"), "utf8")) };
};
const b64 = (p) => fs.readFileSync(p).toString("base64");
const font = (pkg, file) => path.join(path.dirname(require.resolve(`${pkg}/package.json`)), "files", file);
const FACES = `@font-face{font-family:Anton;src:url(data:font/woff2;base64,${b64(font("@fontsource/anton", "anton-latin-400-normal.woff2"))})}` +
  [400, 600, 700, 800, 900].map((w) => `@font-face{font-family:Nunito;font-weight:${w};src:url(data:font/woff2;base64,${b64(font("@fontsource/nunito", `nunito-latin-${w}-normal.woff2`))})}`).join("");
// one page's own markup: what sits inside <x-dc>, after its <helmet>, with every picture inlined
const pageBody = ({ dir, meta }, name) => {
  let s = fs.readFileSync(path.join(dir, "pages", `${name}.dc.html`), "utf8").split("</helmet>")[1].split("</x-dc>")[0].trim();
  for (const [id, file] of Object.entries(meta.images || {})) s = s.split(`/_blob/${id}`).join(`data:image/webp;base64,${b64(path.join(dir, file))}`);
  if (s.includes("/_blob/")) throw new Error(`${name}: a picture is missing from book.json images`);
  return s;
};
const launch = () => require("playwright").chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
module.exports = { ROOT, book, FACES, pageBody, launch };
