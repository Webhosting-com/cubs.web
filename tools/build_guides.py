"""Build TAB guidance sheets: guides/<slug>.html pages + the guide cards on the home page.
Run from the repo root: python3 tools/build_guides.py"""
import html, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guides_content import GUIDES

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
E = html.escape

def md(body):
    out, para, lst = [], [], None
    def flush():
        nonlocal para, lst
        if para: out.append('<p>' + ' '.join(para) + '</p>'); para = []
        if lst: out.append('<%s>%s</%s>' % (lst[0], ''.join('<li>%s</li>' % x for x in lst[1]), lst[0])); lst = None
    for raw in body.strip().split('\n'):
        line = raw.strip()
        if not line: flush(); continue
        t = E(line)
        if line.startswith('## '): flush(); out.append('<h2>%s</h2>' % E(line[3:]))
        elif line.startswith('> '): flush(); out.append('<div class="tip"><b>TAB tip</b>%s</div>' % E(line[2:]))
        elif line.startswith('!! '): flush(); out.append('<div class="tip warn"><b>Watch out</b>%s</div>' % E(line[3:]))
        elif line.startswith('- '):
            if para: flush()
            if not lst or lst[0] != 'ul': flush(); lst = ('ul', [])
            lst[1].append(E(line[2:]))
        elif re.match(r'\d+\. ', line):
            if para: flush()
            if not lst or lst[0] != 'ol': flush(); lst = ('ol', [])
            lst[1].append(E(re.sub(r'^\d+\. ', '', line)))
        else:
            if lst: flush()
            para.append(t)
    flush()
    return '\n'.join(out)

WA = 'https://wa.me/447346791576?text='

PAGE = '''<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | TAB guidance sheets</title>
<meta name="description" content="{summary}">
<meta property="og:title" content="{title} | The Audio Box"><meta property="og:description" content="{summary}">
<meta property="og:image" content="https://theaudiobox.co.uk/og.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23F04A12'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@300;400;500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0B0A09;--panel:#12110F;--ink:#EDE8DF;--muted:#A19B90;--line:#25221F;--accent:#F04A12}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
a{{color:inherit}}.wrap{{max-width:820px;margin:0 auto;padding:0 22px}}
header{{border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(11,10,9,.92);backdrop-filter:blur(10px);z-index:5}}
header .wrap{{max-width:1140px;display:flex;align-items:center;justify-content:space-between;height:64px}}
.logo{{display:flex;align-items:center;gap:12px;text-decoration:none;font-family:Oswald,sans-serif;letter-spacing:.12em;text-transform:uppercase;font-size:17px}}
.badge{{width:38px;height:38px;background:var(--accent);color:#0B0A09;font-family:Anton,sans-serif;font-size:11px;line-height:.9;display:flex;flex-direction:column;justify-content:center;padding:0 4px;letter-spacing:0}}
.badge small{{font-size:.75em}}
.hlinks{{display:flex;gap:18px;font-size:13px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}}.hlinks a{{text-decoration:none;color:var(--muted)}}.hlinks a:hover{{color:var(--ink)}}
.top{{padding:64px 0 28px}}
.eyebrow{{color:var(--accent);font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase}}
h1{{font-family:Anton,Impact,sans-serif;font-weight:400;text-transform:uppercase;font-size:clamp(44px,8vw,84px);line-height:.95;margin:14px 0 16px}}
.lead{{color:#cfc9be;font-size:19px;margin:0 0 22px}}
.meta{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.pill{{border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-size:13px;color:var(--muted)}}
.btn{{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:#0B0A09;border:0;border-radius:999px;padding:13px 24px;font:700 13px Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;cursor:pointer}}
.btn.ghost{{background:none;color:var(--ink);border:1px solid #3a3631}}
article{{padding:10px 0 40px;border-top:1px solid var(--line)}}
article h2{{font-family:Oswald,sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:.02em;font-size:28px;margin:40px 0 12px;color:var(--ink)}}
article h2::before{{content:"";display:inline-block;width:10px;height:10px;background:var(--accent);margin-right:12px;vertical-align:middle}}
article p,article li{{color:#d6d0c5}}
article ul,article ol{{padding-left:22px}}article li{{margin:6px 0}}article li::marker{{color:var(--accent);font-weight:700}}
.tip{{border-left:3px solid var(--accent);background:rgba(240,74,18,.08);padding:14px 18px;border-radius:0 10px 10px 0;margin:24px 0;color:#e6e0d6}}
.tip b{{display:block;color:var(--accent);font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:4px}}
.tip.warn{{border-color:#ffb020;background:rgba(255,176,32,.08)}}.tip.warn b{{color:#ffb020}}
.cta{{border:1px solid var(--accent);border-radius:16px;padding:28px;margin:10px 0 50px;background:linear-gradient(135deg,rgba(240,74,18,.12),var(--panel) 60%)}}
.cta h3{{font-family:Anton,sans-serif;font-weight:400;text-transform:uppercase;font-size:34px;margin:0 0 8px;line-height:1}}.cta p{{color:var(--muted);margin:0 0 18px}}
.cta .row{{display:flex;gap:10px;flex-wrap:wrap}}
.more h3{{font-family:Oswald,sans-serif;font-weight:400;text-transform:uppercase;font-size:22px;margin:0 0 14px}}
.more ul{{list-style:none;padding:0;margin:0 0 60px;display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.more a{{display:block;border:1px solid var(--line);border-radius:10px;padding:14px 16px;text-decoration:none;font-weight:600;background:var(--panel)}}.more a:hover{{border-color:var(--accent)}}
.more small{{display:block;color:var(--accent);font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:2px}}
footer{{border-top:1px solid var(--line);padding:26px 0;color:var(--muted);font-size:13px}}
.print-only{{display:none}}
@media(max-width:600px){{.hlinks{{display:none}}.more ul{{grid-template-columns:1fr}}body{{font-size:16px}}}}
@media print{{
  @page{{margin:16mm}}
  body{{background:#fff;color:#111;font-size:11.5pt;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  header,.no-print,.more,.cta,footer{{display:none!important}}
  .print-only{{display:flex}}
  .top{{padding:0 0 10px}} h1{{color:#111;font-size:36pt}} .lead{{color:#333}}
  article{{border:0}} article p,article li{{color:#222}} article h2{{color:#111;font-size:15pt;margin-top:20px}}
  .tip{{background:#fff4ef;color:#222}} .pill{{color:#555;border-color:#ccc}}
}}
.pbrand{{align-items:center;justify-content:space-between;border-bottom:3px solid #F04A12;padding-bottom:10px;margin-bottom:18px;font:600 10pt Inter,sans-serif;color:#333}}
.pbrand .badge{{width:44px;height:44px;font-size:13px}}
</style></head>
<body>
<header class="no-print"><div class="wrap"><a class="logo" href="/"><span class="badge"><small>THE</small>AUDIO<br>BOX</span>The Audio Box</a>
<nav class="hlinks"><a href="/#guides">All guides</a><a href="/#services">Services</a><a href="/#blog">Blog</a></nav></div></header>
<main class="wrap">
<div class="print-only pbrand"><span class="badge"><small>THE</small>AUDIO<br>BOX</span><span>TAB guidance sheet · theaudiobox.co.uk</span></div>
<section class="top">
<span class="eyebrow">TAB guidance sheet · {cat}</span>
<h1>{title}</h1>
<p class="lead">{summary}</p>
<div class="meta"><span class="pill">{mins} min read</span><button class="btn ghost no-print" type="button" onclick="window.print()">Save as PDF / print</button></div>
</section>
<article>
{body}
</article>
<section class="cta">
<h3>Want us to handle it?</h3>
<p>Our engineers mix, master and record across Cheltenham, Gloucestershire and South London. Book straight on WhatsApp.</p>
<div class="row"><a class="btn" href="/#services">See services</a><a class="btn ghost" href="{wa}" target="_blank" rel="noopener">Ask a question</a></div>
</section>
<section class="more"><h3>More guidance sheets</h3><ul>{more}</ul></section>
</main>
<footer><div class="wrap">© The Audio Box · <a href="/">theaudiobox.co.uk</a> · Free to share with credit.</div></footer>
</body></html>
'''

