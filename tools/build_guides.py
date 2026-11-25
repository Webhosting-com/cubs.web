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
.gate{{position:relative;border:1px solid var(--accent);border-radius:16px;padding:28px;margin:6px 0 30px;background:linear-gradient(135deg,rgba(240,74,18,.14),var(--panel) 60%)}}
.gate::before{{content:"";position:absolute;left:0;right:0;top:-110px;height:104px;background:linear-gradient(rgba(11,10,9,0),var(--bg));pointer-events:none}}
.gate h3{{font-family:Anton,sans-serif;font-weight:400;text-transform:uppercase;font-size:34px;margin:8px 0 8px;line-height:1}}.gate p{{color:var(--muted);margin:0 0 16px}}
.gate form{{display:flex;gap:10px;flex-wrap:wrap}}.gate input{{flex:1 1 240px;background:#0B0A09;border:1px solid #3a3631;border-radius:999px;color:var(--ink);font:16px Inter,sans-serif;padding:12px 18px}}.gate input:focus{{outline:2px solid var(--accent);border-color:transparent}}
.gate .gate-err{{color:#ffb020;margin:10px 0 0}}.gate .gate-fine{{font-size:13px;margin:14px 0 0}}
.linkbtn{{background:none;border:0;color:var(--ink);text-decoration:underline;font:inherit;cursor:pointer;padding:0}}
.unlocked .gate{{display:none}}
footer{{border-top:1px solid var(--line);padding:26px 0;color:var(--muted);font-size:13px}}
@media(max-width:600px){{.hlinks{{display:none}}.more ul{{grid-template-columns:1fr}}body{{font-size:16px}}}}
@media print{{body *{{display:none!important}}body::after{{content:"TAB guidance sheets can be read online at theaudiobox.co.uk";display:block;font:14pt Inter,sans-serif;color:#111;padding:40px}}body{{background:#fff}}}}
</style></head>
<body>
<header class="no-print"><div class="wrap"><a class="logo" href="/"><span class="badge"><small>THE</small>AUDIO<br>BOX</span>The Audio Box</a>
<nav class="hlinks"><a href="/#guides">All guides</a><a href="/#services">Services</a><a href="/#blog">Blog</a></nav></div></header>
<main class="wrap">
<section class="top">
<span class="eyebrow">TAB guidance sheet · {cat}</span>
<h1>{title}</h1>
<p class="lead">{summary}</p>
<div class="meta"><span class="pill">{mins} min read</span></div>
</section>
<article>
{preview}
<div class="gate" id="gate">
<span class="eyebrow">Free for mailing list members</span>
<h3>Read the full sheet</h3>
<p>Join the TAB mailing list to unlock this sheet and every other guidance sheet. You'll also get the blog every Friday.</p>
<form id="gateForm" novalidate><input type="email" id="gateEmail" placeholder="Your email address" autocomplete="email" required><button class="btn" type="submit">Join &amp; unlock</button></form>
<p class="gate-err" id="gateErr" hidden>Enter a valid email address.</p>
<p class="gate-fine">Free. Unsubscribe any time. Signing up opens the TAB mailing list page in a new tab. <button type="button" class="linkbtn" id="gateHave">Already subscribed? Unlock</button></p>
</div>
<div class="locked" id="locked" hidden>
{rest}
</div>
</article>
<section class="cta">
<h3>Want us to handle it?</h3>
<p>Our engineers mix, master and record across Cheltenham, Gloucestershire and South London. Book straight on WhatsApp.</p>
<div class="row"><a class="btn" href="/#services">See services</a><a class="btn ghost" href="{wa}" target="_blank" rel="noopener">Ask a question</a></div>
</section>
<section class="more"><h3>More guidance sheets</h3><ul>{more}</ul></section>
</main>
<footer><div class="wrap">© The Audio Box · <a href="/">theaudiobox.co.uk</a></div></footer>
<script>
(function(){{var K='tab_guides_member',NEWS='https://audios-newsletter.beehiiv.com/subscribe';
function ok(){{try{{return localStorage.getItem(K)==='1'}}catch(e){{return false}}}}
function unlock(){{try{{localStorage.setItem(K,'1')}}catch(e){{}}document.getElementById('locked').hidden=false;document.body.classList.add('unlocked')}}
if(ok()||/[?&]member=1/.test(location.search))unlock();
document.getElementById('gateHave').onclick=unlock;
document.getElementById('gateForm').onsubmit=function(e){{e.preventDefault();var v=document.getElementById('gateEmail').value.trim(),err=document.getElementById('gateErr');
if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v)){{err.hidden=false;return}}err.hidden=true;
window.open(NEWS+'?email='+encodeURIComponent(v)+'&utm_source=guides','_blank','noopener');unlock();document.getElementById('locked').scrollIntoView({{behavior:'smooth'}})}};
}})();
</script>
</body></html>
'''

os.makedirs(os.path.join(ROOT, 'guides'), exist_ok=True)
for g in GUIDES:
    others = [o for o in GUIDES if o['slug'] != g['slug']][:6]
    more = ''.join('<li><a href="%s.html"><small>%s</small>%s</a></li>' % (o['slug'], E(o['cat']), E(o['title'])) for o in others)
    wa = E(WA + urllib.parse.quote('Hi, I found The Audio Box website. I read the "%s" guide and have a question: ' % g['title']))
    full = md(g['body']); i = [m.start() for m in re.finditer('<h2>', full)]
    cut = i[1] if len(i) > 1 else (i[0] if i else len(full))
    pv, rt = full[:cut], full[cut:]
    page = PAGE.format(title=E(g['title']), summary=E(g['summary']), cat=E(g['cat']), mins=g['mins'], preview=pv, rest=rt, more=more, wa=wa)
    open(os.path.join(ROOT, 'guides', g['slug'] + '.html'), 'w', encoding='utf-8').write(page)

# home page cards between the markers
P = os.path.join(ROOT, 'index.html')
s = open(P, encoding='utf-8').read()
cats = []
for g in GUIDES:
    if g['cat'] not in cats: cats.append(g['cat'])
cards = ''.join(
    '<a class="guide" href="guides/%s.html" data-cat="%s"><span class="g-cat">%s · %d min</span><h3>%s</h3><p>%s</p><span class="g-go">Members · read the sheet →</span></a>'
    % (g['slug'], E(g['cat']), E(g['cat']), g['mins'], E(g['title']), E(g['summary'])) for g in GUIDES)
filters = '<button type="button" class="gf on" data-f="all">All</button>' + ''.join('<button type="button" class="gf" data-f="%s">%s</button>' % (E(c), E(c)) for c in cats)
block = '<!--GUIDES-->\n<div class="guides-head"><div><span class="eyebrow">Free from TAB</span><h3 class="guides-title">Guidance sheets</h3><p>Step-by-step guidance on sending stems, bouncing files, using plug-ins and more. Free for TAB mailing list members. Join once to unlock every sheet.</p></div></div>\n<div class="guide-filters" role="group" aria-label="Filter guides">' + filters + '</div>\n<div class="guide-grid">' + cards + '</div>\n<!--/GUIDES-->'
a, b = s.index('<!--GUIDES-->'), s.index('<!--/GUIDES-->') + len('<!--/GUIDES-->')
s = s[:a] + block + s[b:]
open(P, 'w', encoding='utf-8').write(s)
print('built', len(GUIDES), 'guides')
