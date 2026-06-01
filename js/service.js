(function () {
  const RECURRING_TEXT =
    "Life on the North Shore moves fast. Between work, weekend plans, coastal living, and busy schedules, and everything in between, who has time to clean? Our flexible scheduling lets you choose the frequency that fits your lifestyle. Need to skip a week or reschedule? No problem — just give us 24 hours notice.";

  const CHECK_ICON =
    "M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z";

  const CATEGORY_ICON =
    "M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456z";

  const LIST_CHECK =
    "M5 13l4 4L19 7";

  function getSlug() {
    const path = window.location.pathname.replace(/\\/g, "/");
    const match = path.match(/\/services\/([^/.]+)/);
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

  function normalizeIntro(intro) {
    if (!intro) return null;
    return {
      heading: intro.heading,
      paragraphs: intro.paragraphs?.length ? intro.paragraphs : [],
      cards: intro.cards?.length ? intro.cards : null
    };
  }

  function normalizeWhenToBook(whenToBook) {
    if (!whenToBook) return null;
    const options = whenToBook.options || whenToBook.items || [];
    return { heading: whenToBook.heading, options };
  }

  function normalizeWhyChoose(whyChoose) {
    if (!whyChoose) return null;
    return {
      heading: whyChoose.heading,
      items: whyChoose.items || whyChoose.options || []
    };
  }

  function normalizePricing(pricing) {
    if (!pricing) return null;
    return {
      heading: pricing.heading,
      paragraphs: pricing.paragraphs?.length ? pricing.paragraphs : [pricing.intro].filter(Boolean),
      table: pricing.table || null,
      ctaLabel: pricing.ctaLabel || "Get Your Exact Quote"
    };
  }

  function renderHero(slug) {
    const bg = document.getElementById("service-hero-bg");
    if (!bg) return;
    bg.style.backgroundImage = `url('${heroBasePath()}images/heroes/${slug}.jpg')`;
  }

  function renderIntro(intro) {
    const el = document.getElementById("service-intro");
    const data = normalizeIntro(intro);
    if (!el || !data?.heading) return;
    const cardsHtml = data.cards
      ? `<div class="service-intro__cards">
          ${data.cards
            .map(
              (card) => `
            <div class="service-intro__card">
              <h3 class="service-intro__card-title">${card.title}</h3>
              <p class="service-intro__card-desc">${card.description}</p>
            </div>
          `
            )
            .join("")}
        </div>`
      : "";
    el.innerHTML = `
      <div class="container">
        <h2 class="service-section__title">${data.heading}</h2>
        <div class="service-section__body">
          ${data.paragraphs.map((p) => `<p class="service-section__text">${p}</p>`).join("")}
        </div>
        ${cardsHtml}
      </div>
    `;
  }

  function renderChecklist(checklist) {
    const el = document.getElementById("service-checklist");
    if (!el || !checklist) return;
    el.innerHTML = `
      <div class="container">
        <div class="service-section__header">
          <h2 class="service-section__title">${checklist.heading}</h2>
          <p class="service-section__text service-section__text--center">${checklist.intro}</p>
        </div>
        <div class="service-checklist__grid">
          ${checklist.categories
            .map(
              (cat) => `
            <div class="service-checklist__card">
              <h3 class="service-checklist__title">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="${CATEGORY_ICON}"/>
                </svg>
                ${cat.title}
              </h3>
              <ul class="service-checklist__list">
                ${cat.items
                  .map(
                    (item) => `
                  <li>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${LIST_CHECK}"/>
                    </svg>
                    ${item}
                  </li>
                `
                  )
                  .join("")}
              </ul>
            </div>
          `
            )
            .join("")}
        </div>
      </div>
    `;
  }

  function renderHowItWorks(howItWorks) {
    const el = document.getElementById("service-how");
    if (!el) return;
    if (!howItWorks?.steps?.length) {
      el.hidden = true;
      return;
    }
    el.hidden = false;
    el.innerHTML = `
      <div class="container">
        <div class="service-section__header">
          <h2 class="service-section__title">${howItWorks.heading}</h2>
          ${howItWorks.subtitle ? `<p class="service-section__text service-section__text--center">${howItWorks.subtitle}</p>` : ""}
        </div>
        <div class="service-when__stack">
          ${howItWorks.steps
            .map(
              (step, index) => `
            <div class="service-when__card">
              <h3 class="service-when__title">
                <span class="service-when__number">${step.number || index + 1}</span>
                ${step.title}
              </h3>
              <p class="service-when__desc">${step.description}</p>
            </div>
          `
            )
            .join("")}
        </div>
      </div>
    `;
  }

  function renderWhenToBook(whenToBook) {
    const el = document.getElementById("service-when");
    const data = normalizeWhenToBook(whenToBook);
    if (!el || !data?.options?.length) return;
    el.innerHTML = `
      <div class="container">
        <h2 class="service-section__title">${data.heading}</h2>
        <div class="service-when__stack">
          ${data.options
            .map(
              (opt, index) => `
            <div class="service-when__card">
              <h3 class="service-when__title">
                <span class="service-when__number">${opt.number || index + 1}</span>
                ${opt.title}
              </h3>
              <p class="service-when__desc">${opt.description}</p>
            </div>
          `
            )
            .join("")}
        </div>
      </div>
    `;
  }

  function renderOtherServices(currentSlug) {
    const grid = document.getElementById("service-other-grid");
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

  function renderRecurring(recurringTitle, recurringSubtitle) {
    const section = document.getElementById("service-recurring");
    const titleEl = document.getElementById("service-recurring-title");
    const subtitleEl = document.getElementById("service-recurring-subtitle");
    const grid = document.getElementById("service-recurring-grid");
    if (!recurringTitle || !grid || !window.SITE_DATA?.recurringPlans) {
      if (section) section.hidden = true;
      return;
    }
    if (section) section.hidden = false;

    if (titleEl && recurringTitle) titleEl.textContent = recurringTitle;
    if (subtitleEl) subtitleEl.textContent = recurringSubtitle || "Set it and forget it — we'll keep your home spotless on your schedule";

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

    const textEl = document.getElementById("service-recurring-text");
    if (textEl) textEl.textContent = RECURRING_TEXT;
  }

  function renderPricingTable(table) {
    if (!table?.headers?.length || !table?.rows?.length) return "";
    const deepCol = table.headers.length - 1;
    return `
      <div class="service-pricing__table-wrap">
        <table class="service-pricing__table">
          <thead>
            <tr>
              ${table.headers.map((h) => `<th>${h}</th>`).join("")}
            </tr>
          </thead>
          <tbody>
            ${table.rows
              .map(
                (row, i) => `
              <tr class="${i % 2 === 1 ? "service-pricing__row--alt" : ""}">
                ${row
                  .map((cell, j) => {
                    const cls =
                      j === 0
                        ? "service-pricing__cell--size"
                        : j === deepCol
                          ? "service-pricing__cell--deep"
                          : "";
                    return `<td class="${cls}">${cell}</td>`;
                  })
                  .join("")}
              </tr>
            `
              )
              .join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  function isPricingTableRow(paragraph) {
    return (
      /^(Studio|Small|Medium|Large|Extra Large|\d+\s*Bedroom|Studio\/|2BR|\d+\s*BR|Bathroom|Kitchen|Major|Full Gut)/i.test(paragraph) ||
      /(Recurring|Standard Clean|Deep Clean|Price Range)\s+\$/i.test(paragraph) ||
      (/:\s/.test(paragraph) && /\$\d/.test(paragraph))
    );
  }

  function getPricingFooter(paragraphs) {
    return (
      paragraphs.find((p) =>
        /First-time|Prices vary|Recurring clients receive|may cost more|Homes in extreme condition|custom quote|New construction cleaning|Final pricing depends|Condition matters|Send us photos|These are estimates/i.test(
          p
        )
      ) || ""
    );
  }

  function renderPricing(pricing) {
    const el = document.getElementById("service-pricing");
    const data = normalizePricing(pricing);
    if (!el || !data?.heading) {
      if (el) el.hidden = true;
      return;
    }
    el.hidden = false;

    const footerParagraph = data.table ? getPricingFooter(data.paragraphs) : "";
    const introParagraphs = data.table
      ? data.paragraphs.filter((p) => p !== footerParagraph && !isPricingTableRow(p))
      : data.paragraphs;

    el.innerHTML = `
      <div class="container">
        <div class="service-section__header service-section__header--narrow">
          <h2 class="service-section__title">${data.heading}</h2>
          ${introParagraphs.map((p) => `<p class="service-section__text service-section__text--center">${p}</p>`).join("")}
        </div>
        ${renderPricingTable(data.table)}
        ${footerParagraph ? `<p class="service-section__text service-section__text--center service-pricing__note">${footerParagraph}</p>` : ""}
        <div class="service-pricing__cta">
          <button class="btn-quote btn-recurring-quote" type="button">${data.ctaLabel}</button>
        </div>
      </div>
    `;
  }

  function renderWhyChoose(whyChoose) {
    const el = document.getElementById("service-why");
    const data = normalizeWhyChoose(whyChoose);
    if (!el || !data?.items?.length) return;
    el.innerHTML = `
      <div class="container">
        <h2 class="service-section__title">${data.heading}</h2>
        <div class="why-trust__grid">
          ${data.items
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

  function renderLocations(locations) {
    const titleEl = document.getElementById("service-locations-title");
    const introEl = document.getElementById("service-locations-intro");
    const grid = document.getElementById("service-locations-grid");
    if (!grid || !window.SITE_DATA?.locations) return;

    if (titleEl && locations?.heading) titleEl.textContent = locations.heading;
    if (introEl && locations?.intro) introEl.textContent = locations.intro;

    const PIN_ICON =
      "M15 10.5a3 3 0 11-6 0 3 3 0 016 0z M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z";

    grid.innerHTML = window.SITE_DATA.locations
      .map(
        ({ label, href }) => `
      <a class="location-card" href="${resolve(href)}">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" d="${PIN_ICON}"/>
        </svg>
        <span class="location-card__label">${label}</span>
      </a>
    `
      )
      .join("");
  }

  function renderFaq(faq) {
    const titleEl = document.getElementById("service-faq-title");
    const grid = document.getElementById("service-faq-grid");
    if (!grid || !faq?.items?.length) return;

    if (titleEl && faq.heading) titleEl.textContent = faq.heading;

    grid.innerHTML = faq.items
      .map(
        (item, index) => `
      <div class="faq-item" data-faq-index="${index}">
        <button class="faq-item__trigger" type="button" aria-expanded="false" aria-controls="service-faq-panel-${index}" id="service-faq-trigger-${index}">
          <span class="faq-item__question">${item.question}</span>
          <span class="faq-item__icon" aria-hidden="true">+</span>
        </button>
        <div class="faq-item__panel" id="service-faq-panel-${index}" role="region" aria-labelledby="service-faq-trigger-${index}">
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
    const titleEl = document.getElementById("service-cta-title");
    const textEl = document.getElementById("service-cta-text");
    if (titleEl && cta?.title) titleEl.textContent = cta.title;
    if (textEl && cta?.description) textEl.textContent = cta.description;
  }

  function initServicePage() {
    const slug = getSlug();
    const page = window.SERVICE_PAGES?.[slug];
    if (!page) return;

    renderHero(slug);
    window.SITE_LAYOUT?.renderTrustBar?.();
    renderIntro(normalizeIntro(page.intro));
    renderChecklist(page.checklist);
    renderWhenToBook(normalizeWhenToBook(page.whenToBook));
    renderHowItWorks(page.howItWorks);
    renderOtherServices(slug);
    renderRecurring(page.recurringTitle, page.recurringSubtitle);
    renderPricing(page.pricing);
    renderWhyChoose(page.whyChoose);
    renderLocations(page.locations);
    renderFaq(page.faq);
    renderCta(page.cta);
  }

  initServicePage();
})();