os.makedirs(os.path.join(ROOT, 'guides'), exist_ok=True)
for g in GUIDES:
    others = [o for o in GUIDES if o['slug'] != g['slug']][:6]
    more = ''.join('<li><a href="%s.html"><small>%s</small>%s</a></li>' % (o['slug'], E(o['cat']), E(o['title'])) for o in others)
    wa = E(WA + urllib.parse.quote('Hi, I found The Audio Box website. I read the "%s" guide and have a question: ' % g['title']))
    page = PAGE.format(title=E(g['title']), summary=E(g['summary']), cat=E(g['cat']), mins=g['mins'], body=md(g['body']), more=more, wa=wa)
    open(os.path.join(ROOT, 'guides', g['slug'] + '.html'), 'w', encoding='utf-8').write(page)

# home page cards between the markers
P = os.path.join(ROOT, 'index.html')
s = open(P, encoding='utf-8').read()
cats = []
for g in GUIDES:
    if g['cat'] not in cats: cats.append(g['cat'])
cards = ''.join(
    '<a class="guide" href="guides/%s.html" data-cat="%s"><span class="g-cat">%s · %d min</span><h3>%s</h3><p>%s</p><span class="g-go">Read the sheet →</span></a>'
    % (g['slug'], E(g['cat']), E(g['cat']), g['mins'], E(g['title']), E(g['summary'])) for g in GUIDES)
filters = '<button type="button" class="gf on" data-f="all">All</button>' + ''.join('<button type="button" class="gf" data-f="%s">%s</button>' % (E(c), E(c)) for c in cats)
block = '<!--GUIDES-->\n<div class="guides-head"><div><span class="eyebrow">Free from TAB</span><h3 class="guides-title">Guidance sheets</h3><p>Branded, step-by-step sheets on sending stems, bouncing files, using plug-ins and more. Read them here or save them as a PDF.</p></div></div>\n<div class="guide-filters" role="group" aria-label="Filter guides">' + filters + '</div>\n<div class="guide-grid">' + cards + '</div>\n<!--/GUIDES-->'
a, b = s.index('<!--GUIDES-->'), s.index('<!--/GUIDES-->') + len('<!--/GUIDES-->')
s = s[:a] + block + s[b:]
open(P, 'w', encoding='utf-8').write(s)
print('built', len(GUIDES), 'guides')
