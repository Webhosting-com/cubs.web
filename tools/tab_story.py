"""TAB Instagram story frame (1080x1920) built around a 1080x1350 post image.
Usage: python3 tools/tab_story.py post.jpg out.jpg "TOP LINE" "BOTTOM LINE"
Top line sits above the post (e.g. "NEW ON THE BLOG"), bottom line below it (e.g. "LINK IN BIO").
Needs Pillow."""
import sys, os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
O = (240, 74, 18); INK = (237, 232, 223); BG = (12, 11, 10)
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
IB = os.path.join(FD, 'Inter-Bold.otf')

def spaced_w(d, t, f, sp):
    return sum(d.textlength(c, font=f) + sp for c in t) - sp

def spaced(d, x, y, t, f, fill, sp):
    for c in t:
        d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + sp

def main(src, out, top='NEW ON THE BLOG', bottom='LINK IN BIO'):
    base = Image.new('RGB', (W, H), BG)
    post = Image.open(src).convert('RGB').resize((1000, 1250), Image.LANCZOS)
    y0 = (H - 1250) // 2
    base.paste(post, (40, y0))
    d = ImageDraw.Draw(base)
    f = ImageFont.truetype(IB, 34)
    t = top.upper(); w = spaced_w(d, t, f, 6)
    spaced(d, (W - w) / 2, y0 - 110, t, f, O, 6)
    b = bottom.upper(); f2 = ImageFont.truetype(IB, 30); bw = spaced_w(d, b, f2, 5)
    h = 84; x = (W - bw - 90) / 2; y = y0 + 1250 + 60
    d.rounded_rectangle([x, y, x + bw + 90, y + h], radius=h // 2, fill=O)
    spaced(d, x + 45, y + 24, b, f2, BG, 5)
    base.save(out, quality=88)

if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], a[1], *(a[2:4]))
