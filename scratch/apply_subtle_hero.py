import re

pages_to_update = {
    'index.html': 'estate-property-hero.jpg',
    'home-2.html': 'service-business-succession.jpg',
    'about.html': 'about-consulting-room.jpg',
    'service-details.html': 'service-trust-creation.jpg'
}

for page, img in pages_to_update.items():
    content = open(page, 'r', encoding='utf-8').read()
    
    # Replace hero-media with hero-media hero-media--subtle
    pattern = r'<div class="hero-media[^"]*"[^>]*style="[^"]*background-image:\s*url\(\'assets/images/[^\']+\'\);"[^>]*aria-hidden="true"></div>'
    replacement = f'<div class="hero-media hero-media--subtle" style="background-image: url(\'assets/images/{img}\');" aria-hidden="true"></div>'
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        open(page, 'w', encoding='utf-8').write(content)
        print(f"Updated {page} with hero-media--subtle")
    else:
        print(f"WARNING: pattern not matched in {page}")

print("Done updating subtle hero pages.")
