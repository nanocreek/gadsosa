# Gad Sosa — Personal Site

Production site for Gad Sosa, built with [Astro](https://astro.build/).

## Tech stack

- **Astro** — static site generator
- **Vanilla CSS** — design tokens in `src/styles/global.css`
- **Astro Content Collections** — blog posts in `src/content/insights/`
- **Basin** — contact form handling
- **Plausible** — privacy-friendly analytics
- **Cloudflare Pages** — hosting

## Project structure

```text
src/
  components/        # Page sections and UI components
  content/
    insights/        # Markdown blog posts
  layouts/
    Layout.astro     # Base layout with SEO, fonts, nav, footer
  pages/
    index.astro      # Home page
    insights/
      index.astro    # Blog listing
      [slug].astro   # Individual blog post
  styles/
    global.css       # Tokens and all styles
public/
  og-image.png       # Open Graph image
  robots.txt         # Crawler instructions
```

## Local development

```bash
cd site
npm install
npm run dev
```

Open <http://localhost:4321>.

## Build

```bash
npm run build
npm run preview
```

## Add a blog post

1. Create a new Markdown file in `src/content/insights/`.
2. Add frontmatter:

```yaml
---
title: "Your post title"
description: "A short summary for SEO and listings."
date: 2026-08-10
tag: "ML Security"
draft: false
---
```

3. Write the body in Markdown below the frontmatter.
4. Commit and push. The site redeploys automatically.

## Edit page content

The home page is assembled from components in `src/components/`. Each section is a separate file, so copy updates are straightforward.

## Contact form

The form submits to Basin. To make it live:

1. Create a form at <https://usebasin.com>.
2. Copy the form ID (the part after `/f/` in the submission URL).
3. Set it as `PUBLIC_BASIN_FORM_ID` in the Cloudflare Pages environment variables (or in `.env` for local testing).

A honeypot field (`website`) is included for extra spam protection.

## Environment variables

| Variable | Description |
|----------|-------------|
| `PUBLIC_BASIN_FORM_ID` | Basin form endpoint ID |

See `.env.example`.

## Deployment

Cloudflare Pages is connected to the GitHub repository. Every push to `main` triggers the workflow in `.github/workflows/deploy.yml`.

### Manual deployment

If you have Wrangler installed and authenticated:

```bash
cd site
npm run build
npx wrangler pages deploy dist --project-name=gadsosa
```

## Analytics

Plausible is loaded in `src/layouts/Layout.astro` with `data-domain="gadsosa.com"`. No cookies or personal data is collected.

## Open items

- Update portfolio items in `src/components/SectionPortfolio.astro` as projects evolve.
- Provide a real `PUBLIC_BASIN_FORM_ID`.
- Optionally add company logos to the hero trust row.
