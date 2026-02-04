# 📸 Instagram Entegrasyonu

Facebook postlarınızı aynı anda Instagram'a da paylaşabilirsiniz!

## 🎯 Nasıl Çalışır?

- Facebook'a post atılırken, aynı anda Instagram'a da post atılır
- Aynı mesaj ve fotoğraf her iki platformda da paylaşılır
- Instagram için fotoğraf zorunludur

## 📋 Kurulum

### 1️⃣ Instagram Business Account Gereksinimleri

Instagram'a post atmak için:
- ✅ Instagram Business Account veya Creator Account olmalı
- ✅ Facebook sayfanıza bağlı olmalı
- ✅ Instagram Graph API erişimi olmalı

### 2️⃣ Instagram Account ID Bulma

#### Yöntem 1: Graph API Explorer (Önerilen)

1. **Facebook Graph API Explorer**'a gidin: https://developers.facebook.com/tools/explorer/
2. App'inizi seçin
3. Page Access Token'ınızı Access Token alanına yapıştırın
4. Endpoint'i şu şekilde değiştirin: `GET /me/accounts`
5. **"Submit"** butonuna tıklayın
6. Sonuçta şunu göreceksiniz:
   ```json
   {
     "data": [
       {
         "id": "PAGE_ID",
         "name": "Sayfa Adı",
         "instagram_business_account": {
           "id": "INSTAGRAM_ACCOUNT_ID"
         }
       }
     ]
   }
   ```
7. **`instagram_business_account.id`** değerini kopyalayın

**⚠️ Eğer `instagram_business_account` görünmüyorsa:**
- Instagram hesabınız Facebook sayfanıza bağlı değil olabilir
- Aşağıdaki "Instagram Hesabını Bağlama" bölümüne bakın

#### Yöntem 2: Facebook Sayfa Ayarları

1. Facebook sayfanıza gidin
2. **Ayarlar** (Settings) sekmesine tıklayın
3. Sol menüden **Instagram** bölümüne gidin
4. Instagram hesabınızın ID'sini görebilirsiniz

#### Yöntem 3: Instagram Business Account Kontrolü

1. **Facebook Business Suite**'e gidin: https://business.facebook.com
2. Sayfanızı seçin
3. Sol menüden **Instagram** sekmesine tıklayın
4. Instagram hesabınızın ID'sini görebilirsiniz

#### Yöntem 4: Direkt API Çağrısı

Eğer Page ID'nizi biliyorsanız:

1. Graph API Explorer'da endpoint: `GET /{PAGE_ID}?fields=instagram_business_account`
2. Page Access Token'ınızı kullanın
3. Submit'e tıklayın
4. `instagram_business_account.id` değerini kopyalayın

### 🔗 Instagram Hesabını Facebook Sayfasına Bağlama

Eğer Instagram hesabınız görünmüyorsa:

1. **Facebook sayfanıza gidin**
2. **Ayarlar** (Settings) > **Instagram** bölümüne gidin
3. **"Connect Account"** veya **"Bağla"** butonuna tıklayın
4. Instagram hesabınızla giriş yapın
5. İzinleri verin
6. Hesap bağlandıktan sonra Graph API Explorer'da tekrar kontrol edin

**ÖNEMLİ:** 
- Instagram hesabınız **Business Account** veya **Creator Account** olmalı
- Kişisel hesap (Personal Account) çalışmaz!
- Instagram hesabınızı Business Account'a çevirmek için: Instagram App > Ayarlar > Hesap Türü > Business Account'a Geç

### 3️⃣ GitHub Secret Ekleyin

1. GitHub repository'nize gidin
2. **Settings** > **Secrets and variables** > **Actions**
3. **"New repository secret"** butonuna tıklayın
4. Şunları doldurun:
   - **Name:** `INSTAGRAM_ACCOUNT_ID`
   - **Secret:** Instagram Account ID'niz (yukarıdaki adımdan aldığınız)
5. **"Add secret"** butonuna tıklayın

### 4️⃣ Test Edin

1. GitHub Actions'tan workflow'u çalıştırın
2. Hem Facebook hem Instagram'a post atılacak
3. Her iki platformda da post görünecek!

## ⚠️ Önemli Notlar

### Instagram Gereksinimleri

1. **Fotoğraf Zorunlu:** Instagram'a post atmak için fotoğraf zorunludur
   - Eğer `POST_IMAGE_POSTS` kullanıyorsanız, mesaj kısmı boş olsa bile fotoğraf olmalı
   - Fotoğraf yoksa Instagram post atlanır

2. **Fotoğraf Formatı:**
   - JPG veya PNG formatında olmalı
   - Maksimum 8 MB
   - Minimum 320x320 piksel

3. **Mesaj Uzunluğu:**
   - Instagram'da maksimum 2200 karakter
   - Hashtag'ler kullanabilirsiniz

### Instagram vs Facebook

| Özellik | Facebook | Instagram |
|---------|----------|-----------|
| Fotoğraf | Opsiyonel | Zorunlu |
| Mesaj | Opsiyonel | Opsiyonel |
| Video | Desteklenir | Desteklenir (şu an kodda yok) |
| Link | Desteklenir | Bio'da link |

## 🔄 Çalışma Senaryoları

### Senaryo 1: Facebook + Instagram (Fotoğraflı)
```
POST_IMAGE_POSTS = https://i.imgur.com/foto1.jpg|Mesaj 1,https://i.imgur.com/foto2.jpg|Mesaj 2
INSTAGRAM_ACCOUNT_ID = your_instagram_id
```
→ Her iki platforma da post atılır

### Senaryo 2: Sadece Facebook (Fotoğrafsız)
```
POST_MESSAGE = Mesaj
INSTAGRAM_ACCOUNT_ID = (boş veya yok)
```
→ Sadece Facebook'a post atılır (Instagram için fotoğraf gerekli)

### Senaryo 3: Instagram ID Yok
```
POST_IMAGE_POSTS = https://i.imgur.com/foto1.jpg|Mesaj
INSTAGRAM_ACCOUNT_ID = (boş veya yok)
```
→ Sadece Facebook'a post atılır

## 🆘 Sorun Giderme

### Hata: "Instagram Account ID bulunamadı"
**Çözüm:** 
- `INSTAGRAM_ACCOUNT_ID` secret'ını eklediğinizden emin olun
- ID'nin doğru olduğundan emin olun

### Hata: "Instagram için fotoğraf zorunludur"
**Çözüm:**
- `POST_IMAGE_POSTS` veya `POST_IMAGE_URL` kullanın
- Fotoğraf URL'sinin erişilebilir olduğundan emin olun

### Hata: "Container oluşturulamadı"
**Çözüm:**
- Instagram hesabınızın Business Account olduğundan emin olun
- Facebook sayfanıza bağlı olduğundan emin olun
- Token'ın geçerli olduğundan emin olun

### Instagram Post Görünmüyor
**Çözüm:**
- Instagram hesabınızı kontrol edin
- Post'un yayınlanması birkaç saniye sürebilir
- Instagram Graph API loglarını kontrol edin

## 📚 Kaynaklar

- [Instagram Graph API Dokümantasyonu](https://developers.facebook.com/docs/instagram-api)
- [Instagram Business Account Kurulumu](https://www.facebook.com/business/help/898752960195806)
- [Instagram Media Requirements](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media)

---

**Not:** Instagram entegrasyonu tamamen opsiyoneldir. İsterseniz sadece Facebook'a post atabilirsiniz! 📱
