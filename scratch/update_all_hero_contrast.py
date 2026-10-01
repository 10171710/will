import glob
import re

# Update HTML files
pages = sorted(glob.glob('*.html'))

for p in pages:
    content = open(p, 'r', encoding='utf-8').read()
    orig = content
    
    # Locate hero section or first section (for 404, login, etc.)
    # In general, replace text-ink-500 dark:text-ink-400 in hero areas
    
    # 1. Update hero paragraphs with text-ink-500 dark:text-ink-400
    # Specifically in hero sections
    def update_hero_section(match):
        sec = match.group(0)
        # replace paragraph classes
        sec = re.sub(
            r'class="([^"]*?)text-ink-500 dark:text-ink-400([^"]*?)"',
            r'class="\1text-ink-900 dark:text-ink-100 font-medium\2"',
            sec
        )
        sec = re.sub(
            r'class="([^"]*?)text-ink-600 dark:text-ink-300([^"]*?)"',
            r'class="\1text-ink-900 dark:text-ink-100 font-medium\2"',
            sec
        )
        sec = re.sub(
            r'class="([^"]*?)text-primary-900 dark:text-white([^"]*?)"',
            r'class="\1text-primary-950 dark:text-white\2"',
            sec
        )
        return sec

    # Apply to hero-section
    content = re.sub(r'<section[^>]*hero-section[\s\S]*?</section>', update_hero_section, content)
    
    # Also handle main tag in 404, coming-soon, maintenance
    if p in ['404.html', 'coming-soon.html', 'maintenance.html']:
        content = re.sub(r'<main[^>]*hero-section[\s\S]*?</main>', update_hero_section, content)

    if content != orig:
        open(p, 'w', encoding='utf-8').write(content)
        print(f"Updated hero text contrast in {p}")
    else:
        print(f"No changes needed in {p}")

print("HTML hero text contrast updates complete.")
