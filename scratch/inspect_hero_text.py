import glob
import re

pages = sorted(glob.glob('*.html'))
for p in pages:
    c = open(p, 'r', encoding='utf-8').read()
    hero_section = re.search(r'<section[^>]*hero-section[^>]*>([\s\S]*?)</section>', c)
    if not hero_section:
        # Check login/register or first section
        hero_section = re.search(r'<section[^>]*>([\s\S]*?)</section>', c)
    if hero_section:
        content = hero_section.group(1)
        h1s = re.findall(r'<h1[^>]*class="([^"]*)"[^>]*>', content)
        ps = re.findall(r'<p[^>]*class="([^"]*)"[^>]*>', content)
        spans = re.findall(r'<span[^>]*class="([^"]*)"[^>]*>', content)
        print(f"=== {p} ===")
        print(f"  H1: {h1s}")
        print(f"  P: {ps}")
