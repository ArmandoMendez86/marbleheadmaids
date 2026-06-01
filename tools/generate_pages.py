#!/usr/bin/env python3
"""Generate internal HTML pages for Marble Head Maids clone."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_description}">
  <meta name="author" content="Marble Head Maids">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_base}css/styles.css">
</head>
<body>

  <header class="header">
    <div class="container header__inner">
      <a href="{base}index.html" class="logo">Marble Head <span class="text-primary">Maids</span></a>
      <nav class="nav" aria-label="Main navigation">
        <div class="nav__dropdown" data-dropdown="services">
          <button class="nav__dropdown-btn" type="button" aria-expanded="false" aria-haspopup="true">Services
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="nav__dropdown-menu" hidden></div>
        </div>
        <div class="nav__dropdown" data-dropdown="locations">
          <button class="nav__dropdown-btn" type="button" aria-expanded="false" aria-haspopup="true">Locations
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="nav__dropdown-menu" hidden></div>
        </div>
        <a href="{base}about.html" class="nav__link">About</a>
        <a href="{base}checklist.html" class="nav__link">Checklist</a>
        <a href="{base}contact.html" class="nav__link">Contact</a>
      </nav>
      <div class="header__actions">
        <button class="btn-quote btn-quote--header" type="button">Get a Quote</button>
        <a href="tel:+16176866805" class="btn-phone btn-phone--header">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          (617) 686-6805
        </a>
      </div>
      <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </header>

  <div class="mobile-overlay" hidden aria-hidden="true"></div>
  <aside class="mobile-panel" aria-hidden="true" aria-label="Mobile menu">
    <div class="mobile-panel__inner">
      <div class="mobile-panel__header">
        <span class="mobile-panel__title">Menu</span>
        <button class="mobile-panel__close" type="button" aria-label="Close menu">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <nav class="mobile-panel__nav">
        <div class="mobile-panel__group">
          <button class="mobile-panel__toggle" type="button" data-mobile-toggle="services" aria-expanded="false"><span>Services</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="mobile-panel__submenu" hidden data-mobile-submenu="services"></div>
        </div>
        <div class="mobile-panel__group">
          <button class="mobile-panel__toggle" type="button" data-mobile-toggle="locations" aria-expanded="false"><span>Locations</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="mobile-panel__submenu" hidden data-mobile-submenu="locations"></div>
        </div>
        <a href="{base}about.html" class="mobile-panel__link">About</a>
        <a href="{base}checklist.html" class="mobile-panel__link">Checklist</a>
        <a href="{base}contact.html" class="mobile-panel__link">Contact</a>
      </nav>
      <div class="mobile-panel__actions">
        <button class="btn-quote btn-quote--full" type="button">Get a Quote</button>
        <a href="tel:+16176866805" class="btn-phone btn-phone--full">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          <span>(617) 686-6805</span>
        </a>
      </div>
    </div>
  </aside>
"""

FOOTER_SCRIPTS = """
  <footer class="site-footer" id="site-footer"></footer>
  <script src="{js_base}js/data.js"></script>
  <script src="{js_base}js/layout.js"></script>
  <script src="{js_base}js/page.js"></script>
</body>
</html>
"""

SERVICE_FOOTER_SCRIPTS = """
  <footer class="site-footer" id="site-footer"></footer>
  <script src="{js_base}js/data.js"></script>
  <script src="{js_base}js/layout.js"></script>
  <script src="{js_base}js/service-pages.js"></script>
  <script src="{js_base}js/service.js"></script>
  <script src="{js_base}js/page.js"></script>
</body>
</html>
"""

