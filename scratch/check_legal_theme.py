import glob
import re

for f in glob.glob('c:/Users/HP/Downloads/legal-aid-template/**/*.html', recursive=True)[:5]:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    theme_m = re.findall(r'<button[^>]*id="theme-toggle"[^>]*>.*?</button>', c, re.DOTALL)
    if theme_m:
        print(f, theme_m[0])
