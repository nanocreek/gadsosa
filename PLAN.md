# Gad Sosa Personal Site — Implementation Plan

> Based on the **Design Brief**, **Developer Brief**, and the two working prototypes in `plans and docs/mock website/`.

---

## 1. Goal & Success Criteria

Build and deploy a fast, accessible, production-grade personal site for Gad Sosa that:

- Lands his positioning in under five seconds.
- Serves two audiences: non-technical decision-makers (founders, CEOs, boards, recruiters) and technical screeners.
- Wins full-time leadership roles (VP R&D / CTO) and long-term engagements (6+ months).
- Makes adding new articles simple and code-free.
- Submits the contact form privately, without exposing an email address.
- Ranks well for his name and key topics (SEO, structured data, sitemap).

---

## 2. Recommended Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| **Static-site generator** | **Astro** | Zero-JS-by-default (fast), first-class Markdown content collections (perfect for the blog), component-based, easy to keep small and maintainable. |
| **Styling** | **Vanilla CSS with design tokens** | Keeps the bundle tiny and matches the “fast, lightweight” requirement. CSS custom properties for colors, type scale, and spacing. |
| **Fonts** | **Fraunces** (headlines), **Inter** (body), **IBM Plex Mono** (labels) — or the refined **Newsreader / Geist / Geist Mono** set if the designer keeps it. | Loaded from Google Fonts with `preconnect`, `display=swap`, and a system-font fallback. |
| **Interactivity** | Tiny inline/vanilla JS only | Sticky nav active state, mobile menu toggle, contact-form UX, current year. No SPA framework needed. |
| **Blog content** | Astro **Content Collections** | Each post is a Markdown file with frontmatter → own indexable page. No CMS login required. |
| **Contact form** | **Basin** (recommended) or **Formspree** / **Web3Forms** | No backend to maintain, spam filtering, email hidden from visitors, custom redirect/success message. |
| **Analytics** | **Plausible** or **Cloudflare Web Analytics** | Privacy-respecting, lightweight. Decision pending from Gad. |
| **Version control & CI** | **GitHub** + host-native Git integration | Push-to-deploy; no manual build steps. |
| **Hosting / CDN** | **Cloudflare Pages** (recommended) | Global CDN, free SSL, fast edge cache, great Core Web Vitals, custom-domain support. Netlify or Vercel are acceptable alternatives. |

### Alternatives considered

- **Plain HTML/CSS**: Cheapest, but adding blog posts becomes error-prone and repetitive.
- **Eleventy**: Also excellent for static content; Astro was chosen for its component model and slightly richer ecosystem.
- **Next.js**: Overkill for a content site with no dynamic data; adds unnecessary JavaScript.

---

## 3. Site Structure

```text
site/                          # Astro project lives here
src/
├── content/
│   └── insights/
│       ├── ml-security-questions.md
│       ├── ai-driven-engineering.md
│       └── production-inference.md
├── layouts/
│   └── Layout.astro          # HTML shell, fonts, SEO, JSON-LD, nav, footer
├── components/
│   ├── SectionHero.astro
│   ├── SectionHowIWork.astro
│   ├── SectionWhyMe.astro
│   ├── SectionReferences.astro
│   ├── SectionInsights.astro
│   ├── SectionExperience.astro
│   ├── SectionTechDepth.astro
│   ├── SectionContact.astro
│   └── SignatureSpine.astro  # desktop section-register
├── pages/
│   ├── index.astro           # single-page landing
│   ├── insights/
│   │   ├── index.astro       # full blog listing
│   │   └── [slug].astro      # individual post pages
│   └── rss.xml.js            # RSS feed
├── styles/
│   └── global.css            # tokens + base styles
public/
├── og-image.png              # 1200×630 Open Graph image
├── favicon.svg
└── robots.txt
```

---

## 4. Design & UX Approach

### Visual system (starting from the existing prototype)

- **Palette**
  - Ink: `#0e1826` (dark backgrounds, primary text)
  - Paper: `#f7f8fa` (page background)
  - Panel: `#ffffff` (cards)
  - Accent: `#1f6feb`
  - Accent deep: `#0b3d91`
  - Gold: `#c8a24a` (highlights, section numbers)
  - Muted: `#6a7688`
  - Line: `#dfe4ec`
- **Typography scale**: defined as CSS custom properties (e.g. `--text-display`, `--text-body`, `--text-small`) and applied consistently.
- **Spacing scale**: 4/8/16/24/32/48/64/92/104 px increments, also tokenized.
- **Signature element**: keep the refined “section spine” (numbered dots/labels on the right) from the advanced prototype. It is distinctive, tasteful, and useful for a long single-page layout. Respect `prefers-reduced-motion`.
- **Hero**: strong typographic headline, short positioning line, two CTAs, company logo/type row.
- **Testimonials**: treated as trust anchors — prominent, with quote marks and clear attribution once real quotes arrive.
- **Headshot**: recommend a formal/environmental portrait in monochrome or desaturated treatment placed in the hero or the “Why me” section. Provide recommendation in the design review; implement only once asset is supplied.

### Responsive & accessibility

