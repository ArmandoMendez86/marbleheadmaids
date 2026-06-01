(function () {
  const { services, locations } = window.SITE_DATA;

  function renderLinks(items) {
    const resolve = window.SITE_LAYOUT?.resolveHref || ((href) => href);
    return items.map(({ label, href }) => `<a href="${resolve(href)}">${label}</a>`).join('');
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
    const overlay = document.querySelector('.mobile-overlay');
    const panel = document.querySelector('.mobile-panel');
    const menuToggle = document.querySelector('.menu-toggle');
    overlay.hidden = false;
    overlay.classList.add('is-visible');
    panel.classList.add('is-open');
    panel.setAttribute('aria-hidden', 'false');
    menuToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileMenu() {
    const overlay = document.querySelector('.mobile-overlay');
    const panel = document.querySelector('.mobile-panel');
    const menuToggle = document.querySelector('.menu-toggle');
    overlay.classList.remove('is-visible');
    panel.classList.remove('is-open');
    panel.setAttribute('aria-hidden', 'true');
    menuToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    window.setTimeout(() => {
      if (!panel.classList.contains('is-open')) overlay.hidden = true;
    }, 300);
  }

  function initMobileMenu() {
    const overlay = document.querySelector('.mobile-overlay');
    const panel = document.querySelector('.mobile-panel');
    const menuToggle = document.querySelector('.menu-toggle');
    const menuClose = document.querySelector('.mobile-panel__close');

    menuToggle?.addEventListener('click', openMobileMenu);
    menuClose?.addEventListener('click', closeMobileMenu);
    overlay?.addEventListener('click', closeMobileMenu);
    panel?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMobileMenu));

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

  initNavMenus();
  initMobileMenu();
  initDesktopDropdowns();
  window.SITE_LAYOUT?.renderFooter();
})();
