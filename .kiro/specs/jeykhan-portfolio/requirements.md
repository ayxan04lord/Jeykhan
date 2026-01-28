# Requirements Document

## Introduction

Jeykhan layihəsi - restoran idarəçiliyi və musiqi təlimi sahələrində təcrübəli mütəxəssis üçün şəxsi portfel saytıdır. Sayt onun peşəkar təcrübəsini və xidmətlərini təqdim edəcək, müştərilərlə əlaqə qurmaq imkanı yaradacaq.

## Glossary

- **System**: Jeykhan portfel saytı
- **User**: Saytı ziyarət edən şəxs
- **Contact_Button**: Ana səhifədəki əlaqə düyməsi
- **Service_Section**: Xidmətlərin təqdim olunduğu bölmə
- **Portfolio_Content**: Təcrübə və nailiyyətlərin göstərildiyi məzmun

## Requirements

### Requirement 1: Ana Səhifə və Əlaqə Funksionallığı

**User Story:** Ziyarətçi kimi, ana səhifədə əlaqə qurmaq istədiyimdə, asanlıqla telefon edə bilməliyəm.

#### Acceptance Criteria

1. THE System SHALL display a prominent contact button on the homepage
2. WHEN a user clicks the contact button, THE System SHALL initiate a phone call to the specified number
3. THE System SHALL ensure the contact button is easily visible and accessible on all device types
4. THE System SHALL display the phone number clearly for users who prefer manual dialing

### Requirement 2: Xidmətlərin Təqdimatı

**User Story:** Ziyarətçi kimi, təklif olunan xidmətlər haqqında məlumat almaq istəyirəm ki, hansı sahələrdə kömək ala biləcəyimi başa düşüm.

#### Acceptance Criteria

1. THE System SHALL display two main service categories: restaurant management and music training
2. WHEN displaying restaurant management services, THE System SHALL include culinary consulting information
3. WHEN displaying music training services, THE System SHALL include singer development information
4. THE System SHALL provide detailed descriptions for each service category
5. THE System SHALL organize service information in a clear and professional manner

### Requirement 3: Şəxsi Portfel Təqdimatı

**User Story:** Ziyarətçi kimi, mütəxəssisin təcrübəsi və keyfiyyəti haqqında məlumat almaq istəyirəm ki, onun xidmətlərindən istifadə etmək qərarını verə bilim.

#### Acceptance Criteria

1. THE System SHALL display professional background information about the specialist
2. THE System SHALL showcase experience in both restaurant management and music training fields
3. THE System SHALL present the information in a credible and professional manner
4. THE System SHALL highlight key achievements and expertise areas
5. THE System SHALL maintain a personal yet professional tone throughout the content

### Requirement 4: Responsiv Dizayn və İstifadəçi Təcrübəsi

**User Story:** İstifadəçi kimi, saytı müxtəlif cihazlarda (telefon, planşet, kompüter) rahat istifadə edə bilməliyəm.

#### Acceptance Criteria

1. THE System SHALL display correctly on mobile devices, tablets, and desktop computers
2. THE System SHALL maintain readability and functionality across all screen sizes
3. THE System SHALL ensure fast loading times for optimal user experience
4. THE System SHALL provide intuitive navigation between different sections
5. THE System SHALL use appropriate fonts and colors for professional appearance

### Requirement 5: Texniki Tələblər və Performans

**User Story:** Sistem administratoru kimi, saytın texniki tələblərə uyğun işləməsini və yaxşı performans göstərməsini istəyirəm.

#### Acceptance Criteria

1. THE System SHALL be built using HTML, CSS, and JavaScript for the frontend
2. THE System SHALL use Django framework for the backend
3. THE System SHALL load pages within 3 seconds on standard internet connections
4. THE System SHALL be compatible with modern web browsers
5. THE System SHALL implement proper SEO practices for better search visibility

### Requirement 6: Məzmun İdarəetməsi

**User Story:** Sayt sahibi kimi, məzmunu asanlıqla yeniləyə və idarə edə bilməliyəm.

#### Acceptance Criteria

1. THE System SHALL provide an admin interface for content management
2. WHEN updating service information, THE System SHALL reflect changes immediately on the frontend
3. THE System SHALL allow easy modification of contact information
4. THE System SHALL support image uploads for portfolio content
5. THE System SHALL maintain data integrity during content updates
