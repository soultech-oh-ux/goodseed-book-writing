# -*- coding: utf-8 -*-
"""메인페이지 분위기 썸네일(OG) 생성 — 1200x630 PNG. 크리스마스 그린·눈·소나무·책."""
from PIL import Image, ImageDraw, ImageFont
import random

W, H = 1200, 630
BD = "C:/Windows/Fonts/malgunbd.ttf"; RG = "C:/Windows/Fonts/malgun.ttf"
def f(p, s): return ImageFont.truetype(p, s)

img = Image.new("RGB", (W, H), (18, 54, 36)); px = img.load()
top, bot = (20, 56, 38), (15, 81, 50)
for y in range(H):
    t = y/(H-1); c = tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3))
    for x in range(W): px[x, y] = c
d = ImageDraw.Draw(img, "RGBA")

def pine(cx, base, s, col):
    d.polygon([(cx,base-118*s),(cx+34*s,base-66*s),(cx-34*s,base-66*s)], fill=col)
    d.polygon([(cx,base-86*s),(cx+42*s,base-30*s),(cx-42*s,base-30*s)], fill=col)
    d.polygon([(cx,base-54*s),(cx+50*s,base+8*s),(cx-50*s,base+8*s)], fill=col)
    d.polygon([(cx,base-118*s),(cx+12*s,base-94*s),(cx-12*s,base-94*s)], fill=(238,245,241,220))
for cx, sc in [(70,1.05),(158,.72),(1128,1.15),(1052,.72),(972,.95)]:
    pine(cx, H+6, sc, (12,58,37))

random.seed(7)
for _ in range(95):
    x=random.randint(0,W); y=random.randint(0,H); r=random.choice([2,2,3,3,4])
    d.ellipse([x-r,y-r,x+r,y+r], fill=(255,255,255, random.randint(110,235)))

# 책
bx,by,bw,bh = 812,150,248,348
d.rounded_rectangle([bx+10,by+12,bx+bw+10,by+bh+12], radius=12, fill=(0,0,0,70))
d.rounded_rectangle([bx,by,bx+bw,by+bh], radius=10, fill=(16,64,42))
d.rectangle([bx,by,bx+16,by+bh], fill=(9,44,30))
d.rectangle([bx+bw-9,by+8,bx+bw-2,by+bh-8], fill=(239,238,228))
d.text((bx+40,by+34), "GOODSEED PRESS", font=f(BD,15), fill=(201,170,110))
d.line([bx+40,by+66,bx+bw-30,by+66], fill=(200,214,206,160), width=1)
d.text((bx+42,by+92),  "세상에",   font=f(BD,30), fill=(206,224,214))
d.text((bx+42,by+132), "하나뿐인", font=f(BD,34), fill=(255,255,255))
d.text((bx+42,by+180), "나의 책",  font=f(BD,34), fill=(255,255,255))
d.line([bx+40,by+236,bx+bw-30,by+236], fill=(200,214,206,160), width=1)
d.text((bx+42,by+300), "MY IDEA · MY BOOK", font=f(BD,13), fill=(206,224,214))

# 좌측 텍스트
d.text((70,72), "GOODSEED BOOK WRITING", font=f(BD,22), fill=(193,227,203))
d.text((66,158), "생각과 아이디어만 있으면,", font=f(BD,45), fill=(255,255,255))
d.text((66,224), "한 권의 책", font=f(BD,58), fill=(240,201,74))
w = d.textbbox((0,0),"한 권의 책",font=f(BD,58))[2]
d.text((66+w+8,236), "이 됩니다.", font=f(BD,50), fill=(255,255,255))
d.text((68,314), "아이디어에서 출판까지 — 종이책을 손에 받는 전 과정", font=f(RG,24), fill=(221,236,227))
# 하단 강조 바
d.rounded_rectangle([66,360,610,410], radius=10, fill=(158,42,43))
d.text((88,372), "8주 · 하루 2시간 · 오경근 교수와 함께", font=f(BD,24), fill=(255,245,228))

img.save("og-cover.png", "PNG"); print("saved og-cover.png")