SERVICE_BODY = """
  <main>
    <section class="service-hero" id="service-hero">
      <div class="service-hero__bg">
        <div class="service-hero__bg-image" id="service-hero-bg"></div>
        <div class="service-hero__bg-overlay"></div>
      </div>
      <div class="container service-hero__content">
        <div class="service-hero__inner">
          <h1 class="service-hero__title">{h1}</h1>
          <p class="service-hero__subtitle">{hero_subtitle}</p>
          <div class="service-hero__cta">
            <button class="btn-hero-quote btn-page-quote" type="button">Get a Quote</button>
            <a href="tel:+16176866805" class="btn-hero-phone btn-page-phone">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>(617) 686-6805</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="trust" id="service-trust"></section>

    <section class="service-intro" id="service-intro"></section>

    <section class="service-checklist" id="service-checklist"></section>

    <section class="service-when" id="service-when"></section>

    <section class="service-how" id="service-how"></section>

    <section class="services service-page-other">
      <div class="container">
        <div class="services__header">
          <h2 class="services__title">Other Cleaning Services</h2>
          <p class="services__intro">Explore our full range of cleaning services available in the North Shore and North Suburbs.</p>
        </div>
        <div class="services__grid" id="service-other-grid"></div>
      </div>
    </section>

    <section class="recurring" id="service-recurring">
      <div class="container">
        <div class="recurring__header">
          <h2 class="recurring__title" id="service-recurring-title"></h2>
          <p class="recurring__subtitle" id="service-recurring-subtitle"></p>
        </div>
        <div class="recurring__grid" id="service-recurring-grid"></div>
        <div class="recurring__footer">
          <p class="recurring__text" id="service-recurring-text"></p>
          <div class="recurring__cta">
            <button class="btn-quote btn-recurring-quote" type="button">Get A Quote</button>
            <a href="tel:+16176866805" class="btn-phone btn-recurring-phone">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>(617) 686-6805</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="service-pricing" id="service-pricing"></section>

    <section class="why-trust service-why" id="service-why"></section>

    <section class="locations service-locations">
      <div class="container">
        <div class="locations__header">
          <h2 class="locations__title" id="service-locations-title"></h2>
          <div class="locations__divider"></div>
          <p class="locations__label">Locations</p>
          <p class="locations__intro" id="service-locations-intro"></p>
        </div>
        <div class="locations__grid" id="service-locations-grid"></div>
      </div>
    </section>

    <section class="faq service-faq">
      <div class="container">
        <h2 class="faq__title" id="service-faq-title"></h2>
        <div class="faq__grid" id="service-faq-grid"></div>
      </div>
    </section>

    <section class="final-cta" id="final-cta">
      <div class="final-cta__overlay"></div>
      <div class="container final-cta__content">
        <h2 class="final-cta__title" id="service-cta-title"></h2>
        <p class="final-cta__text" id="service-cta-text"></p>
        <div class="final-cta__buttons">
          <button class="btn-quote btn-final-quote" type="button">Get a Quote</button>
          <a href="tel:+16176866805" class="btn-phone btn-final-phone">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>(617) 686-6805</span>
          </a>
        </div>
      </div>
    </section>
  </main>
"""

MAIN_BODY = """
  <main>
    <section class="page-hero">
      <div class="container page-hero__inner">
        <h1 class="page-hero__title">{h1}</h1>
        <p class="page-hero__subtitle">{hero_subtitle}</p>
        <div class="page-hero__cta">
          <button class="btn-quote btn-page-quote" type="button">Get a Quote</button>
          <a href="tel:+16176866805" class="btn-phone btn-page-phone">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>(617) 686-6805</span>
          </a>
        </div>
      </div>
    </section>

    <section class="trust" id="page-trust"></section>

    <section class="page-content">
      <div class="container page-content__inner">
        {sections_html}
      </div>
    </section>

    <section class="final-cta" id="final-cta">
      <div class="final-cta__overlay"></div>
      <div class="container final-cta__content">
        <h2 class="final-cta__title">{cta_title}</h2>
        <p class="final-cta__text">{cta_text}</p>
        <div class="final-cta__buttons">
          <button class="btn-quote btn-final-quote" type="button">Get a Quote</button>
          <a href="tel:+16176866805" class="btn-phone btn-final-phone">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>(617) 686-6805</span>
          </a>
        </div>
      </div>
    </section>
  </main>
"""

