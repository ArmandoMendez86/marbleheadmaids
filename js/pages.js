(function () {
  const CHECK_ICON =
    "M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z";

  const PAGE_HERO_IMAGES = {
    about: "about",
    checklist: "checklist",
    contact: "contact",
    careers: "home",
    privacy: "home",
    terms: "home",
  };

  function getPageType() {
    const bodyType = document.body.dataset.page;
    if (bodyType) return bodyType;
    const path = window.location.pathname.replace(/\\/g, "/");
    const file = path.split("/").pop() || "index.html";
    return file.replace(".html", "");
  }

  function heroBasePath() {
    return window.SITE_LAYOUT?.getBasePath() || "./";
  }

  function renderHero(pageType) {
    const bg = document.getElementById("page-hero-bg");
    const slug = PAGE_HERO_IMAGES[pageType];
    if (!bg || !slug) return;
    bg.style.backgroundImage = `url('${heroBasePath()}images/heroes/${slug}.jpg')`;
  }

  function renderCheckCell(value) {
    if (value === "na") return '<span class="checklist-table__na">N/A</span>';
    if (value) {
      return `<span class="checklist-table__yes" aria-label="Included">✓</span>`;
    }
    return `<span class="checklist-table__no" aria-label="Not included">✗</span>`;
  }

  function initFaqAccordion(root) {
    root.querySelectorAll(".faq-item").forEach((item) => {
      const trigger = item.querySelector(".faq-item__trigger");
      const icon = item.querySelector(".faq-item__icon");
      trigger?.addEventListener("click", () => {
        const isOpen = item.classList.toggle("is-open");
        trigger.setAttribute("aria-expanded", String(isOpen));
        if (icon) icon.textContent = isOpen ? "−" : "+";
      });
    });
  }

  function renderAbout() {
    const data = window.PAGES_CONTENT?.about;
    if (!data) return;

    const intro = document.getElementById("about-intro");
    if (intro) {
      intro.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">${data.intro.heading}</h2>
          <div class="service-section__body">
            ${data.intro.paragraphs.map((p) => `<p class="service-section__text">${p}</p>`).join("")}
          </div>
        </div>
      `;
    }

    const stats = document.getElementById("about-stats");
    if (stats) {
      stats.innerHTML = `
        <div class="container">
          <div class="about-stats__grid">
            ${data.stats
              .map(
                (s) => `
              <div class="about-stats__item">
                <div class="about-stats__value">${s.value}</div>
                <div class="about-stats__label">${s.label}</div>
              </div>
            `
              )
              .join("")}
          </div>
        </div>
      `;
    }

    const beliefs = document.getElementById("about-beliefs");
    if (beliefs) {
      beliefs.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">${data.beliefs.heading}</h2>
          <p class="service-section__text service-section__text--center">${data.beliefs.intro}</p>
          <div class="why-trust__grid">
            ${data.beliefs.items
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

    const team = document.getElementById("about-team");
    if (team) {
      team.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">${data.team.heading}</h2>
          <div class="service-section__body">
            ${data.team.paragraphs.map((p) => `<p class="service-section__text">${p}</p>`).join("")}
          </div>
          <ul class="about-team__list">
            ${data.team.bullets.map((b) => `<li>${b}</li>`).join("")}
          </ul>
        </div>
      `;
    }

    const local = document.getElementById("about-local");
    if (local) {
      local.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">${data.local.heading}</h2>
          <div class="service-section__body">
            ${data.local.paragraphs.map((p) => `<p class="service-section__text">${p}</p>`).join("")}
          </div>
        </div>
      `;
    }

    setCta(data.cta);
  }

  function renderChecklist() {
    const meta = window.PAGES_CONTENT?.checklist;
    const checklist = window.CHECKLIST_DATA;
    const main = document.getElementById("checklist-main");
    if (!main || !checklist?.tabs?.length) return;

    const firstTab = checklist.tabs[0].id;
    main.innerHTML = `
      <div class="container">
        <div class="service-section__header">
          <h2 class="service-section__title">${meta.heading}</h2>
          <p class="service-section__text service-section__text--center">${meta.intro}</p>
        </div>
        <div class="checklist-tabs" role="tablist">
          ${checklist.tabs
            .map(
              (tab, i) => `
            <button class="checklist-tabs__btn${i === 0 ? " is-active" : ""}" type="button" role="tab" aria-selected="${i === 0}" data-tab="${tab.id}">${tab.label}</button>
          `
            )
            .join("")}
        </div>
        ${checklist.tabs
          .map(
            (tab, i) => `
          <div class="checklist-panel${i === 0 ? "" : " hidden"}" data-panel="${tab.id}" role="tabpanel">
            <div class="checklist-table-wrap">
              <table class="checklist-table">
                <thead>
                  <tr>
                    <th>Task</th>
                    ${checklist.columns.map((c) => `<th>${c.label}</th>`).join("")}
                  </tr>
                </thead>
                <tbody>
                  ${tab.tasks
                    .map(
                      (row) => `
                    <tr>
                      <td>${row.task}</td>
                      ${checklist.columns
                        .map((c) => `<td class="checklist-table__cell">${renderCheckCell(row[c.key])}</td>`)
                        .join("")}
                    </tr>
                  `
                    )
                    .join("")}
                </tbody>
              </table>
            </div>
          </div>
        `
          )
          .join("")}
        <div class="checklist-legend">
          <span><span class="checklist-table__yes">✓</span> Included</span>
          <span><span class="checklist-table__no">✗</span> Not Included</span>
        </div>
      </div>
    `;

    main.querySelectorAll(".checklist-tabs__btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const tabId = btn.dataset.tab;
        main.querySelectorAll(".checklist-tabs__btn").forEach((b) => {
          b.classList.toggle("is-active", b === btn);
          b.setAttribute("aria-selected", String(b === btn));
        });
        main.querySelectorAll(".checklist-panel").forEach((panel) => {
          panel.classList.toggle("hidden", panel.dataset.panel !== tabId);
        });
      });
    });

    const footer = document.getElementById("checklist-footer");
    if (footer && meta.footer) {
      footer.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">${meta.footer.heading}</h2>
          ${meta.footer.paragraphs.map((p) => `<p class="service-section__text service-section__text--center">${p}</p>`).join("")}
        </div>
      `;
    }

    setCta(meta.cta);
  }

  function renderQuoteForm(containerId, heading) {
    const el = document.getElementById(containerId);
    if (!el) return;
    el.innerHTML = `
      <div class="container">
        <h2 class="service-section__title">${heading}</h2>
        <form class="quote-form" action="#" method="post">
        <div class="quote-form__grid">
          <label class="quote-form__field"><span>Name</span><input type="text" name="name" autocomplete="name"></label>
          <label class="quote-form__field"><span>Phone</span><input type="tel" name="phone" autocomplete="tel"></label>
          <label class="quote-form__field"><span>Email</span><input type="email" name="email" autocomplete="email"></label>
          <label class="quote-form__field"><span>Service Type</span>
            <select name="service">
              <option>House Cleaning</option>
              <option>Apartment Cleaning</option>
              <option>Deep Cleaning</option>
              <option>Move-In / Move-Out</option>
              <option>Other</option>
            </select>
          </label>
          <label class="quote-form__field quote-form__field--full"><span>Message</span><textarea name="message" rows="4"></textarea></label>
        </div>
        <button class="btn-quote" type="submit">Submit Request</button>
      </form>
      </div>
    `;
    el.querySelector("form")?.addEventListener("submit", (e) => e.preventDefault());
  }

  function renderContact() {
    const data = window.PAGES_CONTENT?.contact;
    if (!data) return;

    const cards = document.getElementById("contact-cards");
    if (cards) {
      cards.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">Other Ways to Reach Us</h2>
          <div class="contact-cards__grid">
            ${data.cards
              .map(
                (card) => `
              <div class="contact-card">
                <h3 class="contact-card__title">${card.title}</h3>
                ${card.lines
                  .map((line, i) => {
                    if (card.href && i === 0) {
                      return `<a class="contact-card__line contact-card__line--link" href="${card.href}">${line}</a>`;
                    }
                    return `<p class="contact-card__line">${line}</p>`;
                  })
                  .join("")}
              </div>
            `
              )
              .join("")}
          </div>
        </div>
      `;
    }

    renderQuoteForm("contact-form", data.formHeading);

    const faq = document.getElementById("contact-faq");
    if (faq) {
      faq.innerHTML = `
        <div class="container">
          <h2 class="faq__title">${data.faqHeading}</h2>
          <div class="faq__grid">
            ${data.faq
              .map(
                (item, index) => `
              <div class="faq-item" data-faq-index="${index}">
                <button class="faq-item__trigger" type="button" aria-expanded="false" aria-controls="contact-faq-panel-${index}">
                  <span class="faq-item__question">${item.question}</span>
                  <span class="faq-item__icon" aria-hidden="true">+</span>
                </button>
                <div class="faq-item__panel" id="contact-faq-panel-${index}" role="region">
                  <div class="faq-item__panel-inner"><div class="faq-item__answer-wrap"><p class="faq-item__answer">${item.answer}</p></div></div>
                </div>
              </div>
            `
              )
              .join("")}
          </div>
        </div>
      `;
      initFaqAccordion(faq);
    }

    const area = document.getElementById("contact-area");
    if (area) {
      area.innerHTML = `
        <div class="container">
          <h2 class="service-section__title">${data.serviceArea.heading}</h2>
          <p class="service-section__text service-section__text--center">${data.serviceArea.text}</p>
        </div>
      `;
    }

    setCta(data.cta);
  }

  function renderCareers() {
    const data = window.PAGES_CONTENT?.careers;
    if (!data) return;
    renderQuoteForm("careers-form", data.heading);
    const intro = document.getElementById("careers-intro");
    if (intro) intro.innerHTML = `<div class="container"><p class="service-section__text service-section__text--center">${data.intro}</p></div>`;
    setCta(data.cta);
  }

  function renderLegal(type) {
    const data = window.PAGES_CONTENT?.[type];
    const el = document.getElementById("legal-content");
    if (!el || !data) return;

    el.innerHTML = `
      <div class="container page-content__inner">
        ${data.sections
          .map((section) => {
            let html = `<div class="page-block"><h2 class="page-block__title">${section.heading}</h2>`;
            if (section.paragraphs) {
              html += section.paragraphs.map((p) => `<p class="page-block__text">${p}</p>`).join("");
            }
            if (section.bullets) {
              html += `<ul class="page-block__list">${section.bullets.map((b) => `<li>${b}</li>`).join("")}</ul>`;
            }
            if (section.subheading) html += `<h3 class="page-block__subtitle">${section.subheading}</h3>`;
            if (section.subBullets) {
              html += `<ul class="page-block__list">${section.subBullets.map((b) => `<li>${b}</li>`).join("")}</ul>`;
            }
            if (section.footer) html += `<p class="page-block__text">${section.footer}</p>`;
            if (section.subsections) {
              html += section.subsections
                .map(
                  (sub) => `
                <h3 class="page-block__subtitle">${sub.title}</h3>
                <p class="page-block__text">${sub.text}</p>
              `
                )
                .join("");
            }
            html += "</div>";
            return html;
          })
          .join("")}
      </div>
    `;
    setCta(data.cta);
  }

  function setCta(cta) {
    if (!cta) return;
    const titleEl = document.getElementById("page-cta-title");
    const textEl = document.getElementById("page-cta-text");
    if (titleEl) titleEl.textContent = cta.title;
    if (textEl) textEl.textContent = cta.description;
  }

  function initPageContent() {
    const type = getPageType();
    renderHero(type);
    window.SITE_LAYOUT?.renderTrustBar?.();

    if (type === "about") renderAbout();
    else if (type === "checklist") renderChecklist();
    else if (type === "contact") renderContact();
    else if (type === "careers") renderCareers();
    else if (type === "privacy" || type === "terms") renderLegal(type);
  }

  initPageContent();
})();
