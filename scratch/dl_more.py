import urllib.request, os

os.makedirs('scratch/more_candidates', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

urls = {
    # Topic 4: Talking with elderly parents / senior family discussion
    '4_senior_couple_talk': 'https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?auto=format&fit=crop&w=800&h=480&q=85',
    '4_family_table_talk': 'https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&h=480&q=85',
    '4_daughter_mother': 'https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?auto=format&fit=crop&w=800&h=480&q=85',
    '4_intergenerational': 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=800&h=480&q=85',
    '4_senior_discussion': 'https://images.unsplash.com/photo-1581579438747-1dc8d17bbce4?auto=format&fit=crop&w=800&h=480&q=85',
    '4_elderly_hands_warm': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&h=480&q=85',
    
    # Topic 9: Contest-proof will / legal seal / courtroom
    '9_scales_justice': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&h=480&q=85',
    '9_legal_contract': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=800&h=480&q=85',
    '9_stamped_law': 'https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=800&h=480&q=85',
    
    # Additional options for parents talk
    '4_senior_home': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=800&h=480&q=85'
}

for name, u in urls.items():
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            with open(f'scratch/more_candidates/{name}.jpg', 'wb') as f:
                f.write(resp.read())
            print('Downloaded', name)
    except Exception as e:
        print('Error', name, e)
