# HASSION Website Project Guide

This file is the long-term project guide for Claude Code and other coding agents working on the HASSION website.

## Project Identity

- Website owner: Guangzhou Hassion Leather Ltd.
- Website type: B2B OEM leather goods factory website.
- Audience: overseas brand buyers, wholesalers, sourcing managers, and OEM/ODM clients.
- Main conversion paths: WhatsApp inquiry and FormSubmit contact form.
- The site should build trust in factory capability, product quality, production stability, and OEM communication.
- This is not a retail store, marketplace catalog, SaaS landing page, or Alibaba-style supplier page.

## Non-Negotiable Facts

- Company name: Guangzhou Hassion Leather Ltd.
- Founded: 1998.
- Factory area: 3,000 square meters / 3,000㎡.
- Never write 10,000 square meters / 10000 square meters.
- Workers: 200+.
- MOQ: 200 pcs.
- Sample lead time: about 7 days.
- Bulk production lead time: about 30 days.
- Core business: leather wallets and small leather goods OEM/ODM manufacturing.
- Protected facts must stay consistent across hero, body copy, metadata, JSON-LD, and footer.

## Brand / Visual Direction

- Style: European leather workshop / slow luxury / restrained OEM factory.
- The visual mood should be quiet, premium, craftsmanship-focused, industrial, minimal, and warm.
- Preserve dark cinematic depth in hero and factory imagery; do not over-brighten images.
- Prefer warm off-white, deep brown, leather brown, warm gray-black, and restrained accent colors.
- Avoid loud sales badges, glossy marketplace styling, neon, tech startup visuals, and generic Chinese OEM website patterns.
- Avoid heavy gradients, glassmorphism, bouncy animation, oversized decorative effects, and visual clutter.
- Use real factory, leather, stitching, QC, packaging, and material imagery when possible.
- Keep the site B2B-conversion focused while avoiding aggressive Alibaba-style sales pressure.
- Typography should feel refined and calm, not bold SaaS or mass-market wholesale.

## Current Site Structure

- Hero
- About
- Why Us
- Production
- Products
- OEM
- Exhibitions
- Contact

Current section IDs include:

- `#hero`
- `#about`
- `#why-us`
- `#production`
- `#products`
- `#oem`
- `#exhibitions`
- `#contact`

Before changing layout or navigation, inspect the current `index.html` and `style.css`.
Do not assume an older structure from memory.

## Technical Rules

- The site is a static HTML/CSS/vanilla JS website.
- Prefer CSS and small vanilla JavaScript.
- Do not introduce heavy animation libraries.
- Scroll reveal should remain subtle: opacity plus small translateY, no bounce, no scale.
- JSON-LD already exists; do not remove it.
- OG / Twitter meta already exists; do not remove it.
- Hero image optimization uses AVIF/WebP assets and CSS `image-set`; preserve responsive loading behavior.
- Mobile drawer navigation exists; preserve accessibility attributes and close behavior.
- Do not re-add the heavy hero specs pill.
- MOQ, sample time, production time, and worker count may appear in a trust row or body content, but not as a loud sales badge.
- Keep mobile readability and responsive spacing as first-class requirements.
- If changing forms, links, metadata, or image paths, verify the exact current code first.

## Git Rules

- Never use `git add .`.
- Stage exact files or exact hunks only.
- Do not auto commit unless the user explicitly asks for a commit.
- Do not auto push unless the user explicitly asks for a push.
- Before committing, review `git status` and `git diff --staged`.
- Do not stage or commit unrelated files.
- Do not stage or commit `CLAUDE.md` unless the user explicitly asks.
- Keep independent changes in independent commits.

## Do Not Break

- Do not break FormSubmit.
- Do not break WhatsApp links.
- Do not break the `thanks.html` redirect.
- Do not break `thanks.html`.
- Do not remove JSON-LD, OG meta, Twitter meta, canonical URL, or important SEO copy.
- Do not change protected company facts without explicit instruction.
- Do not change factory area to 10,000 square meters.
- Do not remove the contact form or floating WhatsApp CTA.
- Do not make the hero look like a loud sales banner again.
- Do not redesign the whole website when the task asks for a focused edit.
- Do not replace working static behavior with a framework or build system.
- Do not modify images, forms, navigation, or redirects unless the task specifically asks for it.
