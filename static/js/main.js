/* ═══════════════════════════════════════════════
   CEYHAN NUR PORTFOLIO — Main JS
   ═══════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Mobile Menu ── */
  const toggle  = document.getElementById('mobile-menu');
  const navMenu = document.getElementById('nav-menu');

  if (toggle && navMenu) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      toggle.classList.toggle('active');
      navMenu.classList.toggle('active');
    });

    // Close on link click
    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });

    // Close on outside click
    document.addEventListener('click', e => {
      if (!navMenu.contains(e.target) && !toggle.contains(e.target)) {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.classList.remove('active');
        navMenu.classList.remove('active');
      }
    });

    // ESC key
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && navMenu.classList.contains('active')) {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.classList.remove('active');
        navMenu.classList.remove('active');
      }
    });
  }

  /* ── Navbar Scroll Effect ── */
  const navbar = document.querySelector('.navbar-header');
  if (navbar) {
    let lastY = 0;
    const onScroll = () => {
      const y = window.scrollY;
      if (y > 60) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
      // Hide on scroll down, show on scroll up
      if (y > lastY && y > 200) {
        navbar.style.transform = 'translateY(-100%)';
      } else {
        navbar.style.transform = 'translateY(0)';
      }
      lastY = y;
    };
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ── Scroll Animations (IntersectionObserver) ── */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll(
    '.service-card, .experience-item, .skill-category, .card, .medal-card, .restaurant-card, .show-card, .product-card'
  ).forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity 0.55s ease, transform 0.55s ease';
    io.observe(el);
  });

  /* ── Back to Top ── */
  const topBtn = document.createElement('button');
  topBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
  topBtn.setAttribute('aria-label', 'Yuxarıya qayıt');
  Object.assign(topBtn.style, {
    position:     'fixed',
    bottom:       '28px',
    right:        '28px',
    width:        '48px',
    height:       '48px',
    background:   'linear-gradient(135deg, #D4AF37, #F0D060)',
    color:        '#0D0D0D',
    border:       'none',
    borderRadius: '50%',
    cursor:       'pointer',
    fontSize:     '1rem',
    boxShadow:    '0 4px 20px rgba(212,175,55,0.45)',
    transform:    'translateY(80px)',
    transition:   'transform 0.35s ease, opacity 0.35s ease',
    zIndex:       '900',
    opacity:      '0',
    display:      'flex',
    alignItems:   'center',
    justifyContent:'center',
  });
  document.body.appendChild(topBtn);

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      topBtn.style.transform = 'translateY(0)';
      topBtn.style.opacity   = '1';
    } else {
      topBtn.style.transform = 'translateY(80px)';
      topBtn.style.opacity   = '0';
    }
  }, { passive: true });

  topBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ── Smooth anchor scroll ── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
      }
    });
  });

  /* ── Number counter animation ── */
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    const cio = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el  = entry.target;
          const end = parseInt(el.dataset.count, 10);
          const dur = 1800;
          const step = end / (dur / 16);
          let cur = 0;
          const tick = () => {
            cur = Math.min(cur + step, end);
            el.textContent = Math.round(cur);
            if (cur < end) requestAnimationFrame(tick);
          };
          requestAnimationFrame(tick);
          cio.unobserve(el);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(el => cio.observe(el));
  }

});
