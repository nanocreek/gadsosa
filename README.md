# Gad Sosa Personal Site

This repository contains the planning, design/developer briefs, mock prototypes, and production code for Gad Sosa's personal site.

## What's here

| Path | Description |
|------|-------------|
| `PLAN.md` | Implementation plan: goals, tech stack, structure, deployment |
| `DEPLOY.md` | Step-by-step guide to deploy to Cloudflare Pages |
| `site/` | Astro project — the production site |
| `plans and docs/` | Original design brief, developer brief, and HTML prototypes |

## Quick start

```bash
npm install   # run inside site/ for dependency installation
npm run dev
```

## Build & deploy

```bash
npm run build
npm run deploy   # requires Cloudflare credentials; see DEPLOY.md
```

All npm scripts can be run from the repository root; they delegate to the `site/` directory.

Or use the GitHub Actions workflow in `.github/workflows/deploy.yml` for automatic deploys on every push to `main`.

## Status

- ✅ Astro project initialized
- ✅ Design tokens, layout, and all sections built
- ✅ Blog/Insights content collection with 3 posts
- ✅ Contact form wired to Basin (placeholder endpoint)
- ✅ SEO, sitemap, robots.txt, RSS, Open Graph image, JSON-LD
- ✅ Plausible analytics configured
- ✅ Deployed to Cloudflare Pages
  - Production: https://www.gadsosa.com
  - Also resolves at https://gadsosa.com and https://gadsosa.pages.dev
- ✅ Contact form wired to Basin

See `site/README.md` for content-editing and maintenance instructions.
