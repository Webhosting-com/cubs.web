"""Add a spotlight and/or blog post to index.html.
python3 tools/add_to_site.py spotlight spot.json   -> appends to SPOTLIGHTS
  spot.json: {"name","handle" (no @),"bio","photo" and "photo2" (data:image/... URL or path to a jpg; give both so both frames fill; saved to img/ as files),"pos":"50% 30%","pos2",
              "release": {"url","verb","title","by"} or null}
python3 tools/add_to_site.py post post.json        -> adds to the top of POSTS
  post.json: {"title","date":"YYYY-MM-DD","tag","excerpt","url"}"""
import sys, json, base64, os, io, hashlib
from PIL import Image, ImageOps
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
s = open(P, encoding='utf-8').read()
kind, f = sys.argv[1], sys.argv[2]
d = json.load(open(f, encoding='utf-8'))
J = lambda v: json.dumps(v, ensure_ascii=False)
if kind == 'spotlight':
    def img(ph):
        raw = base64.b64decode(ph.split(',', 1)[1]) if ph.startswith('data:') else open(ph, 'rb').read()
        im = ImageOps.exif_transpose(Image.open(io.BytesIO(raw))).convert('RGB'); im.thumbnail((1600, 1600))
        rel = 'img/' + hashlib.sha1(raw).hexdigest()[:12] + '.jpg'
        os.makedirs(os.path.join(ROOT, 'img'), exist_ok=True)
        im.save(os.path.join(ROOT, rel), quality=82, optimize=True, progressive=True)
        print('saved', rel)
        return rel
    phs = [(img(d['photo']), d.get('pos', '50% 30%'))]
    if d.get('photo2'): phs.append((img(d['photo2']), d.get('pos2', d.get('pos', '50% 30%'))))
    else: print('WARNING: only one photo given, second frame will be empty', file=sys.stderr)
    if J(d['name']) in s.split('const SPOTLIGHTS')[1].split('\n];')[0]: sys.exit('already on the site')
    rel = d.get('release')
    entry = ('  { name: %s, handle: %s, bio: %s,\n    photos: [%s],\n    release: %s },\n'
             % (J(d['name']), J(d['handle'].lstrip('@')), J(d.get('bio', '')), ', '.join('{ src: %s, pos: %s }' % (J(a), J(b)) for a, b in phs),
                J(rel) if rel else "{ url: 'https://instagram.com/" + d['handle'].lstrip('@') + "', verb: 'Follow', title: '@" + d['handle'].lstrip('@') + "', by: 'Instagram' }"))
    a = s.index('const SPOTLIGHTS'); b = s.index('\n];', a)
    s = s[:b] + '\n' + entry.rstrip('\n') + s[b:]
elif kind == 'post':
    if d['url'] in s: sys.exit('already on the site')
    entry = '  { title: %s, date: %s, tag: %s, excerpt: %s, url: %s },\n' % (J(d['title']), J(d['date']), J(d.get('tag', 'Blog')), J(d.get('excerpt', '')), J(d['url']))
    a = s.index('const POSTS = ['); a = s.index('\n', a) + 1
    s = s[:a] + entry + s[a:]
open(P, 'w', encoding='utf-8').write(s)
print('ok', kind)
