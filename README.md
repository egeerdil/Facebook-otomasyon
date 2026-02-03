# 📱 Facebook Otomasyon - GitHub Actions

Bu proje, GitHub Actions kullanarak Facebook Graph API ile otomatik post atma sistemidir. Server'a ihtiyaç duymaz, bilgisayarınızın açık olmasına gerek yoktur ve tamamen ücretsizdir.

## 🎯 Özellikler

- ✅ Server gerektirmez
- ✅ Bilgisayarın açık olmasına gerek yok
- ✅ Tamamen ücretsiz (GitHub Actions free tier)
- ✅ Zamanlı çalışır (cron job)
- ✅ Kod tamamen sizin kontrolünüzde
- ✅ Her gün otomatik post atar

## 🚀 Kurulum

### 1. Facebook Graph API Ayarları

#### Facebook Page Access Token Alma

1. **Facebook Developers** hesabı oluşturun: https://developers.facebook.com/
2. Yeni bir **App** oluşturun
3. **Graph API Explorer**'a gidin: https://developers.facebook.com/tools/explorer/
4. App'inizi seçin
5. **User Token (Kullanıcı Token'ı) alın:**
   - Sağ üstteki **"Get Token"** butonuna tıklayın
   - **"Get User Access Token"** seçin
   - **⚠️ ÖNEMLİ - İZİN HATASI ALIRSANIZ:**
     - Eğer "Invalid Scopes: pages_show_list" gibi bir hata görürseniz:
       1. **"Tamam"** butonuna tıklayın
       2. Permissions sekmesinde **TÜM izinleri kaldırın** (X işaretine tıklayarak)
       3. İzin listesini tamamen temizleyin
       4. Tekrar **"Generate Access Token"** butonuna tıklayın
   - **"Generate Access Token"** butonuna tıklayın
   - Facebook'ta izin verin (eğer istenirse)
   - Çıkan token'ı kopyalayın (bu geçici bir token, yaklaşık 1-2 saat geçerli)
   - 📝 **ÖNEMLİ:** Bu token'ı bir not defterine veya metin dosyasına kaydedin (şimdilik geçici olarak saklayın)
   - ✅ **Not:** İzin seçmeye gerek yok! Bir sonraki adımda (`/me/accounts`) sayfa token'ı alırken gerekli tüm izinler otomatik olarak eklenir
   
6. **User Token'ı Page Token'a çevirin (ASIL İHTİYACINIZ OLAN TOKEN):**
   
   **ADIM 1: Token'ı Access Token alanına yapıştırın**
   - Sağ taraftaki **"Access Token"** alanına az önce kopyaladığınız User Token'ı yapıştırın
   - Token'ın doğru yapıştırıldığından emin olun (tamamen görünüyor olmalı)
   
   **ADIM 2: Endpoint'i değiştirin**
   - Graph API Explorer'ın **üst kısmındaki URL alanına** gidin
   - Şu anda muhtemelen `/me?fields=id,name` yazıyor
   - Bunu **tamamen silin** ve şunu yazın: `/me/accounts`
   - ⚠️ **ÖNEMLİ:** Sadece `/me/accounts` yazın, `GET` yazmayın (GET zaten seçili)
   
   **ADIM 3: Submit'e basın**
   - **"Submit"** (mavi buton) butonuna tıklayın
   
   **ADIM 4: Sonucu kontrol edin**
   - Sol tarafta JSON formatında sonuç göreceksiniz
   - **Eğer hata alırsanız:**
     - `"error"` mesajı görüyorsanız → Aşağıdaki "Sorun Giderme" bölümüne bakın
     - `"data": []` (boş array) görüyorsanız → Sayfanızın yöneticisi değilsiniz veya token geçersiz
   - **Başarılı olursa** şöyle bir yapı göreceksiniz:
     ```json
     {
       "data": [
         {
           "access_token": "BURASI SİZİN PAGE TOKEN'INIZ",
           "id": "SAYFA_ID",
           "name": "Sayfa Adınız"
         }
       ]
     }
     ```
   - **"access_token"** alanındaki değeri kopyalayın (bu sizin **Page Access Token**'ınız - ASIL İHTİYACINIZ OLAN BU!)
   - **"id"** alanındaki değeri de kopyalayın (bu sizin **Page ID**'niz)
   - 📝 **ÖNEMLİ:** Bu Page Token'ı ve Page ID'yi bir yere kaydedin
   
7. **Token'ı uzun süreli yapın (60 gün):**
   - Yeni bir sekmede şu URL'yi açın (TOKEN yerine Page Token'ınızı yazın):
     ```
     https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=APP_ID&client_secret=APP_SECRET&fb_exchange_token=PAGE_TOKEN
     ```
   - `APP_ID` ve `APP_SECRET` değerlerini Facebook App ayarlarından alın
   - `PAGE_TOKEN` yerine az önce aldığınız Page Token'ı yazın
   - Sonuçta çıkan yeni token'ı kopyalayın (bu 60 gün geçerli)

#### Page ID Bulma

1. Facebook sayfanıza gidin
2. **Sayfa Hakkında** bölümüne gidin
3. **Sayfa Kimliği** (Page ID) değerini kopyalayın
   - Veya Graph API Explorer'da `GET /me/accounts` ile bulabilirsiniz

### 2. GitHub Repository Ayarları

1. Bu repository'yi GitHub'a push edin
2. GitHub repository'nize gidin
3. **Settings** (Ayarlar) sekmesine tıklayın
4. Sol menüden **Secrets and variables** > **Actions** bölümüne gidin
5. **"New repository secret"** butonuna tıklayın
6. Aşağıdaki **Secrets**'ları tek tek ekleyin:

   - **Secret 1:**
     - Name: `FACEBOOK_PAGE_ID`
     - Value: `/me/accounts` adımında aldığınız sonuçtaki **"id"** değeri (sayfa ID'niz)
     - **"Add secret"** butonuna tıklayın
   
   - **Secret 2:**
     - Name: `FACEBOOK_ACCESS_TOKEN`
     - Value: `/me/accounts` adımında aldığınız **"access_token"** değeri (Page Token'ınız)
     - **"Add secret"** butonuna tıklayın
   
   - **Secret 3 (Opsiyonel):**
     - Name: `POST_MESSAGE`
     - Value: Özel post mesajınız (boş bırakabilirsiniz, otomatik mesaj kullanılır)
     - **"Add secret"** butonuna tıklayın
   
   - **Secret 4 (Opsiyonel - Fotoğraf için):**
     - Name: `POST_IMAGE_URL`
     - Value: Fotoğraf URL'si (örnek: `https://example.com/image.jpg`)
     - **"Add secret"** butonuna tıklayın
     - 📸 **Not:** Fotoğraf eklemek istemiyorsanız bu secret'ı eklemeyin
   
   ✅ **ÖNEMLİ:** `/me/accounts` adımında aldığınız **"id"** ve **"access_token"** değerlerini buraya ekleyin!

### 3. Cron Zamanını Ayarlama

`.github/workflows/daily_post.yml` dosyasında cron zamanını düzenleyin:

```yaml
- cron: "0 6 * * *"  # Her gün 06:00 UTC (Türkiye saati 09:00)
```

**Cron formatı:** `dakika saat gün ay haftanın-günü`

**Örnekler:**
- `"0 9 * * *"` - Her gün 09:00 UTC
- `"0 12 * * 1"` - Her Pazartesi 12:00 UTC
- `"30 8 * * *"` - Her gün 08:30 UTC

**Türkiye saati için:** UTC'den 3 saat çıkarın
- Türkiye saati 09:00 → UTC 06:00 → `"0 6 * * *"`

### 4. Manuel Çalıştırma

GitHub Actions sekmesinden **"Run workflow"** butonuna tıklayarak manuel olarak çalıştırabilirsiniz.

## 📝 Post Mesajını Özelleştirme

`post_to_facebook.py` dosyasındaki `get_daily_message()` fonksiyonunu düzenleyerek kendi mesajlarınızı ekleyebilirsiniz:

```python
def get_daily_message():
    today = datetime.now()
    date_str = today.strftime("%d.%m.%Y")
    
    messages = [
        "Kendi mesajınız 1",
        "Kendi mesajınız 2",
        "Kendi mesajınız 3",
    ]
    
    day_index = today.timetuple().tm_yday % len(messages)
    return messages[day_index]
```

Veya GitHub Secrets'ta `POST_MESSAGE` değişkenini ayarlayarak sabit bir mesaj kullanabilirsiniz.

## 🖼️ Fotoğraf Ekleme

Postlarınıza fotoğraf eklemek için:

1. **Fotoğrafı internete yükleyin:**
   - Fotoğrafınızı bir yere yükleyin (örnek: Imgur, Google Drive, kendi web siteniz)
   - Fotoğrafın **doğrudan erişilebilir URL'sini** alın (örnek: `https://example.com/image.jpg`)

2. **GitHub Secret ekleyin:**
   - Settings > Secrets and variables > Actions
   - Yeni secret: `POST_IMAGE_URL`
   - Value: Fotoğraf URL'si (örnek: `https://i.imgur.com/abc123.jpg`)

3. **Otomatik çalışır:**
   - Artık her post otomatik olarak bu fotoğrafla birlikte atılacak
   - Fotoğraf eklemek istemiyorsanız `POST_IMAGE_URL` secret'ını silin veya eklemeyin

**Örnek fotoğraf servisleri:**
- [Imgur](https://imgur.com) - Ücretsiz, hızlı
- [Cloudinary](https://cloudinary.com) - Ücretsiz plan mevcut
- Kendi web siteniz
- Google Drive (paylaşım linki oluşturun)

## 🔒 Güvenlik

- ⚠️ **Asla** `FACEBOOK_ACCESS_TOKEN` ve `FACEBOOK_PAGE_ID` değerlerini kod içine yazmayın
- ✅ Sadece GitHub Secrets kullanın
- ✅ Token'larınızı düzenli olarak yenileyin
- ✅ `.env` dosyasını `.gitignore`'a eklediğinizden emin olun

## 📊 Workflow Durumunu Kontrol Etme

1. GitHub repository'nize gidin
2. **Actions** sekmesine tıklayın
3. Her çalıştırmanın durumunu görebilirsiniz
4. Başarısız olursa logları kontrol edin

## 🛠️ Sorun Giderme

### `/me/accounts` çalışmıyor veya hata veriyor

**Hata: "Invalid OAuth access token" veya "Token expired"**
- Token'ın süresi dolmuş olabilir (1-2 saat geçerli)
- **Çözüm:** Yeni bir User Token oluşturun (Adım 5'i tekrarlayın)

**Hata: "Insufficient permissions" veya "Requires extended permission"**
- Token'ın gerekli izinleri yok
- **Çözüm:** 
  1. Yeni bir User Token oluşturun
  2. Token oluştururken Facebook'ta **tüm izinleri verin** (eğer istenirse)
  3. Sayfanızın **yöneticisi** olduğunuzdan emin olun

**Sonuç: `"data": []` (boş array)**
- Sayfanızın yöneticisi değilsiniz veya sayfa bulunamadı
- **Çözüm:**
  1. Facebook sayfanıza gidin
  2. **Sayfa Ayarları** > **Sayfa Rolleri** bölümünden kendinizin **Yönetici** olduğundan emin olun
  3. Eğer yönetici değilseniz, sayfa sahibinden yönetici yetkisi isteyin

**Hata: "Unsupported get request"**
- Endpoint'i yanlış yazmış olabilirsiniz
- **Çözüm:** Sadece `/me/accounts` yazın (GET yazmayın, zaten seçili)

**Token'ı Access Token alanına yapıştırmadınız**
- Token'ı sağ taraftaki "Access Token" alanına yapıştırmayı unutmuş olabilirsiniz
- **Çözüm:** Token'ı sağ taraftaki "Access Token" alanına yapıştırın, sonra Submit'e basın

### Post atılmıyor

1. **Token kontrolü:** Token'ın geçerli ve süresi dolmamış olduğundan emin olun
2. **Page ID kontrolü:** Doğru Page ID kullandığınızdan emin olun
3. **İzinler:** Sayfa token'ı aldıktan sonra (`/me/accounts` adımı) gerekli izinler otomatik olarak eklenir. Ekstra bir şey yapmanıza gerek yok.
4. **Loglar:** GitHub Actions loglarını kontrol edin

### Token süresi doldu

1. Yeni bir token oluşturun
2. GitHub Secrets'ta güncelleyin
3. Uzun süreli token kullanın

## 📚 Kaynaklar

- [Facebook Graph API Dokümantasyonu](https://developers.facebook.com/docs/graph-api)
- [GitHub Actions Dokümantasyonu](https://docs.github.com/en/actions)
- [Cron Expression Generator](https://crontab.guru/)

## 📄 Lisans

Bu proje özgürce kullanılabilir.

## 🤝 Katkıda Bulunma

İyileştirme önerileriniz için issue açabilir veya pull request gönderebilirsiniz!

---

**Not:** Bu sistem marketing yapanların gizli silahı! 🚀
