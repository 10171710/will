import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    theme_m = re.search(r'<button id="theme-toggle"[^>]*>(.*?)</button>', c, re.DOTALL)
    if theme_m:
        inner = re.sub(r'\s+', ' ', theme_m.group(1).strip())
        print(f"{f:30} : {inner}")
