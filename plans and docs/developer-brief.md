# Developer Brief — Gad Sosa Personal Site

**Prepared for:** Web developer
**Prepared by:** Gad Sosa
**Date:** July 2026

---

## 1. What this is

A single-page personal/marketing site for a technology executive. The goal is to win full-time leadership roles (VP R&D / CTO) and long-term engagements. Audience is largely non-technical decision-makers plus recruiters, with a secondary technical screener.

A **working single-file HTML/CSS prototype already exists** (`index.html`) with all content, structure, and a functional contact form. It is a strong starting point. This brief covers turning it into a maintainable, deployed, production site — and the improvements to make along the way.

---

## 2. Scope

**In scope:**
- Take the existing prototype to production: clean structure, deploy, connect a domain.
- Make the contact form submit reliably and privately (see section 4).
- Wire up the blog/"Insights" so new posts can be added easily (see section 5).
- SEO/technical hygiene (see section 6).
- Implement the designer's visual updates when those land (coordinate on handoff).

**Out of scope (unless quoted separately):** ongoing content writing, marketing/SEO campaigns, analytics dashboards beyond basic setup.

---

## 3. Tech preferences

- **Keep it simple and fast.** This is a content site, not an app. A static site is ideal — plain HTML/CSS, or a lightweight static generator (Astro, Eleventy, or similar) if it makes the blog easier to maintain. Please don't over-engineer with a heavy SPA framework unless there's a clear reason.
- **Hosting:** a static host is fine — Netlify, Vercel, Cloudflare Pages, or GitHub Pages. Recommend one and set it up.
- **No login, no database** required for the core site. If the blog generator needs a build step, that's fine.

---

## 4. Contact form (important)

The current form uses a `mailto:` link, which opens the visitor's email client. Replace this with a form that:
- Submits **without exposing Gad's email address** on the page or to the sender.
- Delivers submissions reliably to an inbox he controls.
- Includes basic spam protection (honeypot or a service with built-in filtering).

A hosted form service (Formspree, Basin, Web3Forms, or the host's native form handling on Netlify/Cloudflare) is perfectly acceptable — no need to build a backend. Keep the existing fields: name, email, company, "what are you looking for?" (dropdown), and message.

---

## 5. Blog / "Insights"

There's an Insights section with a few article entries. Set it up so Gad can **add a new article without touching layout code** — ideally markdown files or a simple CMS (e.g. a static-generator content folder, or a lightweight headless CMS if he'd prefer a UI). Each post should be its own indexable page (good for SEO and shareable links), with title, date, tag, and body. Start with 2–3 posts; content will be supplied.

---

## 6. SEO & technical hygiene

The prototype already includes meta tags, Open Graph tags, and JSON-LD `Person` structured data — preserve and extend these. Additionally:
- Per-page `<title>` and meta description for each blog post.
- Generate `sitemap.xml` and `robots.txt`.
- Ensure the JSON-LD stays valid (test in Google's Rich Results tool).
- Add an Open Graph image (coordinate with designer).
- Set up a simple, privacy-respectful analytics option (e.g. Plausible or Cloudflare Web Analytics) — Gad to confirm preference.
- Fast Core Web Vitals: optimize/lazy-load any images, subset or preload fonts.

---

## 7. Quality bar

- Fully responsive; verified on real mobile devices, not just a resized browser.
- Accessible: semantic HTML, visible keyboard focus, sufficient contrast, `prefers-reduced-motion` respected (the prototype already does this — maintain it).
- Cross-browser: current Chrome, Safari, Firefox, Edge.
- No console errors; valid HTML.

---

## 8. Deliverables

- Deployed production site on the chosen host, connected to the domain (domain to be provided/purchased — advise).
- Source in a Git repository handed over to Gad.
- Working contact form delivering to his inbox.
- Blog set up with a documented, simple way to add posts.
- Brief handover notes: how to add a post, how to edit content, where the form goes, how to deploy changes.

---

## 9. What I'll provide

- The existing `index.html` prototype.
- Final domain, X handle, headshot (if used), real testimonial quotes, and blog article content.
- The designer's Figma file and assets when ready.

---

## 10. To include in your quote

- Approach (static vs. generator) and hosting recommendation.
- Timeline.
- Whether design implementation is included or depends on the designer's handoff.
- Any ongoing maintenance option (optional).
