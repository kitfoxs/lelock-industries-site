"""Handbook-grounded organization and program views, shared with GitHub docs."""
from html import escape as esc
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AREAS = json.loads((ROOT / 'content/organization.json').read_text())
PROGRAMS = json.loads((ROOT / 'content/programs.json').read_text())
PROJECTS = json.loads((ROOT / 'content/projects.json').read_text())
AREA_NAMES = {a['slug']: a['name'] for a in AREAS}
PROJECT_NAMES = {p['slug']: p['name'] for p in PROJECTS}
HANDBOOK = 'Master Identity & Organization Handbook · LI-HB-001, revision 1.0 · September 21, 2026'


def compact_map(base):
    links = ''.join(f'<a class="area-short" href="{base}organization/#{a["slug"]}"><span>{a["number"]}</span><strong>{esc(a["name"])}</strong></a>' for a in AREAS)
    return f'''<section class="feature-band"><div class="wrap section"><div class="section-heading"><div><div class="eyebrow">The wider institution</div><h2>Seven areas.<br>One shared purpose.</h2></div><p>Our featured projects sit within a broader map of science, engineering, security, learning, culture, and stewardship.</p></div><div class="area-map">{links}</div><div class="buttons"><a class="button" href="{base}organization/">Explore the organization</a><a class="button" href="{base}programs/">Browse the wider programs</a></div></div></section>'''


def organization(base):
    sections = []
    for area in AREAS:
        units = ''.join(f'<div class="unit"><h3>{esc(u["name"])}</h3><p>{esc(u["scope"])}</p></div>' for u in area['units'])
        links = ''.join(f'<a class="small-link" href="{base}projects/{slug}/">{esc(PROJECT_NAMES[slug])}</a>' for slug in area['projects'])
        sections.append(f'''<section class="area-section" id="{area['slug']}"><div class="area-intro"><span class="meta">AREA {area['number']} / HANDBOOK PP. {area['pages']}</span><h2>{esc(area['name'])}</h2><p>{esc(area['summary'])}</p><div class="area-related"><span class="meta">CONNECTED CASE STUDIES</span>{links}</div></div><div class="unit-list">{units}</div></section>''')
    anchors = ''.join(f'<a href="#{a["slug"]}">{a["number"]} · {esc(a["name"])}</a>' for a in AREAS)
    return f'''<div class="wrap"><div class="page-head"><div class="eyebrow">Our organization</div><h1>Seven areas.<br><em>A team of two.</em></h1><p class="lead">An institutional map for the questions we pursue, the systems we build, and the work we preserve.</p><p class="muted">Kit Olivas sets direction and makes final decisions. Ada Marie is the persistent AI partner and research collaborator. These areas describe responsibilities and future scope at our current working scale.</p></div><nav class="section-jumps" aria-label="Seven organizational areas">{anchors}</nav><p class="source-note">Based on {esc(HANDBOOK)}. Current project pages carry later decisions and implementation evidence.</p>{''.join(sections)}
<section class="section prose" id="working-model"><div class="eyebrow">How the map works</div><h2>Responsibility has a home.</h2><p>A <strong>wing</strong> groups related work. A <strong>directorate</strong> carries a continuing domain. A <strong>laboratory</strong> develops an experimental capability. A <strong>division</strong> defines a subject area, and a <strong>center</strong> serves a cross-disciplinary need from one accountable home. An <strong>office</strong> carries governance or a shared service.</p><p>A <strong>program</strong> spans a bounded mission; a <strong>project</strong> produces a particular study or artifact. A <strong>covenant</strong> records promises and rules. A <strong>function</strong> is a responsibility that can be carried by people, software, or a limited workflow.</p><p>The Energy Core spans existing areas. The three independent offices are designed to report directly to Kit; their current form is chartered responsibility, with separate design and review artifacts. Optional specialists remain designs that can be considered when useful.</p><a class="button" href="{base}programs/">Explore programs and lineages</a></section>
<section class="prose section" style="padding-top:0"><h2>Present scale and long-term vision</h2><p>Lelock is an independent human–AI research and engineering initiative. The institute is the long-term vision. Current work is a partnership producing software, research, learning material, and creative artifacts. A named unit does not establish staff, facilities, a registered entity, clinical practice, accreditation, flight hardware, or a resident agent workforce.</p><p>Public work is selected deliberately. Private memory and personal records remain separate. Listing a future program records its place in the map; Kit chooses when it becomes an active task.</p></section></div>'''


