// Əlaqə düyməsi funksionallığı

document.addEventListener('DOMContentLoaded', function() {
    const contactButtons = document.querySelectorAll('.contact-button');
    
    contactButtons.forEach(button => {
        // Klik izləmə və analitika
        button.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            const buttonText = this.textContent.trim();
            
            // Klik məlumatlarını qeyd et
            logContactInteraction('click', {
                buttonText: buttonText,
                href: href,
                timestamp: new Date().toISOString(),
                userAgent: navigator.userAgent,
                pageUrl: window.location.href
            });

            // Tel: link dəstəyini yoxla
            if (href && href.startsWith('tel:')) {
                handleTelLink(e, href, this);
            }
        });

        // Hover effekti və izləmə
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.02)';
            
            // Hover məlumatlarını qeyd et
            logContactInteraction('hover', {
                buttonText: this.textContent.trim(),
                timestamp: new Date().toISOString()
            });
        });

        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });

        // Focus və keyboard dəstəyi
        button.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });

        // Touch events for mobile
        button.addEventListener('touchstart', function() {
            this.style.transform = 'translateY(-1px) scale(1.01)';
        });

        button.addEventListener('touchend', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Tel: link idarəetməsi
function handleTelLink(event, href, button) {
    const phoneNumber = href.replace('tel:', '');
    const isMobile = detectMobileDevice();
    
    if (isMobile) {
        // Mobil cihazda - tel: linki işə sal
        console.log('Telefon zəngi başladılır:', href);
        logContactInteraction('call_initiated', {
            phoneNumber: phoneNumber,
            device: 'mobile'
        });
    } else {
        // Masaüstündə - zərif deqradasiya
        event.preventDefault();
        handleDesktopTelLink(phoneNumber, button);
    }
}

// Masaüstü üçün tel: link idarəetməsi
function handleDesktopTelLink(phoneNumber, button) {
    // Nömrəni clipboard-a kopyala
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(phoneNumber).then(() => {
            showNotification('Telefon nömrəsi kopyalandı: ' + phoneNumber, 'success');
            logContactInteraction('number_copied', { phoneNumber: phoneNumber });
        }).catch(() => {
            showFallbackDialog(phoneNumber);
        });
    } else {
        showFallbackDialog(phoneNumber);
    }
}

// Fallback dialog göstər
function showFallbackDialog(phoneNumber) {
    const dialog = createPhoneDialog(phoneNumber);
    document.body.appendChild(dialog);
    dialog.showModal();
    
    logContactInteraction('fallback_dialog_shown', { phoneNumber: phoneNumber });
}

// Telefon dialoqu yarat
function createPhoneDialog(phoneNumber) {
    const dialog = document.createElement('dialog');
    dialog.className = 'phone-dialog';
    dialog.innerHTML = `
        <div class="dialog-content">
            <h3>Əlaqə Məlumatı</h3>
            <p>Telefon nömrəsi:</p>
            <div class="phone-display">
                <span class="phone-number">${phoneNumber}</span>
                <button class="copy-btn" type="button" aria-label="Nömrəni kopyala">📋</button>
            </div>
            <div class="dialog-actions">
                <button class="dialog-close" type="button">Bağla</button>
            </div>
        </div>
    `;

    // Dialog stilləri
    dialog.style.cssText = `
        border: none;
        border-radius: 12px;
        padding: 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        max-width: 400px;
        width: 90%;
    `;

    // Event listeners
    const closeBtn = dialog.querySelector('.dialog-close');
    const copyBtn = dialog.querySelector('.copy-btn');

    closeBtn.addEventListener('click', () => {
        dialog.close();
        dialog.remove();
    });

    copyBtn.addEventListener('click', () => {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(phoneNumber).then(() => {
                showNotification('Nömrə kopyalandı!', 'success');
                dialog.close();
                dialog.remove();
            });
        } else {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = phoneNumber;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            showNotification('Nömrə kopyalandı!', 'success');
            dialog.close();
            dialog.remove();
        }
    });

    // ESC ilə bağla
    dialog.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            dialog.close();
            dialog.remove();
        }
    });

    return dialog;
}

// Mobil cihaz aşkarlanması
function detectMobileDevice() {
    const mobileRegex = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i;
    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    const isSmallScreen = window.innerWidth <= 768;
    
    return mobileRegex.test(navigator.userAgent) || (isTouchDevice && isSmallScreen);
}