PAGE_HERO = """
    <section class="service-hero" id="page-hero">
      <div class="service-hero__bg">
        <div class="service-hero__bg-image" id="page-hero-bg"></div>
        <div class="service-hero__bg-overlay"></div>
      </div>
      <div class="container service-hero__content">
        <div class="service-hero__inner">
          <h1 class="service-hero__title">{h1}</h1>
          <p class="service-hero__subtitle">{hero_subtitle}</p>
          <div class="service-hero__cta">
            <button class="btn-hero-quote btn-page-quote" type="button">Get a Quote</button>
            <a href="tel:+16176866805" class="btn-hero-phone btn-page-phone">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>(617) 686-6805</span>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

LOCATION_HERO = """
    <section class="service-hero" id="location-hero">
      <div class="service-hero__bg">
        <div class="service-hero__bg-image" id="location-hero-bg"></div>
        <div class="service-hero__bg-overlay"></div>
      </div>
      <div class="container service-hero__content">
        <div class="service-hero__inner">
          <h1 class="service-hero__title">{h1}</h1>
          <p class="service-hero__subtitle">{hero_subtitle}</p>
          <div class="service-hero__cta">
            <button class="btn-hero-quote btn-page-quote" type="button">Get a Quote</button>
            <a href="tel:+16176866805" class="btn-hero-phone btn-page-phone">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>(617) 686-6805</span>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

FINAL_CTA = """
    <section class="final-cta" id="final-cta">
      <div class="final-cta__overlay"></div>
      <div class="container final-cta__content">
        <h2 class="final-cta__title" id="page-cta-title">{cta_title}</h2>
        <p class="final-cta__text" id="page-cta-text">{cta_text}</p>
        <div class="final-cta__buttons">
          <button class="btn-quote btn-final-quote" type="button">Get a Quote</button>
          <a href="tel:+16176866805" class="btn-phone btn-final-phone">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>(617) 686-6805</span>
          </a>
        </div>
      </div>
    </section>
"""

ABOUT_BODY = """
  <main>
""" + PAGE_HERO + """
    <section class="trust" id="page-trust"></section>
    <section class="service-intro about-section" id="about-intro"></section>
    <section class="about-stats" id="about-stats"></section>
    <section class="why-trust about-beliefs" id="about-beliefs"></section>
    <section class="service-intro about-team-section" id="about-team"></section>
    <section class="service-intro about-local-section" id="about-local"></section>
""" + FINAL_CTA + """
  </main>
"""

CHECKLIST_BODY = """
  <main>
""" + PAGE_HERO + """
    <section class="trust" id="page-trust"></section>
    <section class="checklist-page" id="checklist-main"></section>
    <section class="checklist-footer" id="checklist-footer"></section>
""" + FINAL_CTA + """
  </main>
"""

CONTACT_BODY = """
  <main>
""" + PAGE_HERO + """
    <section class="trust" id="page-trust"></section>
    <section class="contact-cards" id="contact-cards"></section>
    <section class="contact-form-section" id="contact-form"></section>
    <section class="faq contact-faq" id="contact-faq"></section>
    <section class="contact-area" id="contact-area"></section>
""" + FINAL_CTA + """
  </main>
"""

CAREERS_BODY = """
  <main>
""" + PAGE_HERO + """
    <section class="careers-intro" id="careers-intro"></section>
    <section class="contact-form-section careers-form-section" id="careers-form"></section>
""" + FINAL_CTA + """
  </main>
"""

LEGAL_BODY = """
  <main>
""" + PAGE_HERO + """
    <section class="page-content" id="legal-content"></section>
""" + FINAL_CTA + """
  </main>
"""

