# First iteration / Validation

Reviewed 10 November 2026. Local source only; no deployment, commit or push.

## Completed checks

- Parsed homepage HTML: internal file links and fragment targets resolve, IDs are unique, all images have alt attributes, and the heading sequence is h1 → h2 → h3 → h3 → h2.
- Checked semantic header, main, sections, footer and named navigation; a skip link, explicit card destination names, visible focus styling and reduced-motion overrides are present. Decorative illustrations are hidden from assistive technology.
- Checked public destinations: Coastal, Cycling and the existing public `/privacy.html` each returned HTTP 200 after redirects.
- Compared `privacy.html` and `CNAME` against Git HEAD: both are byte-for-byte unchanged. The original privacy notice had no fragment IDs or embedded links to preserve. The homepage now links directly to `privacy.html`.
- Parsed all five SVG assets as XML and checked viewBoxes. Generated native Quick Look thumbnails successfully and visually inspected the map, wordmark, light/dark symbol geometry and favicon. Also inspected resized 24px symbol and 16px favicon previews: the route remains recognisable. Native thumbnailing is not a substitute for cross-browser SVG/font rendering checks.
- Served the homepage, privacy notice, both stylesheets and all five SVGs through a temporary loopback HTTP server: all returned 200 and matched the source bytes. The server was stopped afterwards.
- Calculated sRGB contrast: midnight on paper 13.45:1; muted light text 5.53:1; dark copper on paper 4.76:1; paper on midnight 13.45:1; muted dark text 8.78:1; light copper on midnight 7.29:1. Muted text on the secondary light/dark surfaces is 5.19:1 / 7.76:1. Sage hero text is large and meets the large-text threshold at 3.88:1. These calculations cover the intended text pairs, not a complete accessibility audit.
- Reviewed responsive CSS: two-column desktop composition, reduced tablet gutters, stacked mobile hero/projects/about, wrapping header/footer navigation, and a reduced-height mobile map. These are source checks, not rendered viewport tests.
- No JavaScript, framework, backend, package manifest, remote fonts, analytics or other runtime dependencies were added. Homepage plus all assets total approximately 45 KB uncompressed.
- `git diff --check` passed. No hosting configuration or workflows were changed; no other repositories or private operational destinations were added.

## Browser limitation and human review

Local browser tooling reported **“Local browser use is disabled in Work settings.”** No browser screenshot, rendered responsive test, keyboard interaction test or automated browser accessibility audit was possible. Native SVG thumbnails and HTTP/source checks were completed independently.

Before publication, preview locally and check:

1. Layout at 320, 390, 768, 1024 and 1440px, especially header wrapping and map prominence. Confirm no horizontal scrolling.
2. At 200% zoom and with larger text settings, confirm readable text and usable navigation.
3. Tab through the skip link, header links, project cards and footer. Confirm the focus outline remains visible and anchor destinations land appropriately.
4. Check SVG/favicon rendering in the intended browsers, the installed font fallback, and the reversed symbol on a midnight background.
5. Confirm the introduction and first-person About copy reflect the owner’s voice and approve the proposed identity direction.

There is no technical decision requiring infrastructure changes. The exact GitHub Pages publishing source remains unverified; no publication was attempted.
