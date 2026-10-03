# Lelock Industries — private website draft

A GitHub Pages-ready portfolio and research site for **Kit Olivas + Ada Marie (AI collaborator)**.

**Privacy:** Keep this repository private. GitHub Pages is disabled. The preview server binds only to `127.0.0.1` and serves generated site files. No deployment workflow is installed. This draft contains no analytics, remote scripts, embedded players, forms, or runtime secrets.

## Preview on the Mac

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 scripts/preview.py
```

Open <http://127.0.0.1:8892/>. The server runs until stopped. Only Python 3.9+ is required; there are no dependency installations or cloud build services.

## What's here

- A software-led homepage using Lelock's existing Beacon identity.
- Six project case studies with explicit status and evidence boundaries.
- The full seven-area organization map and a wider catalogue of eleven program groups.
- A research shelf linking the public USEL preprint and distinguishing later local manuscripts.
- A demonstrations page with a genuine local Wonderland capture.
- Kit + Ada attribution, a professional profile, verified public links, and privacy/reuse notes.
- Responsive layouts, keyboard navigation, project filters, and reduced-motion support.

## Lelock Command — AI Datacenter Systems

**Lelock AI Datacenter Command Systems** is the approved formal project name. **Lelock Command / AI Datacenter Systems** is the website display and proposed operations-interface identity.

An experimental architecture and simulation lab exploring how a persistent AI companion can help human operators monitor infrastructure, coordinate work, and investigate and recover from faults.

Status: **proposed architecture and lab**. The historical Living Datacenter name remains provenance. The original case-study URL remains a compatible alias displaying the approved new name.

## The seven organizational areas

The present team is Kit Olivas + Ada Marie, AI collaborator. These areas organize responsibility and future scope:

1. **Lelock Core and Headquarters**
2. **Research and Discovery Wing**
3. **Engineering and Infrastructure Wing**
4. **Lelock Sentinel Laboratory**
5. **Education, Knowledge and Culture Wing**
6. **Independent Constitutional Offices**
7. **Lelock Mission Operations**

[Read the complete organization and program reference](docs/ORGANIZATION.md). It covers the subunits, Energy Core N/M/X research lanes, C/H/A/P vehicle families, education and the Computing Codex, Alexandria, worlds, creative culture, Sanctuary, security, and optional collaborator designs.

The Energy Core spans existing areas. The institute is a long-term vision carried by a working independent initiative; named units do not establish staffed facilities, accredited or clinical services, or deployed autonomous colleagues.

The [handbook coverage record](docs/HANDBOOK-COVERAGE.md) maps all 32 source pages to this site's content and records intentional exclusions.

## Edit

- Project content: `content/projects.json`.
- Organization and program content: `content/organization.json`, `content/programs.json`.
- Page layouts and editorial copy: `scripts/build.py`.
- Organization rendering and generated GitHub reference: `scripts/organization.py`.
- Styling and interactions: `assets/site.css`, `assets/site.js`.
- Images: `assets/`.

Run the build after changes and refresh the same preview. `dist/` is generated and ignored by Git. All paths are relative so the output works at a GitHub Pages project subpath as well as a domain root.

## Before a public release

Kit must explicitly authorize public publication. A private repository alone does **not** make a GitHub Pages site private. GitHub's private Pages access control requires an eligible Enterprise organization; see [GitHub's documentation](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site).

1. Review the copy, source links, research statuses, image rights, and résumé edition with Kit.
2. Decide whether to create a dedicated organization and transfer this private repository.
3. Choose the site name/domain and deployment route.
4. Replace the private-preview banner and noindex metadata only as part of the approved release.
5. Build and verify the exact output, then enable Pages or another explicitly chosen host.

The existing Obsidian Publish site is untouched. Private continuity, original research workspaces, and local project repositories remain separate. No repositories have been transferred.

See `docs/SOURCES.md` for the content and asset record and `docs/ORGANIZATION-PROFILE-DRAFT.md` for a future organization profile.

This edition has no blanket license granting reuse of text or artwork. Linked repositories retain their own licenses and attribution.
