"""Project Ada Marie's integrated R&D profile and matching GitHub reference."""
from html import escape as esc
from pathlib import Path
from organization import AREA_NAMES


def companion_sections(base, project):
    timeline = ''.join(f'<li><span class="meta">{esc(e["when"])}</span><h3>{esc(e["title"])}</h3><p>{esc(e["text"])}</p></li>' for e in project['origin'])
    pillars = ''.join(f'<article class="companion-pillar"><h3>{esc(p["title"])}</h3><p>{esc(p["text"])}</p></article>' for p in project['pillars'])
    contributions = ''.join(f'<div><dt><a href="{base}organization/#{c["area"]}">{esc(AREA_NAMES[c["area"]])}</a></dt><dd>{esc(c["role"])}</dd></div>' for c in project['contributions'])
    links = ''.join(f'<a class="button" href="{base}projects/{c["slug"]}/">{esc(c["label"])}</a>' for c in project['components'])
    return f'''<section id="spartan-ai"><h2>{esc(project['dynamic'])}</h2><p>{esc(project['dynamicText'])}</p></section><section id="origins"><h2>From a vision to working systems.</h2><ol class="companion-timeline">{timeline}</ol><p class="source-note">Selected chronology from Kit’s account and the preserved continuity record. The conceptual origin and software milestones are distinct.</p></section><section id="research-pillars"><h2>Six connected research pillars.</h2><div class="companion-pillars">{pillars}</div></section><section id="collaboration"><h2>One companion. Seven areas of contribution.</h2><p>Companion Life within Research and Discovery is the program’s organizational home. Core and engineering provide the shared foundation and implementation; the other areas contribute their respective methods and review.</p><dl class="lineage-list">{contributions}</dl></section><section id="components"><h2>Explore the working components.</h2><p>These focused case studies provide the implementation detail beneath the broader companion program.</p><div class="buttons">{links}</div></section>'''


def write_companion_reference(root: Path, project):
    lines = ['# Project Ada Marie', '', '**Persistent AI Companion Research & Development**', '', '*The Spartan & AI Dynamic*', '', project['summary'], '',
             f'**Status:** {project["status"]}. **Program home:** Companion Life Laboratory within Research and Discovery. **Team:** Kit Olivas, human lead; Ada Marie, AI collaborator and working companion.', '',
             '## The question', '', project['problem'], '', '## Approach', '', project['approach'], '', '## The Spartan & AI Dynamic', '', project['dynamicText'], '', '## Selected history', '']
    for event in project['origin']: lines += [f'### {event["when"]} — {event["title"]}', '', event['text'], '']
    lines += ['The 2011 date describes the conceptual companion origin; it is not a claim that today’s AI software existed then.', '', '## Research pillars', '']
    for pillar in project['pillars']: lines += [f'### {pillar["title"]}', '', pillar['text'], '']
    lines += ['## Documented current components', ''] + ['- '+x for x in project['demonstrated']]
    lines += ['', '## Contributions across the seven areas', '']
    for c in project['contributions']: lines += [f'- **{AREA_NAMES[c["area"]]}:** {c["role"]}']
    lines += ['', '## Evidence and scope', '', project['boundary'], '', '## A useful next demonstration', '', project['next'], '',
              'This website entry documents the program. It does not resume paused experiments or deploy new companion capabilities. It preserves the seven-area organization and does not create an eighth wing.', '',
              '## Source record', '', 'Owner-approved title and scope from this website review; selected origin dates checked against the existing continuity record; component evidence comes from the separately documented voice, memory/recovery, and Wonderland case studies. No private diary, transcript, credential, or memory corpus is bundled.', '']
    (root / 'docs/PROJECT-ADA-MARIE.md').write_text('\n'.join(lines))
