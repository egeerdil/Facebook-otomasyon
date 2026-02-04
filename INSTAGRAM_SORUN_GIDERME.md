# 🔧 Instagram Sorun Giderme

Instagram hesabınız görünmüyorsa, şu adımları takip edin:

## ❌ Sorun: Instagram Hesabı Görünmüyor

### 1️⃣ Instagram Hesabı Bağlı mı?

**Kontrol:**
1. Facebook sayfanıza gidin
2. **Ayarlar** (Settings) > **Instagram** bölümüne gidin
3. Instagram hesabınız bağlı mı kontrol edin

**Çözüm - Bağlama:**
1. **"Connect Account"** veya **"Bağla"** butonuna tıklayın
2. Instagram hesabınızla giriş yapın
3. İzinleri verin
4. Hesap bağlandıktan sonra tekrar kontrol edin

### 2️⃣ Instagram Hesap Türü

**Kontrol:**
- Instagram hesabınız **Business Account** veya **Creator Account** olmalı
- Kişisel hesap (Personal Account) çalışmaz!

**Çözüm - Business Account'a Geçirme:**
1. Instagram App'i açın
2. **Profil** > **Menü** (☰) > **Ayarlar**
3. **Hesap Türü** veya **Account Type** seçeneğine gidin
4. **"Switch to Business Account"** veya **"Business Account'a Geç"** seçeneğini seçin
5. Facebook sayfanızı bağlayın
6. İşletme bilgilerinizi doldurun (opsiyonel)

### 3️⃣ Graph API Explorer'da Kontrol

**Adım 1: Page Access Token Kontrolü**
1. Graph API Explorer'a gidin: https://developers.facebook.com/tools/explorer/
2. App'inizi seçin
3. Page Access Token'ınızı Access Token alanına yapıştırın

**Adım 2: Instagram Account ID'yi Bul**
1. Endpoint: `GET /me/accounts`
2. Submit'e tıklayın
3. Sonuçta `instagram_business_account` görünüyor mu?

**Eğer görünmüyorsa:**
- Endpoint'i değiştirin: `GET /{PAGE_ID}?fields=instagram_business_account`
- `{PAGE_ID}` yerine sayfa ID'nizi yazın
- Submit'e tıklayın

### 4️⃣ Alternatif: Facebook Business Suite

1. **Facebook Business Suite**'e gidin: https://business.facebook.com
2. Sayfanızı seçin
3. Sol menüden **Instagram** sekmesine tıklayın
4. Instagram hesabınız görünüyor mu?

**Eğer görünmüyorsa:**
- **"Connect Instagram Account"** butonuna tıklayın
- Instagram hesabınızla giriş yapın

### 5️⃣ Token İzinleri Kontrolü

Page Access Token'ınızın gerekli izinlere sahip olduğundan emin olun:

**Gerekli İzinler:**
- `pages_show_list`
- `pages_read_engagement`
- `instagram_basic`
- `instagram_content_publish` (post atmak için)

**Kontrol:**
1. Graph API Explorer'da **"Get Token"** > **"Get User Access Token"**
2. İzinleri kontrol edin
3. Eksik izinler varsa ekleyin
4. Yeni token oluşturun

## ✅ Başarılı Kurulum Kontrolü

Instagram Account ID'yi bulduktan sonra:

1. **GitHub Secret ekleyin:**
   - Name: `INSTAGRAM_ACCOUNT_ID`
   - Value: Instagram Account ID'niz

2. **Test edin:**
   - GitHub Actions'tan workflow'u çalıştırın
   - Logları kontrol edin
   - Instagram'da post görünüyor mu?

## 🆘 Hala Çalışmıyor mu?

### Hata: "Instagram Account ID bulunamadı"
**Çözüm:**
- Instagram hesabınızın Business Account olduğundan emin olun
- Facebook sayfanıza bağlı olduğundan emin olun
- Token'ın geçerli olduğundan emin olun

### Hata: "Container oluşturulamadı"
**Çözüm:**
- Instagram hesabınızın Business Account olduğundan emin olun
- Facebook sayfanıza bağlı olduğundan emin olun
- Token'ın `instagram_content_publish` iznine sahip olduğundan emin olun

### Hata: "Invalid Instagram Account ID"
**Çözüm:**
- Instagram Account ID'nin doğru olduğundan emin olun
- ID'nin sadece sayılardan oluştuğundan emin olun (harf yok)
- Graph API Explorer'dan tekrar kontrol edin

## 📚 Yardımcı Kaynaklar

- [Instagram Business Account Kurulumu](https://www.facebook.com/business/help/898752960195806)
- [Instagram Graph API Dokümantasyonu](https://developers.facebook.com/docs/instagram-api)
- [Facebook Business Suite](https://business.facebook.com)

---

**Not:** Instagram entegrasyonu için Instagram hesabınızın mutlaka Business Account olması ve Facebook sayfanıza bağlı olması gerekir! 📱
