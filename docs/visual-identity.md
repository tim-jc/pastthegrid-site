# Past the Grid / Visual identity

## Expedition Field Notebook

A modern field notebook for cycling, geography, exploration and technical work. Lead with clear editorial content; let survey lines and routes suggest discovery. Warm paper, precise typography and generous space carry the character. Avoid distressed textures, imitation parchment, stamps or theatrical adventure styling.

Two expressions share one geometry, type system and spacing scale:

- **Field Notebook:** paper surfaces, midnight ink, sage contours and copper routes. The public homepage’s primary expression.
- **Navigation Instrument:** midnight surfaces, paper text, survey-blue grid lines and copper routes. Demonstrated by the Cycling card; suitable for future analytical interfaces.

## Palette and tokens

The portable foundation is `assets/identity.css`. Copy this file and the needed SVGs into another application; no shared package or build step is required. Application layout belongs in its own stylesheet.

| Role | Field Notebook | Navigation Instrument |
| --- | --- | --- |
| `--bg` | Paper `#F1EFE7` | Midnight `#172630` |
| `--ink` | Midnight `#172630` | Paper `#F1EFE7` |
| `--muted` | `#52635C` | `#B5C6CC` |
| `--accent` | Dark copper `#9B582E` | Light copper `#E2A577` |
| `--surface` | `#E7E9DF` | `#1C303B` |
| `--line` | `#C8CDC2` | `#435965` |
| `--focus` | `#854822` | `#E2A577` |

Base colours also include sage `#667C73`, copper `#D18B58` and survey blue `#8BA9B7`. These are cartographic colours, not universal text or control colours. Use semantic ink, muted and accent tokens for text. Fine low-contrast rules are decorative; do not use them alone to communicate an interactive state.

Apply `data-theme="dark"` to a container or the document element. Theme switching does not require JavaScript. The homepage intentionally uses a light editorial canvas and a dark project surface rather than an automatic system-theme switch.

## Typography

Use the installed system stack: Avenir Next, Avenir, Segoe UI, sans-serif. The wordmark uses weight 600 and tight tracking; editorial headings use weight 500 and approximately −0.045em tracking. Paragraphs use normal weight, comfortable 1.65–1.9 line height and short reading widths. No remote fonts are loaded.

Use SFMono-Regular, Consolas, Liberation Mono, monospace for restrained labels and actual coordinates, timestamps or measurements when those exist. Uppercase technical labels use approximately 0.13em tracking. Small labels are supplementary, never the only source of meaningful information. Avoid fabricated coordinates and numerical readouts.

## Wordmark and symbol

- The primary lockup is the route symbol plus the live-text **Past the Grid.** wordmark. The copper full stop is optional in monochrome contexts.
- `assets/wordmark.svg` is a portable light-surface lockup. It uses live SVG text and system fonts, so exact metrics vary by platform. Use the HTML lockup when accessible live text is practical.
- `assets/symbol.svg` is the monochrome midnight symbol for light surfaces; `assets/symbol-dark.svg` reverses it to paper with dark waypoint interiors. Both use a 40-unit square and work at 24px and above. For coloured surfaces, inline the SVG and set `currentColor` and `--symbol-bg` to the appropriate ink and background; an SVG loaded through an image does not inherit page variables.
- `assets/favicon.svg` simplifies the identity into a midnight tile with a copper route and ivory waypoints for 16–32px browser use. At these sizes the route is primary and the grid is supporting detail.
- Leave at least one quarter of the symbol width clear around a standalone symbol. Keep grid and route proportions intact; never stretch or rotate the lockup. Do not add shadows or texture.
- For monochrome output, use the symbol as supplied or set the inline SVG’s current colour to the print ink and waypoint fill to the substrate. The route and endpoints communicate the idea without relying on colour.
- Give a logo link an accessible name; hide a redundant symbol beside a live-text name. Decorative art uses empty alt text and `aria-hidden`.

## Layout and components

Use the 4px spacing family in the CSS: 4, 8, 12, 16, 24, 32, 48, 64 and 96px. The homepage caps at 1440px including its gutters, with roughly 6.25% desktop gutters and 24px on mobile. Use hairline section rules, square project cards and restrained decoration. Rounded container stacks and floating ornamental badges are not part of this direction.

Cards have a cartographic illustration, a category, a plain project title, a brief explanation and a clear destination label. Each card uses separate primary dashboard and secondary source links, grouped in a wrapping action row; never nest links or other controls within a link. Use solid text, an arrow and a visible focus outline; colour alone must not identify interaction. Keep line lengths around 45–70 characters. At narrow widths, stack content and reduce map height before reducing text size.

## Cartography

`assets/field-map.svg` is a compact, schematic illustration: contour lines, a survey grid, a plotted route, two waypoints and a north cue. It represents no real location or journey. Coastal uses an abstract shoreline and Cycling an abstract route profile; neither is a chart or live feed. Keep these decorative and subordinate to real content. Do not reuse them as factual maps or graph axes.

Use thin, low-opacity sage contours on paper and survey-blue grids on midnight. Use copper for routes. Do not place readable content directly over busy line work. Reuse the route’s angular bends and circular endpoints across applications rather than replicating the entire homepage.

## Accessibility and motion

Semantic landmarks, logical headings, a skip link, named navigation and keyboard-visible focus are required. Normal text should meet WCAG AA 4.5:1; large text and essential interface graphics need 3:1. Copper and sage base colours do not automatically meet every combination: use semantic variants and recheck contrast on each actual surface. The homepage uses no essential low-contrast graphics.

Links have a 44px navigation height or a large card target. Respect reduced motion; the only effects are smooth anchor scrolling and a small hover-arrow translation, both disabled for reduced motion. Do not introduce scroll-triggered reveals or content that requires animation to become visible. Verify reflow, keyboard operation and 200% zoom in the consuming application.

## Adoption elsewhere

For Cycling and Coastal, copy the tokens, font stacks, logo assets and spacing conventions, then apply them to existing application structures. For Grafana, map semantic colours to its supported theme configuration and use the standalone symbol where branding is supported; no Grafana integration is implemented here. Dark analytical surfaces should prioritise chart contrast and distinguish series using labels or patterns as well as colour. Keep map motifs away from actual plots and measurements.

This is an initial identity specification, not a component library. No changes to other repositories or private services are included.