LOCATION_BODY = """
  <main>
""" + LOCATION_HERO + """
    <section class="trust" id="page-trust"></section>
    <section class="service-intro" id="location-about"></section>
    <section class="services location-services">
      <div class="container">
        <div class="services__header">
          <h2 class="services__title" id="location-services-title">Cleaning Services Available</h2>
          <p class="services__intro" id="location-services-intro"></p>
        </div>
        <div class="services__grid" id="location-services-grid"></div>
      </div>
    </section>
    <section class="recurring" id="location-recurring">
      <div class="container">
        <div class="recurring__header">
          <h2 class="recurring__title" id="location-recurring-title"></h2>
          <p class="recurring__subtitle" id="location-recurring-subtitle"></p>
        </div>
        <div class="recurring__grid" id="location-recurring-grid"></div>
        <div class="recurring__footer">
          <p class="recurring__text" id="location-recurring-text"></p>
          <div class="recurring__cta">
            <button class="btn-quote btn-recurring-quote" type="button">Get A Quote</button>
            <a href="tel:+16176866805" class="btn-phone btn-recurring-phone">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              <span>(617) 686-6805</span>
            </a>
          </div>
        </div>
      </div>
    </section>
    <section class="why-trust service-why" id="location-why"></section>
    <section class="faq service-faq">
      <div class="container">
        <h2 class="faq__title" id="location-faq-title"></h2>
        <div class="faq__grid" id="location-faq-grid"></div>
      </div>
    </section>
    <section class="final-cta" id="final-cta">
      <div class="final-cta__overlay"></div>
      <div class="container final-cta__content">
        <h2 class="final-cta__title" id="location-cta-title">{cta_title}</h2>
        <p class="final-cta__text" id="location-cta-text">{cta_text}</p>
        <div class="final-cta__buttons">
          <button class="btn-quote btn-final-quote" type="button">Get a Quote</button>
          <a href="tel:+16176866805" class="btn-phone btn-final-phone">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>(617) 686-6805</span>
          </a>
        </div>
      </div>
    </section>
  </main>
"""

PAGE_BODIES = {
    "about": ABOUT_BODY,
    "checklist": CHECKLIST_BODY,
    "contact": CONTACT_BODY,
    "careers": CAREERS_BODY,
    "privacy": LEGAL_BODY,
    "terms": LEGAL_BODY,
    "location": LOCATION_BODY,
}

