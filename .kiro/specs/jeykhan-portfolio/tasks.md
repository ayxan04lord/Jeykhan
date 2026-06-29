# İcra Planı: Jeykhan Portfel Saytı

## Ümumi Məlumat

Bu icra planı restoran idarəçiliyi və musiqi təlimi sahələrində təcrübəni nümayiş etdirən peşəkar Django əsaslı portfel saytı yaradır. Yanaşma Django-nun MVT arxitekturasına, responsiv dizayna və əlaqə funksionallığının önə çıxarılmasına fokuslanır.

## Tapşırıqlar

- [x] 1. Django layihə strukturunu və əsas konfiqurasiyanı qur
  - Django layihəsi və portfel tətbiqini yarat
  - Static fayllar və verilənlər bazası üçün settings.py-ni konfiqurasiya et
  - URL marşrutlaşdırma strukturunu qur
  - Şablonlar və static fayllar üçün qovluq strukturunu yarat
  - _Tələblər: 5.1, 5.2_

- [x] 2. Məlumat modellərini və admin interfeysi yarat
  - [x] 2.1 Service, Experience və ContactInfo modellərini tətbiq et
    - Düzgün validasiya ilə model sahələrini təyin et
    - String təqdimatları və sıralama əlavə et
    - _Tələblər: 2.1, 2.2, 2.3, 3.1, 3.2_
  - [ ]\* 2.2 Məlumat modelləri üçün xassə testi yaz
    - **Xassə 6: Məzmun İdarəetməsi Bütövlüyü**
    - **Təsdiq edir: Tələblər 6.2, 6.4, 6.5**
  - [x] 2.3 Django admin interfeysi konfiqurasiya et
    - Modelləri admin interfeysi ilə qeydiyyatdan keçir
    - Admin formalarını və siyahı göstərilməsini fərdiləşdir
    - _Tələblər: 6.1, 6.3_

- [x] 3. Əsas görünüşləri və URL marşrutlaşdırmasını tətbiq et
  - [x] 3.1 Ana səhifə, xidmətlər və haqqında görünüşlərini yarat
    - Düzgün kontekst məlumatları ilə görünüş funksiyalarını tətbiq et
    - Dinamik məzmun üçün verilənlər bazası sorğularını idarə et
    - _Tələblər: 1.1, 2.1, 3.1_
  - [x] 3.2 URL nümunələrini konfiqurasiya et
    - Bütün görünüşlər üçün URL marşrutlaşdırmasını qur
    - Tətbiq URL-lərini əsas layihəyə daxil et
    - _Tələblər: 4.4_

- [x] 4. Əsas şablon və responsiv tərtibat yarat
  - [x] 4.1 Responsiv framework ilə base.html şablonu qur
    - Düzgün meta teqləri ilə HTML5 strukturu yarat
    - CSS və JavaScript istinadlarını daxil et
    - Naviqasiya strukturunu əlavə et
    - _Tələblər: 4.1, 4.2, 5.5_
  - [ ]\* 4.2 Responsiv dizayn üçün xassə testi yaz
    - **Xassə 3: Responsiv Dizayn Ardıcıllığı**
    - **Təsdiq edir: Tələblər 4.1, 4.2**

- [x] 5. Əlaqə funksionallığını tətbiq et
  - [x] 5.1 Tel: linki ilə əlaqə düyməsi komponenti yarat
    - Təkrar istifadə edilə bilən əlaqə düyməsi şablonu qur
    - Düzgün telefon nömrəsi formatlaşdırması ilə tel: linki tətbiq et
    - Masaüstü istifadəçiləri üçün ehtiyat göstəriş əlavə et
    - _Tələblər: 1.1, 1.2, 1.4_
  - [ ]\* 5.2 Əlaqə düyməsi funksionallığı üçün xassə testi yaz
    - **Xassə 1: Əlaqə Düyməsi Funksionallığı**
    - **Təsdiq edir: Tələblər 1.2, 1.3**

- [x] 6. Səhifə şablonlarını və məzmun göstərilməsini qur
  - [x] 6.1 Ana səhifə şablonu yarat
    - Önə çıxan əlaqə düyməsi ilə qəhrəman bölməsini dizayn et
    - Seçilmiş xidmətləri və təcrübə vurğularını göstər
    - _Tələblər: 1.1, 1.3, 3.4_
  - [x] 6.2 Xidmətlər səhifəsi şablonu yarat
    - Kateqoriyaya görə təşkil edilmiş xidmətləri göstər
    - Hər xidmət kateqoriyası üçün ətraflı təsvirləri göstər
    - _Tələblər: 2.1, 2.2, 2.3, 2.4_
  - [x] 6.3 Haqqında səhifəsi şablonu yarat
    - Peşəkar keçmiş və təcrübəni nümayiş etdir
    - Hər iki sahədə ekspertliyi vurğula
    - _Tələblər: 3.1, 3.2, 3.4_

