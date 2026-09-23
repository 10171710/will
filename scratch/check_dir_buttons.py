import glob, re

for fn in sorted(glob.glob('**/*.html', recursive=True)):
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'(<button id="dir-toggle".*?</button>)', content, re.DOTALL)
    if m:
        print(f"=== {fn} ===")
        print(m.group(1))
