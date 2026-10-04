import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    sec_match = re.search(r'<section[^>]*class="([^"]*hero-section[^"]*)"[^>]*>', c)
    media_match = re.search(r'<div[^>]*class="([^"]*hero-media[^"]*)"[^>]*style="([^"]*)"[^>]*>', c)
    inner_match = re.search(r'<div[^>]*class="([^"]*max-w-7xl[^"]*py-[^"]*)"[^>]*>', c)
    
    sec_class = sec_match.group(1) if sec_match else 'NO HERO SECTION'
    media_info = f'{media_match.group(1)} | {media_match.group(2)}' if media_match else 'NO HERO MEDIA'
    inner_class = inner_match.group(1) if inner_match else 'NO INNER'
    
    print(f'{f:30} | {sec_class}')
    print(f'   Media: {media_info}')
    print(f'   Inner: {inner_class}\n')
