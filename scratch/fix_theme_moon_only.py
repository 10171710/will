import glob
import re

files = sorted(glob.glob('*.html') + glob.glob('docs/partials/*.html'))
print(f"Updating theme toggle in {len(files)} files...")

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Pattern matching theme-toggle button with multiple icons or dark:hidden / hidden dark:inline
    pattern = r'(<button id="theme-toggle"[^>]*>)\s*<i class="ri-moon-line[^"]*"[^>]*></i>\s*<i class="ri-sun-line[^"]*"[^>]*></i>\s*(</button>)'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\g<1>\n          <i class="ri-moon-line text-lg"></i>\n        \g<2>', content)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print(f"Updated {f}")
    else:
        # Check single line format
        pattern2 = r'(<button id="theme-toggle"[^>]*>)\s*<i class="ri-moon-line[^"]*"[^>]*></i>\s*(?:<i class="ri-sun-line[^"]*"[^>]*></i>)?\s*(</button>)'
        if re.search(pattern2, content):
            new_content = re.sub(pattern2, r'\g<1><i class="ri-moon-line text-lg"></i>\g<2>', content)
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            print(f"Updated (pattern2) {f}")
        else:
            print(f"Check manually: {f}")

print("\nDone updating theme toggle.")
