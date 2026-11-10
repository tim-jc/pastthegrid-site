# Public code invitation / Readiness review

Reviewed 10 November 2026. Read-only review of the current public default branches; other repositories were not modified. Findings are a scoped source/documentation review, not a full security audit, history scan, licence opinion or fresh-clone execution test.

## Confirmed destinations

- Coastal: https://github.com/tim-jc/coastal — README identifies the coastal ride dashboard and its GitHub Pages root artifact; its `CNAME` is `coastal.pastthegrid.uk`.
- Cycling: https://github.com/tim-jc/cycling-analytics — README identifies the personal cycling dashboard and describes the production artifact, public Pages publication and separate platform infrastructure. Coastal’s README also links directly to its Activity Inspector documentation.
- Owner: https://github.com/tim-jc.

All three GitHub web destinations returned HTTP 200 without changing destinations. The public privacy notice also returned 200. Repository names were established through the owner’s public repository listing and verified against project documentation, not inferred from dashboard hostnames. The connected GitHub tool was unavailable; public GitHub API and raw-file endpoints were used instead.

## Readiness findings

| Check | Coastal | Cycling Analytics |
| --- | --- | --- |
| Explicit open-source licence | None found in the complete current file tree; GitHub licence metadata is null | None found in the complete current file tree; GitHub licence metadata is null |
| Purpose explained | Yes: README describes the coastal ride dashboard and its data source | Yes: README describes the R Markdown/flexdashboard cycling dashboard |
| Setup/adaptation guidance | Partial: environment template, module layout, metadata maintenance, validation/render commands and development/data-contract docs | Partial: `renv::restore()`, environment requirements, render command and detailed runtime contract |
| Independently reusable demo | Not established: requires the owner’s platform Silver data and hand-maintained metadata; README currently reports an upstream streams blocker | Not established: requires platform database/schema/data and a map API key; no self-contained sample-data workflow established in this review |

Neither repository is described on the homepage as unrestricted or licensed for reuse. The invitation accurately says the code is public to explore and asks people interested in adapting it to make contact. An explicit licence is an owner decision before strengthening the invitation to fork/adapt freely. Consider separate permissions for photographs, maps, ride data and other third-party material; a code licence alone does not resolve those rights.

## Configuration and publication review

Read both READMEs and complete file listings. Inspected Coastal’s `.gitignore`, `.Renviron.example`, `R/database.R`, `index.Rmd`, development, publishing and data-contract documentation and publication helper. Inspected Cycling’s `.gitignore`, `db/db.R`, runtime helpers, runtime contract, Activity Inspector guide and architecture assessment.

- Both database modules read credentials from environment variables. Both repositories ignore `.Renviron`; no tracked real `.Renviron` appeared in their current file listings. The inspected Coastal example uses obvious credential placeholders. No live credentials were identified in the selected files reviewed; this does not establish that the full repositories or their history are secret-free.
- Coastal’s example and documentation name an internal database host and a machine-specific Homebrew/Pandoc path. Cycling documentation names production infrastructure and related operational repositories. Review whether those details should remain public; replace owner-specific examples with portable placeholders where appropriate. No such details were copied into the homepage.
- Coastal explicitly preserves GPS/date metadata in its public photo-processing workflow. Review the actual published photographs and generated rider/location material for intended disclosure; the image binaries and generated dashboard payloads were not audited here.
- Cycling’s database helper logs connection host, database and username (not the password). Review where those logs may be published. Its architecture assessment is useful internally but includes detailed operational assumptions worth reviewing for a public audience.

## Recommended owner follow-up

1. Choose and add explicit licences to the two projects, accounting separately for non-code assets and third-party material. No licence was added automatically.
2. Add a short “adapt this project” path with sample/synthetic data, the minimum schema, dependency prerequisites and generic configuration examples. Clarify the Coastal input blocker if its status has changed.
3. Review public infrastructure descriptions, photo metadata and generated ride data; run a dedicated current-tree/history secret scan if a broader publication audit is wanted.

## Homepage implementation and checks

- Converted each card’s outer anchor to an article so the primary dashboard link and secondary GitHub link are valid sibling destinations. The primary action retains stronger typography; source links are small and underlined. The action row wraps without fixed card heights.
- Preserved hero markup/artwork, project artwork, identity tokens, privacy content and domain declaration. Added the owner’s profile in the existing footer navigation, before the retained privacy link.
- Browser reviewed at 1280px desktop and 320px mobile; measured reflow at 390 and 768px too. No horizontal document overflow at these widths; all four project actions remain within their cards and have 44px-high targets.
- Keyboard checked dashboard → source → next dashboard → source, with visible focus outlines including 3px outlines on source links. Browser accessibility snapshot exposes each project as a named article and gives each source link a distinct project-specific accessible name.
- Followed the footer privacy link in the local browser and verified the existing notice. Checked local file/fragment links, unique IDs, absence of nested anchors, preserved file hashes and `git diff --check`.
- No JavaScript or runtime dependencies introduced. No commit, push or deployment. Browser checks cover the available in-app browser, not every browser or a complete accessibility audit.
