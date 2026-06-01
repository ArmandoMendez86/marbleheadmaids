// Extraction script for madtownmaids.com service pages (use with Runtime.evaluate)
(() => {
  const slug = location.pathname.split('/').filter(Boolean).pop();
  const pageTitle = document.title;
  const metaDescription = document.querySelector('meta[name="description"]')?.content || null;
  const sections = [...document.querySelectorAll('main section')];
  const h2Of = (s) => (s?.querySelector('h2')?.innerText || '').trim();
  const find = (fn) => sections.find(fn);
  const hero = sections.find(s => s.querySelector('h1')) || sections[0];
  const h1 = hero?.querySelector('h1')?.innerText?.trim() || '';
  const heroSubtitle = hero?.querySelector('h1 + p')?.innerText?.trim() || '';
  const isKnown = (h2) =>
    /What's Included|Included in|When to Book|Scheduling Options|Other Cleaning|How It Works|Save with Recurring|Prices in|Pricing|Why .+ Choose|Why Madison Hosts|Throughout|Across Madison|FAQ|Common Questions/i.test(h2) ||
    /^(Get Your|Ready to|Give Your|Start Your|Move Out|Turn Your|Your Reviews|Ready for)/i.test(h2);
  const introSec = find(s => {
    const h2 = h2Of(s);
    return h2 && !isKnown(h2) && !s.querySelector('h1');
  });
  const introParagraphs = [];
  if (introSec) {
    for (const el of introSec.querySelectorAll('h2, h3, p')) {
      if (el.tagName === 'H2') continue;
      if (el.tagName === 'H3') break;
      if (el.tagName === 'P') {
        const text = el.innerText.trim();
        if (text) introParagraphs.push(text);
      }
    }
  }
  const intro = {
    heading: h2Of(introSec),
    paragraphs: introParagraphs,
  };
  const checklistSec = find((s) => /What's Included|Included in/i.test(h2Of(s)));
  const checklistIntro = checklistSec?.querySelector('h2 + p')?.innerText?.trim() || '';
  const checklist = {
    heading: h2Of(checklistSec),
    intro: checklistIntro,
    categories: checklistSec
      ? [...checklistSec.querySelectorAll('h3')]
          .map((h3) => {
            const ul =
              h3.nextElementSibling?.tagName === 'UL'
                ? h3.nextElementSibling
                : h3.parentElement.querySelector('ul');
            return {
              title: h3.innerText.trim(),
              items: [...(ul?.querySelectorAll('li') || [])].map((li) => li.innerText.trim()),
            };
          })
          .filter((c) => c.items.length)
      : [],
  };
  const whenSec = find((s) => /When to Book|Scheduling Options/i.test(h2Of(s)));
  const whenToBook = {
    heading: h2Of(whenSec),
    options: whenSec
      ? [...whenSec.querySelectorAll('h3')].map((h3) => ({
          number: parseInt(h3.querySelector('span')?.innerText || '0', 10),
          title: h3.innerText.replace(/^\d+\s*/, '').trim(),
          description: h3.nextElementSibling?.innerText?.trim() || '',
        }))
      : [],
  };
  const pricingSec = find((s) => /Prices in|Pricing/i.test(h2Of(s)));
  const pricing = {
    heading: h2Of(pricingSec),
    paragraphs: pricingSec
      ? [...pricingSec.querySelectorAll('p')].map((p) => p.innerText.trim())
      : [],
  };
  const whySec = find(
    (s) =>
      /Why .+ Choose|Why Madison Hosts Choose|Why Madison Businesses Choose/i.test(h2Of(s))
  );
  const whyChoose = {
    heading: h2Of(whySec),
    items: whySec
      ? [...whySec.querySelectorAll('h3')].map((h3) => ({
          title: h3.innerText.trim(),
          description: h3.nextElementSibling?.innerText?.trim() || '',
        }))
      : [],
  };
  const locSec = find((s) => /Throughout|Across Madison/i.test(h2Of(s)));
  const locPs = locSec
    ? [...locSec.querySelectorAll('p')]
        .map((p) => p.innerText.trim())
        .filter((t) => t && t !== 'Locations' && t.length > 15)
    : [];
  const locations = { heading: h2Of(locSec), intro: locPs[0] || '' };
  const recurSec = find((s) => {
    const h2 = h2Of(s);
    if (/Other Cleaning|FAQ|Throughout|When to Book|What's Included|Why |Prices in/i.test(h2))
      return false;
    const h3s = [...s.querySelectorAll('h3')].map((h) => h.innerText.trim());
    return h3s.includes('Weekly') && h3s.includes('Bi-Weekly');
  });
  const recurringTitle = h2Of(recurSec);
  const faqSec = find((s) => /FAQ|Common Questions/i.test(h2Of(s)));
  const faq = {
    heading: h2Of(faqSec),
    items: faqSec
      ? [...faqSec.querySelectorAll('.bg-light.rounded-xl, .rounded-xl.overflow-hidden')]
          .map((card) => ({
            question: card.querySelector('button span')?.innerText?.trim() || '',
            answer: card.querySelector('p')?.innerText?.trim() || '',
          }))
          .filter((x) => x.question)
      : [],
  };
  const ctaSec =
    find((s) => s.className.includes('bg-dark') && s.querySelector('h2')) ||
    sections.filter((s) => s.querySelector('h2')).slice(-1)[0];
  const ctaPs = ctaSec
    ? [...ctaSec.querySelectorAll('p')]
        .map((p) => p.innerText.trim())
        .filter((t) => t.length > 20)
    : [];
  const cta = { title: h2Of(ctaSec), description: ctaPs[0] || '' };
  return {
    slug,
    pageTitle,
    metaDescription,
    h1,
    heroSubtitle,
    intro,
    checklist,
    whenToBook,
    pricing,
    whyChoose,
    locations,
    recurringTitle,
    faq,
    cta,
  };
})();
