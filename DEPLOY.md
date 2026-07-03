# Deployment Guide — gadsosa.com

This project deploys automatically from GitHub to **Cloudflare Pages**.

## 1. Cloudflare Pages project

1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/).
2. Go to **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Select the GitHub repository for this project.
4. Configure the build:
   - **Project name:** `gadsosa`
   - **Production branch:** `main`
   - **Build command:** `cd site && npm run build`
   - **Build output directory:** `/site/dist`
5. Add environment variables:
   - `NODE_VERSION` = `22`
   - `PUBLIC_BASIN_FORM_ID` = your Basin form ID
6. Save and deploy.

## 2. GitHub Action (recommended)

The repository includes `.github/workflows/deploy.yml`. It runs on every push to `main`.

Add these secrets to the GitHub repository under **Settings → Secrets and variables → Actions**:

- `CLOUDFLARE_API_TOKEN` — create one at <https://dash.cloudflare.com/profile/api-tokens> with the **Cloudflare Pages** template.
- `CLOUDFLARE_ACCOUNT_ID` — found on the right side of the Cloudflare dashboard overview.
- `PUBLIC_BASIN_FORM_ID` — your Basin form ID.

## 3. Domain setup

1. Purchase or manage `gadsosa.com` in Cloudflare (or your existing registrar).
2. In Cloudflare Pages, go to the project → **Custom domains** → **Set up a custom domain**.
3. Add `www.gadsosa.com` and follow the verification steps.
4. Add a redirect rule from the apex (`gadsosa.com`) to `www.gadsosa.com`:
   - In **Rules** → **Redirect Rules**, create a dynamic redirect:
     - When hostname equals `gadsosa.com`, redirect to `https://www.gadsosa.com${request.uri}` with status **301**.
5. Ensure **Always Use HTTPS** is enabled.

## 4. Plausible analytics

1. Create an account at <https://plausible.io>.
2. Add the domain `gadsosa.com`.
3. The tracking script is already in `site/src/layouts/Layout.astro`:
   ```html
   <script defer data-domain="gadsosa.com" src="https://plausible.io/js/script.js"></script>
   ```

## 5. Basin contact form

1. Sign up at <https://usebasin.com>.
2. Create a new form.
3. Copy the form ID from the submission URL (`https://usebasin.com/f/<FORM_ID>`).
4. Set `PUBLIC_BASIN_FORM_ID=<FORM_ID>` as an environment variable in Cloudflare Pages (and GitHub secrets for the workflow).
5. Test the form on the live site.

## 6. Post-launch checks

- [ ] Site loads at `https://www.gadsosa.com`.
- [ ] `https://gadsosa.com` redirects to `www`.
- [ ] SSL certificate is active.
- [ ] Contact form submits successfully.
- [ ] Sitemap is reachable at `/sitemap-index.xml`.
- [ ] RSS feed is reachable at `/rss.xml`.
- [ ] Run the site through [Google Rich Results Test](https://search.google.com/test/rich-results).
- [ ] Verify Core Web Vitals in [PageSpeed Insights](https://pagespeed.web.dev/).