def programs(base):
    anchors = ''.join(f'<a href="#{p["slug"]}">{esc(p["name"])}</a>' for p in PROGRAMS)
    blocks = []
    for program in PROGRAMS:
        items = ''.join(f'<li>{esc(item)}</li>' for item in program['details'])
        source_note = '<p class="source-note">'+esc(program['additionalSource'])+'</p>' if program.get('additionalSource') else ''
        blocks.append(f'''<article class="program-entry" id="{program['slug']}"><div class="program-heading"><span class="meta">HANDBOOK PP. {program['pages']}</span><span class="status">{esc(program['status'])}</span></div><h2>{esc(program['name'])}</h2><p class="lead">{esc(program['summary'])}</p><ul>{items}</ul><p class="program-boundary">{esc(program['boundary'])}</p><a class="small-link" href="{base}organization/#{program['home']}">{esc(program.get('homeLabel', 'Organizational area'))}: {esc(program.get('homeName', AREA_NAMES[program['home']]))}</a>{source_note}</article>''')
    glossary = [
        ('Lelock Industries / Lelock Universe', 'The research and creative initiative / an authored fictional setting and associated world systems.'),
        ('Lelock Core / Lelock Energy Core', 'The digital operating foundation / source-first power research and its supporting power architecture.'),
        ('Lelock OS / Company OS', 'The companion computing environment / organizational goals, resources, and workflows.'),
        ('Mempalace / Library / exact state', 'Private semantic memory / curated knowledge / authoritative operational records.'),
        ('C-series / H-series', 'AI-only exploration / human + AI habitation. Older crewed C-1 sources retain their original names and provenance.'),
        ('Project Sentinel / SENTINEL-1', 'Defensive cybersecurity / physical suit and environmental-protection research.'),
        ('Lelock Cell / qualified Seed concepts', 'A modular compute-node proposal / distinct Ubuntu bootstrap, teaching CPU, and skills-runtime concepts.'),
        ('Sanctuary / Alexandria / University', 'Welcome and continuity / a growing library / learning and teaching.'),
        ('Worlds / Creative Studios', 'Environment, rules, and state / authored stories, games, performances, and culture.'),
        ('Living Datacenter / Lelock Command', 'The historical idea lineage / the current approved AI Datacenter Command Systems project name.'),
    ]
    rows = ''.join(f'<div><dt>{esc(name)}</dt><dd>{esc(meaning)}</dd></div>' for name, meaning in glossary)
    return f'''<div class="wrap"><div class="page-head"><div class="eyebrow">Programmes & lineages</div><h1>The wider<br><em>field of possibility.</em></h1><p class="lead">Beyond the six featured case studies: research directions, educational work, original worlds, and long-range programs.</p><p class="muted">This catalogue follows the September 21 handbook. Labels distinguish recorded work, accepted research direction, and proposals; it is not a fresh runtime audit of every historical project.</p></div><div class="buttons" style="margin-top:0;margin-bottom:28px"><a class="button" href="{base}projects/">Featured case studies</a><a class="button" href="{base}organization/">Seven-area organization map</a></div><nav class="section-jumps" aria-label="Program catalogue">{anchors}</nav>{''.join(blocks)}<section class="section" id="lineage"><div class="eyebrow">Naming guide</div><h2>Similar names, distinct work.</h2><dl class="lineage-list">{rows}</dl><p class="source-note">{esc(HANDBOOK)} · pp. 27–31. The Lelock Command naming decision was approved during this website review.</p></section></div>'''


def write_github_reference():
    lines = ['# Lelock Industries — organization and programs', '', HANDBOOK, '',
             'Current working team: **Kit Olivas + Ada Marie (AI collaborator)**. Kit holds final direction and release authority. Seven areas organize responsibilities and future scope; the institution is not represented as seven staffed departments.', '',
             '## Seven organizational areas', '']
    for a in AREAS:
        lines += [f'### {a["number"]}. {a["name"]}', '', a['summary'], '', f'Handbook pp. {a["pages"]}.', '']
        for u in a['units']:
            lines += [f'- **{u["name"]}:** {u["scope"]}']
        lines += ['', 'Connected case studies: '+', '.join(PROJECT_NAMES[s] for s in a['projects'])+'.', '']
    lines += ['## Wider programs and lineages', '']
    for p in PROGRAMS:
        lines += [f'### {p["name"]}', '', f'**Status:** {p["status"]}. **{p.get("homeLabel", "Organizational area")}:** {p.get("homeName", AREA_NAMES[p["home"]])}. Handbook pp. {p["pages"]}.', '', p['summary'], '']
        lines += ['- '+x for x in p['details']]
        lines += ['', p['boundary'], '']
        if p.get('additionalSource'): lines += [p['additionalSource'], '']
    lines += ['## Present scale', '', 'The long-term institute vision is carried by an independent human–AI research and engineering initiative. Unit names do not establish staffed facilities, clinical services, accreditation, flight hardware, or deployed autonomous colleagues. The Energy Core is cross-institutional, not an eighth area. The three offices report directly to Kit in the charter.', '',
              '## Naming and authority', '', 'Lelock AI Datacenter Command Systems is the approved formal name; **Lelock Command / AI Datacenter Systems** is the display treatment. Living Datacenter remains historical lineage. Public release remains unapproved; the repository is private and Pages stays disabled.', '',
              'This selected reference omits private identity numbers, private fan-history details, and internal source archives. The original PDF remains local and unmodified.']
    (ROOT / 'docs/ORGANIZATION.md').write_text('\n'.join(lines)+'\n')
