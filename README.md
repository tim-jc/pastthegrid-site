# Past the Grid

A small, buildless public homepage for [pastthegrid.uk](https://pastthegrid.uk), introducing the Coastal and Cycling projects.

## Structure

- `index.html` — public homepage.
- `privacy.html` — existing Home Assistant Nest privacy notice; preserve its public URL and content.
- `assets/identity.css` — portable light/dark colour, typography and spacing tokens.
- `assets/home.css` — homepage layout and responsive styles.
- `assets/symbol.svg`, `symbol-dark.svg`, `wordmark.svg`, `favicon.svg` — identity assets.
- `assets/field-map.svg` — decorative schematic cartography.
- `docs/visual-identity.md` — identity specification and adoption guidance.
- `docs/validation.md` — checks and remaining visual review.
- `CNAME` — existing custom domain declaration, `pastthegrid.uk`.

## Local preview

From this directory, run:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000>. Check `/privacy.html` as well. Stop the server with Ctrl+C. No installation, compilation, JavaScript runtime or external font service is needed to serve the site.

## Publication

The public site has been observed serving from GitHub hosting, and its domain is declared in `CNAME`. There are no deployment workflows in this checkout. The exact GitHub Pages source branch/folder setting has not been verified; check repository Settings → Pages before planning a deployment. This iteration changes local source only. No DNS, hosting settings, deployments, commits or pushes are included.

## Editing

Update copy and destinations in `index.html`, reusable values in `identity.css`, and page composition in `home.css`. Keep `privacy.html` available at its current URL: that notice specifically supports a separate private Nest integration and is not a general privacy statement for the linked cycling projects. The homepage adds no analytics, cookies, forms, remote scripts or private operational links.
