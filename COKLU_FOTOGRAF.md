# 📸 Çoklu Fotoğraf Otomasyonu

10 (veya daha fazla) fotoğrafı otomatik olarak sırayla post etmek için:

## 🎯 Nasıl Çalışır?

- Her gün farklı bir fotoğraf otomatik olarak seçilir
- 10 fotoğraf varsa, 10 günde bir döngü tamamlanır
- 11. günde tekrar 1. fotoğraf kullanılır
- Böylece fotoğraflar sürekli döngü halinde paylaşılır

## 📋 Adım Adım Kurulum

### 1️⃣ Fotoğraflarınızı Hazırlayın

10 fotoğrafınızı internete yükleyin (Imgur, Cloudinary, vb.)
- Her fotoğraf için direkt görsel linkini alın
- Örnek:
  - `https://i.imgur.com/foto1.jpg`
  - `https://i.imgur.com/foto2.jpg`
  - `https://i.imgur.com/foto3.jpg`
  - ... (10 fotoğraf)

### 2️⃣ GitHub Secret Ekleyin

1. GitHub repository'nize gidin
2. **Settings** > **Secrets and variables** > **Actions**
3. **"New repository secret"** butonuna tıklayın
4. Şunları doldurun:
   - **Name:** `POST_IMAGE_URLS`
   - **Secret:** Fotoğraf URL'lerini **virgülle ayırarak** yazın:
     ```
     https://i.imgur.com/foto1.jpg,https://i.imgur.com/foto2.jpg,https://i.imgur.com/foto3.jpg,https://i.imgur.com/foto4.jpg,https://i.imgur.com/foto5.jpg,https://i.imgur.com/foto6.jpg,https://i.imgur.com/foto7.jpg,https://i.imgur.com/foto8.jpg,https://i.imgur.com/foto9.jpg,https://i.imgur.com/foto10.jpg
     ```
5. **"Add secret"** butonuna tıklayın

### 3️⃣ Tek Fotoğraf vs Çoklu Fotoğraf

**Çoklu fotoğraf kullanmak için:**
- `POST_IMAGE_URLS` secret'ını kullanın (virgülle ayrılmış liste)

**Tek fotoğraf kullanmak için:**
- `POST_IMAGE_URL` secret'ını kullanın (tek URL)

**İkisi de varsa:**
- `POST_IMAGE_URLS` önceliklidir (çoklu fotoğraf kullanılır)

## 📅 Örnek Senaryo

10 fotoğrafınız var:
- **1. Gün:** 1. fotoğraf
- **2. Gün:** 2. fotoğraf
- **3. Gün:** 3. fotoğraf
- ...
- **10. Gün:** 10. fotoğraf
- **11. Gün:** 1. fotoğraf (tekrar başlar)
- **12. Gün:** 2. fotoğraf
- ... (sonsuz döngü)

## 🎨 Fotoğraf Sırasını Değiştirme

Fotoğraf sırasını değiştirmek için:
1. GitHub Secrets'ta `POST_IMAGE_URLS` secret'ını bulun
2. **"Update"** butonuna tıklayın
3. URL'leri istediğiniz sıraya göre yeniden düzenleyin
4. **"Update secret"** butonuna tıklayın

## 🔢 Fotoğraf Sayısını Artırma/Azaltma

- **Daha fazla fotoğraf eklemek:** Listeye yeni URL'ler ekleyin
- **Fotoğraf çıkarmak:** Listeden URL'leri silin
- **Fotoğraf sayısı önemli değil:** 5, 10, 20, 100... istediğiniz kadar!

## ⚙️ Kod İçinde Fotoğraf Listesi (Alternatif)

Eğer GitHub Secret kullanmak istemiyorsanız, `post_to_facebook.py` dosyasını düzenleyebilirsiniz:

```python
def get_daily_image():
    """
    Günlük fotoğraf URL'sini döndürür
    """
    # Fotoğraf URL'lerinizi buraya ekleyin
    image_urls = [
        "https://i.imgur.com/foto1.jpg",
        "https://i.imgur.com/foto2.jpg",
        "https://i.imgur.com/foto3.jpg",
        # ... daha fazla fotoğraf
    ]
    
    today = datetime.now()
    day_index = today.timetuple().tm_yday % len(image_urls)
    return image_urls[day_index]
```

Sonra `main()` fonksiyonunda:
```python
image_url = get_daily_image()
```

## ✅ Test Etme

1. GitHub Actions'tan workflow'u manuel çalıştırın
2. Her çalıştırmada farklı bir fotoğraf seçildiğini göreceksiniz
3. Facebook sayfanızda fotoğrafların sırayla paylaşıldığını kontrol edin

## 🆘 Sorun Giderme

**Tüm fotoğraflar aynı:**
- GitHub Secret'ta URL'lerin virgülle ayrıldığından emin olun
- Boşluk olmamalı (veya her URL'den sonra boşluk varsa temizleyin)

**Fotoğraf görünmüyor:**
- Her URL'nin doğru olduğundan emin olun
- URL'leri tarayıcıda test edin

**Fotoğraf sayısı değişti:**
- GitHub Secret'ı güncelleyin
- Yeni URL'leri ekleyin veya eski URL'leri silin

---

**Not:** Bu sistem sayesinde 365 gün boyunca farklı fotoğraflar paylaşabilirsiniz! 🎉