PAGES = {
    "about.html": {
        "page_type": "about",
        "title": "About Marble Head Maids — Locally Owned Cleaning Company in North Shore, MA | Marble Head Maids",
        "meta_description": "Marble Head Maids is a locally owned cleaning company in North Shore, MA. Background-checked teams, transparent pricing, no contracts.",
        "h1": "About Marble Head Maids",
        "hero_subtitle": "A North Shore cleaning company built on trust. Locally owned, locally operated, and accountable to the community we serve.",
        "cta_title": "Ready to Work With Us?",
        "cta_text": "If what you've read sounds like the kind of cleaning company you want in your home, let's get started. No contracts, no pressure — just a straightforward quote based on what you need.",
        "extra_scripts": ['  <script src="{js_base}js/pages-content.js"></script>\n  <script src="{js_base}js/pages.js"></script>'],
    },
    "checklist.html": {
        "page_type": "checklist",
        "title": "Cleaning Checklist North Shore, MA | What's Included in Our Cleaning | Marble Head Maids",
        "meta_description": "See exactly what's included in our North Shore cleaning services. Detailed room-by-room checklist for apartment and house cleaning.",
        "h1": "Our Cleaning Checklist",
        "hero_subtitle": "Know exactly what to expect. Every room, every detail, every time. No surprises—just a spotless home.",
        "cta_title": "Ready for a Spotless Home?",
        "cta_text": "Book your cleaning today and experience the difference a detailed, professional clean makes.",
        "extra_scripts": [
            '  <script src="{js_base}js/checklist-data.js"></script>\n  <script src="{js_base}js/pages-content.js"></script>\n  <script src="{js_base}js/pages.js"></script>'
        ],
    },
    "contact.html": {
        "page_type": "contact",
        "title": "Contact Marble Head Maids — Get a Cleaning Quote in North Shore, MA | Marble Head Maids",
        "meta_description": "Contact Marble Head Maids for a free cleaning quote in North Shore, MA. Call, email, or fill out our form — most quotes returned within a few hours.",
        "h1": "Get a Free Cleaning Quote",
        "hero_subtitle": "Ready to get your home, apartment, or office cleaned? Fill out the quick form below, give us a call, or shoot us a message. Most quotes come back within a few hours.",
        "cta_title": "Get a Cleaner Home This Week",
        "cta_text": "Stop putting it off. Whether it's a one-time deep clean or a recurring plan that keeps your home spotless month after month — Marble Head Maids is ready when you are.",
        "extra_scripts": ['  <script src="{js_base}js/pages-content.js"></script>\n  <script src="{js_base}js/pages.js"></script>'],
    },
    "careers.html": {
        "page_type": "careers",
        "title": "Careers at Marble Head Maids — Join Our Cleaning Team in North Shore, MA | Marble Head Maids",
        "meta_description": "Join the Marble Head Maids team! We're hiring reliable, detail-oriented cleaners in the North Shore and North Suburbs, MA.",
        "h1": "Join the Marble Head Maids Team",
        "hero_subtitle": "We're always looking for reliable, detail-oriented people who take pride in their work. Flexible schedules, competitive pay, and a team that has your back.",
        "cta_title": "Ready to Join Our Team?",
        "cta_text": "Contact us today to learn more about open positions with Marble Head Maids in the North Shore and North Suburbs.",
        "extra_scripts": ['  <script src="{js_base}js/pages-content.js"></script>\n  <script src="{js_base}js/pages.js"></script>'],
    },
    "privacy.html": {
        "page_type": "privacy",
        "title": "Privacy Policy — Marble Head Maids | Marble Head Maids",
        "meta_description": "Privacy Policy for Marble Head Maids, covering mobile contact information handling, cookies, and tracking technologies.",
        "h1": "Privacy Policy",
        "hero_subtitle": "How we handle your information, mobile contact data, and the cookies we use on our site.",
        "cta_title": "Questions About Our Privacy Policy?",
        "cta_text": "Contact us at support@marbleheadmaids.com if you have any questions about how we handle your information.",
        "extra_scripts": ['  <script src="{js_base}js/pages-content.js"></script>\n  <script src="{js_base}js/pages.js"></script>'],
    },
    "terms.html": {
        "page_type": "terms",
        "title": "Terms and Conditions — Marble Head Maids | Marble Head Maids",
        "meta_description": "Terms and Conditions for Marble Head Maids, including SMS communications, messaging rates, and opt-out instructions.",
        "h1": "Terms and Conditions",
        "hero_subtitle": "Please review the terms that govern your use of our services and SMS communications.",
        "cta_title": "Get a Cleaner Home This Week",
        "cta_text": "Stop putting it off. Whether it's a one-time deep clean or a recurring plan that keeps your home spotless month after month — Marble Head Maids is ready when you are.",
        "extra_scripts": ['  <script src="{js_base}js/pages-content.js"></script>\n  <script src="{js_base}js/pages.js"></script>'],
    },
}

