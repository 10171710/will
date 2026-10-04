import glob, re

pages_updated = []
for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check if page has hero-section
    if 'hero-section' in content:
        # Standardize inner container py-14 sm:py-20 to py-16 sm:py-24 in hero-section
        # Find hero section block
        hero_match = re.search(r'(<section[^>]*hero-section[^>]*>)(.*?)(</section>)', content, re.DOTALL)
        if hero_match:
            hero_full = hero_match.group(0)
            hero_updated = re.sub(r'py-14\s+sm:py-20', 'py-16 sm:py-24', hero_full)
            if hero_updated != hero_full:
                content = content.replace(hero_full, hero_updated)
                with open(f, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                pages_updated.append(f)

print(f"Updated hero inner padding to py-16 sm:py-24 in {len(pages_updated)} pages:")
for p in pages_updated:
    print(f"  - {p}")
