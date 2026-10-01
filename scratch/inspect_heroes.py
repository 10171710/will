import glob
import re

files = sorted(glob.glob('*.html'))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Hero section tag
    hero_section_match = re.search(r'<section[^>]*class="([^"]*hero-section[^"]*)"[^>]*>', content)
    hero_sec = hero_section_match.group(1) if hero_section_match else 'NO HERO'
    
    # Hero image style
    hero_img_match = re.search(r'--hero-image\s*:\s*url\(([^)]+)\)', content)
    hero_img = hero_img_match.group(1) if hero_img_match else 'NO HERO IMG'
    
    # Header CTA in desktop / header utility
    header_area = content[:content.find('</header>')] if '</header>' in content else ''
    cta_header = re.findall(r'<a[^>]*contact\.html[^>]*class="([^"]*)"[^>]*>(.*?)</a>', header_area, re.DOTALL)
    
    print(f"{f:30} | HeroClass: {hero_sec:45} | Img: {hero_img:40}")
    for cls, inner in cta_header:
        inner_clean = re.sub(r'\s+', ' ', inner.strip())
        print(f"   CTA: cls='{cls}' inner='{inner_clean}'")
