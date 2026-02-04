# 🔍 Instagram Account ID Bulma (Adım Adım)

Instagram hesabınız bağlı görünüyor! Şimdi Instagram Account ID'yi bulalım:

## 📋 Adım Adım

### 1️⃣ Graph API Explorer'a Gidin

1. **Facebook Graph API Explorer**'a gidin: https://developers.facebook.com/tools/explorer/
2. Üst kısımda **Meta App** dropdown'ından app'inizi seçin
3. Sağ tarafta **Access Token** alanına **Page Access Token**'ınızı yapıştırın

### 2️⃣ Instagram Account ID'yi Bulun

**Yöntem A: /me/accounts ile (Önerilen)**

1. Endpoint alanına şunu yazın: `GET /me/accounts`
2. **"Submit"** butonuna tıklayın
3. Sonuçta şunu göreceksiniz:
   ```json
   {
     "data": [
       {
         "id": "PAGE_ID",
         "name": "Sayfa Adı",
         "instagram_business_account": {
           "id": "17841405309211844"
         }
       }
     ]
   }
   ```
4. **`instagram_business_account.id`** değerini kopyalayın (bu sizin Instagram Account ID'niz!)

**Yöntem B: Direkt Page ID ile**

Eğer Page ID'nizi biliyorsanız:

1. Endpoint alanına şunu yazın: `GET /{PAGE_ID}?fields=instagram_business_account`
2. `{PAGE_ID}` yerine sayfa ID'nizi yazın (örnek: `GET /123456789012345?fields=instagram_business_account`)
3. **"Submit"** butonuna tıklayın
4. Sonuçta şunu göreceksiniz:
   ```json
   {
     "id": "PAGE_ID",
     "instagram_business_account": {
       "id": "17841405309211844"
     }
   }
   ```
5. **`instagram_business_account.id`** değerini kopyalayın

### 3️⃣ GitHub Secret Ekleyin

1. GitHub repository'nize gidin: https://github.com/egeerdil/facebook-otomasyon
2. **Settings** > **Secrets and variables** > **Actions**
3. **"New repository secret"** butonuna tıklayın
4. Şunları doldurun:
   - **Name:** `INSTAGRAM_ACCOUNT_ID`
   - **Secret:** Instagram Account ID'niz (yukarıdaki adımdan aldığınız, örnek: `17841405309211844`)
5. **"Add secret"** butonuna tıklayın

### 4️⃣ Test Edin

1. GitHub Actions'tan workflow'u çalıştırın
2. Hem Facebook hem Instagram'a post atılacak
3. Instagram'da post görünecek!

## ⚠️ Önemli Notlar

- Instagram Account ID sadece **sayılardan** oluşur (harf yok)
- Örnek format: `17841405309211844`
- Her Instagram Business Account'ın benzersiz bir ID'si vardır

## 🆘 Sorun mu var?

### "instagram_business_account" görünmüyor

**Çözüm:**
1. Instagram hesabınızın **Business Account** olduğundan emin olun
2. Facebook sayfanıza **bağlı** olduğundan emin olun (ekranda görünüyor ✅)
3. Token'ın **geçerli** olduğundan emin olun

### ID buldum ama çalışmıyor

**Kontrol:**
- ID'nin sadece sayılardan oluştuğundan emin olun
- GitHub Secret'ta doğru yazdığınızdan emin olun
- Başında/sonunda boşluk olmadığından emin olun

---

**Not:** Instagram hesabınız bağlı görünüyor, bu yüzden ID'yi bulmak çok kolay olacak! 🎉