- Mobile-first CSS; verify on real devices.
- Semantic HTML (`<nav>`, `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- Visible keyboard focus states.
- `prefers-reduced-motion` disables animations and smooth scroll.
- ARIA labels where needed (mobile menu button, icon-only links).
- Color contrast ≥ WCAG AA for all text.

---

## 5. Contact Form

- Replace the `mailto:` behavior with a true form POST.
- Use **Basin** (or chosen service) endpoint.
- Fields: Name, Email, Company, “What are you looking for?” (dropdown), Message.
- Add a hidden honeypot field for extra spam protection.
- No email address appears in the HTML, JS, or network payload visible to the visitor.
- Provide an inline success/error message after submission.
- If the host is **Netlify**, Netlify Forms is a zero-config alternative.

---

## 6. Blog / Insights

- Each post is a Markdown file in `src/content/insights/` with frontmatter:

```yaml
---
title: "Your AI feature is an attack surface..."
date: 2026-08-01
tag: "ML Security"
description: "A plain-language guide to the new risks AI introduces into a product."
---
```

- Astro generates a page per post at `/insights/[slug]/`.
- The home page lists the three latest posts.
- An optional `/insights/` index lists all posts.
- Add an **RSS feed** (`/rss.xml`) so posts can be followed.

To add a new post, Gad only needs to create one Markdown file and push it to Git.

---

## 7. SEO & Technical Hygiene

- Preserve and extend existing meta tags, Open Graph, Twitter Cards, and JSON-LD `Person` schema.
- Add `BlogPosting` structured data for each Insights article.
- Per-page `<title>` and `<meta name="description">` for home and every post.
- Auto-generate `sitemap.xml` (Astro sitemap integration).
- Static `robots.txt`.
- Canonical URLs.
- Open Graph image: 1200×630, generated by/with the designer.
- Font preloading/subsetting; lazy-load below-the-fold images.
- Validate JSON-LD in Google’s Rich Results Test before launch.

---

## 8. Hosting, Domain & Deployment

The site has been built and is ready to deploy. The Astro project is in the `site/` directory, with a GitHub Actions workflow at `.github/workflows/deploy.yml`. Actual deployment to Cloudflare Pages requires a Cloudflare API token and account ID (or using the Cloudflare dashboard Git integration).

### Recommended: Cloudflare Pages

1. Create a GitHub repository for the project.
2. Connect the repo to Cloudflare Pages.
3. Build command: `npm run build` (outputs `dist/`).
4. Every push to `main` auto-deploys.
5. Add custom domain `gadsosa.com` (or whatever domain Gad purchases) and enable “Always Use HTTPS”.
6. Set build environment variable `NODE_VERSION` to the LTS version.

### Domain

- The existing prototype already uses `https://www.gadsosa.com/` as canonical.
- Recommendation: purchase/keep `gadsosa.com`, CNAME `www` to Cloudflare Pages, redirect apex to `www`.

### Alternatives

- **Netlify**: very simple, has built-in forms, excellent DX.
- **Vercel**: great Astro support and previews.

Cloudflare Pages is preferred here for global edge performance and cost (free tier is sufficient).

---

## 9. Implementation Phases

### Phase 1 — Foundation (1–2 days)

- Initialize Astro project with static output.
- Set up Git repo, linting/formatting (optional), and folder structure.
- Port design tokens and global styles.
- Create `Layout.astro` with SEO shell, fonts, JSON-LD.

### Phase 2 — Single-page site (3–4 days)

- Build all sections as Astro components using existing content.
- Implement nav, signature spine, and responsive behavior.
- Add reduced-motion and accessibility polish.
- Integrate placeholder content for testimonials and Insights.

### Phase 3 — Blog (1–2 days)

- Set up content collection schema.
- Create post template and slug route.
- Port the three draft posts into Markdown.
- Add RSS feed and optional `/insights/` index.

### Phase 4 — Contact form & integrations (1 day)

- Wire form to Basin/Formspree.
- Add honeypot and success/error states.
- Set up privacy-friendly analytics (pending preference).

### Phase 5 — SEO & performance (1 day)

- Sitemap, robots, canonical, OG tags, JSON-LD validation.
- Image optimization, font loading strategy.
- Lighthouse / PageSpeed audit.

### Phase 6 — Deploy & handover (1 day)

- Deploy to Cloudflare Pages.
- Connect domain and verify SSL.
- QA on Chrome, Safari, Firefox, Edge, and real mobile devices.
- Write handover notes (how to add a post, edit content, where form goes, how to redeploy).

**Estimated total: 1–1.5 weeks** of focused development, assuming design assets and final copy are available.

---

## 10. What Is Needed from Gad Before / During Build

- Final domain name and registrar access (or decision to purchase).
- Final X/Twitter handle to replace `GADSOSA_HANDLE`.
- Real testimonial quotes and attributions for the References section.
- Decision + asset for headshot/portrait (or confirmation to skip).
- Final blog post copy for the first 2–3 articles.
- Optional: company logos in SVG/PNG for the trust row (monochrome preferred).
- Preference for analytics: Plausible, Cloudflare Web Analytics, or none.
- Access to an email inbox for form-forwarding configuration.

---

## 11. Deliverables

- Source code in a GitHub repository.
- Deployed production site on Cloudflare Pages, connected to the chosen domain.
- Working contact form with spam protection.
- Blog set up with documented, one-file process for adding posts.
- Handover notes for content updates and deployments.

---

## 12. Notes on the Existing Prototypes

- `plans and docs/mock website/uploads/index.html` is the clean, production-ready HTML prototype. Use its content, structure, and SEO metadata as the primary source of truth.
- `plans and docs/mock website/Gad Sosa.dc.html` is a more polished visual exploration built in a design tool’s runtime. Borrow its refined details (signature spine, dark hero, typography) but do **not** deploy the dc-runtime/React wrapper to production; rebuild the same effects in Astro + vanilla CSS/JS.

---

## 13. Open Decisions to Confirm

1. **Hosting**: Cloudflare Pages (recommended), Netlify, or Vercel?
2. **Form service**: Basin (recommended), Formspree, Web3Forms, or Netlify Forms?
3. **Analytics**: Plausible, Cloudflare Web Analytics, or skip for now?
4. **Headshot**: use one or keep the site text-only?
5. **Domain**: confirm `gadsosa.com` and whether to use `www` or apex as canonical.

Once these are confirmed, Phase 1 can begin immediately.
