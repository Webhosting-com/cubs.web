"""TAB Instagram post renderer (1080x1350, black/orange house style).
Usage: python3 tools/tab_post.py spec.json out.jpg
spec keys: photo (path), pos [x,y], bg, tag, kicker, headline ("LINE\nLINE"), hsize, accent_line,
body, items [[name, price]], cta, footl, footr, marks (quote mark).
Needs Pillow (pip install pillow)."""
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import os
W,H=1080,1350
O=(240,74,18); INK=(237,232,223); BG=(12,11,10); MUTED=(170,163,153)
import os as _os
_FD=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'fonts')
ANTON=_os.path.join(_FD,'Anton.ttf')
IB=_os.path.join(_FD,'Inter-Bold.otf'); IS=_os.path.join(_FD,'Inter-SemiBold.otf'); IR=_os.path.join(_FD,'Inter-Regular.otf')
F=lambda p,s: ImageFont.truetype(p,s)
def spaced(d,xy,text,font,fill,sp=4,anchor_right=False):
    x,y=xy
    w=sum(d.textlength(c,font=font)+sp for c in text)-sp
    if anchor_right: x-=w
    for c in text:
        d.text((x,y),c,font=font,fill=fill); x+=d.textlength(c,font=font)+sp
    return w
def cover(img,pos=(0.5,0.3)):
    iw,ih=img.size; s=max(W/iw,H/ih); img=img.resize((int(iw*s)+1,int(ih*s)+1),Image.LANCZOS)
    iw,ih=img.size; x=int((iw-W)*pos[0]); y=int((ih-H)*pos[1]); return img.crop((x,y,x+W,y+H))
def wrap(d,text,font,maxw):
    out=[]
    for para in text.split('\n'):
        line=''
        for w in para.split():
            t=(line+' '+w).strip()
            if d.textlength(t,font=font)<=maxw: line=t
            else: out.append(line); line=w
        out.append(line)
    return out
def render(p,out):
    if p.get('photo'):
        im=Image.open(p['photo']).convert('RGB'); im=ImageOps.grayscale(im).convert('RGB')
        im=ImageOps.autocontrast(im,cutoff=1); im=cover(im,p.get('pos',(0.5,0.3)))
        base=im
        grad=Image.new('L',(1,H))
        for y in range(H):
            t=max(0,(y-H*0.28)/(H*0.62)); grad.putpixel((0,y),int(255*min(1,t**0.9*1.2)))
        grad=grad.resize((W,H)); dark=Image.new('RGB',(W,H),BG)
        base=Image.composite(dark,base,grad)
        top=Image.new('L',(1,H))
        for y in range(H): top.putpixel((0,y),int(170*max(0,1-y/220)))
        base=Image.composite(dark,base,top.resize((W,H)))
    else:
        base=Image.new('RGB',(W,H),p.get('bg',BG))
    d=ImageDraw.Draw(base)
    orange_bg=p.get('bg')==O
    hd=BG if orange_bg else INK; acc=BG if orange_bg else O
    M=56
    spaced(d,(M,52),'THE AUDIO BOX',F(IB,22),hd,sp=5)
    if p.get('tag'): spaced(d,(W-M,52),p['tag'].upper(),F(IB,22),acc if not orange_bg else BG,sp=5,anchor_right=True)
    # bottom-up layout
    y_footer=H-78
    d.line([(M,y_footer-26),(W-M,y_footer-26)],fill=(60,56,52) if not orange_bg else (180,55,10),width=2)
    spaced(d,(M,y_footer),p.get('footl','THE AUDIO BOX').upper(),F(IS,19),MUTED if not orange_bg else BG,sp=4)
    spaced(d,(W-M,y_footer),p.get('footr','@THEAUDIOBOX_').upper(),F(IS,19),MUTED if not orange_bg else BG,sp=4,anchor_right=True)
    y=y_footer-60
    blocks=[]
    if p.get('cta'):
        f=F(IB,26); tw=spaced(ImageDraw.Draw(Image.new('RGB',(1,1))),(0,0),p['cta'].upper(),f,(0,0,0),sp=4)
        h=74; y-=h
        d.rounded_rectangle([M,y,M+tw+76,y+h],radius=h//2,fill=BG if orange_bg else O)
        spaced(d,(M+38,y+22),p['cta'].upper(),f,O if orange_bg else BG,sp=4)
        y-=36
    if p.get('items'):
        f1=F(IB,36); f2=F(IR,30)
        rows=p['items'][::-1]
        for name,price in rows:
            y-=64
            d.text((M,y),name,font=f1,fill=hd)
            pw=d.textlength(price,font=f1); d.text((W-M-pw,y),price,font=f1,fill=acc)
            d.line([(M,y+56),(W-M,y+56)],fill=(60,56,52) if not orange_bg else (180,55,10),width=1)
        y-=30
    if p.get('body'):
        f=F(IR,32); lines=wrap(d,p['body'],f,W-2*M-80)
        y-=len(lines)*44
        for i,l in enumerate(lines): d.text((M,y+i*44),l,font=f,fill=INK if not orange_bg else BG)
        y-=58
    # headline
    hs=p.get('hsize',150); fh=F(ANTON,hs); lh=int(hs*1.0)
    hl=p['headline'].split('\n')
    y-=len(hl)*lh
    for i,line in enumerate(hl):
        x=M; yy=y+i*lh
        accent_from=p.get('accent_line',len(hl)-1)
        col=acc if i>=accent_from else hd
        d.text((x,yy),line,font=fh,fill=col)
        if i==len(hl)-1 and line[-1] not in '?.!':
            x2=x+d.textlength(line,font=fh)
            d.text((x2+4,yy),'.',font=fh,fill=O if not orange_bg else BG)
    y-=22
    if p.get('kicker'): spaced(d,(M,y-30),p['kicker'].upper(),F(IB,24),acc,sp=6)
    if p.get('marks'):
        fm=F(ANTON,240); d.text((M-6,y-330),'“',font=fm,fill=acc)
    base.save(out,quality=95)


if __name__ == '__main__':
    import sys, json
    spec = json.load(open(sys.argv[1]))
    if 'pos' in spec: spec['pos'] = tuple(spec['pos'])
    if 'bg' in spec and isinstance(spec['bg'], list): spec['bg'] = tuple(spec['bg'])
    render(spec, sys.argv[2])
