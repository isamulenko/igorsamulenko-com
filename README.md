# igorsamulenko.com

Single-page portfolio website for Igor Samulenko, Staff Software Engineer.

## Files

| File | Description |
|------|-------------|
| `index.html` | Main site (development version) |
| `s3/index.html` | Minified production version |
| `s3/images/avatar.jpeg` | Profile photo (production) |
| `images/avatar.jpeg` | Profile photo (source) |
| `minify.py` | Minification script |

## Features

- **Sections**: Hero, Summary, Skills, Experience, Education, Interests, Footer
- **Dark/Light mode**: Toggle button, follows system preference by default
- **Responsive**: Mobile-first design with hamburger menu
- **Smooth scroll**: Anchor navigation with scroll padding
- **Timeline**: Connected dots for experience section
- **Animations**: Fade-in on scroll via Intersection Observer

## Tech Stack

- Vanilla HTML/CSS/JS (no frameworks)
- Fonts: Playfair Display + DM Sans (Google Fonts)
- Icons: Heroicons (inline SVGs)

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