// Əlaqə qarşılıqlı əlaqəsini qeyd et
function logContactInteraction(action, data) {
    const logEntry = {
        action: action,
        data: data,
        timestamp: new Date().toISOString()
    };
    
    // Console-da qeyd et (development üçün)
    console.log('Contact Interaction:', logEntry);
    
    // Local storage-da saxla (analytics üçün)
    try {
        const existingLogs = JSON.parse(localStorage.getItem('contactInteractions') || '[]');
        existingLogs.push(logEntry);
        
        // Son 100 qeydi saxla
        if (existingLogs.length > 100) {
            existingLogs.splice(0, existingLogs.length - 100);
        }
        
        localStorage.setItem('contactInteractions', JSON.stringify(existingLogs));
    } catch (error) {
        console.warn('Local storage-a yazma xətası:', error);
    }
    
    // Analytics service-ə göndər (gələcəkdə tətbiq ediləcək)
    // sendToAnalytics(logEntry);
}

// Bildiriş göstər (təkmilləşdirilmiş versiya)
function showNotification(message, type = 'info') {
    // Mövcud bildirişi sil
    const existingNotification = document.querySelector('.contact-notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    // Rəng sxemi
    const colors = {
        success: '#27ae60',
        error: '#e74c3c',
        warning: '#f39c12',
        info: '#3498db'
    };

    // Yeni bildiriş yarat
    const notification = document.createElement('div');
    notification.className = 'contact-notification';
    notification.setAttribute('role', 'alert');
    notification.setAttribute('aria-live', 'polite');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: ${colors[type] || colors.info};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 10000;
        font-weight: 500;
        max-width: 300px;
        word-wrap: break-word;
        animation: slideIn 0.3s ease;
        font-family: inherit;
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
            .phone-dialog .dialog-content {
                padding: 2rem;
                text-align: center;
            }
            .phone-dialog .phone-display {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 1rem;
                margin: 1rem 0;
                padding: 1rem;
                background-color: #f8f9fa;
                border-radius: 8px;
                border: 2px solid #e9ecef;
            }
            .phone-dialog .phone-number {
                font-size: 1.2rem;
                font-weight: bold;
                color: #2c3e50;
                font-family: monospace;
            }
            .phone-dialog .copy-btn {
                background: none;
                border: none;
                font-size: 1.2rem;
                cursor: pointer;
                padding: 0.5rem;
                border-radius: 4px;
                transition: background-color 0.2s;
            }
            .phone-dialog .copy-btn:hover {
                background-color: #e9ecef;
            }
            .phone-dialog .dialog-actions {
                margin-top: 1.5rem;
            }
            .phone-dialog .dialog-close {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 6px;
                cursor: pointer;
                font-size: 1rem;
                transition: background-color 0.2s;
            }
            .phone-dialog .dialog-close:hover {
                background-color: #2980b9;
            }
            .phone-dialog::backdrop {
                background-color: rgba(0, 0, 0, 0.5);
            }
        `;
        document.head.appendChild(style);
    }

    document.body.appendChild(notification);

    // 4 saniyə sonra bildirişi sil
    setTimeout(() => {
        if (notification.parentNode) {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }
    }, 4000);

    // Klik ilə bildirişi bağla
    notification.addEventListener('click', () => {
        if (notification.parentNode) {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 300);
        }
    });
}

// Analytics məlumatlarını əldə et (development və debugging üçün)
function getContactAnalytics() {
    try {
        const logs = JSON.parse(localStorage.getItem('contactInteractions') || '[]');
        const analytics = {
            totalInteractions: logs.length,
            clickCount: logs.filter(log => log.action === 'click').length,
            hoverCount: logs.filter(log => log.action === 'hover').length,
            callsInitiated: logs.filter(log => log.action === 'call_initiated').length,
            numbersCopied: logs.filter(log => log.action === 'number_copied').length,
            recentInteractions: logs.slice(-10)
        };
        return analytics;
    } catch (error) {
        console.warn('Analytics məlumatlarını oxuma xətası:', error);
        return null;
    }
}

// Global funksiya kimi təyin et (console-dan istifadə üçün)
window.getContactAnalytics = getContactAnalytics;