SERVICES = [
    ("apartment-cleaning.html", "Apartment Cleaning in North Shore, MA — Sized for Your Space, Priced for Renters", "Apartment cleaning across North Shore — from studios to multi-bedroom units. Priced for your unit size, not a 4-bedroom house.", "From studios near campus to 3-bedrooms along the Route 128 corridor — apartment cleaning that's priced for your unit size, not a 4-bedroom house."),
    ("house-cleaning.html", "House Cleaning North Shore, MA — Recurring Home Cleaning You Can Count On", "Recurring weekly, biweekly, or monthly cleaning that keeps your North Shore home consistently fresh.", "Recurring weekly, biweekly, or monthly cleaning that keeps your North Shore home consistently fresh. Our teams follow a detailed checklist so nothing gets missed — visit after visit."),
    ("deep-cleaning.html", "Deep Cleaning North Shore, MA — Top-to-Bottom Home Reset", "When surface-level isn't cutting it. We go behind appliances, inside cabinets, into grout lines, and across every baseboard.", "When surface-level isn't cutting it. We go behind appliances, inside cabinets, into grout lines, and across every baseboard. A true top-to-bottom reset."),
    ("move-in-cleaning.html", "Move-In Cleaning North Shore, MA — Start Fresh in Your New Home", "Start fresh. We'll clean every surface, drawer, and fixture in your new place before you unpack a single box.", "Start fresh. We'll clean every surface, drawer, and fixture in your new place before you unpack a single box."),
    ("move-out-cleaning.html", "Move-Out Cleaning North Shore, MA — Get Your Deposit Back", "Leave your place landlord-ready. Designed around what North Shore property managers actually inspect.", "Leave your place landlord-ready. Designed around what North Shore property managers actually inspect — so you get your deposit back."),
    ("post-construction-cleaning.html", "Post-Construction Cleaning North Shore, MA — After the Renovation", "Renovation dust doesn't clean itself. We handle drywall dust, paint residue, adhesive removal, and construction debris.", "Renovation dust doesn't clean itself. We handle drywall dust, paint residue, adhesive removal, and construction debris so you can enjoy the finished project."),
    ("airbnb-rental-cleaning.html", "Airbnb & Rental Cleaning North Shore, MA — Guest-Ready Every Time", "Same-day turnovers, linen changes, restocking, and damage reports. Reliable cleaning that protects your reviews.", "Same-day turnovers, linen changes, restocking, and damage reports. Reliable cleaning that protects your reviews — every guest, every time."),
    ("commercial-cleaning.html", "Commercial Cleaning North Shore, MA — Offices & Business Spaces", "Offices, retail, medical, and business spaces cleaned on your schedule. Evening and weekend availability.", "Offices, retail, medical, and business spaces cleaned on your schedule. Evening and weekend availability, dedicated teams, no long-term contracts."),
]

LOCATIONS = [
    ("sun-prairie.html", "Sun Prairie", "House Cleaning in Sun Prairie, MA", "Marble Head Maids is a locally owned cleaning company based on the North Shore, and Sun Prairie is one of our most active service areas."),
    ("middleton.html", "Middleton", "House Cleaning in Middleton, MA", "Professional cleaning services for Middleton homes and apartments. Recurring, deep cleaning, move-in/out, and more."),
    ("verona.html", "Verona", "House Cleaning in Verona, MA", "Trusted cleaning teams serving Verona and the North Shore and North Suburbs with transparent pricing and no contracts."),
    ("fitchburg.html", "Fitchburg", "House Cleaning in Fitchburg, MA", "From Fitchburg neighborhoods to new developments — Marble Head Maids keeps your home spotless on your schedule."),
    ("waunakee.html", "Waunakee", "House Cleaning in Waunakee, MA", "Recurring and one-time cleaning for Waunakee homes. Background-checked teams, satisfaction guaranteed."),
    ("stoughton.html", "Stoughton", "House Cleaning in Stoughton, MA", "House cleaning services in Stoughton, MA. Locally owned, fully insured, and ready when you are."),
    ("deforest.html", "DeForest", "House Cleaning in DeForest, MA", "Professional residential cleaning in DeForest. Weekly, biweekly, monthly, and deep cleaning available."),
    ("cottage-grove.html", "Cottage Grove", "House Cleaning in Cottage Grove, MA", "Marble Head Maids serves Cottage Grove with the same quality and checklist-driven cleaning as North Shore proper."),
    ("mcfarland.html", "McFarland", "House Cleaning in McFarland, MA", "Reliable house cleaning in McFarland. Flat-rate quotes, no contracts, background-checked teams."),
    ("monona.html", "Monona", "House Cleaning in Monona, MA", "Cleaning services for Monona homes and rentals. Book online or call for a free quote today."),
]


def build_internal_page(page_data, base="../", css_base="../", js_base="../"):
    head = HEADER.format(
        title=page_data["title"],
        meta_description=page_data["meta_description"],
        css_base=css_base,
        base=base,
    )
    body_tpl = PAGE_BODIES[page_data["page_type"]]
    body = body_tpl.format(
        h1=page_data["h1"],
        hero_subtitle=page_data["hero_subtitle"],
        cta_title=page_data["cta_title"],
        cta_text=page_data["cta_text"],
    )
    extra = "".join(s.format(js_base=js_base) for s in page_data.get("extra_scripts", []))
    scripts = f"""
  <footer class="site-footer" id="site-footer"></footer>
  <script src="{js_base}js/data.js"></script>
  <script src="{js_base}js/layout.js"></script>
{extra}
  <script src="{js_base}js/page.js"></script>
</body>
</html>
"""
    return head + body + scripts


