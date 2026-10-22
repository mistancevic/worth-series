# The Worth series

Short books by Milan Stancevic on product thinking and on living well with food and training.

| Book | Status | Read it |
| --- | --- | --- |
| Worth Building | Published, version 2.0 | [github.com/mistancevic/worth-building](https://github.com/mistancevic/worth-building) |
| Worthy Numbers | Published, version 1.0 (22 October 2026) | [chefmealan.com/worthy-numbers](https://chefmealan.com/worthy-numbers) |
| Worth Eating | In the making | |
| Worth Living | Planned | |

Worth Building keeps its own repository, because its links and its case pages point there. Every other book lives here.

## What is in this repository

```
books/<book>/
  book.json        title, version, release date, page order, page size, where it is published
  pages/           one file per page, the same files as the book's design canvas (and the cover options)
  assets/          pictures the pages use
  releases/        every released PDF, never overwritten: <book>-<version>.pdf
  reviews/         the editor, product, reader and proofreading reviews before a release
  CHANGELOG.md     what changed in each version
kit/               the series look: the cover generator (dot artwork), the Chef Mealan icon and lockup
tools/             check.cjs (every page fits) and build.cjs (the PDF)
```

## How a book is made and released

1. **Write and lay out on the design canvas.** The canvas is the editing desk: Milan edits text there, and Claude edits layout and pages there.
2. **Save the pages here.** Copy every page from the canvas into `books/<book>/pages/`, and its pictures into `assets/`.
3. **Check.** `npm install` once, then `npm run check -- <book>`. Every page must fit.
4. **Raise the version** in `book.json` and add a line to `CHANGELOG.md`. Version 1.1 for corrections, 2.0 for a new edition.
5. **Build.** `npm run build -- <book>` writes `releases/<book>-<version>.pdf`. A released file is never overwritten.
6. **Tag** the commit `<book>-v<version>`, for example `worthy-numbers-v1.0`, and attach the PDF to a GitHub release.
7. **Publish.** Copy the PDF to the Chef Mealan app (`public/books/<book>.pdf`), raise the version on the book's page there, and deploy.

The PDF on chefmealan.com always carries the latest version; every older version stays in `releases/` and in the GitHub releases.
