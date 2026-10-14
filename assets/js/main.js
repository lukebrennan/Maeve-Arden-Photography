/* Progressive enhancement: navigation, gallery and a browser-only enquiry. */
(() => {
  'use strict';
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const prefix = document.body.dataset.assetPrefix || '';

  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  const stickyEnquiry = $('.mobile-enquire');
  if (stickyEnquiry && 'IntersectionObserver' in window) {
    const visibleCallsToAction = new Map();
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => visibleCallsToAction.set(entry.target, entry.isIntersecting));
      stickyEnquiry.hidden = [...visibleCallsToAction.values()].some(Boolean);
    });
    const targets = [$('.hero-actions .button'), $('.closing-cta'), $('.site-footer')].filter(Boolean);
    if ($('.hero-actions .button')) stickyEnquiry.hidden = true;
    targets.forEach(target => observer.observe(target));
  }

  // Keep Tab navigation inside the dialogs across browser keyboard preferences.
  const trapTab = dialog => dialog.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const controls = $$('a[href],button:not(:disabled)', dialog).filter(el => el.getClientRects().length);
    const first = controls[0];
    const last = controls[controls.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault(); last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault(); first.focus();
    }
  });

  // Native dialogs provide focus containment, background inertness and Escape.
  const menu = $('#navigation-dialog');
  const menuButton = $('[data-menu-open]');
  if (menu && menuButton && typeof menu.showModal === 'function') {
    trapTab(menu);
    menuButton.addEventListener('click', () => {
      menu.showModal();
      menuButton.setAttribute('aria-expanded', 'true');
      document.body.classList.add('dialog-open');
    });
    $('[data-menu-close]', menu).addEventListener('click', () => menu.close());
    menu.addEventListener('click', e => { if (e.target === menu) menu.close(); });
    menu.addEventListener('close', () => {
      menuButton.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('dialog-open');
      menuButton.focus();
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', e => {
      if (e.matches && menu.open) menu.close();
    });
  } else if (menu && menuButton) {
    // Older browsers still get the same navigation links without a modal.
    menuButton.addEventListener('click', () => {
      const open = !menu.hasAttribute('open');
      menu.toggleAttribute('open', open);
      menuButton.setAttribute('aria-expanded', String(open));
    });
    $('[data-menu-close]', menu).addEventListener('click', () => {
      menu.removeAttribute('open');
      menuButton.setAttribute('aria-expanded', 'false');
    });
  }

  const filters = $$('[data-filter]');
  const photographs = $$('[data-lightbox]');
  if (filters.length) {
    $('[data-gallery-toolbar]').hidden = false;
    filters.forEach(button => button.addEventListener('click', () => {
      const category = button.dataset.filter;
      filters.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
      photographs.forEach(photo => {
        photo.hidden = category !== 'all' && photo.dataset.category !== category;
      });
      const count = photographs.filter(photo => !photo.hidden).length;
      $('[data-gallery-status]').textContent = `${count} photograph${count === 1 ? '' : 's'}`;
    }));
  }

  const galleryDialog = $('[data-lightbox-dialog]');
  if (galleryDialog && photographs.length && typeof galleryDialog.showModal === 'function') {
    trapTab(galleryDialog);
    const galleryImage = $('[data-lightbox-image]', galleryDialog);
    const count = $('[data-lightbox-count]', galleryDialog);
    const title = $('#lightbox-title', galleryDialog);
    const credit = $('[data-lightbox-credit]', galleryDialog);
    const previous = $('[data-lightbox-prev]', galleryDialog);
    const next = $('[data-lightbox-next]', galleryDialog);
    let current = 0;
    let visible = [];
    let trigger;
    let imageManifest;
    const manifest = () => imageManifest || (imageManifest = fetch(`${prefix}assets/images/manifest.json`)
      .then(response => { if (!response.ok) throw new Error('Manifest unavailable'); return response.json(); })
      .catch(() => null));

    const renderPhoto = () => {
      const link = visible[current];
      const key = link.dataset.lightbox;
      galleryImage.src = `${prefix}assets/images/${key}-1600.webp`;
      galleryImage.alt = $('img', link).alt;
      // Match the natural ratio before decode; the viewer uses object-fit:contain.
      galleryImage.width = $('img', link).width;
      galleryImage.height = $('img', link).height;
      title.textContent = link.dataset.title;
      count.textContent = `${current + 1} / ${visible.length}`;
      previous.disabled = next.disabled = visible.length < 2;
      credit.href = `${prefix}credits.html`;
      credit.textContent = 'View photographer credits ↗';
      manifest().then(data => {
        // Ignore a late response if the user has moved to another photograph.
        if (visible[current].dataset.lightbox !== key || !data?.[key]) return;
        credit.textContent = `Photograph by ${data[key].photographer} ↗`;
        credit.href = data[key].sourceUrl;
      });
    };
    const move = delta => {
      current = (current + delta + visible.length) % visible.length;
      renderPhoto();
    };
    photographs.forEach(link => link.addEventListener('click', e => {
      e.preventDefault();
      visible = photographs.filter(photo => !photo.hidden);
      current = visible.indexOf(link);
      trigger = link;
      renderPhoto();
      galleryDialog.showModal();
      document.body.classList.add('dialog-open');
    }));
    previous.addEventListener('click', () => move(-1));
    next.addEventListener('click', () => move(1));
    $('[data-lightbox-close]', galleryDialog).addEventListener('click', () => galleryDialog.close());
    galleryDialog.addEventListener('click', e => { if (e.target === galleryDialog) galleryDialog.close(); });
    galleryDialog.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        e.preventDefault();
        move(e.key === 'ArrowLeft' ? -1 : 1);
      }
    });
    galleryDialog.addEventListener('close', () => {
      document.body.classList.remove('dialog-open');
      trigger?.focus();
    });
  }

  const form = $('[data-enquiry-form]');
  if (!form) return;
  const fields = $('[data-form-fields]', form);
  fields.disabled = false;
  const result = $('[data-enquiry-result]');
  const errorSummary = $('[data-error-summary]', form);
  const date = $('#date', form);
  const flexible = $('#flexible', form);
  const name = $('#name', form);
  const email = $('#email', form);
  let currentStep = 1;
  let previewText = '';
  const collectionLabels = {
    intimate: 'The Intimate · from £1,450',
    story: 'The Story · from £2,850',
    complete: 'The Complete · from £4,900',
    destination: 'Destination · bespoke quote'
  };
  const requestedCollection = new URLSearchParams(location.search).get('collection');
  if (Object.hasOwn(collectionLabels, requestedCollection)) {
    $(`input[name="collection"][value="${requestedCollection}"]`, form).checked = true;
  }
  // Local date avoids a UTC offset changing the minimum around midnight.
  const today = new Date();
  const todayString = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
  date.min = todayString;
  const dateLabel = () => flexible.checked ? 'Date to be confirmed' :
    new Intl.DateTimeFormat('en-GB', {day:'numeric',month:'long',year:'numeric'}).format(new Date(`${date.value}T12:00:00`));
  const clearError = input => {
    input.removeAttribute('aria-invalid');
    $(`#${input.id}-error`, form).textContent = '';
  };
  const clearErrors = () => {
    [date, name, email].forEach(clearError);
    errorSummary.hidden = true;
    errorSummary.replaceChildren();
  };
  const showErrors = errors => {
    errorSummary.replaceChildren();
    const heading = document.createElement('p');
    heading.textContent = 'Please check these details:';
    errorSummary.append(heading);
    for (const [input, message] of errors) {
      input.setAttribute('aria-invalid', 'true');
      $(`#${input.id}-error`, form).textContent = message;
      const link = document.createElement('a');
      link.href = `#${input.id}`;
      link.textContent = message;
      link.addEventListener('click', e => { e.preventDefault(); input.focus(); });
      errorSummary.append(link);
    }
    errorSummary.hidden = false;
    errors[0][0].focus();
  };
  const validate = step => {
    clearErrors();
    const errors = [];
    if (step === 1) {
      if (!flexible.checked && !date.value) errors.push([date, 'Choose a date, or tell us it isn’t set yet.']);
      else if (!flexible.checked && (date.validity.badInput || date.value < todayString)) errors.push([date, 'Choose today or a future date.']);
    } else {
      if (!name.value.trim()) errors.push([name, 'Enter your name or names.']);
      if (!email.value.trim()) errors.push([email, 'Enter your email address.']);
      else if (email.validity.typeMismatch) errors.push([email, 'Enter a valid email address, like you@example.com.']);
    }
    if (errors.length) showErrors(errors);
    return errors.length === 0;
  };
  const setStep = step => {
    currentStep = step;
    clearErrors();
    $$('[data-form-step]', form).forEach(section => { section.hidden = Number(section.dataset.formStep) !== step; });
    $$('[data-step-indicator]', form).forEach(indicator => {
      const selected = Number(indicator.dataset.stepIndicator) === step;
      indicator.classList.toggle('current', selected);
      if (selected) indicator.setAttribute('aria-current', 'step');
      else indicator.removeAttribute('aria-current');
    });
    if (step === 2) {
      const collection = $('input[name="collection"]:checked', form).value;
      const venue = $('#venue', form).value.trim();
      $('[data-enquiry-summary]').textContent = `${collectionLabels[collection]} · ${dateLabel()}${venue ? ' · ' + venue : ''}`;
    }
    $(`#${step === 1 ? 'plans-title' : 'about-you-title'}`, form).focus({preventScroll:true});
    form.scrollIntoView({block:'start', behavior:'instant'});
  };
  flexible.addEventListener('change', () => {
    date.disabled = flexible.checked;
    date.required = !flexible.checked;
    $('[data-date-required]', form).textContent = flexible.checked ? '(not set yet)' : '(required)';
    clearError(date);
    errorSummary.hidden = true;
  });
  [date, name, email].forEach(input => input.addEventListener('input', () => clearError(input)));
  $('[data-next-step]', form).addEventListener('click', () => { if (validate(1)) setStep(2); });
  $('[data-previous-step]', form).addEventListener('click', () => setStep(1));
  form.addEventListener('submit', e => {
    e.preventDefault();
    if (currentStep === 1) { if (validate(1)) setStep(2); return; }
    if (!validate(2)) return;
    const collection = $('input[name="collection"]:checked', form).value;
    const details = [
      ['Names', name.value.trim()],
      ['Email', email.value.trim()],
      ['Collection', collectionLabels[collection]],
      ['Date', dateLabel()],
      ['Venue', $('#venue', form).value.trim() || 'To be confirmed'],
      ['Your plans', $('#message', form).value.trim() || 'To talk through together']
    ];
    const list = $('[data-result-details]');
    list.replaceChildren();
    for (const [label, value] of details) {
      const row = document.createElement('div');
      const term = document.createElement('dt');
      const description = document.createElement('dd');
      term.textContent = label;
      description.textContent = value;
      row.append(term, description);
      list.append(row);
    }
    previewText = 'Maeve Arden — enquiry preview\n\n' + details.map(([label,value]) => `${label}: ${value}`).join('\n') + '\n\nPortfolio demo: no enquiry has been sent.';
    form.hidden = true;
    result.hidden = false;
    $('#result-title').focus({preventScroll:true});
    result.scrollIntoView({block:'start',behavior:'instant'});
  });
  $('[data-edit-enquiry]').addEventListener('click', () => {
    result.hidden = true;
    form.hidden = false;
    $('[data-copy-status]').textContent = '';
    setStep(2);
  });
  $('[data-copy-enquiry]').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(previewText);
      $('[data-copy-status]').textContent = 'Copied to your clipboard. Nothing has been sent.';
    } catch {
      $('[data-copy-status]').textContent = 'Your browser couldn’t copy this. You can select the preview text instead.';
    }
  });
})();
