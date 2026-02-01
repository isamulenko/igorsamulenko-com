# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Single-page portfolio website for Igor Samulenko. Vanilla HTML/CSS/JS with no frameworks or build tool dependencies.

## Commands

**Development server:**
```bash
python3 -m http.server 8000
```
View at http://localhost:8000

**Production build:**
```bash
python3 minify.py        # Minifies index.html -> s3/index.html
cp -r images s3/         # Copies images to production folder
```

## Architecture

**Single-file architecture:** All HTML, CSS, and JavaScript live in `index.html` (development) which minifies to `s3/index.html` (production).

**File structure:**
- `index.html` - Full source (~1,500 lines)
- `s3/index.html` - Minified production output
- `images/` - Source assets
- `minify.py` - Python minification script

**Page sections:** Navigation → Hero → Summary → Skills → Experience → Education → Interests → Footer

**Key JavaScript features:**
- Dark/light theme toggle (persisted in localStorage, respects system preference)
- Mobile hamburger menu (< 768px breakpoint)
- Intersection Observer for scroll animations
- Active nav section highlighting on scroll

**CSS theming:** Uses CSS custom properties. Light theme is default; dark theme applied via `[data-theme="dark"]` attribute on `<html>`.

**Typography:** Playfair Display (headings) + DM Sans (body) from Google Fonts. Icons are inline Heroicons SVGs.

## Content Editing Notes

**Version backups:** Save versions as `index.v0.html`, `index.v1.html`, etc. before major changes.

**Text styling in Professional Summary:**
- `<strong>` for emphasis (companies, product names, role description)
- `<span class="highlight">` for metrics/numbers (years, percentages, performance gains)

**Experience section formatting:**
- Multiple accomplishments: use `<ul class="experience-bullets">` with `<li>` items
- Single accomplishment: use `<p class="experience-summary">` (no bullets)

**SEO meta tags** (lines 7-13 in index.html):
- `<meta name="description">` - Google search excerpt
- `<meta property="og:description">` - Social sharing preview

**Workflow:** After any content changes, run `python3 minify.py && cp -r images s3/` to update production build.
