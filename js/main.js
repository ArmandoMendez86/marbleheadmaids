(function () {
  const { services, locations } = window.SITE_DATA;

  const overlay = document.querySelector('.mobile-overlay');
  const panel = document.querySelector('.mobile-panel');
  const menuToggle = document.querySelector('.menu-toggle');
  const menuClose = document.querySelector('.mobile-panel__close');

  function renderLinks(items) {
    return items.map(({ label, href }) => `<a href="${href}">${label}</a>`).join('');
  }

  function initNavMenus() {
    document.querySelectorAll('[data-dropdown]').forEach((dropdown) => {
      const key = dropdown.dataset.dropdown;
      const menu = dropdown.querySelector('.nav__dropdown-menu');
      const items = key === 'services' ? services : locations;
      menu.innerHTML = renderLinks(items);
    });

    document.querySelectorAll('[data-mobile-submenu]').forEach((submenu) => {
      const key = submenu.dataset.mobileSubmenu;
      const items = key === 'services' ? services : locations;
      submenu.innerHTML = renderLinks(items);
    });
  }

  function openMobileMenu() {
    overlay.hidden = false;
    overlay.classList.add('is-visible');
    panel.classList.add('is-open');
    panel.setAttribute('aria-hidden', 'false');
    menuToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileMenu() {
    overlay.classList.remove('is-visible');
    panel.classList.remove('is-open');
    panel.setAttribute('aria-hidden', 'true');
    menuToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    window.setTimeout(() => {
      if (!panel.classList.contains('is-open')) {
        overlay.hidden = true;
      }
    }, 300);
  }

  function initMobileMenu() {
    menuToggle?.addEventListener('click', openMobileMenu);
    menuClose?.addEventListener('click', closeMobileMenu);
    overlay?.addEventListener('click', closeMobileMenu);

    panel?.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeMobileMenu);
    });

    document.querySelectorAll('[data-mobile-toggle]').forEach((toggle) => {
      toggle.addEventListener('click', () => {
        const key = toggle.dataset.mobileToggle;
        const submenu = document.querySelector(`[data-mobile-submenu="${key}"]`);
        const isOpen = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', String(!isOpen));
        submenu.hidden = isOpen;
      });
    });
  }

  function initDesktopDropdowns() {
    document.querySelectorAll('.nav__dropdown').forEach((dropdown) => {
      const button = dropdown.querySelector('.nav__dropdown-btn');
      const menu = dropdown.querySelector('.nav__dropdown-menu');

      button.addEventListener('click', (event) => {
        event.stopPropagation();
        const isOpen = dropdown.classList.contains('is-open');

        document.querySelectorAll('.nav__dropdown.is-open').forEach((openDropdown) => {
          openDropdown.classList.remove('is-open');
          openDropdown.querySelector('.nav__dropdown-btn').setAttribute('aria-expanded', 'false');
          openDropdown.querySelector('.nav__dropdown-menu').hidden = true;
        });

        if (!isOpen) {
          dropdown.classList.add('is-open');
          button.setAttribute('aria-expanded', 'true');
          menu.hidden = false;
        }
      });
    });

    document.addEventListener('click', () => {
      document.querySelectorAll('.nav__dropdown.is-open').forEach((dropdown) => {
        dropdown.classList.remove('is-open');
        dropdown.querySelector('.nav__dropdown-btn').setAttribute('aria-expanded', 'false');
        dropdown.querySelector('.nav__dropdown-menu').hidden = true;
      });
    });
  }

  function renderServiceCards() {
    const grid = document.getElementById('services-grid');
    if (!grid || !window.SITE_DATA.serviceCards) return;

    grid.innerHTML = window.SITE_DATA.serviceCards.map((card) => `
      <a class="service-card" href="${card.href}">
        <div class="service-card__icon">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="${card.icon}"/>
          </svg>
        </div>
        <h3 class="service-card__title">${card.title}</h3>
        <p class="service-card__desc">${card.description}</p>
        <span class="service-card__link">
          ${card.title}
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </span>
      </a>
    `).join('');
  }

  function renderRecurringPlans() {
    const grid = document.getElementById('recurring-grid');
    if (!grid || !window.SITE_DATA.recurringPlans) return;

    grid.innerHTML = window.SITE_DATA.recurringPlans.map((plan) => {
      const dotsHtml = plan.dots > 0
        ? `<div class="recurring-card__dots${plan.popular ? ' recurring-card__dots--offset' : ''}">
            ${Array.from({ length: plan.dots }, () => '<span class="recurring-card__dot"></span>').join('')}
          </div>`
        : '';

      const badgeHtml = plan.popular
        ? '<span class="recurring-card__badge">MOST POPULAR</span>'
        : '';

      const discountHtml = plan.discount
        ? `<span class="recurring-card__discount">${plan.discount}</span>`
        : '';

      return `
        <div class="recurring-card${plan.popular ? ' recurring-card--popular' : ''}">
          ${badgeHtml}
          ${dotsHtml}
          <h3 class="recurring-card__title">${plan.title}</h3>
          <p class="recurring-card__desc">${plan.description}</p>
          ${discountHtml}
        </div>
      `;
    }).join('');
  }

  function renderTrustSection() {
    const grid = document.getElementById('why-trust-grid');
    const promiseEl = document.getElementById('why-trust-promise');
    if (!grid || !window.SITE_DATA.trustItems) return;

    const checkIcon = 'M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z';
    const shieldIcon = 'M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z';

    grid.innerHTML = window.SITE_DATA.trustItems.map((item) => `
      <div class="trust-card">
        <div class="trust-card__icon">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${checkIcon}"/>
          </svg>
        </div>
        <h3 class="trust-card__title">${item.title}</h3>
        <p class="trust-card__desc">${item.description}</p>
      </div>
    `).join('');

    if (promiseEl && window.SITE_DATA.cleaningPromise) {
      const { title, description } = window.SITE_DATA.cleaningPromise;
      promiseEl.innerHTML = `
        <div class="trust-promise__icon">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${shieldIcon}"/>
          </svg>
        </div>
        <h3 class="trust-promise__title">${title}</h3>
        <p class="trust-promise__desc">${description}</p>
      `;
    }
  }

  function renderBookingSteps() {
    const grid = document.getElementById('booking-steps-grid');
    if (!grid || !window.SITE_DATA.bookingSteps) return;

    grid.innerHTML = window.SITE_DATA.bookingSteps.map((step) => `
      <div class="step-card">
        <div class="step-card__icon-wrap">
          <div class="step-card__circle">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="${step.icon}"/>
            </svg>
          </div>
          <span class="step-card__badge">${step.step}</span>
        </div>
        <h3 class="step-card__title">${step.title}</h3>
        <p class="step-card__desc">${step.description}</p>
      </div>
    `).join('');
  }

  const PIN_ICON = 'M15 10.5a3 3 0 11-6 0 3 3 0 016 0z M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z';

  function renderTestimonialCard(testimonial, compact) {
    const initial = testimonial.name.charAt(0);
    const paddingClass = compact ? '' : '';

    return `
      <div class="testimonial-card${paddingClass}">
        <div class="testimonial-card__stars" aria-hidden="true">
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </div>
        <p class="testimonial-card__quote">"${testimonial.quote}"</p>
        <div class="testimonial-card__author">
          <div class="testimonial-card__avatar">
            <span class="testimonial-card__initial">${initial}</span>
          </div>
          <div>
            <p class="testimonial-card__name">${testimonial.name}</p>
            <p class="testimonial-card__location">${testimonial.location}</p>
          </div>
        </div>
      </div>
    `;
  }

  function renderLocations() {
    const grid = document.getElementById('locations-grid');
    if (!grid) return;

    grid.innerHTML = locations.map(({ label, href }) => `
      <a class="location-card" href="${href}">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" d="${PIN_ICON}"/>
        </svg>
        <span class="location-card__label">${label}</span>
      </a>
    `).join('');
  }

  function renderTestimonials() {
    const grid = document.getElementById('testimonials-grid');
    const track = document.getElementById('testimonials-track');
    const dots = document.getElementById('testimonials-dots');
    const items = window.SITE_DATA.testimonials;

    if (!items?.length) return;

    if (grid) {
      grid.innerHTML = items.map((item) => renderTestimonialCard(item)).join('');
    }

    if (track) {
      track.innerHTML = items.map((item) => `
        <div class="testimonials__slide">
          ${renderTestimonialCard(item, true)}
        </div>
      `).join('');
    }

    if (dots) {
      dots.innerHTML = items.map((_, index) => `
        <button
          class="testimonials__dot${index === 0 ? ' is-active' : ''}"
          type="button"
          aria-label="Go to testimonial ${index + 1}"
          data-index="${index}"
        ></button>
      `).join('');
    }
  }

  function initTestimonialCarousel() {
    const track = document.getElementById('testimonials-track');
    const dotsContainer = document.getElementById('testimonials-dots');
    const prevBtn = document.querySelector('.testimonials__nav--prev');
    const nextBtn = document.querySelector('.testimonials__nav--next');
    const items = window.SITE_DATA.testimonials;

    if (!track || !items?.length) return;

    let currentIndex = 0;

    function goTo(index) {
      currentIndex = (index + items.length) % items.length;
      track.style.transform = `translateX(-${currentIndex * 100}%)`;

      dotsContainer?.querySelectorAll('.testimonials__dot').forEach((dot, i) => {
        dot.classList.toggle('is-active', i === currentIndex);
      });
    }

    prevBtn?.addEventListener('click', () => goTo(currentIndex - 1));
    nextBtn?.addEventListener('click', () => goTo(currentIndex + 1));

    dotsContainer?.querySelectorAll('.testimonials__dot').forEach((dot) => {
      dot.addEventListener('click', () => {
        goTo(Number(dot.dataset.index));
      });
    });
  }

  function renderFaq() {
    const grid = document.getElementById('faq-grid');
    if (!grid || !window.SITE_DATA.faqItems) return;

    grid.innerHTML = window.SITE_DATA.faqItems.map((item, index) => `
      <div class="faq-item" data-faq-index="${index}">
        <button
          class="faq-item__trigger"
          type="button"
          aria-expanded="false"
          aria-controls="faq-panel-${index}"
          id="faq-trigger-${index}"
        >
          <span class="faq-item__question">${item.question}</span>
          <span class="faq-item__icon" aria-hidden="true">+</span>
        </button>
        <div class="faq-item__panel" id="faq-panel-${index}" role="region" aria-labelledby="faq-trigger-${index}">
          <div class="faq-item__panel-inner">
            <div class="faq-item__answer-wrap">
              <p class="faq-item__answer">${item.answer}</p>
            </div>
          </div>
        </div>
      </div>
    `).join('');
  }

  function initFaqAccordion() {
    document.querySelectorAll('.faq-item').forEach((item) => {
      const trigger = item.querySelector('.faq-item__trigger');
      const icon = item.querySelector('.faq-item__icon');

      trigger?.addEventListener('click', () => {
        const isOpen = item.classList.toggle('is-open');
        trigger.setAttribute('aria-expanded', String(isOpen));
        if (icon) icon.textContent = isOpen ? '−' : '+';
      });
    });
  }

  initNavMenus();
  initMobileMenu();
  initDesktopDropdowns();
  renderServiceCards();
  renderRecurringPlans();
  renderTrustSection();
  renderBookingSteps();
  renderLocations();
  renderTestimonials();
  initTestimonialCarousel();
  renderFaq();
  initFaqAccordion();
  window.SITE_LAYOUT?.renderFooter();
})();
