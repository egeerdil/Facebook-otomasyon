# 🔧 Instagram İzinleri Görünmüyor - Sorun Giderme

İzinleri eklediniz ama Instagram hesabı hala görünmüyorsa:

## 🔍 Adım Adım Kontrol

### 1️⃣ Instagram Graph API Ürünü Eklendi mi?

**Kontrol:**
1. **Facebook Developers** > **App Dashboard**
2. Sol menüden **Products** bölümüne gidin
3. **"Instagram Graph API"** ürünü listede var mı?

**Eğer yoksa:**
1. **"+"** butonuna tıklayın
2. **"Instagram Graph API"** ürününü bulun
3. **"Set Up"** butonuna tıklayın
4. Kurulum adımlarını tamamlayın

### 2️⃣ Yeni Token Oluşturdunuz mu?

**ÖNEMLİ:** İzinleri ekledikten sonra **YENİ** token oluşturmanız gerekir!

**Adımlar:**
1. **Graph API Explorer**'a gidin: https://developers.facebook.com/tools/explorer/
2. App'inizi seçin
3. **"Get Token"** > **"Get User Access Token"**
4. **Permissions** sekmesine gidin
5. Şu izinlerin **seçili** olduğundan emin olun:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `instagram_basic`
   - `instagram_content_publish`
6. **"Generate Access Token"** butonuna tıklayın
7. Facebook'ta **TÜM izinleri verin**
8. Yeni token'ı kopyalayın
9. `/me/accounts` ile **YENİ** Page Token alın

### 3️⃣ Token'da İzinleri Kontrol Edin

**Test:**
1. Graph API Explorer'da **YENİ** Page Token'ı kullanın
2. Endpoint: `GET /me/accounts?fields=instagram_business_account`
3. Submit'e tıklayın
4. `instagram_business_account` görünüyor mu?

**Eğer görünmüyorsa:**
- Token'da izinler eksik olabilir
- Yeni token oluşturun ve tüm izinleri seçin

### 4️⃣ App Review Gerekli mi?

**Kontrol:**
1. **App Dashboard** > **App Review** > **Permissions and Features**
2. `instagram_content_publish` iznini bulun
3. Durum ne? (Available / Requires Review / Approved)

**Eğer "Requires Review" ise:**
- App Review başvurusu yapmanız gerekir
- Bu birkaç gün sürebilir
- Onaylanana kadar Test Mode'da çalışabilirsiniz

### 5️⃣ Test Mode vs Live Mode

**Kontrol:**
1. **App Dashboard** > **Settings** > **Basic**
2. **App Mode** nedir? (Development / Live)

**Eğer Development Mode ise:**
- Sadece test kullanıcıları post atabilir
- Live Mode'a geçmek için App Review gerekir

## 🚀 Hızlı Çözüm

### Yöntem 1: Sıfırdan Token Oluşturma

1. **Graph API Explorer**'da eski token'ı temizleyin
2. **"Get Token"** > **"Get User Access Token"**
3. **Permissions** sekmesinde **TÜM izinleri seçin:**
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `instagram_basic`
   - `instagram_content_publish`
4. **"Generate Access Token"** butonuna tıklayın
5. Facebook'ta **TÜM izinleri verin**
6. Token'ı kopyalayın
7. `/me/accounts` ile Page Token alın
8. Tekrar test edin

### Yöntem 2: Direkt Page ID ile Test

1. Page ID'nizi biliyorsanız:
2. Endpoint: `GET /{PAGE_ID}?fields=instagram_business_account`
3. `{PAGE_ID}` yerine sayfa ID'nizi yazın
4. Page Token kullanın
5. Submit'e tıklayın

## ⚠️ Yaygın Hatalar

### Hata 1: "instagram_business_account" görünmüyor
**Neden:**
- Token'da `instagram_basic` izni yok
- Instagram Graph API ürünü eklenmemiş
- Token eski (yeni token oluşturun)

**Çözüm:**
- Yeni token oluşturun
- Tüm izinleri seçin
- Instagram Graph API ürününü ekleyin

### Hata 2: "Permission denied"
**Neden:**
- `instagram_content_publish` izni App Review'den geçmemiş
- Test Mode'da çalışıyorsunuz

**Çözüm:**
- App Review başvurusu yapın
- Veya Test Mode'da test kullanıcıları ile test edin

### Hata 3: "Instagram Graph API not enabled"
**Neden:**
- Instagram Graph API ürünü app'e eklenmemiş

**Çözüm:**
- Products bölümünden Instagram Graph API'yi ekleyin

## ✅ Başarı Kontrolü

Instagram Account ID'yi bulduktan sonra:

1. **GitHub Secret ekleyin:**
   - Name: `INSTAGRAM_ACCOUNT_ID`
   - Value: Instagram Account ID

2. **Test edin:**
   - GitHub Actions'tan workflow'u çalıştırın
   - Logları kontrol edin
   - Instagram'da post görünüyor mu?

## 📞 Hala Çalışmıyor mu?

Şunları kontrol edin:
1. ✅ Instagram Graph API ürünü eklendi mi?
2. ✅ Yeni token oluşturdunuz mu?
3. ✅ Token'da tüm izinler var mı?
4. ✅ Instagram hesabı Business Account mı?
5. ✅ Instagram hesabı Facebook sayfasına bağlı mı?

---

**Özet:** İzinleri ekledikten sonra **MUTLAKA yeni token oluşturun**! Eski token'da yeni izinler olmaz! 🔐
