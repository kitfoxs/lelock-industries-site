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
- A research shelf linking the public USEL preprint and distinguishing later local manuscripts.
- A demonstrations page with a genuine local Wonderland capture.
- Kit + Ada attribution, a professional profile, verified public links, and privacy/reuse notes.
- Responsive layouts, keyboard navigation, project filters, and reduced-motion support.

## Edit

- Project content: `content/projects.json`.
- Page layouts and editorial copy: `scripts/build.py`.
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
