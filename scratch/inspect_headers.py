import glob
import re

files = sorted(glob.glob('*.html'))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    header_m = re.search(r'(<header.*?</header>)', c, re.DOTALL)
    if not header_m:
        print(f"=== {f} : NO HEADER ===")
        continue
    
    header = header_m.group(1)
    
    has_desktop_nav = 'aria-label="Primary"' in header
    has_mobile_nav = 'id="mobile-menu"' in header
    
    dir_btn = re.search(r'<button id="dir-toggle"[^>]*>', header)
    theme_btn = re.search(r'<button id="theme-toggle"[^>]*>', header)
    
    cta_btns = re.findall(r'<a[^>]*contact\.html[^>]*>.*?</a>', header, re.DOTALL)
    
    print(f"=== {f} ===")
    print(f"  DesktopNav: {has_desktop_nav}, MobileNav: {has_mobile_nav}")
    print(f"  DirBtn:   {dir_btn.group(0) if dir_btn else 'NONE'}")
    print(f"  ThemeBtn: {theme_btn.group(0) if theme_btn else 'NONE'}")
    print(f"  CTAs in header ({len(cta_btns)}):")
    for b in cta_btns:
        print(f"    {re.sub(r'\s+', ' ', b.strip())}")
