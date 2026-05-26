# AGENTS.md — HASSION Website

## Project Overview

This is the official B2B OEM website for Guangzhou Hassion Leather Ltd.

Business:
Leather wallets and small leather goods OEM/ODM manufacturing.

Target customers:
Overseas brand sourcing managers, wholesalers, corporate buyers, and OEM clients.

Primary goal:
Build trust and convert visitors into WhatsApp or inquiry form leads.

Do not treat this website like a retail ecommerce site.
Do not make it look like an Alibaba shop template.

---

## Core Company Facts

Always keep these facts consistent:

- Company name: Guangzhou Hassion Leather Ltd.
- Brand name: HASSION Leather
- Founded: 1998
- Production facility: 3,000㎡
- Workers: 200+
- MOQ: 200 pcs per style per color
- Sample lead time: ~7 days
- Bulk production time: ~30 days
- Main products: men's wallets, women's wallets, passport holders, card holders, key holders, coin cases
- Main CTA: Get OEM Quotation / Chat on WhatsApp / Send Inquiry

Never change these numbers unless explicitly instructed.

---

## Brand Direction

Style direction:
Premium Leather Factory.

The site should feel:
- professional
- trustworthy
- warm
- clean
- B2B-focused
- leather-industry appropriate

Use:
- dark brown
- cream / off-white
- deep gray
- muted gold
- real product and factory photography
- clean spacing
- clear hierarchy

Avoid:
- AI-tech startup style
- cyberpunk style
- neon colors
- excessive gradients
- overdesigned animations
- Alibaba-style clutter
- cheap wholesale visual language
- fake luxury fashion wording

Primary colors:
- #5C2D1A
- #FDFBF7
- #333333
- #C8945A

Do not introduce a new color system.

---

## Site Structure

Current main sections:

1. Hero
2. About
3. Why Choose HASSION
4. Production Capability
5. Products
6. OEM
7. Quality / Certifications
8. Clients
9. Exhibitions & Buyer Visits
10. Contact
11. Footer

Do not delete sections unless explicitly instructed.
Do not rename section ids.
Do not add Alibaba Store back to the main navigation.

Main navigation should stay simple:
Home / About / Products / OEM / Quality / Contact

Alibaba Store may stay only in the footer as a low-priority trust reference.

---

## Hero Rules

Hero must clearly communicate:

1. Company name
2. OEM/ODM leather goods positioning
3. MOQ / sample time / production time / workers
4. Quote CTA
5. Product category CTA
6. Trust badges

Do not make Hero abstract, vague, or purely decorative.

Hero should not become:
- a tech startup homepage
- a luxury fashion campaign
- an Alibaba promo banner
- a discount or sale banner

---

## Product Image Rules

Products section is a priority.

Product image requirements:
- Use 1:1 square images when possible
- Recommended export: 1600×1600 WebP
- Quality: 85–90
- Color profile: sRGB
- Product should occupy around 75–85% of the frame
- Keep product fully visible
- Keep object-fit: contain
- Do not crop product edges
- Keep visual style consistent across all 6 product cards

Preferred product colors:
- black
- dark brown
- chocolate brown
- caramel brown
- burgundy brown
- taupe / milk tea / beige

Avoid using bright blue, bright red, neon, or overly colorful patchwork items as main product card images.

Use colorful items only for future Custom Color / Material Options sections.

---

## Product Detail Page Rules

Product detail pages should feel like premium brand catalog pages, not retail ecommerce pages.

Primary goal:
Help overseas B2B buyers understand product quality, materials, craftsmanship, customization options, and OEM capability, then guide them to inquiry.

Preferred page structure:
1. Large clean product visual
2. Product name and short B2B-focused description
3. Key specifications
4. Material / color / logo customization options
5. Craftsmanship and quality details
6. OEM inquiry CTA

Avoid:
- prices
- discount labels
- stock counters
- add-to-cart UI
- consumer reviews
- fake urgency
- marketplace-style icon grids
- cluttered selling points
- Taobao / Amazon product detail layout

Visual direction:
- large product imagery
- generous whitespace
- restrained typography
- calm premium tone
- brand catalog feeling
- close-up craftsmanship details when available

Do not create cart, checkout, payment, account, or review features unless explicitly requested.

---

## Responsive Rules

Mobile quality is critical.

Always check:
- 375px mobile width
- product cards stay readable
- images are not cropped
- buttons align neatly
- clients/exhibitions photos do not cut off people
- logo is not distorted
- Hero is not overcrowded

For product cards:
- Keep object-fit: contain
- Keep Inquire buttons aligned
- Keep card text readable
- Avoid uneven card heights where possible

For exhibitions and client photos:
- Desktop can use object-fit: cover
- Mobile should prioritize complete image visibility over perfect crop

---

## Content / Copywriting Rules

Write for overseas B2B sourcing managers.

Prioritize:
- factory capability
- OEM/ODM support
- MOQ
- sample time
- production time
- quality control
- customization options
- target market compliance
- inquiry conversion

Avoid:
- vague marketing words
- exaggerated claims
- fake luxury wording
- emotional consumer-facing copy
- discount or promotion language
- unsupported brand claims

Tone:
Clear, direct, professional, international B2B.

---

## Technical Rules

Do not remove or break:

- FormSubmit integration
- WhatsApp links
- JSON-LD
- Open Graph tags
- Twitter Card tags
- canonical / hreflang tags
- section ids
- existing image paths unless specifically asked
- footer Alibaba Store link
- mobile hamburger behavior

Before modifying:
1. Read `index.html`
2. Read `style.css`
3. Summarize the intended change
4. Make the smallest safe edit

After modifying:
1. Summarize changed files
2. Explain what changed and why
3. Mention anything that should be manually checked in browser
4. Do not commit unless explicitly asked

---

## Git Rules

Use small commits.

Do not include unrelated files in a commit.

Examples:

Good:
- Update SEO URLs and improve thank-you page
- Replace product images and polish product cards
- Fix mobile product card layout
- Update project instructions

Bad:
- update
- final version
- fix everything
- random changes

If `CLAUDE.md` or `AGENTS.md` is modified, commit it separately from website UI changes.

---

## Current Near-Term Priority

Current priority:
1. Finalize product and factory photography.
2. Replace the 6 Products section images with consistent product photos.
3. Prepare product detail page structure after real product photos and material details are ready.

Do not redesign Hero, Production, OEM, or Contact until product images and product detail direction are finalized.

For now, avoid large visual redesigns. Focus on:
- better product imagery
- consistent product cards
- clean product detail page planning
- mobile readability
- inquiry conversion