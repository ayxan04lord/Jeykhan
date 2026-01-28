// Əlaqə düyməsi funksionallığı

document.addEventListener('DOMContentLoaded', function() {
    const contactButtons = document.querySelectorAll('.contact-button');
    
    contactButtons.forEach(button => {
        // Klik izləmə
        button.addEventListener('click', function(e) {
            // Tel: link dəstəyini yoxla
            const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            const href = this.getAttribute('href');
            
            if (href && href.startsWith('tel:')) {
                // Mobil cihazlarda tel: linki işləyir
                if (isMobile) {
                    // Mobil cihazda - tel: linki işə sal
                    console.log('Telefon zəngi başladılır:', href);
                } else {
                    // Masaüstündə - istifadəçiyə məlumat ver
                    e.preventDefault();
                    const phoneNumber = href.replace('tel:', '');
                    
                    // Nömrəni clipboard-a kopyala
                    if (navigator.clipboard) {
                        navigator.clipboard.writeText(phoneNumber).then(() => {
                            showNotification('Telefon nömrəsi kopyalandı: ' + phoneNumber);
                        }).catch(() => {
                            showNotification('Telefon nömrəsi: ' + phoneNumber);
                        });
                    } else {
                        showNotification('Telefon nömrəsi: ' + phoneNumber);
                    }
                }
            }
        });

        // Hover effekti
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
        });

        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Bildiriş göstər
function showNotification(message) {
    // Mövcud bildirişi sil
    const existingNotification = document.querySelector('.contact-notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    // Yeni bildiriş yarat
    const notification = document.createElement('div');
    notification.className = 'contact-notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #27ae60;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 10000;
        font-weight: 500;
        max-width: 300px;
        word-wrap: break-word;
        animation: slideIn 0.3s ease;
    `;

    // CSS animasiyası əlavə et
    if (!document.querySelector('#notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            @keyframes slideOut {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(notification);

    // 3 saniyə sonra bildirişi sil
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}