# Anime Wheel — web edition

Single-file browser game generated from the question bank in `anime_wheel.py`.

## Play locally

Double-click `web/index.html`. That's it — no server, no install.

## Deploy (pick one)

**Netlify Drop** (easiest)
1. Go to https://app.netlify.com/drop
2. Drag the whole `web` folder onto the page
3. Done — you get a public URL immediately

**GitHub Pages**
1. Push this folder to a repo
2. Repo → Settings → Pages → deploy from branch, root
3. URL appears in a minute

**Vercel** — `npx vercel` inside the `web` folder, accept defaults

**itch.io** — zip `index.html`, upload as HTML game at https://itch.io/game/new

## Editing questions

Add or edit questions/tiers/styles in `anime_wheel.py` (QUESTIONS / QUOTE_BANK / TIERS / STYLES), then rebuild:

```
python build_web.py
```

This regenerates `web/index.html` with the new data baked in.