- [x] 7. CSS stilləşdirməsi və responsiv dizaynı tətbiq et
  - [x] 7.1 Əsas stillər ilə main.css yarat
    - Tipoqrafiya, rənglər və tərtibat stillərini təyin et
    - Peşəkar dizayn sistemini tətbiq et
    - _Tələblər: 4.5_
  - [x] 7.2 Media sorğuları ilə responsive.css yarat
    - Mobil-ilk responsiv kəsim nöqtələrini əlavə et
    - Bütün cihazlarda əlaqə düyməsinin görünməsini təmin et
    - _Tələblər: 4.1, 4.2, 1.3_
  - [x] 7.3 Təkrar istifadə edilə bilən elementlər üçün components.css yarat
    - Xidmət kartları və təcrübə bölmələrini stilləşdir
    - Əlaqə düyməsi və naviqasiya elementlərini dizayn et
    - _Tələblər: 2.5_

- [x] 8. JavaScript funksionallığı və təkmilləşdirmələr əlavə et
  - [x] 8.1 Əsas qarşılıqlı əlaqələr üçün main.js yarat
    - Hamar sürüşmə və naviqasiya təkmilləşdirmələri əlavə et
    - Mobil menyu funksionallığını tətbiq et
    - _Tələblər: 4.4_
  - [x] 8.2 Əlaqə düyməsi davranışı üçün contact.js yarat
    - Klik izləmə və istifadəçi rəyini əlavə et
    - Tel: linklər üçün zərif deqradasiya tətbiq et
    - _Tələblər: 1.2_

- [ ] 9. Nəzarət nöqtəsi - Bütün testlərin keçməsini təmin et
  - Bütün testlərin keçməsini təmin et, suallar yaranarsa istifadəçidən soruş.

- [ ] 10. SEO optimallaşdırması və performansı tətbiq et
  - [ ] 10.1 SEO meta teqləri və strukturlaşdırılmış məlumat əlavə et
    - Düzgün meta təsvirləri və başlıqları tətbiq et
    - Open Graph və Twitter Card teqlərini əlavə et
    - Biznes məlumatları üçün strukturlaşdırılmış məlumat daxil et
    - _Tələblər: 5.5_
  - [ ]\* 10.2 SEO tətbiqi üçün xassə testi yaz
    - **Xassə 5: SEO Tətbiqi**
    - **Təsdiq edir: Tələblər 5.5**
  - [ ] 10.3 Static faylları və performansı optimallaşdır
    - CSS və JavaScript fayllarını minimallaşdır
    - Şəkilləri optimallaşdır və tənbəl yükləmə tətbiq et
    - _Tələblər: 4.3, 5.3_
  - [ ]\* 10.4 Performans standartları üçün xassə testi yaz
    - **Xassə 4: Performans və Uyğunluq Standartları**
    - **Təsdiq edir: Tələblər 5.3, 5.4**

- [ ] 11. Nümunə məzmun və məlumat miqrasiyası yarat
  - [ ] 11.1 Nümunə məzmun ilə məlumat fiksturları yarat
    - Hər iki kateqoriya üçün nümunə xidmətlər əlavə et
    - Peşəkar təcrübə qeydlərini daxil et
    - Əlaqə məlumatlarını qur
    - _Tələblər: 2.1, 2.2, 2.3, 3.1, 3.2_
  - [ ]\* 11.2 Xidmət təsvirləri üçün xassə testi yaz
    - **Xassə 2: Xidmət Təsviri Tamlığı**
    - **Təsdiq edir: Tələblər 2.4**

- [ ] 12. Son inteqrasiya və test
  - [ ] 12.1 Bütün komponentləri bir araya gətir
    - Görünüşləri, şablonları və static faylları birləşdir
    - Bütün naviqasiya və funksionallığı test et
    - _Tələblər: 4.4_
  - [ ]\* 12.2 Tam iş axınları üçün inteqrasiya testləri yaz
    - Başdan-sona istifadəçi səyahətlərini test et
    - Admin interfeysi funksionallığını yoxla
    - _Tələblər: 6.1, 6.2, 6.3_

- [ ] 13. Son nəzarət nöqtəsi - Bütün testlərin keçməsini təmin et
  - Bütün testlərin keçməsini təmin et, suallar yaranarsa istifadəçidən soruş.

## Qeydlər

- `*` ilə işarələnmiş tapşırıqlar ixtiyaridir və daha sürətli MVP üçün keçilə bilər
- Hər tapşırıq izlənə bilmək üçün xüsusi tələblərə istinad edir
- Nəzarət nöqtələri artımlı validasiyanı təmin edir
- Xassə testləri Hypothesis istifadə edərək universal düzgünlük xassələrini yoxlayır
- Vahid testlər xüsusi nümunələri və kənar halları yoxlayır
- Django admin interfeysi məzmun idarəetməsi imkanları təmin edir
- Tel: linklər mobil cihazlardan birbaşa telefon zəngi etməyə imkan verir
