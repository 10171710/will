import re

def inspect_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"=== {filename} ===")
    for i, line in enumerate(lines):
        if re.search(r'class="[^"]*(?:p-\d|rounded-2xl|rounded-xl|border)[^"]*bg-white dark:bg-ink-900', line) or \
           re.search(r'class="[^"]*bg-white dark:bg-primary-900', line) or \
           re.search(r'<input|<textarea|<select', line):
            print(f"Line {i+1}: {line.strip()[:110]}")

inspect_file('service-details.html')
