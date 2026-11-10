# Hero cartography refinement

10 November 2026. Local changes only.

## Construction

Run `python3 scripts/generate-hero-contours.py` from the repository to regenerate `assets/field-map.svg`. Python’s standard library is sufficient; this is an optional authoring tool, not a runtime dependency.

The elevation surface uses elliptical coordinates centred at (340, 255):

```
u = (x - 340) / 280
v = (y - 255) / 196
q(theta) = 1 + 0.075 cos(3 theta) + 0.045 sin(5 theta)
rho = hypot(u, v) / q(atan2(v, u))
H = 1 - rho²
```

The centre has elevation H = 1. Constant rho produces a constant-elevation contour. The angular perturbation makes the hill organic without changing the order of its contours. Since q is always at least 0.88, each ray has exactly one positive radius for each contour. Eighteen contours use radii 0.12 through 0.97 in steps of 0.05; the corresponding elevation intervals are deliberately not uniform. No elevation measurements are presented in the artwork.

Each loop uses the same 192 angular samples, closes with `Z`, and exports coordinates rounded to 0.1 SVG units. The script validates these rounded polygonal paths before writing them. The original 680 × 520 viewBox, grid, contour stroke colour/opacity/weight, copper route, waypoint circles and north annotation are retained. Endpoint labels now read HERE and THERE in their original technical type style, positioned outside the terrain loops beside their respective markers.

One narrowly scoped CSS adjustment changes the mobile artwork from `object-fit: cover` to `contain`. Its existing box and page layout are unchanged. This prevents the original fixed-height box from cropping route endpoints or labels at wider mobile widths.

## Validation

- Exhaustively checked 5,966,784 non-adjacent self-edge and inter-contour segment pairs on the actual rounded geometry; no crossing or touching segments found. Adjacent edges within the same loop are excluded because they intentionally share a vertex.
- Checked unique vertices and strict containment of every inner contour’s vertices inside the next contour. Together with the edge-intersection checks, the exported polygons are nested.
- Checked contour vertices against a one-unit inset from the SVG boundaries; straight edges remain within those bounds too. No contour strokes are clipped.
- Checked conservatively padded label rectangles against all contours and route segments. HERE and THERE are clear of the route and terrain; their placements also leave clear space from waypoint circles and the north annotation.
- Confirmed regeneration is byte-for-byte deterministic. XML comparison confirms that only the contour and endpoint-label groups changed within the SVG.
- Generated and inspected native SVG thumbnail previews before and after. The route remains the principal accent; labels are clear at the reference size. The topology is now visibly coherent and the outer terrain fits inside the illustration.
- Checked the `contain` sizing calculation at 320, 390 and 640px viewports: the entire SVG fits the existing mobile image box. The unchanged SVG viewBox preserves proportional scaling at other widths.
- `privacy.html` and `CNAME` remain identical to Git HEAD. No HTML content, tokens, identity symbols, other page sections, hosting configuration or runtime dependencies were changed by this refinement. `git diff --check` passed.

## Limits and review

The intersection checks use ordinary floating-point arithmetic on the exported straight segments; they are not a formal symbolic proof or a GIS survey validation. The surface and plotted route are schematic, not geographical data. Label bounds are conservative estimates for the monospace font rather than browser-measured glyph boxes.

Native SVG rendering was inspected, but browser access was previously reported disabled in Work settings. No new browser-rendered desktop/mobile or font-metric verification is claimed. Final review should confirm the smaller, fully visible mobile artwork is balanced within its unchanged box and inspect the labels at the actual desktop display size. No redesign or infrastructure decision is required.
