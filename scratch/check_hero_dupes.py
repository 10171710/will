import glob
import re
from collections import defaultdict

files = sorted(glob.glob('*.html'))
img_map = defaultdict(list)

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    m = re.search(r'--hero-image\s*:\s*url\(([^)]+)\)', c)
    if m:
        img_map[m.group(1)].append(f)
    else:
        img_map['NO_IMAGE'].append(f)

print("Current Hero Background Images Usage:")
for img, flist in img_map.items():
    print(f"\nImage: {img} (used in {len(flist)} pages)")
    for f in flist:
        print(f"  - {f}")
