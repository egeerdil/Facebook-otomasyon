# 🚀 Hızlı Kurulum Adımları

Page ID ve Token hazırsa, şu adımları takip edin:

## 1️⃣ Git Repository Oluşturma ve GitHub'a Push

Terminal'de şu komutları çalıştırın:

```bash
cd "/Users/egeerdil/Desktop/Facebook otomasyon"

# Git repository başlat
git init

# Tüm dosyaları ekle
git add .

# İlk commit
git commit -m "Initial commit: Facebook otomasyon sistemi"

# GitHub'da yeni bir repository oluşturun (github.com'da)
# Sonra şu komutları çalıştırın (YOUR_USERNAME ve REPO_NAME'i değiştirin):
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## 2️⃣ GitHub Secrets Ekleme

1. GitHub repository'nize gidin
2. **Settings** (Ayarlar) sekmesine tıklayın
3. Sol menüden **Secrets and variables** > **Actions** bölümüne gidin
4. **"New repository secret"** butonuna tıklayın
5. İki secret ekleyin:

   **Secret 1:**
   - Name: `FACEBOOK_PAGE_ID`
   - Value: Sayfa ID'niz (örnek: `123456789012345`)
   - **"Add secret"** butonuna tıklayın

   **Secret 2:**
   - Name: `FACEBOOK_ACCESS_TOKEN`
   - Value: Page Access Token'ınız (uzun bir string)
   - **"Add secret"** butonuna tıklayın

## 3️⃣ İlk Test - Manuel Çalıştırma

1. GitHub repository'nizde **Actions** sekmesine gidin
2. Sol tarafta **"Daily Facebook Post"** workflow'unu göreceksiniz
3. Sağ üstte **"Run workflow"** butonuna tıklayın
4. **"Run workflow"** butonuna tekrar tıklayın
5. Workflow çalışmaya başlayacak (yaklaşık 1-2 dakika sürer)
6. Başarılı olursa Facebook sayfanızda post göreceksiniz! ✅

## 4️⃣ Otomatik Çalışma Zamanını Ayarlama (Opsiyonel)

`.github/workflows/daily_post.yml` dosyasında cron zamanını değiştirebilirsiniz:

```yaml
- cron: "0 6 * * *"  # Her gün 06:00 UTC (Türkiye saati 09:00)
```

**Örnek zamanlar:**
- `"0 9 * * *"` - Her gün 09:00 UTC (Türkiye 12:00)
- `"0 12 * * *"` - Her gün 12:00 UTC (Türkiye 15:00)
- `"0 18 * * 1"` - Her Pazartesi 18:00 UTC

## ✅ Tamamlandı!

Artık sistem her gün otomatik olarak Facebook sayfanıza post atacak! 🎉

## 🔍 Sorun mu var?

- **Post atılmıyor:** Actions sekmesindeki logları kontrol edin
- **Token hatası:** Token'ın geçerli olduğundan emin olun
- **Page ID hatası:** Doğru Page ID kullandığınızdan emin olun
