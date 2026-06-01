(function () {
  const RECURRING_DEFAULT =
    "Life on the North Shore moves fast. Between work, weekend plans, coastal living, and busy schedules, and everything in between, who has time to clean? Our flexible scheduling lets you choose the frequency that fits your lifestyle. Need to skip a week or reschedule? No problem — just give us 24 hours notice.";

  const CHECK_ICON =
    "M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z";

  function getSlug() {
    const path = window.location.pathname.replace(/\\/g, "/");
    const match = path.match(/\/locations\/([^/.]+)/);
    if (match) return match[1];
    const file = path.split("/").pop() || "";
    return file.replace(".html", "");
  }

  function resolve(href) {
    return window.SITE_LAYOUT?.resolveHref(href) || href;
  }

  function heroBasePath() {
    return window.SITE_LAYOUT?.getBasePath() || "../";
  }

  function renderHero(slug) {
    const bg = document.getElementById("location-hero-bg");
    if (!bg) return;
    bg.style.backgroundImage = `url('${heroBasePath()}images/heroes/${slug}.jpg')`;
  }

  function renderAbout(about) {
    const el = document.getElementById("location-about");
    if (!el || !about) return;
    el.innerHTML = `
      <div class="container">
        <h2 class="service-section__title">${about.heading}</h2>
        <div class="service-section__body">
          ${about.paragraphs.map((p) => `<p class="service-section__text">${p}</p>`).join("")}
        </div>
      </div>
    `;
  }

  function renderServices(intro) {
    const grid = document.getElementById("location-services-grid");
    const introEl = document.getElementById("location-services-intro");
    if (introEl && intro) introEl.textContent = intro;
    if (!grid || !window.SITE_DATA?.serviceCards) return;
    grid.innerHTML = window.SITE_DATA.serviceCards
      .map(
        (card) => `
          <a class="service-card" href="${resolve(card.href)}">
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
        `
      )
      .join("");
  }

  function renderRecurring(page) {
    const titleEl = document.getElementById("location-recurring-title");
    const subtitleEl = document.getElementById("location-recurring-subtitle");
    const grid = document.getElementById("location-recurring-grid");
    const textEl = document.getElementById("location-recurring-text");
    if (!grid || !window.SITE_DATA?.recurringPlans) return;

    if (titleEl) titleEl.textContent = page.recurringTitle || "";
    if (subtitleEl) subtitleEl.textContent = page.recurringSubtitle || "";
    if (textEl) textEl.textContent = page.recurringText || RECURRING_DEFAULT;

    grid.innerHTML = window.SITE_DATA.recurringPlans
      .map((plan) => {
        const dotsHtml =
          plan.dots > 0
            ? `<div class="recurring-card__dots${plan.popular ? " recurring-card__dots--offset" : ""}">
                ${Array.from({ length: plan.dots }, () => '<span class="recurring-card__dot"></span>').join("")}
              </div>`
            : "";
        const badgeHtml = plan.popular ? '<span class="recurring-card__badge">MOST POPULAR</span>' : "";
        const discountHtml = plan.discount ? `<span class="recurring-card__discount">${plan.discount}</span>` : "";
        return `
          <div class="recurring-card${plan.popular ? " recurring-card--popular" : ""}">
            ${badgeHtml}
            ${dotsHtml}
            <h3 class="recurring-card__title">${plan.title}</h3>
            <p class="recurring-card__desc">${plan.description}</p>
            ${discountHtml}
          </div>
        `;
      })
      .join("");
  }

  function renderWhyChoose(whyChoose) {
    const el = document.getElementById("location-why");
    if (!el || !whyChoose?.items?.length) return;
    el.innerHTML = `
      <div class="container">
        <h2 class="service-section__title">${whyChoose.heading}</h2>
        <div class="why-trust__grid">
          ${whyChoose.items
            .map(
              (item) => `
            <div class="trust-card">
              <div class="trust-card__icon">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${CHECK_ICON}"/>
                </svg>
              </div>
              <h3 class="trust-card__title">${item.title}</h3>
              <p class="trust-card__desc">${item.description}</p>
            </div>
          `
            )
            .join("")}
        </div>
      </div>
    `;
  }

  function renderFaq(faq) {
    const titleEl = document.getElementById("location-faq-title");
    const grid = document.getElementById("location-faq-grid");
    if (!grid || !faq?.items?.length) return;
    if (titleEl) titleEl.textContent = faq.heading;

    grid.innerHTML = faq.items
      .map(
        (item, index) => `
      <div class="faq-item" data-faq-index="${index}">
        <button class="faq-item__trigger" type="button" aria-expanded="false" aria-controls="location-faq-panel-${index}" id="location-faq-trigger-${index}">
          <span class="faq-item__question">${item.question}</span>
          <span class="faq-item__icon" aria-hidden="true">+</span>
        </button>
        <div class="faq-item__panel" id="location-faq-panel-${index}" role="region" aria-labelledby="location-faq-trigger-${index}">
          <div class="faq-item__panel-inner">
            <div class="faq-item__answer-wrap">
              <p class="faq-item__answer">${item.answer}</p>
            </div>
          </div>
        </div>
      </div>
    `
      )
      .join("");

    grid.querySelectorAll(".faq-item").forEach((item) => {
      const trigger = item.querySelector(".faq-item__trigger");
      const icon = item.querySelector(".faq-item__icon");
      trigger?.addEventListener("click", () => {
        const isOpen = item.classList.toggle("is-open");
        trigger.setAttribute("aria-expanded", String(isOpen));
        if (icon) icon.textContent = isOpen ? "−" : "+";
      });
    });
  }

  function renderCta(cta) {
    const titleEl = document.getElementById("location-cta-title");
    const textEl = document.getElementById("location-cta-text");
    if (titleEl && cta?.title) titleEl.textContent = cta.title;
    if (textEl && cta?.description) textEl.textContent = cta.description;
  }

  function initLocationPage() {
    const slug = getSlug();
    const page = window.LOCATION_PAGES?.[slug];
    if (!page) return;

    renderHero(slug);
    window.SITE_LAYOUT?.renderTrustBar?.();
    renderAbout(page.about);
    const servicesTitle = document.getElementById("location-services-title");
    if (servicesTitle && page.city) {
      servicesTitle.textContent = `Cleaning Services Available in ${page.city}`;
    }
    renderServices(page.servicesIntro);
    renderRecurring(page);
    renderWhyChoose(page.whyChoose);
    renderFaq(page.faq);
    renderCta(page.cta);
  }

  initLocationPage();
})();
