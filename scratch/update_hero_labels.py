import glob
import re

pages = sorted(glob.glob('*.html'))

for p in pages:
    content = open(p, 'r', encoding='utf-8').read()
    orig = content
    
    # In hero sections, upgrade any remaining text-ink-400 or text-ink-500 to darker high contrast text
    def update_hero_section(match):
        sec = match.group(0)
        # update dt labels in hero
        sec = re.sub(
            r'class="([^"]*?)text-ink-400([^"]*?)"',
            r'class="\1text-ink-700 dark:text-ink-300 font-medium\2"',
            sec
        )
        return sec

    content = re.sub(r'<section[^>]*hero-section[\s\S]*?</section>', update_hero_section, content)
    
    if content != orig:
        open(p, 'w', encoding='utf-8').write(content)
        print(f"Updated secondary hero text in {p}")

print("Completed.")
