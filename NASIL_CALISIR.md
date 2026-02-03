# 🔄 Sistem Nasıl Çalışır?

## 📅 Günlük Post Sistemi

**ÖNEMLİ:** Her gün sadece **BİR** post atılır!

### Örnek: 3 Fotoğraf + 3 Mesaj

Eğer 3 fotoğraf + 3 mesajınız varsa:

```
POST_IMAGE_POSTS='https://i.imgur.com/foto1.jpg|🌅 Günaydın!,https://i.imgur.com/foto2.jpg|✨ Yeni gün!,https://i.imgur.com/foto3.jpg|🚀 Başarılar!'
```

**Çalışma şekli:**

- **1. Gün:** Fotoğraf 1 + "🌅 Günaydın!" → **1 POST**
- **2. Gün:** Fotoğraf 2 + "✨ Yeni gün!" → **1 POST**
- **3. Gün:** Fotoğraf 3 + "🚀 Başarılar!" → **1 POST**
- **4. Gün:** Fotoğraf 1 + "🌅 Günaydın!" → **1 POST** (tekrar başlar)
- **5. Gün:** Fotoğraf 2 + "✨ Yeni gün!" → **1 POST**
- ... (sonsuz döngü)

## 📊 Özet

| Fotoğraf Sayısı | Her Gün Atılan Post | Döngü Süresi |
|-----------------|---------------------|--------------|
| 1 fotoğraf | 1 post | Her gün aynı |
| 3 fotoğraf | 1 post | 3 günde bir döngü |
| 10 fotoğraf | 1 post | 10 günde bir döngü |
| 30 fotoğraf | 1 post | 30 günde bir döngü |

## ❓ Sık Sorulan Sorular

### S: 3 fotoğrafın hepsi aynı gün paylaşılır mı?
**C:** Hayır! Her gün sadece **BİR** fotoğraf paylaşılır. 3 günde bir döngü tamamlanır.

### S: Aynı gün 3 post atmak istiyorum, nasıl yaparım?
**C:** Şu anda sistem bunu desteklemiyor. Her gün sadece 1 post atılır. Aynı gün 3 post atmak için:
- Workflow'u 3 kez çalıştırmanız gerekir (manuel olarak)
- Veya kodda değişiklik yapmanız gerekir

### S: Her gün farklı fotoğraf nasıl seçiliyor?
**C:** Sistem günün index'ine göre otomatik seçer:
- 1. gün → 1. fotoğraf
- 2. gün → 2. fotoğraf
- 3. gün → 3. fotoğraf
- 4. gün → 1. fotoğraf (tekrar başlar)

### S: Fotoğraf sırasını değiştirebilir miyim?
**C:** Evet! GitHub Secrets'ta `POST_IMAGE_POSTS` secret'ını güncelleyerek sırayı değiştirebilirsiniz.

## 🎯 Örnek Senaryolar

### Senaryo 1: Haftalık Döngü (7 Fotoğraf)
```
7 fotoğraf → Her gün 1 post → 7 günde bir döngü
Pazartesi: Fotoğraf 1
Salı: Fotoğraf 2
Çarşamba: Fotoğraf 3
...
Pazar: Fotoğraf 7
Pazartesi: Fotoğraf 1 (tekrar)
```

### Senaryo 2: Aylık Döngü (30 Fotoğraf)
```
30 fotoğraf → Her gün 1 post → 30 günde bir döngü
1. Gün: Fotoğraf 1
2. Gün: Fotoğraf 2
...
30. Gün: Fotoğraf 30
31. Gün: Fotoğraf 1 (tekrar)
```

### Senaryo 3: Yıllık Döngü (365 Fotoğraf)
```
365 fotoğraf → Her gün 1 post → 365 günde bir döngü
Her gün farklı bir fotoğraf!
```

## 💡 İpuçları

1. **Daha sık tekrar için:** Daha az fotoğraf kullanın (örnek: 7 fotoğraf = haftalık döngü)

2. **Daha az tekrar için:** Daha fazla fotoğraf kullanın (örnek: 365 fotoğraf = yıllık döngü)

3. **Aynı gün birden fazla post:** Şu anda desteklenmiyor, kod değişikliği gerekir

4. **Manuel test:** GitHub Actions'tan workflow'u birden fazla kez çalıştırarak farklı fotoğrafları test edebilirsiniz

---

**Özet:** Her gün sadece **1 post** atılır, ama her gün **farklı bir fotoğraf + mesaj** kombinasyonu kullanılır! 🎯
