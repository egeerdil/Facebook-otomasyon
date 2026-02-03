# 📸🖊️ Fotoğraf + Mesaj Eşleştirme

Her fotoğraf için özel bir mesaj paylaşmak için:

## 🎯 Nasıl Çalışır?

- Her fotoğraf için farklı bir mesaj tanımlayabilirsiniz
- Her gün otomatik olarak hem fotoğraf hem de mesaj seçilir
- 10 fotoğraf + 10 mesaj varsa, 10 günde bir döngü tamamlanır

## 📋 Adım Adım Kurulum

### 1️⃣ Fotoğraflarınızı ve Mesajlarınızı Hazırlayın

10 fotoğrafınızı internete yükleyin ve her biri için direkt görsel linkini alın.
Her fotoğraf için bir mesaj yazın.

**Örnek:**
- Fotoğraf 1: `https://i.imgur.com/foto1.jpg` → Mesaj: "🌅 Günaydın! Bugün harika bir gün!"
- Fotoğraf 2: `https://i.imgur.com/foto2.jpg` → Mesaj: "✨ Yeni fırsatlar kapınızda!"
- Fotoğraf 3: `https://i.imgur.com/foto3.jpg` → Mesaj: "🚀 Hedeflerinize ulaşın!"
- ... (10 fotoğraf + 10 mesaj)

### 2️⃣ GitHub Secret Ekleyin

1. GitHub repository'nize gidin
2. **Settings** > **Secrets and variables** > **Actions**
3. **"New repository secret"** butonuna tıklayın
4. Şunları doldurun:
   - **Name:** `POST_IMAGE_POSTS`
   - **Secret:** Fotoğraf URL'leri ve mesajları **virgülle ayırarak** ve **| (pipe) ile ayırarak** yazın:
     ```
     https://i.imgur.com/foto1.jpg|🌅 Günaydın! Bugün harika bir gün!,https://i.imgur.com/foto2.jpg|✨ Yeni fırsatlar kapınızda!,https://i.imgur.com/foto3.jpg|🚀 Hedeflerinize ulaşın!,https://i.imgur.com/foto4.jpg|💪 Güçlü olun!,https://i.imgur.com/foto5.jpg|🌟 Yıldız gibi parlayın!
     ```
   
   **Format:** `URL|MESAJ,URL|MESAJ,URL|MESAJ,...`
   
   - Her fotoğraf için: `URL|MESAJ`
   - Fotoğraflar arası: `,` (virgül)
   - URL ve mesaj arası: `|` (pipe karakteri)

5. **"Add secret"** butonuna tıklayın

### 3️⃣ Örnek Format

```
https://i.imgur.com/foto1.jpg|🌅 Günaydın! Bugün harika bir gün!,https://i.imgur.com/foto2.jpg|✨ Yeni fırsatlar kapınızda!,https://i.imgur.com/foto3.jpg|🚀 Hedeflerinize ulaşın!
```

**Açıklama:**
- `https://i.imgur.com/foto1.jpg` → Fotoğraf URL'si
- `|` → Ayırıcı
- `🌅 Günaydın! Bugün harika bir gün!` → Mesaj
- `,` → Bir sonraki fotoğraf+mesaj

## 📅 Örnek Senaryo

10 fotoğraf + 10 mesajınız var:

- **1. Gün:** Fotoğraf 1 + "🌅 Günaydın! Bugün harika bir gün!"
- **2. Gün:** Fotoğraf 2 + "✨ Yeni fırsatlar kapınızda!"
- **3. Gün:** Fotoğraf 3 + "🚀 Hedeflerinize ulaşın!"
- ...
- **10. Gün:** Fotoğraf 10 + "🎉 Başarılar!"
- **11. Gün:** Fotoğraf 1 + "🌅 Günaydın! Bugün harika bir gün!" (tekrar başlar)

## 🎨 Mesaj Özelleştirme

Mesajlarınızda şunları kullanabilirsiniz:
- Emojiler: 🌅 ✨ 🚀 💪 🌟
- Tarih: Sistem otomatik olarak tarih ekleyebilir (kodda özelleştirebilirsiniz)
- Özel metinler: İstediğiniz herhangi bir mesaj

## ⚙️ Öncelik Sırası

Sistem şu sırayla kontrol eder:

1. **`POST_IMAGE_POSTS`** (Fotoğraf + Mesaj eşleştirmesi) - **EN ÖNCELİKLİ**
2. `POST_IMAGE_URLS` (Sadece fotoğraf listesi)
3. `POST_IMAGE_URL` (Tek fotoğraf)
4. `POST_MESSAGE` (Sadece mesaj, fotoğraf yok)

## 🔄 Güncelleme

Fotoğraf veya mesaj değiştirmek için:

1. GitHub Secrets'ta `POST_IMAGE_POSTS` secret'ını bulun
2. **"Update"** butonuna tıklayın
3. İstediğiniz değişiklikleri yapın
4. **"Update secret"** butonuna tıklayın

## 📝 Örnek Kullanım Senaryoları

### Senaryo 1: Motivasyon Postları
```
https://i.imgur.com/motivasyon1.jpg|💪 Bugün kendinize inanın!,https://i.imgur.com/motivasyon2.jpg|🌟 Yıldız gibi parlayın!,https://i.imgur.com/motivasyon3.jpg|🚀 Hedeflerinize ulaşın!
```

### Senaryo 2: Günlük İpuçları
```
https://i.imgur.com/ipucu1.jpg|💡 İpucu: Her gün yeni bir şey öğrenin!,https://i.imgur.com/ipucu2.jpg|📚 Kitap okumak zihninizi açar!,https://i.imgur.com/ipucu3.jpg|🏃 Spor yapmak sağlıklıdır!
```

### Senaryo 3: Ürün Tanıtımları
```
https://i.imgur.com/urun1.jpg|🛍️ Yeni ürünümüz çıktı! İndirimli fiyatlarla!,https://i.imgur.com/urun2.jpg|🎁 Özel kampanya! Kaçırmayın!,https://i.imgur.com/urun3.jpg|⭐ Müşterilerimiz çok memnun!
```

## ✅ Test Etme

1. GitHub Actions'tan workflow'u manuel çalıştırın
2. Her çalıştırmada farklı bir fotoğraf + mesaj kombinasyonu seçildiğini göreceksiniz
3. Facebook sayfanızda fotoğraf ve mesajın birlikte paylaşıldığını kontrol edin

## 🆘 Sorun Giderme

**Mesaj görünmüyor:**
- `|` karakterinin doğru kullanıldığından emin olun
- Mesajın boş olmadığından emin olun

**Yanlış fotoğraf + mesaj eşleşmesi:**
- Formatı kontrol edin: `URL|MESAJ,URL|MESAJ`
- Virgül ve pipe karakterlerinin doğru kullanıldığından emin olun

**Fotoğraf görünmüyor:**
- URL'nin doğru olduğundan emin olun
- URL'yi tarayıcıda test edin

---

**Not:** Bu sistem sayesinde her fotoğraf için özel mesajlar paylaşabilirsiniz! 🎉
