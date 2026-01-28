// Əsas JavaScript funksionallığı

document.addEventListener('DOMContentLoaded', function() {
    // Mobil menyu funksionallığı
    const mobileMenu = document.getElementById('mobile-menu');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileMenu && navMenu) {
        mobileMenu.addEventListener('click', function() {
            const isExpanded = mobileMenu.getAttribute('aria-expanded') === 'true';
            
            mobileMenu.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Update aria-expanded attribute for accessibility
            mobileMenu.setAttribute('aria-expanded', !isExpanded);
        });

        // Menyu linklərini klikləyəndə menyunu bağla
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
                navMenu.classList.remove('active');
                mobileMenu.setAttribute('aria-expanded', 'false');
            });
        });

        // ESC düyməsi ilə menyunu bağla
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                mobileMenu.classList.remove('active');
                navMenu.classList.remove('active');
                mobileMenu.setAttribute('aria-expanded', 'false');
                mobileMenu.focus(); // Return focus to menu button
            }
        });
    }

    // Hamar sürüşmə
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Set focus to target element for accessibility
                targetElement.setAttribute('tabindex', '-1');
                targetElement.focus();
            }
        });
    });

    // Aktiv naviqasiya linkini vurğula (Django template already handles this with aria-current)
    const currentLocation = location.pathname;
    const menuItems = document.querySelectorAll('.nav-link');
    
    menuItems.forEach(item => {
        if (item.getAttribute('href') === currentLocation) {
            item.classList.add('active');
        }
    });
});

// Səhifə yüklənəndə animasiyalar
window.addEventListener('load', function() {
    // Fade-in animasiyası
    const elements = document.querySelectorAll('.service-card, .experience-item');
    elements.forEach((element, index) => {
        setTimeout(() => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            
            setTimeout(() => {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }, 100);
        }, index * 100);
    });
});