# igorsamulenko.com

Single-page portfolio website for Igor Samulenko, Staff Frontend Engineer.

## Files

| File | Description |
|------|-------------|
| `index.html` | Main site (development version) |
| `s3/index.html` | Minified production version |
| `s3/images/avatar.jpeg` | Profile photo (production) |
| `images/avatar.jpeg` | Profile photo (source) |
| `Igor_Samulenko_Staff_SWE_2026.pdf` | Downloadable resume |
| `minify.py` | Minification script |

## Features

- **Sections**: Hero, About, Selected Work, Experience, How I Work, What Colleagues Say, Contact
- **Selected Work**: Expandable case-study cards with metrics, tags, and SVG mockups
- **Interactive terminal**: Command-line contact section with easter eggs
- **Animated metrics**: Count-up effect on scroll via Intersection Observer
- **Dark/Light mode**: Toggle button, follows system preference by default
- **Responsive**: Mobile-first design with hamburger menu
- **Smooth scroll**: Anchor navigation with scroll padding
- **Scroll reveal**: Fade-in animations via Intersection Observer
- **Accessible**: Skip link, ARIA attributes, keyboard support, reduced-motion support

## Tech Stack

- Vanilla HTML/CSS/JS (no frameworks)
- Fonts: DM Serif Display + Outfit + JetBrains Mono (Google Fonts)
- Icons: Inline SVGs

## Configuration

| Setting | Value |
|---------|-------|
| GitHub | `https://github.com/isamulenko` |
| LinkedIn | `https://www.linkedin.com/in/igorsamulenko` |
| Email | `igor.samulenko@gmail.com` |

## Development

Start local server:
```bash
python3 -m http.server 8000
```

View at: http://localhost:8000

## Build for Production

Minify and copy to `s3/` folder:
```bash
python3 minify.py
cp -r images s3/
```

## Deployment

Upload contents of `s3/` folder to:
- AWS S3 (static website hosting)
- GitHub Pages
- Netlify
- Vercel
- Any static hosting provider
