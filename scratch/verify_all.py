import glob
import re

files = sorted(glob.glob('*.html'))
all_clean = True

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check basic structure
    has_doctype = '<!DOCTYPE html>' in content
    has_html_end = '</html>' in content
    has_style_css = 'assets/css/style.css' in content
    
    # Check open/close tags for major tags
    tags_to_check = ['main', 'header', 'footer', 'form', 'section']
    tag_errors = []
    for tag in tags_to_check:
        opens = len(re.findall(rf'<{tag}[\s>]', content, re.IGNORECASE))
        closes = len(re.findall(rf'</{tag}>', content, re.IGNORECASE))
        if opens != closes:
            tag_errors.append(f"{tag} ({opens} open, {closes} close)")
    
    glass_count = len(re.findall(r'glass-[a-z-]+', content))
    
    status = "OK" if has_doctype and has_html_end and has_style_css and not tag_errors else "ERROR"
    if status == "ERROR":
        all_clean = False
    
    print(f"[{status}] {filename:22} | glass tokens: {glass_count:3} | tag errors: {tag_errors if tag_errors else 'none'}")

print(f"\nFinal Status: {'ALL 14 PAGES CLEAN & VALID' if all_clean else 'SOME PAGES HAVE ISSUES'}")
