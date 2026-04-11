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
cp *.pdf s3/             # Copies resume PDF to production folder
```

## Architecture

**Single-file architecture:** All HTML, CSS, and JavaScript live in `index.html` (development) which minifies to `s3/index.html` (production).

**File structure:**
- `index.html` - Full source (~830 lines)
- `s3/index.html` - Minified production output
- `images/` - Source assets
- `Igor_Samulenko_Staff_SWE_2026.pdf` - Downloadable resume
- `minify.py` - Python minification script

**Page sections:** Navigation → Hero → About → Selected Work → Experience → How I Work → What Colleagues Say → Contact (terminal) → Footer

**Key JavaScript features:**
- Dark/light theme toggle (persisted in localStorage, respects system preference)
- Mobile hamburger menu (< 768px breakpoint)
- Intersection Observer for scroll reveal animations
- Animated metric counting (count-up effect on scroll)
- Interactive SVG mockup hover effects
- Expandable case-study cards with keyboard support
- Interactive terminal with commands and easter eggs

**CSS theming:** Uses CSS custom properties. Light theme is default; dark theme applied via `[data-theme="dark"]` attribute on `<html>`.

**Typography:** DM Serif Display (headings) + Outfit (body) + JetBrains Mono (code/mono) from Google Fonts. Icons are inline SVGs.

## Content Editing Notes

**Version backups:** Save versions as `index.v0.html`, `index.v1.html`, etc. before major changes.

**About section:** Uses `<strong>` for emphasis and `<p class="about-text">` for the narrative.

**Selected Work cards:** Each `<article class="case-card">` contains metrics (`data-target`, `data-suffix`, `data-prefix` attributes for animation), tags, and an expandable detail section with optional SVG mockup.

**Experience timeline:** Simple grid layout with role, company, detail, and dates.

**SEO meta tags** (lines 7-15 in index.html):
- `<meta name="description">` - Google search excerpt
- `<meta property="og:description">` - Social sharing preview
- JSON-LD structured data for Person schema

**Workflow:** After any content changes, run `python3 minify.py && cp -r images s3/` to update production build.

## Claude Code Permissions

Allowed commands (`.claude/settings.local.json`):
- `git add:*` - Stage files
- `git commit:*` - Create commits
- `git push:*` - Push to remote
