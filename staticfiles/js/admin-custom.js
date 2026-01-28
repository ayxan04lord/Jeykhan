// Jeykhan Portfolio Admin Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Jeykhan Portfolio Admin loaded');
    
    // Add custom styling to status fields
    addStatusStyling();
    
    // Add category badges
    addCategoryBadges();
    
    // Enhanced form validation
    enhanceFormValidation();
    
    // Add tooltips
    addTooltips();
});

function addStatusStyling() {
    // Style active/inactive status in list views
    const statusCells = document.querySelectorAll('td');
    statusCells.forEach(cell => {
        if (cell.textContent.trim() === 'True' || cell.textContent.trim() === '✓') {
            cell.classList.add('status-active');
            cell.innerHTML = '<span class="status-active">✓ Aktiv</span>';
        } else if (cell.textContent.trim() === 'False' || cell.textContent.trim() === '✗') {
            cell.classList.add('status-inactive');
            cell.innerHTML = '<span class="status-inactive">✗ Qeyri-aktiv</span>';
        }
    });
}

function addCategoryBadges() {
    // Add styled badges for categories
    const categoryCells = document.querySelectorAll('td');
    categoryCells.forEach(cell => {
        const text = cell.textContent.trim();
        if (text === 'Restaurant Management' || text === 'restaurant') {
            cell.innerHTML = '<span class="category-restaurant">🍽️ Restoran</span>';
        } else if (text === 'Music Training' || text === 'music') {
            cell.innerHTML = '<span class="category-music">🎵 Musiqi</span>';
        }
    });
}

function enhanceFormValidation() {
    // Add real-time validation for phone numbers
    const phoneFields = document.querySelectorAll('input[name*="phone"]');
    phoneFields.forEach(field => {
        field.addEventListener('input', function() {
            const phoneRegex = /^\+?1?\d{9,15}$/;
            const isValid = phoneRegex.test(this.value);
            
            if (this.value && !isValid) {
                this.style.borderColor = '#e74c3c';
                showValidationMessage(this, 'Telefon nömrəsi formatı: +994501234567');
            } else {
                this.style.borderColor = '#27ae60';
                hideValidationMessage(this);
            }
        });
    });
    
    // Add validation for years of experience
    const yearsFields = document.querySelectorAll('input[name*="years_experience"]');
    yearsFields.forEach(field => {
        field.addEventListener('input', function() {
            const years = parseInt(this.value);
            if (years && (years < 0 || years > 50)) {
                this.style.borderColor = '#e74c3c';
                showValidationMessage(this, 'Təcrübə ili 0-50 arasında olmalıdır');
            } else {
                this.style.borderColor = '#27ae60';
                hideValidationMessage(this);
            }
        });
    });
}

function showValidationMessage(field, message) {
    // Remove existing message
    hideValidationMessage(field);
    
    // Create new message
    const messageDiv = document.createElement('div');
    messageDiv.className = 'validation-message';
    messageDiv.style.cssText = `
        color: #e74c3c;
        font-size: 0.8rem;
        margin-top: 4px;
        padding: 4px 8px;
        background-color: rgba(231, 76, 60, 0.1);
        border-radius: 4px;
        border-left: 3px solid #e74c3c;
    `;
    messageDiv.textContent = message;
    
    field.parentNode.appendChild(messageDiv);
}

function hideValidationMessage(field) {
    const existingMessage = field.parentNode.querySelector('.validation-message');
    if (existingMessage) {
        existingMessage.remove();
    }
}

function addTooltips() {
    // Add helpful tooltips to form fields
    const tooltips = {
        'icon': 'CSS class adı (məsələn: fas fa-utensils)',
        'order': 'Göstəriş sırası (kiçik rəqəmlər əvvəl göstərilir)',
        'is_featured': 'Ana səhifədə göstərilsin',
        'is_active': 'Saytda göstərilsin'
    };
    
    Object.keys(tooltips).forEach(fieldName => {
        const field = document.querySelector(`input[name*="${fieldName}"], select[name*="${fieldName}"]`);
        if (field) {
            field.title = tooltips[fieldName];
            field.setAttribute('data-tooltip', tooltips[fieldName]);
        }
    });
}

// Add smooth transitions to admin elements
function addSmoothTransitions() {
    const style = document.createElement('style');
    style.textContent = `
        .unfold-table tr,
        .unfold-btn,
        .unfold-form-field input,
        .unfold-form-field select,
        .unfold-form-field textarea {
            transition: all 0.2s ease;
        }
    `;
    document.head.appendChild(style);
}

// Initialize smooth transitions
addSmoothTransitions();