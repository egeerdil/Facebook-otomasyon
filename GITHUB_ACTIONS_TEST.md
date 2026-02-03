# 🚀 GitHub Actions'tan Test Etme Rehberi

`POST_IMAGE_POSTS`'u GitHub Actions üzerinden test etmek için:

## 📋 Adım Adım

### 1️⃣ GitHub Secret Ekleyin

1. GitHub repository'nize gidin: https://github.com/egeerdil/facebook-otomasyon
2. **Settings** (Ayarlar) sekmesine tıklayın
3. Sol menüden **Secrets and variables** > **Actions** bölümüne gidin
4. **"New repository secret"** butonuna tıklayın
5. Şunları doldurun:
   - **Name:** `POST_IMAGE_POSTS`
   - **Secret:** Fotoğraf URL'leri ve mesajları virgülle ayırarak ve | (pipe) ile ayırarak yazın:
     ```
     https://i.imgur.com/foto1.jpg|🌅 Günaydın! Bugün harika bir gün!,https://i.imgur.com/foto2.jpg|✨ Yeni fırsatlar kapınızda!,https://i.imgur.com/foto3.jpg|🚀 Hedeflerinize ulaşın!
     ```
6. **"Add secret"** butonuna tıklayın

### 2️⃣ GitHub Actions'tan Çalıştırın

1. GitHub repository'nizde **Actions** sekmesine gidin
2. Sol tarafta **"Daily Facebook Post"** workflow'unu göreceksiniz
3. Üzerine tıklayın
4. Sağ üstte **"Run workflow"** butonuna tıklayın
5. Açılan pencerede:
   - Branch: `main` (veya mevcut branch'iniz)
   - **"Run workflow"** butonuna tekrar tıklayın

### 3️⃣ Sonucu Kontrol Edin

1. Workflow çalışmaya başlayacak (yaklaşık 1-2 dakika sürer)
2. Çalışma tamamlandığında:
   - ✅ **Yeşil tik** görürseniz → Başarılı! Facebook sayfanızda post görünecek
   - ❌ **Kırmızı X** görürseniz → Hata var, logları kontrol edin

3. **Logları görmek için:**
   - Çalışmaya tıklayın
   - **"📱 Facebook'a post at"** adımına tıklayın
   - Tüm logları göreceksiniz

## 📸 Örnek Secret Formatı

```
https://i.imgur.com/foto1.jpg|🌅 Günaydın! Bugün harika bir gün!,https://i.imgur.com/foto2.jpg|✨ Yeni fırsatlar kapınızda!,https://i.imgur.com/foto3.jpg|🚀 Hedeflerinize ulaşın!
```

**Format:** `URL|MESAJ,URL|MESAJ,URL|MESAJ`

## ✅ Başarılı Test Sonucu

Loglarda şunları göreceksiniz:

```
📸 Toplam 3 fotoğraf+mesaj var, bugün 1. post seçildi
📝 Seçilen mesaj: 🌅 Günaydın! Bugün harika bir gün!
📝 Post mesajı: 🌅 Günaydın! Bugün harika bir gün!
🖼️ Fotoğraf URL'si: https://i.imgur.com/foto1.jpg
📅 Tarih: 2026-02-03 19:30:00
📥 Fotoğraf URL'si ile yükleniyor: https://i.imgur.com/foto1.jpg
✅ Fotoğraf URL yöntemi ile başarıyla yüklendi!
✅ Post başarıyla atıldı!
📌 Post ID: 1234567890_987654321
🔗 Post URL: https://facebook.com/1234567890_987654321
```

## ❌ Hata Durumları

### Hata 1: Secret Bulunamadı
```
ValueError: POST_IMAGE_POSTS environment variable bulunamadı!
```

**Çözüm:** GitHub Secrets'ta `POST_IMAGE_POSTS` secret'ını eklediğinizden emin olun.

### Hata 2: Format Yanlış
```
❌ Hiç post bulunamadı! Formatı kontrol edin.
```

**Çözüm:** Formatı kontrol edin: `URL|MESAJ,URL|MESAJ`

### Hata 3: Fotoğraf Yüklenemiyor
```
❌ Fotoğraf indirme/yükleme hatası: ...
```

**Çözüm:** 
- Fotoğraf URL'sinin doğru olduğundan emin olun
- URL'yi tarayıcıda test edin
- Fotoğrafın erişilebilir olduğundan emin olun

## 🔄 Tekrar Test Etme

Her test için:
1. **Actions** sekmesine gidin
2. **"Run workflow"** butonuna tıklayın
3. Her çalıştırmada farklı bir post seçilecek (günün index'ine göre)

## 💡 İpuçları

1. **İlk test için tek bir post kullanın:**
   ```
   https://i.imgur.com/foto1.jpg|Test mesajı
   ```

2. **Başarılı olursa tüm listeyi ekleyin**

3. **Her postu ayrı ayrı test edin:**
   - İlk önce tek bir post ile test edin
   - Başarılı olursa tüm listeyi ekleyin

4. **Logları mutlaka kontrol edin:**
   - Hata varsa loglarda detaylı bilgi göreceksiniz

## 🎯 Hızlı Kontrol Listesi

- [ ] `POST_IMAGE_POSTS` secret'ı eklendi
- [ ] Format doğru: `URL|MESAJ,URL|MESAJ`
- [ ] Fotoğraf URL'leri erişilebilir
- [ ] `FACEBOOK_PAGE_ID` secret'ı var
- [ ] `FACEBOOK_ACCESS_TOKEN` secret'ı var
- [ ] Workflow çalıştırıldı
- [ ] Loglar kontrol edildi
- [ ] Facebook sayfasında post göründü

---

**Not:** GitHub Actions'tan test etmek, gerçek ortamda test etmek demektir. Facebook sayfanızda gerçek bir post oluşturulacak! 🚀
