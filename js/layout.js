(function () {
  const FOOTER_ADDRESS_LINE1 = "450 B Paradise Rd 162";
  const FOOTER_ADDRESS_LINE2 = "Swampscott, MA 01907";
  const FOOTER_PHONE_DISPLAY = "(617) 686-6805";
  const FOOTER_PHONE_TEL = "+16176866805";
  const MAP_EMBED =
    "https://www.google.com/maps?q=450+B+Paradise+Rd+162+Swampscott,+MA+01907&hl=en&z=15&output=embed";

  function getBasePath() {
    const path = window.location.pathname.replace(/\\/g, '/');
    if (path.includes('/services/') || path.includes('/locations/')) return '../';
    return '';
  }

  function resolveHref(href) {
    if (/^(https?:|tel:|mailto:|#)/.test(href)) return href;
    return `${getBasePath()}${href}`;
  }

  function renderFooter() {
    const footer = document.getElementById('site-footer');
    if (!footer || !window.SITE_DATA) return;

    const base = getBasePath();
    const { services, footer: footerData } = window.SITE_DATA;
    const year = new Date().getFullYear();

    const socialHtml = footerData.social.map(({ label, href, icon }) => `
      <a href="${href}" class="footer__social-link" target="_blank" rel="noopener noreferrer" aria-label="${label}">
        ${icon}
      </a>
    `).join('');

    const servicesHtml = services.map(({ label, href }) => `
      <li><a href="${resolveHref(href)}">${label}</a></li>
    `).join('');

    const legalHtml = footerData.legalLinks.map(({ label, href }, index) => {
      const separator = index < footerData.legalLinks.length - 1 ? '<span class="footer__sep">|</span>' : '';
      return `<a href="${resolveHref(href)}">${label}</a>${separator}`;
    }).join('');

    footer.innerHTML = `
      <div class="container footer__inner">
        <div class="footer__grid">
          <div class="footer__brand">
            <a href="${base}index.html" class="footer__logo">
              Marblehead <span class="text-primary">Maids</span>
            </a>
            <p class="footer__tagline">${footerData.tagline}</p>
            <div class="footer__social">${socialHtml}</div>
          </div>
          <div class="footer__col">
            <h3 class="footer__heading">Services</h3>
            <ul class="footer__links">${servicesHtml}</ul>
          </div>
          <div class="footer__col">
            <h3 class="footer__heading">Contact</h3>
            <ul class="footer__contact">
              <li>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                <span>${FOOTER_ADDRESS_LINE1}<br>${FOOTER_ADDRESS_LINE2}</span>
              </li>
              <li>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <a href="tel:${FOOTER_PHONE_TEL}">${FOOTER_PHONE_DISPLAY}</a>
              </li>
              <li>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                <a href="mailto:hello@marbleheadmaids.com">hello@marbleheadmaids.com</a>
              </li>
              <li>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <span>Every Day from 7am-9pm</span>
              </li>
            </ul>
            <div class="footer__map">
              <iframe src="${MAP_EMBED}" width="100%" height="100%" style="border:0" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Marblehead Maids - ${FOOTER_ADDRESS_LINE2}"></iframe>
            </div>
          </div>
        </div>
        <div class="footer__bottom">
          <div class="footer__legal">${legalHtml}</div>
          <p class="footer__copy">&copy; ${year} Marblehead Maids. All rights reserved.</p>
        </div>
        <div class="footer__credit">
          <a href="https://www.bostonsilvadigital.com/en/" target="_blank" rel="noopener noreferrer" title="Professional and Smart Web Design" class="footer__credit-link">
            Boston Silva Digital
          </a>
        </div>
      </div>
    `;
  }

  function renderTrustBar() {
    const el = document.getElementById("service-trust") || document.getElementById("page-trust");
    if (!el) return;

    const star = '<svg viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>';
    const stars = (cls) => `<div class="stars ${cls}">${star.repeat(5)}</div>`;

    el.innerHTML = `
      <div class="container trust__inner">
        <div class="trust__heading">
          <h3>Trusted by North Shore Residents</h3>
          <p>5 star rated service</p>
        </div>
        <div class="trust__logos">
          <div class="trust__grid">
            <div class="trust__item">
              <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google Reviews">
              ${stars("stars--yellow")}
            </div>
            <div class="trust__item">
              <img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/2023_Facebook_icon.svg" alt="Facebook Reviews">
              ${stars("stars--blue")}
            </div>
            <div class="trust__item">
              <img src="https://upload.wikimedia.org/wikipedia/commons/a/ad/Yelp_Logo.svg" alt="Yelp Reviews">
              ${stars("stars--red")}
            </div>
            <div class="trust__item">
              <div class="trust__brand">Thumbtack</div>
              ${stars("stars--dark")}
            </div>
            <div class="trust__item trust__item--nextdoor">
              <div class="trust__brand trust__brand--nextdoor">nextdoor</div>
              ${stars("stars--green")}
            </div>
          </div>
        </div>
      </div>
    `;
  }

  window.SITE_LAYOUT = { getBasePath, resolveHref, renderFooter, renderTrustBar };
})();