def build_location_page(page_data, base="../", css_base="../", js_base="../"):
    head = HEADER.format(
        title=page_data["title"],
        meta_description=page_data["meta_description"],
        css_base=css_base,
        base=base,
    )
    body = LOCATION_BODY.format(
        h1=page_data["h1"],
        hero_subtitle=page_data["hero_subtitle"],
        cta_title=page_data["cta_title"],
        cta_text=page_data["cta_text"],
    )
    scripts = f"""
  <footer class="site-footer" id="site-footer"></footer>
  <script src="{js_base}js/data.js"></script>
  <script src="{js_base}js/layout.js"></script>
  <script src="{js_base}js/location-pages.js"></script>
  <script src="{js_base}js/location.js"></script>
  <script src="{js_base}js/page.js"></script>
</body>
</html>
"""
    return head + body + scripts


def build_service_page(page_data, base="../", css_base="../", js_base="../"):
    head = HEADER.format(
        title=page_data["pageTitle"],
        meta_description=page_data["metaDescription"],
        css_base=css_base,
        base=base,
    )
    body = SERVICE_BODY.format(
        h1=page_data["h1"],
        hero_subtitle=page_data["heroSubtitle"],
    )
    scripts = SERVICE_FOOTER_SCRIPTS.format(js_base=js_base)
    return head + body + scripts


def main():
    for filename, data in PAGES.items():
        path = ROOT / filename
        path.write_text(build_internal_page(data, base="", css_base="", js_base=""), encoding="utf-8")
        print(f"Created {path}")

    service_pages_path = ROOT / "js" / "service-pages.js"
    if not service_pages_path.exists():
        raise SystemExit(
            "Missing js/service-pages.js — run: python tools/build_service_pages.py"
        )

    services_dir = ROOT / "services"
    services_dir.mkdir(exist_ok=True)

    import re
    import json as json_lib

    service_js = service_pages_path.read_text(encoding="utf-8")
    match = re.search(r"window\.SERVICE_PAGES\s*=\s*(\{[\s\S]*\});?\s*$", service_js)
    if not match:
        raise SystemExit("Could not parse js/service-pages.js")
    service_pages = json_lib.loads(match.group(1))

    for slug, page_data in service_pages.items():
        path = services_dir / f"{slug}.html"
        path.write_text(build_service_page(page_data), encoding="utf-8")
        print(f"Created {path}")

    locations_dir = ROOT / "locations"
    locations_dir.mkdir(exist_ok=True)

    location_pages_path = ROOT / "js" / "location-pages.js"
    if not location_pages_path.exists():
        raise SystemExit("Missing js/location-pages.js — run: python tools/build_location_pages.py")

    loc_js = location_pages_path.read_text(encoding="utf-8")
    loc_match = re.search(r"window\.LOCATION_PAGES\s*=\s*(\{[\s\S]*\});?\s*$", loc_js)
    if not loc_match:
        raise SystemExit("Could not parse js/location-pages.js")
    location_pages = json_lib.loads(loc_match.group(1))

    for slug, page_data in location_pages.items():
        path = locations_dir / f"{slug}.html"
        data = {
            "title": page_data["pageTitle"],
            "meta_description": page_data["metaDescription"],
            "h1": page_data["h1"],
            "hero_subtitle": page_data["heroSubtitle"],
            "cta_title": page_data["cta"]["title"],
            "cta_text": page_data["cta"]["description"],
        }
        path.write_text(build_location_page(data), encoding="utf-8")
        print(f"Created {path}")

    valid_slugs = set(location_pages.keys())
    for stale in locations_dir.glob("*.html"):
        if stale.stem not in valid_slugs:
            stale.unlink()
            print(f"Removed stale {stale}")


if __name__ == "__main__":
    main()
