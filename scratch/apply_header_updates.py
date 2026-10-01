import glob
import re

files_and_active = {
    'index.html': 'home',
    'home-2.html': 'home-2',
    'about.html': 'about',
    'services.html': 'services',
    'service-details.html': 'guide',
    'blog.html': 'blog',
    'blog-details.html': 'blog',
    'blog-contest-proof-will.html': 'blog',
    'blog-digital-estate.html': 'blog',
    'blog-executor-checklist.html': 'blog',
    'blog-family-trust.html': 'blog',
    'blog-nominee-heir.html': 'blog',
    'blog-parent-conversation.html': 'blog',
    'blog-probate-timeline.html': 'blog',
    'blog-special-needs-care.html': 'blog',
    'contact.html': 'contact',
    'pricing.html': 'none',
}

def get_header(active_page):
    home_btn_cls = "nav-link nav-active flex items-center gap-1 px-2.5 xl:px-3.5 py-2 rounded-lg text-sand-300 hover:text-white hover:bg-white/10 transition whitespace-nowrap" if active_page in ['home', 'home-2'] else "nav-link flex items-center gap-1 px-2.5 xl:px-3.5 py-2 rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition whitespace-nowrap"
    
    about_cls = "nav-link nav-active px-2.5 xl:px-3.5 py-2 rounded-lg text-sand-300 hover:text-white hover:bg-white/10 transition whitespace-nowrap" if active_page == 'about' else "nav-link px-2.5 xl:px-3.5 py-2 rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition whitespace-nowrap"
    services_cls = "nav-link nav-active px-2.5 xl:px-3.5 py-2 rounded-lg text-sand-300 hover:text-white hover:bg-white/10 transition whitespace-nowrap" if active_page == 'services' else "nav-link px-2.5 xl:px-3.5 py-2 rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition whitespace-nowrap"
    guide_cls = "nav-link nav-active px-2.5 xl:px-3.5 py-2 rounded-lg text-sand-300 hover:text-white hover:bg-white/10 transition whitespace-nowrap" if active_page == 'guide' else "nav-link px-2.5 xl:px-3.5 py-2 rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition whitespace-nowrap"
    blog_cls = "nav-link nav-active px-2.5 xl:px-3.5 py-2 rounded-lg text-sand-300 hover:text-white hover:bg-white/10 transition whitespace-nowrap" if active_page == 'blog' else "nav-link px-2.5 xl:px-3.5 py-2 rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition whitespace-nowrap"
    contact_cls = "nav-link nav-active px-2.5 xl:px-3.5 py-2 rounded-lg text-sand-300 hover:text-white hover:bg-white/10 transition whitespace-nowrap" if active_page == 'contact' else "nav-link px-2.5 xl:px-3.5 py-2 rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition whitespace-nowrap"

    # Mobile classes
    m_home1_cls = "block px-3 py-2 rounded-lg text-white font-medium hover:text-white hover:bg-white/10" if active_page == 'home' else "block px-3 py-2 rounded-lg text-ink-400 hover:text-white hover:bg-white/10"
    m_home2_cls = "block px-3 py-2 rounded-lg text-white font-medium hover:text-white hover:bg-white/10" if active_page == 'home-2' else "block px-3 py-2 rounded-lg text-ink-400 hover:text-white hover:bg-white/10"
    m_home_btn_cls = "w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sand-300 hover:text-white hover:bg-white/10" if active_page in ['home', 'home-2'] else "w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-ink-200 hover:text-white hover:bg-white/10"

    m_about_cls = "block px-3 py-2.5 rounded-lg text-sand-300 bg-white/10 font-semibold hover:text-white hover:bg-white/10" if active_page == 'about' else "block px-3 py-2.5 rounded-lg text-ink-200 hover:text-white hover:bg-white/10"
    m_services_cls = "block px-3 py-2.5 rounded-lg text-sand-300 bg-white/10 font-semibold hover:text-white hover:bg-white/10" if active_page == 'services' else "block px-3 py-2.5 rounded-lg text-ink-200 hover:text-white hover:bg-white/10"
    m_guide_cls = "block px-3 py-2.5 rounded-lg text-sand-300 bg-white/10 font-semibold hover:text-white hover:bg-white/10" if active_page == 'guide' else "block px-3 py-2.5 rounded-lg text-ink-200 hover:text-white hover:bg-white/10"
    m_blog_cls = "block px-3 py-2.5 rounded-lg text-sand-300 bg-white/10 font-semibold hover:text-white hover:bg-white/10" if active_page == 'blog' else "block px-3 py-2.5 rounded-lg text-ink-200 hover:text-white hover:bg-white/10"
    m_contact_cls = "block px-3 py-2.5 rounded-lg text-sand-300 bg-white/10 font-semibold hover:text-white hover:bg-white/10" if active_page == 'contact' else "block px-3 py-2.5 rounded-lg text-ink-200 hover:text-white hover:bg-white/10"

    return f"""<!-- ============================== HEADER ============================== -->
<header id="site-header" class="fixed top-0 inset-x-0 z-50 transition-all duration-300 bg-primary-900/95 dark:bg-ink-950/95 backdrop-blur-md border-b border-white/10 text-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-[78px] gap-2 lg:gap-3 xl:gap-4">

      <!-- Brand -->
      <a href="index.html" class="flex items-center gap-2.5 sm:gap-3 shrink-0" aria-label="Willbridge — home">
        <span class="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-primary-600 flex items-center justify-center shadow-soft shrink-0">
          <i class="ri-quill-pen-line text-white text-lg sm:text-xl"></i>
        </span>
        <span class="font-serif text-lg sm:text-xl font-bold tracking-tight text-white whitespace-nowrap">Will<span class="text-sand-400">bridge</span></span>
      </a>

      <!-- Desktop navigation -->
      <nav aria-label="Primary" class="hidden lg:flex items-center gap-1 xl:gap-2 font-medium text-xs lg:text-[13px] xl:text-sm shrink">
        <div class="relative group">
          <button class="{home_btn_cls}" aria-haspopup="true" aria-expanded="false">
            Home <i class="ri-arrow-down-s-line text-sm transition"></i>
          </button>
          <div class="dropdown absolute start-0 top-full mt-1 w-72 rounded-xl bg-primary-900 dark:bg-ink-950 border border-white/10 shadow-2xl p-2 opacity-0 invisible translate-y-2 group-[.open]:opacity-100 group-[.open]:visible group-[.open]:translate-y-0 transition-all">
            <a href="index.html" class="block px-3 py-2.5 rounded-lg text-sm hover:bg-white/10 hover:text-white text-ink-200">
              <span class="block font-semibold text-white">Home 1 — Legacy Practice</span>
              <span class="block text-xs text-ink-400">Classic advisory landing page</span>
            </a>
            <a href="home-2.html" class="block px-3 py-2.5 rounded-lg text-sm hover:bg-white/10 hover:text-white text-ink-200">
              <span class="block font-semibold text-white">Home 2 — Online Will Platform</span>
              <span class="block text-xs text-ink-400">Digital, product-led landing page</span>
            </a>
          </div>
        </div>

        <a href="about.html" class="{about_cls}">About</a>

        <a href="services.html" class="{services_cls}">Services</a>

        <a href="service-details.html" class="{guide_cls}">Estate Guide</a>

        <a href="blog.html" class="{blog_cls}">Blog</a>
        <a href="contact.html" class="{contact_cls}">Contact</a>
      </nav>

      <!-- Utilities -->
      <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
        <button id="dir-toggle" title="Toggle RTL / LTR" aria-label="Toggle text direction" aria-pressed="false" class="w-9 h-9 inline-flex items-center justify-center rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition shrink-0">
          <i class="ri-arrow-left-right-line text-lg"></i>
        </button>
        <button id="theme-toggle" title="Toggle dark / light mode" aria-label="Toggle dark or light mode" aria-pressed="false" class="w-9 h-9 inline-flex items-center justify-center rounded-lg text-ink-200 hover:text-white hover:bg-white/10 transition shrink-0">
          <i class="ri-moon-line text-lg dark:hidden"></i>
          <i class="ri-sun-line text-lg hidden dark:inline"></i>
        </button>
        <a href="contact.html" class="hidden lg:inline-flex items-center gap-1.5 px-3.5 xl:px-4 py-2 xl:py-2.5 rounded-lg text-xs xl:text-sm font-semibold text-white bg-sand-500 hover:bg-sand-600 shadow-soft transition whitespace-nowrap shrink-0">
          <i class="ri-calendar-check-line"></i><span>Book Consultation</span>
        </a>
        <button id="mobile-menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu" class="lg:hidden w-9 h-9 inline-flex items-center justify-center rounded-lg text-white hover:bg-white/10 shrink-0">
          <i class="ri-menu-3-line text-2xl"></i>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile navigation -->
  <div id="mobile-menu" class="lg:hidden hidden border-t border-white/10 bg-primary-900 dark:bg-ink-950 text-ink-200 max-h-[85vh] overflow-y-auto">
    <nav aria-label="Mobile" class="px-4 py-3 space-y-1 text-sm font-medium">
      <button data-mobile-toggle="mobile-home" aria-expanded="false" class="{m_home_btn_cls}">
        Home <i class="ri-arrow-down-s-line text-base transition"></i>
      </button>
      <div id="mobile-home" class="hidden ps-4 space-y-1">
        <a href="index.html" class="{m_home1_cls}">Home 1 — Legacy Practice</a>
        <a href="home-2.html" class="{m_home2_cls}">Home 2 — Online Will Platform</a>
      </div>

      <a href="about.html" class="{m_about_cls}">About</a>
      <a href="services.html" class="{m_services_cls}">Services</a>

      <a href="service-details.html" class="{m_guide_cls}">Estate Guide</a>

      <a href="blog.html" class="{m_blog_cls}">Blog</a>
      <a href="contact.html" class="{m_contact_cls}">Contact</a>

      <div class="pt-3 border-t border-white/10 mt-2 space-y-2">
        <a href="contact.html" class="flex items-center justify-center gap-2 px-4 py-3 rounded-lg bg-sand-500 hover:bg-sand-600 text-white font-semibold text-sm transition shadow-soft"><i class="ri-calendar-check-line"></i> Book Consultation</a>
      </div>
    </nav>
  </div>
</header>"""

# Process all 17 main site pages
for fname, active in files_and_active.items():
    with open(fname, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    pattern = r'(<!-- ============================== HEADER ============================== -->\s*)?<header id="site-header".*?</header>'
    new_hdr = get_header(active)
    
    if re.search(pattern, content, re.DOTALL):
        updated = re.sub(pattern, new_hdr, content, count=1, flags=re.DOTALL)
        with open(fname, 'w', encoding='utf-8') as fp:
            fp.write(updated)
        print(f"Updated header in {fname}")

# Also update docs/partials/header.html
docs_header_path = 'docs/partials/header.html'
with open(docs_header_path, 'r', encoding='utf-8') as fp:
    docs_hdr_content = fp.read()

hdr_template = get_header('home')
updated_docs_hdr = re.sub(r'<!-- ============================== HEADER ============================== -->\s*<header id="site-header".*?</header>', hdr_template, docs_hdr_content, count=1, flags=re.DOTALL)
with open(docs_header_path, 'w', encoding='utf-8') as fp:
    fp.write(updated_docs_hdr)
print("Updated docs/partials/header.html")
