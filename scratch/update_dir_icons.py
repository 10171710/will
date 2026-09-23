import glob, re

files = sorted(glob.glob('**/*.html', recursive=True))

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for dir-toggle button with span dir-ltr / dir-rtl
    pattern = r'(<button id="dir-toggle"[^>]*>)\s*<span class="dir-ltr[^>]*>RTL</span>\s*<span class="dir-rtl[^>]*>LTR</span>\s*(</button>)'
    
    def repl(m):
        btn_open = m.group(1)
        btn_close = m.group(2)
        # Check indentation of button
        return f'{btn_open}\n          <i class="ri-translate-2 text-lg"></i>\n        {btn_close}'

    new_content = re.sub(pattern, repl, content)
    if new_content != content:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {fn}")
    else:
        print(f"No match in: {fn}")
