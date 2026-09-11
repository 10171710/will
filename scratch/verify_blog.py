import os, re

def check_html(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check images
    img_srcs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content)
    print(f"Checking {path} ({len(img_srcs)} images):")
    for src in img_srcs:
        if src.startswith('http'):
            print(f"  [EXTERNAL/PLACEHOLDER] {src}")
        elif not os.path.exists(src.replace('/', os.sep)):
            print(f"  [MISSING FILE] {src}")
        else:
            print(f"  [OK] {src}")
    
    # Check pagination
    has_pag = 'aria-label="Pagination"' in content or 'Pagination' in content
    print(f"  Pagination present: {has_pag}")

check_html('blog.html')
print('-'*50)
check_html('blog-details.html')
print('-'*50)
check_html('index.html')
