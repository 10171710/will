import re
import os

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all cards
pattern = r'<article id="([^"]+)"[^>]*>([\s\S]*?)</article>'
cards = re.findall(pattern, content)

print(f"Found {len(cards)} service cards:")
for card_id, body in cards:
    links = re.findall(r'href="([^"]+)"', body)
    title_match = re.search(r'<h3[^>]*>.*?<a[^>]*>([^<]+)</a>', body)
    title = title_match.group(1) if title_match else card_id
    print(f"\n- Service: {title} (ID: #{card_id})")
    for link in links:
        exists = os.path.exists(link.split('#')[0])
        status = "EXISTS" if exists else "NOT FOUND"
        print(f"    Link: {link} -> {status}")
