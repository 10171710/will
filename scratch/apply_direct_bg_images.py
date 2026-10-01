import glob
import re

page_to_hero_image = {
    'index.html': 'assets/images/estate-property-hero.jpg',
    'home-2.html': 'assets/images/service-business-succession.jpg',
    'about.html': 'assets/images/about-consulting-room.jpg',
    'services.html': 'assets/images/service-will-drafting.jpg',
    'service-details.html': 'assets/images/service-trust-creation.jpg',
    'blog.html': 'assets/images/organised-family-folder.jpg',
    'blog-details.html': 'assets/images/blog-witnessing-will.jpg',
    'blog-contest-proof-will.html': 'assets/images/blog-contest-proof-will.jpg',
    'blog-digital-estate.html': 'assets/images/blog-digital-estate.jpg',
    'blog-executor-checklist.html': 'assets/images/blog-executor-checklist.jpg',
    'blog-family-trust.html': 'assets/images/blog-family-trust.jpg',
    'blog-nominee-heir.html': 'assets/images/blog-nominee-heir.jpg',
    'blog-parent-conversation.html': 'assets/images/blog-parent-conversation.jpg',
    'blog-probate-timeline.html': 'assets/images/blog-probate-timeline.jpg',
    'blog-special-needs-care.html': 'assets/images/blog-special-needs-care.jpg',
    'contact.html': 'assets/images/estate-consultation.jpg',
    'pricing.html': 'assets/images/estate-investment.jpg',
    'login.html': 'assets/images/hero-quiet-conversation.jpg',
    'register.html': 'assets/images/service-power-attorney.jpg',
    '404.html': 'assets/images/service-estate-review.jpg',
    'coming-soon.html': 'assets/images/service-property-deeds.jpg',
    'maintenance.html': 'assets/images/property-inspection.jpg',
}

for page, img in page_to_hero_image.items():
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace hero-media div tag
    # e.g. <div class="hero-media" ... aria-hidden="true"></div>
    # or <div class="hero-media hero-media--panel" ...>
    
    pattern = r'<div class="([^"]*hero-media[^"]*)"[^>]*>'
    
    def repl(m):
        cls = m.group(1)
        return f'<div class="{cls}" style="background-image: url(\'{img}\'); --hero-image: url(\'{img}\');" aria-hidden="true">'
    
    new_content = re.sub(pattern, repl, content)
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {page:30} -> {img}")

print("\nAll 22 files updated with direct background-image inline styles on .hero-media.")
