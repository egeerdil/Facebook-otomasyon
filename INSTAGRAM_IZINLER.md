# 🔐 Instagram için Gerekli İzinler (Permissions)

Instagram'a post atmak için bazı özel izinlere ihtiyacınız var!

## 📋 Gerekli İzinler

### 1️⃣ Facebook App İzinleri

Facebook App'inizde şu izinler olmalı:

#### Temel İzinler:
- ✅ `pages_show_list` - Sayfaları listelemek için
- ✅ `pages_read_engagement` - Sayfa bilgilerini okumak için
- ✅ `pages_manage_posts` - Facebook'a post atmak için

#### Instagram İzinleri:
- ✅ `instagram_basic` - Instagram hesap bilgilerini okumak için
- ✅ `instagram_content_publish` - Instagram'a post atmak için (EN ÖNEMLİSİ!)

### 2️⃣ İzinleri Kontrol Etme

#### Adım 1: Facebook App Ayarları

1. **Facebook Developers**'a gidin: https://developers.facebook.com/
2. App'inizi seçin
3. **Settings** > **Basic** bölümüne gidin
4. **App ID** ve **App Secret** değerlerini not edin

#### Adım 2: İzinleri Kontrol Etme

1. **App Dashboard**'da **Products** bölümüne gidin
2. **Instagram Graph API** ürününü ekleyin (yoksa)
3. **Permissions** bölümüne gidin
4. Şu izinlerin ekli olduğundan emin olun:
   - `instagram_basic`
   - `instagram_content_publish`

#### Adım 3: Token'da İzinleri Kontrol Etme

1. **Graph API Explorer**'a gidin: https://developers.facebook.com/tools/explorer/
2. App'inizi seçin
3. **"Get Token"** > **"Get User Access Token"**
4. **Permissions** sekmesine gidin
5. Şu izinlerin seçili olduğundan emin olun:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `instagram_basic`
   - `instagram_content_publish`

### 3️⃣ İzinleri Ekleme

#### Eğer İzinler Yoksa:

1. **Graph API Explorer**'da **"Get Token"** butonuna tıklayın
2. **"Get User Access Token"** seçin
3. **Permissions** sekmesine gidin
4. Eksik izinleri seçin:
   - `pages_show_list`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `instagram_basic`
   - `instagram_content_publish`
5. **"Generate Access Token"** butonuna tıklayın
6. Facebook'ta izinleri verin
7. Token'ı kopyalayın
8. `/me/accounts` ile Page Token'ı alın

### 4️⃣ Instagram Graph API Ürününü Ekleme

Eğer Instagram Graph API ürünü yoksa:

1. **Facebook Developers** > **App Dashboard**
2. **Products** bölümüne gidin
3. **"+"** butonuna tıklayın
4. **"Instagram Graph API"** ürününü bulun
5. **"Set Up"** butonuna tıklayın
6. Kurulum adımlarını takip edin

## ⚠️ Önemli Notlar

### İzin Onayı

Bazı izinler (özellikle `instagram_content_publish`) **App Review** gerektirebilir:

1. **App Review** için:
   - **App Dashboard** > **App Review** > **Permissions and Features**
   - `instagram_content_publish` iznini bulun
   - **"Request"** butonuna tıklayın
   - Gerekli bilgileri doldurun
   - Meta'nın onayını bekleyin (birkaç gün sürebilir)

2. **Test Modu:**
   - App Review onaylanana kadar **Test Mode**'da çalışabilirsiniz
   - Test Mode'da sadece test kullanıcıları post atabilir

### Token Süresi

- **User Token:** 1-2 saat geçerli
- **Page Token:** 60 gün geçerli (uzun süreli token)
- **Uzun süreli token:** Token'ı 60 güne kadar uzatabilirsiniz

## 🔍 İzinleri Test Etme

### Test 1: Instagram Account ID Bulma

1. Graph API Explorer'da Page Token ile
2. `GET /me/accounts` endpoint'ini çağırın
3. `instagram_business_account` görünüyorsa → İzinler çalışıyor ✅

### Test 2: Instagram Post Atma

1. GitHub Actions'tan workflow'u çalıştırın
2. Logları kontrol edin
3. Başarılı olursa → İzinler tamam ✅

## 🆘 Sorun Giderme

### Hata: "Insufficient permissions"
**Çözüm:**
- Token'da gerekli izinlerin olduğundan emin olun
- Yeni token oluşturun ve tüm izinleri seçin

### Hata: "Permission not granted"
**Çözüm:**
- Facebook App'te izinlerin ekli olduğundan emin olun
- App Review'den geçmeniz gerekebilir

### Hata: "Instagram Graph API not enabled"
**Çözüm:**
- Facebook App'e Instagram Graph API ürününü ekleyin
- Products bölümünden ekleyebilirsiniz

## 📚 Kaynaklar

- [Instagram Graph API Permissions](https://developers.facebook.com/docs/instagram-api/overview#permissions)
- [Facebook App Review](https://developers.facebook.com/docs/app-review)
- [Instagram Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing)

---

**Özet:** Instagram'a post atmak için `instagram_content_publish` izni en önemlisi! Bu izin App Review gerektirebilir. 🔐
