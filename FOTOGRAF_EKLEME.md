# 🖼️ Facebook Post'una Fotoğraf Ekleme Rehberi

## 📸 Adım Adım Fotoğraf Ekleme

### 1️⃣ Fotoğrafı İnternete Yükleyin

Fotoğrafınızı internete yüklemek için birkaç seçenek:

#### Seçenek A: Imgur (En Kolay - Önerilen) ⭐

1. https://imgur.com adresine gidin
2. **"New post"** butonuna tıklayın
3. Fotoğrafınızı sürükleyip bırakın veya seçin
4. Fotoğraf yüklendikten sonra, sağ tarafta **"Copy"** butonuna tıklayın
5. **"Copy link"** seçeneğini seçin
6. URL'yi kopyalayın (örnek: `https://i.imgur.com/abc123.jpg`)

**ÖNEMLİ:** 
- URL'nin sonunda `.jpg`, `.png` gibi uzantı olmalı!
- **Direkt görsel linkini** alın (örnek: `https://i.imgur.com/abc123.jpg`)
- Sayfa linkini değil, görsel linkini kullanın!

**Imgur'da doğru linki almak için:**
- Fotoğrafa sağ tıklayın > **"Copy image address"** veya
- Fotoğrafa tıklayın, URL çubuğundaki linki kopyalayın (`.jpg` ile biten)

#### Seçenek B: Google Drive

1. Google Drive'a fotoğrafınızı yükleyin
2. Fotoğrafa sağ tıklayın > **"Paylaş"**
3. **"Herkes linke sahip olan herkes"** seçeneğini seçin
4. **"Bağlantıyı kopyala"** butonuna tıklayın
5. Link şöyle olacak: `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`
6. Bu linki şu formata çevirin: `https://drive.google.com/uc?export=view&id=FILE_ID`
   - `FILE_ID` kısmını linkten kopyalayın

#### Seçenek C: Kendi Web Siteniz

1. Fotoğrafı web sitenize yükleyin
2. Doğrudan erişilebilir URL'yi alın
3. Örnek: `https://www.example.com/images/foto.jpg`

### 2️⃣ Fotoğraf URL'sini Test Edin

Fotoğraf URL'sinin çalıştığından emin olun:

1. Yeni bir tarayıcı sekmesi açın
2. URL'yi adres çubuğuna yapıştırın
3. Enter'a basın
4. Fotoğraf görünüyorsa ✅ - URL doğru!
5. Fotoğraf görünmüyorsa ❌ - Başka bir yöntem deneyin

### 3️⃣ GitHub Secret Ekleyin

1. GitHub repository'nize gidin: https://github.com/egeerdil/facebook-otomasyon
2. **Settings** (Ayarlar) sekmesine tıklayın
3. Sol menüden **Secrets and variables** > **Actions** bölümüne gidin
4. **"New repository secret"** butonuna tıklayın
5. Şunları doldurun:
   - **Name:** `POST_IMAGE_URL`
   - **Secret:** Fotoğraf URL'niz (örnek: `https://i.imgur.com/abc123.jpg`)
6. **"Add secret"** butonuna tıklayın

### 4️⃣ Test Edin

1. GitHub'da **Actions** sekmesine gidin
2. **"Daily Facebook Post"** workflow'unu bulun
3. **"Run workflow"** butonuna tıklayın
4. 1-2 dakika bekleyin
5. Facebook sayfanızı kontrol edin - fotoğraflı post görünmeli! ✅

## 🔄 Fotoğrafı Değiştirme

Fotoğrafı değiştirmek isterseniz:

1. GitHub'da Settings > Secrets > Actions
2. `POST_IMAGE_URL` secret'ını bulun
3. **"Update"** butonuna tıklayın
4. Yeni fotoğraf URL'sini girin
5. **"Update secret"** butonuna tıklayın

## ❌ Fotoğrafı Kaldırma

Fotoğraf eklemek istemiyorsanız:

1. GitHub'da Settings > Secrets > Actions
2. `POST_IMAGE_URL` secret'ını bulun
3. **"Delete"** butonuna tıklayın
4. Artık postlar fotoğrafsız atılacak

## 🎨 Her Post İçin Farklı Fotoğraf

Her gün farklı fotoğraf kullanmak isterseniz:

1. `post_to_facebook.py` dosyasını açın
2. `get_daily_message()` fonksiyonunu bulun
3. Şu şekilde güncelleyin:

```python
def get_daily_message():
    today = datetime.now()
    date_str = today.strftime("%d.%m.%Y")
    
    # Her gün için farklı mesaj ve fotoğraf
    posts = [
        {
            "message": f"🌅 Günaydın! Bugün {date_str}",
            "image": "https://i.imgur.com/foto1.jpg"
        },
        {
            "message": f"✨ Yeni bir gün! {date_str}",
            "image": "https://i.imgur.com/foto2.jpg"
        },
        {
            "message": f"🚀 Bugün {date_str}",
            "image": "https://i.imgur.com/foto3.jpg"
        },
    ]
    
    day_index = today.timetuple().tm_yday % len(posts)
    return posts[day_index]
```

Sonra `main()` fonksiyonunu da güncellemeniz gerekir. (Daha detaylı kod için README'ye bakın)

## ⚠️ Önemli Notlar

- ✅ Fotoğraf URL'si **doğrudan erişilebilir** olmalı
- ✅ URL'nin sonunda dosya uzantısı olmalı (`.jpg`, `.png`, vb.)
- ✅ Fotoğraf **public** olmalı (herkes erişebilmeli)
- ❌ Google Drive linklerini direkt kullanamazsınız (formatı değiştirmeniz gerekir)
- ❌ Facebook, Instagram linklerini kullanamazsınız

## 🆘 Sorun mu var?

**Fotoğraf görünmüyor:**
- URL'yi tarayıcıda test edin
- URL'nin doğrudan erişilebilir olduğundan emin olun
- GitHub Actions loglarını kontrol edin

**"Invalid image URL" hatası:**
- Fotoğraf URL'si geçersiz olabilir
- URL formatını kontrol edin
- Başka bir fotoğraf servisi deneyin
