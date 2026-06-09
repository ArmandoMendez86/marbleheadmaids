(function () {
  'use strict';

  // Capturar la raíz del sitio desde la URL del propio script.
  // Funciona en cualquier entorno: XAMPP en subdirectorio, Hostinger en raíz, etc.
  const _scriptSrc = (document.currentScript || document.querySelector('script[src*="quote-modal"]'))?.src || '';
  const _siteRoot  = _scriptSrc
    ? new URL(_scriptSrc).origin + new URL(_scriptSrc).pathname.replace(/\/js\/quote-modal\.js.*$/, '')
    : '';

  // ── Insertar modal en el DOM ──────────────────────────────────
  const MODAL_HTML = `
  <div class="quote-modal-overlay" id="quoteModalOverlay" role="dialog" aria-modal="true" aria-labelledby="quoteModalTitle">
    <div class="quote-modal">
      <div class="quote-modal__header">
        <h2 class="quote-modal__title" id="quoteModalTitle">Get a Free Quote</h2>
        <button class="quote-modal__close" id="quoteModalClose" aria-label="Close">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <!-- Success state -->
      <div class="quote-modal__success" id="quoteSuccess">
        <div class="quote-modal__success-icon">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
          </svg>
        </div>
        <div class="quote-modal__success-title">Request received!</div>
        <p class="quote-modal__success-msg">Thanks for reaching out. We'll get back to you shortly to discuss your cleaning needs.</p>
        <button class="qf-submit" id="quoteSuccessClose" style="max-width:200px;margin-top:0.5rem">Close</button>
      </div>

      <!-- Form -->
      <div class="quote-modal__body" id="quoteFormWrap">
        <p class="quote-modal__subtitle">Fill out the form below and we'll get back to you with a personalized quote.</p>

        <div class="qf-general-error" id="quoteGeneralError"></div>

        <form id="quoteForm" novalidate>
          <div class="qf-grid">

            <div class="qf-group">
              <label class="qf-label" for="qf_first_name">First Name <span class="qf-req">*</span></label>
              <input class="qf-input" type="text" id="qf_first_name" name="first_name" placeholder="Jane" autocomplete="given-name">
              <span class="qf-error" id="qf_first_name_err"></span>
            </div>

            <div class="qf-group">
              <label class="qf-label" for="qf_last_name">Last Name</label>
              <input class="qf-input" type="text" id="qf_last_name" name="last_name" placeholder="Smith" autocomplete="family-name">
            </div>

            <div class="qf-group qf-full">
              <label class="qf-label" for="qf_email">Email <span class="qf-req">*</span></label>
              <input class="qf-input" type="email" id="qf_email" name="email" placeholder="jane@example.com" autocomplete="email">
              <span class="qf-error" id="qf_email_err"></span>
            </div>

            <div class="qf-group qf-full">
              <label class="qf-label" for="qf_phone">Phone <span class="qf-req">*</span></label>
              <div class="qf-phone-wrap" id="qf_phone_wrap">
                <div class="qf-phone-prefix">
                  <span class="flag">🇺🇸</span>
                  <span>+1</span>
                </div>
                <input class="qf-phone-input" type="tel" id="qf_phone" name="phone" placeholder="(617) 000-0000" autocomplete="tel">
              </div>
              <span class="qf-error" id="qf_phone_err"></span>
            </div>

            <div class="qf-group qf-full">
              <label class="qf-label" for="qf_address">Address</label>
              <input class="qf-input" type="text" id="qf_address" name="address" placeholder="123 Main St" autocomplete="street-address">
            </div>

            <div class="qf-group qf-full">
              <label class="qf-label" for="qf_zip_code">Zip Code <span class="qf-req">*</span></label>
              <input class="qf-input" type="text" id="qf_zip_code" name="zip_code" placeholder="01945" autocomplete="postal-code" inputmode="numeric" maxlength="10">
              <span class="qf-error" id="qf_zip_code_err"></span>
            </div>

            <div class="qf-group qf-full">
              <div class="qf-checkbox-row">
                <input class="qf-checkbox" type="checkbox" id="qf_marketing" name="marketing_consent">
                <label class="qf-checkbox-label" for="qf_marketing">
                  I agree to receive marketing messaging from Marblehead Maids at the +1 (617) 686-6805. Reply <strong>STOP</strong> to opt out.
                </label>
              </div>
            </div>

          </div><!-- /qf-grid -->

          <button type="submit" class="qf-submit" id="quoteSubmitBtn">
            <span class="btn-text">Send My Request</span>
            <span class="spinner" aria-hidden="true"></span>
          </button>
        </form>
      </div>
    </div>
  </div>`;

  document.body.insertAdjacentHTML('beforeend', MODAL_HTML);

  // ── Referencias ───────────────────────────────────────────────
  const overlay    = document.getElementById('quoteModalOverlay');
  const closeBtn   = document.getElementById('quoteModalClose');
  const form       = document.getElementById('quoteForm');
  const submitBtn  = document.getElementById('quoteSubmitBtn');
  const formWrap   = document.getElementById('quoteFormWrap');
  const successEl  = document.getElementById('quoteSuccess');
  const successClose = document.getElementById('quoteSuccessClose');
  const generalErr = document.getElementById('quoteGeneralError');

  // ── Abrir / Cerrar ────────────────────────────────────────────
  function openModal() {
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    setTimeout(() => closeBtn.focus(), 50);
    resetForm();
  }

  function closeModal() {
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  // Conectar todos los botones "Get a Quote" del sitio (header, hero, CTA, etc.)
  document.querySelectorAll('.btn-quote, .btn-hero-quote').forEach(btn => {
    btn.addEventListener('click', openModal);
  });

  closeBtn.addEventListener('click', closeModal);
  successClose.addEventListener('click', closeModal);

  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeModal();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('is-open')) closeModal();
  });

  // ── Validación ────────────────────────────────────────────────
  function setError(fieldId, msg) {
    const input = document.getElementById(fieldId);
    const errEl = document.getElementById(fieldId + '_err');
    if (input) input.classList.toggle('is-error', !!msg);
    if (errEl) errEl.textContent = msg || '';

    // El campo de teléfono tiene un wrapper especial
    if (fieldId === 'qf_phone') {
      const wrap = document.getElementById('qf_phone_wrap');
      if (wrap) wrap.classList.toggle('is-error', !!msg);
    }
  }

  function validate(data) {
    let valid = true;

    if (!data.first_name) {
      setError('qf_first_name', 'First name is required.');
      valid = false;
    } else {
      setError('qf_first_name', '');
    }

    if (!data.email) {
      setError('qf_email', 'Email is required.');
      valid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
      setError('qf_email', 'Please enter a valid email.');
      valid = false;
    } else {
      setError('qf_email', '');
    }

    if (!data.phone) {
      setError('qf_phone', 'Phone is required.');
      valid = false;
    } else {
      setError('qf_phone', '');
    }

    if (!data.zip_code) {
      setError('qf_zip_code', 'Zip code is required.');
      valid = false;
    } else {
      setError('qf_zip_code', '');
    }

    return valid;
  }

  // ── Envío ─────────────────────────────────────────────────────
  form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const data = {
      first_name:        form.first_name.value.trim(),
      last_name:         form.last_name.value.trim(),
      email:             form.email.value.trim(),
      phone:             form.phone.value.trim(),
      address:           form.address.value.trim(),
      zip_code:          form.zip_code.value.trim(),
      marketing_consent: form.marketing_consent.checked,
    };

    generalErr.classList.remove('is-shown');

    if (!validate(data)) return;

    // Determinar la ruta a la API (relativa a la raíz del sitio)
    const apiBase = getApiBase();

    submitBtn.classList.add('loading');
    submitBtn.disabled = true;

    try {
      const res = await fetch(apiBase + '/api/index.php/quotes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      const json = await res.json();

      if (res.ok && json.success) {
        formWrap.style.display = 'none';
        successEl.classList.add('is-shown');
      } else if (res.status === 422 && json.errors) {
        // Errores de validación del servidor
        const fieldMap = {
          first_name: 'qf_first_name',
          email:      'qf_email',
          phone:      'qf_phone',
          zip_code:   'qf_zip_code',
        };
        for (const [field, msg] of Object.entries(json.errors)) {
          if (fieldMap[field]) setError(fieldMap[field], msg);
        }
      } else {
        showGeneralError(json.error || 'Something went wrong. Please try again or call us directly.');
      }
    } catch (err) {
      showGeneralError('Network error. Please try again or call us at (617) 686-6805.');
    } finally {
      submitBtn.classList.remove('loading');
      submitBtn.disabled = false;
    }
  });

  function showGeneralError(msg) {
    generalErr.textContent = msg;
    generalErr.classList.add('is-shown');
  }

  function resetForm() {
    form.reset();
    ['qf_first_name', 'qf_email', 'qf_phone', 'qf_zip_code'].forEach(id => setError(id, ''));
    generalErr.classList.remove('is-shown');
    formWrap.style.display = '';
    successEl.classList.remove('is-shown');
    submitBtn.classList.remove('loading');
    submitBtn.disabled = false;
  }

  // ── Detectar base URL de la API ───────────────────────────────
  function getApiBase() {
    return _siteRoot;
  }
})();
