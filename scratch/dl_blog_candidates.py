import urllib.request, json, os

os.makedirs('scratch/blog_candidates', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Curated high quality Unsplash photos for each theme:
candidates = {
    # 1. Witnessing a will / signing with pen
    'witness_1': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=800&h=480&q=85', # Signing contract pen
    'witness_2': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&h=480&q=85', # Law books gavel
    'witness_3': 'https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=800&h=480&q=85', # Handshake signing

    # 2. Probate timeline / court documents
    'probate_1': 'https://images.unsplash.com/photo-1505664194779-8beaceb93744?auto=format&fit=crop&w=800&h=480&q=85', # Library law court
    'probate_2': 'https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?auto=format&fit=crop&w=800&h=480&q=85', # Focus lens on document
    'probate_3': 'https://images.unsplash.com/photo-1589391886645-d51941baf7fb?auto=format&fit=crop&w=800&h=480&q=85', # Scales of justice

    # 3. Family trusts / wealth planning
    'trust_1': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=800&h=480&q=85', # Finance calculation papers
    'trust_2': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=800&h=480&q=85', # Financial planning chart
    'trust_3': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&h=480&q=85', # Real estate home trust

    # 4. Talking to elderly parents / family conversation
    'family_1': 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=800&h=480&q=85', # Warm family conversation
    'family_2': 'https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?auto=format&fit=crop&w=800&h=480&q=85', # Elderly hands holding
    'family_3': 'https://images.unsplash.com/photo-1581579438747-1dc8d17bbce4?auto=format&fit=crop&w=800&h=480&q=85', # Senior family talk

    # 5. Nominee vs heir / banking assets
    'nominee_1': 'https://images.unsplash.com/photo-1559526324-593bc073d998?auto=format&fit=crop&w=800&h=480&q=85', # Bank finance documents
    'nominee_2': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=800&h=480&q=85', # Banking certificate
    'nominee_3': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=800&h=480&q=85', # Wealth coins plant

    # 6. Executor checklist / 30 days
    'checklist_1': 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&w=800&h=480&q=85', # Checklist to-do list notepad
    'checklist_2': 'https://images.unsplash.com/photo-1517842645767-c639042777db?auto=format&fit=crop&w=800&h=480&q=85', # Notepad pen coffee
    'checklist_3': 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&w=800&h=480&q=85', # Checklist form

    # 7. Special needs trust / lifelong care
    'care_1': 'https://images.unsplash.com/photo-1536640712-4d4c36ff0e4e?auto=format&fit=crop&w=800&h=480&q=85', # Caring hands support
    'care_2': 'https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?auto=format&fit=crop&w=800&h=480&q=85', # Holding hands supportive
    'care_3': 'https://images.unsplash.com/photo-1609220136736-443140cffec6?auto=format&fit=crop&w=800&h=480&q=85', # Warm family embrace

    # 8. Digital estate / passwords & accounts
    'digital_1': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&h=480&q=85', # Digital security code
    'digital_2': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&h=480&q=85', # Cybersecurity tech laptop
    'digital_3': 'https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?auto=format&fit=crop&w=800&h=480&q=85', # Mobile digital account

    # 9. Harder to contest / sealed stamped will
    'contest_1': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=800&h=480&q=85', # Hand writing testament
    'contest_2': 'https://images.unsplash.com/photo-1589216532372-1c2a367900d9?auto=format&fit=crop&w=800&h=480&q=85', # Gavel and law stamps
    'contest_3': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=800&h=480&q=85', # Formal suit document
}

for name, url in candidates.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            with open(f'scratch/blog_candidates/{name}.jpg', 'wb') as f:
                f.write(resp.read())
            print(f'Downloaded {name}')
    except Exception as e:
        print(f'Error on {name}: {e}')
