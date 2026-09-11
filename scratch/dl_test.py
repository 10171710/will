import urllib.request, os

os.makedirs('scratch/test_images', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

photo_urls = {
    # 1. Witnessing a will: Signing legal document with pen
    '1_pen_signing': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=800&h=480&q=85',
    '1_hands_signing': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=800&h=480&q=85',
    '1_agreement_pen': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&h=480&q=85',
    '1_office_signing': 'https://images.unsplash.com/photo-1554224154-26032ffc0d07?auto=format&fit=crop&w=800&h=480&q=85',

    # 2. Probate timeline: Legal justice / court files / gavel
    '2_gavel_marble': 'https://images.unsplash.com/photo-1589391886645-d51941baf7fb?auto=format&fit=crop&w=800&h=480&q=85',
    '2_law_library': 'https://images.unsplash.com/photo-1505664194779-8beaceb93744?auto=format&fit=crop&w=800&h=480&q=85',
    '2_justice_scale': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&h=480&q=85',

    # 3. Family trusts: Family estate / wealth architecture / home trust
    '3_estate_home': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&h=480&q=85',
    '3_wealth_meeting': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=800&h=480&q=85',
    '3_modern_house': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&h=480&q=85',

    # 4. Talking to parents: Senior conversation / elder family
    '4_senior_tea': 'https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?auto=format&fit=crop&w=800&h=480&q=85',
    '4_elderly_hands': 'https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?auto=format&fit=crop&w=800&h=480&q=85',
    '4_family_living': 'https://images.unsplash.com/photo-1511895426328-dc8714191300?auto=format&fit=crop&w=800&h=480&q=85',

    # 5. Nominee is not an heir: Financial accounts / banking & investments
    '5_finance_chart': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&h=480&q=85',
    '5_bank_docs': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=800&h=480&q=85',
    '5_money_growth': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=800&h=480&q=85',

    # 6. Executor checklist: Clean checklist notepad with pen
    '6_checklist_pad': 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?auto=format&fit=crop&w=800&h=480&q=85',
    '6_planner_coffee': 'https://images.unsplash.com/photo-1517842645767-c639042777db?auto=format&fit=crop&w=800&h=480&q=85',
    '6_binder_desk': 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&w=800&h=480&q=85',

    # 7. Special needs trust: Caring hands / compassionate support
    '7_support_hands': 'https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?auto=format&fit=crop&w=800&h=480&q=85',
    '7_caring_touch': 'https://images.unsplash.com/photo-1536640712-4d4c36ff0e4e?auto=format&fit=crop&w=800&h=480&q=85',
    '7_warm_hug': 'https://images.unsplash.com/photo-1609220136736-443140cffec6?auto=format&fit=crop&w=800&h=480&q=85',

    # 8. Digital estate: Tech / cyber security / digital keys
    '8_cyber_security': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&h=480&q=85',
    '8_code_vault': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=800&h=480&q=85',
    '8_mobile_laptop': 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&h=480&q=85',

    # 9. Harder to contest: Legal binding documents / notary stamp / law gavel
    '9_law_books': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&h=480&q=85',
    '9_notary_seal': 'https://images.unsplash.com/photo-1589216532372-1c2a367900d9?auto=format&fit=crop&w=800&h=480&q=85',
    '9_parchment_quill': 'https://images.unsplash.com/photo-1506784365847-bbad939e9335?auto=format&fit=crop&w=800&h=480&q=85'
}

for name, url in photo_urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            with open(f'scratch/test_images/{name}.jpg', 'wb') as f:
                f.write(resp.read())
            print('Saved', name)
    except Exception as e:
        print('Error', name, e)
