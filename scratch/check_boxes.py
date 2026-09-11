import re

def check_boxes(filename):
    print(f"=== {filename} ===")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if re.search(r'class="[^"]*(?:bg-white\s+dark:bg-ink-900|bg-white\s+dark:bg-primary-900|bg-white\s+dark:bg-ink-950)', line):
            print(f"Line {i+1}: {line.strip()[:100]}")

for f in ['index.html', 'home-2.html', 'pricing.html', 'services.html']:
    check_boxes(f)
