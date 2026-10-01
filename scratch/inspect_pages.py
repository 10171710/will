import glob
import re

files = sorted(glob.glob('*.html'))
print(f"Total HTML files: {len(files)}")

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Hero section regex
    hero_section_match = re.search(r'<section[^>]*hero-section[^>]*>', content)
    hero_section = hero_section_match.group(0) if hero_section_match else 'NO HERO SECTION CLASS'
    
    hero_media_match = re.search(r'<div[^>]*hero-media[^>]*>', content)
    hero_media = hero_media_match.group(0) if hero_media_match else 'NO HERO MEDIA'
    
    # Header buttons
    dir_btn = 'YES' if 'id="dir-toggle"' in content else 'NO'
    theme_btn = 'YES' if 'id="theme-toggle"' in content else 'NO'
    
    # CTA in header
    header_part = content[:content.find('</header>')] if '</header>' in content else content[:3000]
    ctas_in_header = re.findall(r'<a[^>]*class="[^"]*rounded-lg[^"]*"[^>]*>.*?</a>', header_part, re.DOTALL)
    
    print(f"\n--- {f} ---")
    print(f"  Hero Section: {hero_section}")
    print(f"  Hero Media: {hero_media}")
    print(f"  Header RTL: {dir_btn}, Theme: {theme_btn}")
    print(f"  Header CTA buttons found ({len(ctas_in_header)}):")
    for c in ctas_in_header:
        clean_c = re.sub(r'\s+', ' ', c.strip())
        print(f"    {clean_c}")
