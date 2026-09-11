import glob
import re

files = sorted(glob.glob('*.html'))
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    white_boxes = len(re.findall(r'bg-white\s+dark:bg-ink-900', content)) + len(re.findall(r'bg-white\s+dark:bg-primary-900', content)) + len(re.findall(r'bg-white\s+dark:bg-ink-950', content))
    glass_cards = len(re.findall(r'glass-card|morphism-card', content))
    glass_panels = len(re.findall(r'glass-panel', content))
    glass_inputs = len(re.findall(r'glass-input', content))
    glass_steps = len(re.findall(r'glass-step', content))
    glass_icons = len(re.findall(r'glass-icon', content))
    glass_tables = len(re.findall(r'glass-table-wrap', content))
    glass_pills = len(re.findall(r'glass-pill', content))
    
    print(f"=== {filename} ===")
    print(f"  plain white/dark boxes: {white_boxes}")
    print(f"  glass cards: {glass_cards} | panels: {glass_panels} | inputs: {glass_inputs} | steps: {glass_steps} | icons: {glass_icons} | tables: {glass_tables} | pills: {glass_pills}")
