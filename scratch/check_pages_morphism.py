import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Found {len(html_files)} HTML files: {html_files}")

for fname in sorted(html_files):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    glass_cards = len(re.findall(r'glass-card|morphism-card', content))
    glass_pills = len(re.findall(r'glass-pill', content))
    glass_badges = len(re.findall(r'glass-badge', content))
    glass_floating = len(re.findall(r'glass-floating', content))
    glass_panels = len(re.findall(r'glass-panel', content))
    print(f"{fname:20s} -> glass-card: {glass_cards:2d}, pill: {glass_pills:2d}, badge: {glass_badges:2d}, floating: {glass_floating:2d}, panel: {glass_panels:2d}")
