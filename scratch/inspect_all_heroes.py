import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    hero_cls = re.search(r'<section[^>]*class="([^"]*hero[^"]*)"', c)
    hero_img = re.search(r'--hero-image\s*:\s*url\(([^)]+)\)', c)
    cls_str = hero_cls.group(1) if hero_cls else "no hero section"
    img_str = hero_img.group(1) if hero_img else "no img"
    print(f"{f:30} | {cls_str:55} | {img_str}")
