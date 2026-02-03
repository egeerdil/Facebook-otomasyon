# 🧪 Manuel Test Rehberi

`POST_IMAGE_POSTS`'u yerel olarak test etmek için:

## 🚀 Hızlı Test

### Yöntem 1: Test Scripti Kullanma (Önerilen)

1. **Terminal'de proje klasörüne gidin:**
   ```bash
   cd "/Users/egeerdil/Desktop/Facebook otomasyon"
   ```

2. **Facebook bilgilerinizi environment variable olarak set edin:**
   ```bash
   export FACEBOOK_PAGE_ID='your_page_id'
   export FACEBOOK_ACCESS_TOKEN='your_access_token'
   ```

3. **Test scriptini çalıştırın:**
   ```bash
   python test_post.py
   ```

### Yöntem 2: Direkt Python Scripti

1. **Terminal'de:**
   ```bash
   cd "/Users/egeerdil/Desktop/Facebook otomasyon"
   ```

2. **Environment variable'ları set edin:**
   ```bash
   export FACEBOOK_PAGE_ID='your_page_id'
   export FACEBOOK_ACCESS_TOKEN='your_access_token'
   export POST_IMAGE_POSTS='https://i.imgur.com/foto1.jpg|🌅 Günaydın!,https://i.imgur.com/foto2.jpg|✨ Yeni gün!'
   ```

3. **Ana scripti çalıştırın:**
   ```bash
   python post_to_facebook.py
   ```

## 📝 Örnek Test Komutları

### Tam Örnek:

```bash
cd "/Users/egeerdil/Desktop/Facebook otomasyon"

export FACEBOOK_PAGE_ID='123456789012345'
export FACEBOOK_ACCESS_TOKEN='your_token_here'
export POST_IMAGE_POSTS='https://i.imgur.com/foto1.jpg|🌅 Günaydın! Bugün harika bir gün!,https://i.imgur.com/foto2.jpg|✨ Yeni fırsatlar kapınızda!,https://i.imgur.com/foto3.jpg|🚀 Hedeflerinize ulaşın!'

python post_to_facebook.py
```

## 🔍 Format Kontrolü (Facebook Bilgileri Olmadan)

Sadece formatı test etmek için:

```bash
python test_post.py
```

Bu komut Facebook bilgileri olmadan formatı kontrol eder ve postları gösterir.

## ✅ Başarılı Test Sonucu

```
============================================================
🧪 POST_IMAGE_POSTS Test Scripti
============================================================

✅ 3 post bulundu:

  1. Fotoğraf: https://i.imgur.com/foto1.jpg
     Mesaj: 🌅 Günaydın! Bugün harika bir gün!

  2. Fotoğraf: https://i.imgur.com/foto2.jpg
     Mesaj: ✨ Yeni fırsatlar kapınızda!

  3. Fotoğraf: https://i.imgur.com/foto3.jpg
     Mesaj: 🚀 Hedeflerinize ulaşın!

============================================================
🚀 İlk postu test ediyoruz...
============================================================

📝 Mesaj: 🌅 Günaydın! Bugün harika bir gün!
🖼️  Fotoğraf: https://i.imgur.com/foto1.jpg

📥 Fotoğraf URL'si ile yükleniyor: https://i.imgur.com/foto1.jpg
✅ Fotoğraf URL yöntemi ile başarıyla yüklendi!

============================================================
✅ TEST BAŞARILI!
============================================================
📌 Post ID: 1234567890_987654321
🔗 Post URL: https://facebook.com/1234567890_987654321
```

## ❌ Hata Durumları

### Hata 1: Facebook Bilgileri Yok
```
⚠️  Facebook bilgileri bulunamadı!
📝 Lütfen şu environment variable'ları set edin:
   - FACEBOOK_PAGE_ID
   - FACEBOOK_ACCESS_TOKEN
```

**Çözüm:** Environment variable'ları set edin.

### Hata 2: Format Yanlış
```
❌ Hiç post bulunamadı! Formatı kontrol edin.
```

**Çözüm:** `POST_IMAGE_POSTS` formatını kontrol edin: `URL|MESAJ,URL|MESAJ`

### Hata 3: Fotoğraf Yüklenemiyor
```
❌ Fotoğraf indirme/yükleme hatası: ...
```

**Çözüm:** 
- Fotoğraf URL'sinin doğru olduğundan emin olun
- URL'yi tarayıcıda test edin
- Fotoğrafın erişilebilir olduğundan emin olun

## 🎯 İpuçları

1. **İlk test için tek bir post kullanın:**
   ```bash
   export POST_IMAGE_POSTS='https://i.imgur.com/foto1.jpg|Test mesajı'
   ```

2. **Formatı kontrol etmek için test scriptini kullanın:**
   ```bash
   python test_post.py
   ```

3. **Gerçek test için Facebook bilgilerinizi kullanın:**
   - GitHub Secrets'tan kopyalayın
   - Environment variable olarak set edin

4. **Her postu ayrı ayrı test edin:**
   - İlk önce tek bir post ile test edin
   - Başarılı olursa tüm listeyi ekleyin

## 📚 Daha Fazla Bilgi

- `FOTOGRAF_MESAJ_ESLESTIRME.md` - Detaylı kullanım rehberi
- `README.md` - Genel proje dokümantasyonu
