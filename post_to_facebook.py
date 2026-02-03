#!/usr/bin/env python3
"""
Facebook Graph API ile otomatik post atma scripti
GitHub Actions ile çalışacak şekilde tasarlandı
"""

import os
import requests
import json
import tempfile
import mimetypes
from datetime import datetime
from io import BytesIO


def post_to_facebook(page_id, access_token, message, image_url=None):
    """
    Facebook sayfasına post atar (fotoğraflı veya fotoğrafsız)
    
    Args:
        page_id: Facebook sayfa ID'si
        access_token: Page Access Token
        message: Post mesajı
        image_url: (Opsiyonel) Fotoğraf URL'si veya dosya yolu
    
    Returns:
        dict: API yanıtı
    """
    # Eğer fotoğraf varsa /photos endpoint'ini kullan
    if image_url:
        url = f"https://graph.facebook.com/v18.0/{page_id}/photos"
        
        payload = {
            'message': message,
            'access_token': access_token
        }
        
        # URL'den fotoğraf yükleme
        if image_url.startswith('http://') or image_url.startswith('https://'):
            try:
                # Önce URL yöntemini dene (daha hızlı)
                print(f"📥 Fotoğraf URL'si ile yükleniyor: {image_url}")
                payload_with_url = payload.copy()
                payload_with_url['url'] = image_url
                
                try:
                    response = requests.post(url, data=payload_with_url)
                    response.raise_for_status()
                    result = response.json()
                    print(f"✅ Fotoğraf URL yöntemi ile başarıyla yüklendi!")
                    return result
                except requests.exceptions.HTTPError as url_error:
                    # URL yöntemi başarısız oldu, dosya yöntemini dene
                    print(f"⚠️ URL yöntemi başarısız, dosya yöntemi deneniyor...")
                    if hasattr(url_error, 'response') and url_error.response is not None:
                        error_data = url_error.response.json()
                        if error_data.get('error', {}).get('error_subcode') == 1366046:
                            # "Can't Read Files" hatası - dosya yöntemini kullan
                            pass
                        else:
                            raise
                    
                    # Fotoğrafı indir
                    print(f"📥 Fotoğraf indiriliyor...")
                    img_response = requests.get(image_url, timeout=30, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                        'Accept': 'image/*'
                    })
                    img_response.raise_for_status()
                    
                    # Dosya boyutunu kontrol et (10 MB limit)
                    file_size = len(img_response.content)
                    if file_size > 10 * 1024 * 1024:
                        raise ValueError(f"Fotoğraf çok büyük: {file_size / (1024*1024):.2f} MB (Maksimum: 10 MB)")
                    
                    print(f"✅ Fotoğraf indirildi ({file_size / 1024:.2f} KB)")
                    
                    # Content-Type'ı belirle
                    content_type = img_response.headers.get('Content-Type', '')
                    if not content_type or not content_type.startswith('image/'):
                        # URL'den dosya uzantısını al
                        ext = os.path.splitext(image_url.split('?')[0])[1].lower()
                        if ext in ['.jpg', '.jpeg']:
                            content_type = 'image/jpeg'
                        elif ext == '.png':
                            content_type = 'image/png'
                        elif ext == '.gif':
                            content_type = 'image/gif'
                        elif ext == '.webp':
                            content_type = 'image/webp'
                        else:
                            # İçeriği kontrol et
                            if img_response.content[:4] == b'\xff\xd8\xff\xe0':
                                content_type = 'image/jpeg'
                            elif img_response.content[:8] == b'\x89PNG\r\n\x1a\n':
                                content_type = 'image/png'
                            else:
                                content_type = 'image/jpeg'  # Varsayılan
                    
                    print(f"📋 Dosya tipi: {content_type}")
                    
                    # Dosya adını belirle
                    filename = 'image.jpg'
                    if content_type == 'image/png':
                        filename = 'image.png'
                    elif content_type == 'image/gif':
                        filename = 'image.gif'
                    elif content_type == 'image/webp':
                        filename = 'image.webp'
                    
                    # Dosyayı BytesIO ile yükle
                    image_data = BytesIO(img_response.content)
                    image_data.seek(0)
                    
                    # Facebook'a yükle
                    files = {
                        'source': (filename, image_data, content_type)
                    }
                    
                    print(f"📤 Facebook'a dosya olarak yükleniyor...")
                    response = requests.post(url, data=payload, files=files)
                    response.raise_for_status()
                    result = response.json()
                    
                    print(f"✅ Fotoğraf başarıyla yüklendi!")
                    return result
                
            except requests.exceptions.RequestException as e:
                print(f"❌ Fotoğraf indirme/yükleme hatası: {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"Yanıt: {e.response.text}")
                raise
            except Exception as e:
                print(f"❌ Beklenmeyen hata: {e}")
                raise
        else:
            # Dosya yolu ise dosyayı yükle
            with open(image_url, 'rb') as image_file:
                files = {'source': image_file}
                try:
                    response = requests.post(url, data=payload, files=files)
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as e:
                    print(f"❌ Hata: {e}")
                    if hasattr(e, 'response') and e.response is not None:
                        print(f"Yanıt: {e.response.text}")
                    raise
    else:
        # Fotoğraf yoksa normal post
        url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
        
        payload = {
            'message': message,
            'access_token': access_token
        }
        
        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Hata: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Yanıt: {e.response.text}")
            raise


def get_daily_message():
    """
    Günlük post mesajını oluşturur
    Bu fonksiyonu kendi ihtiyaçlarınıza göre özelleştirebilirsiniz
    """
    today = datetime.now()
    date_str = today.strftime("%d.%m.%Y")
    
    # Örnek mesaj - kendi mesajınızı buraya yazabilirsiniz
    messages = [
        f"🌅 Günaydın! Bugün {date_str} - Harika bir gün olsun!",
        f"✨ Yeni bir gün, yeni fırsatlar! {date_str}",
        f"🚀 Bugün {date_str} - Hedeflerinize bir adım daha yaklaşın!",
    ]
    
    # Günün index'ine göre mesaj seç (her gün farklı mesaj)
    day_index = today.timetuple().tm_yday % len(messages)
    return messages[day_index]


def main():
    """
    Ana fonksiyon
    Environment variable'lardan gerekli bilgileri alır
    """
    # Facebook Page ID
    page_id = os.getenv('FACEBOOK_PAGE_ID')
    if not page_id:
        raise ValueError("FACEBOOK_PAGE_ID environment variable bulunamadı!")
    
    # Facebook Page Access Token
    access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
    if not access_token:
        raise ValueError("FACEBOOK_ACCESS_TOKEN environment variable bulunamadı!")
    
    # Post mesajı (opsiyonel - yoksa otomatik oluşturulur)
    message = os.getenv('POST_MESSAGE')
    if not message:
        message = get_daily_message()
    
    # Fotoğraf URL'si ve mesajı (opsiyonel)
    # Önce çoklu fotoğraf+mesaj listesini kontrol et
    image_posts_str = os.getenv('POST_IMAGE_POSTS')  # Format: "URL|MESAJ,URL|MESAJ"
    image_urls_str = os.getenv('POST_IMAGE_URLS')  # Virgülle ayrılmış sadece URL listesi
    single_image_url = os.getenv('POST_IMAGE_URL')  # Tek fotoğraf
    
    image_url = None
    selected_message = message  # Varsayılan olarak mevcut mesajı kullan
    
    # Eğer fotoğraf+mesaj eşleştirmesi varsa (en öncelikli)
    if image_posts_str:
        # Format: "URL1|MESAJ1,URL2|MESAJ2,..."
        posts = []
        for post_str in image_posts_str.split(','):
            post_str = post_str.strip()
            if '|' in post_str:
                parts = post_str.split('|', 1)  # İlk | karakterinden böl
                img_url = parts[0].strip()
                post_msg = parts[1].strip() if len(parts) > 1 else message
                posts.append({'url': img_url, 'message': post_msg})
        
        if posts:
            today = datetime.now()
            # Günün index'ine göre post seç (yılın kaçıncı günü + saat + dakika)
            # Bu sayede aynı gün içinde farklı çalıştırmalarda farklı post seçilir
            day_of_year = today.timetuple().tm_yday
            hour = today.hour
            minute = today.minute
            # Her saat ve dakikaya göre farklı index hesapla
            index = (day_of_year * 24 * 60 + hour * 60 + minute) % len(posts)
            selected_post = posts[index]
            image_url = selected_post['url']
            selected_message = selected_post['message']
            print(f"📸 Toplam {len(posts)} fotoğraf+mesaj var, {index + 1}. post seçildi")
            print(f"📝 Seçilen mesaj: {selected_message}")
            print(f"⏰ Seçim zamanı: {today.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Eğer sadece fotoğraf listesi varsa (mesaj yok)
    elif image_urls_str:
        image_urls = [url.strip() for url in image_urls_str.split(',') if url.strip()]
        if image_urls:
            today = datetime.now()
            # Günün index'ine göre fotoğraf seç (yılın kaçıncı günü + saat + dakika)
            day_of_year = today.timetuple().tm_yday
            hour = today.hour
            minute = today.minute
            index = (day_of_year * 24 * 60 + hour * 60 + minute) % len(image_urls)
            image_url = image_urls[index]
            print(f"📸 Toplam {len(image_urls)} fotoğraf var, {index + 1}. fotoğraf seçildi")
            print(f"⏰ Seçim zamanı: {today.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Tek fotoğraf varsa
    elif single_image_url:
        image_url = single_image_url
    
    print(f"📝 Post mesajı: {selected_message}")
    if image_url:
        print(f"🖼️ Fotoğraf URL'si: {image_url}")
    print(f"📅 Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Facebook'a post at
    result = post_to_facebook(page_id, access_token, selected_message, image_url)
    
    print(f"✅ Post başarıyla atıldı!")
    print(f"📌 Post ID: {result.get('id', 'N/A')}")
    print(f"🔗 Post URL: https://facebook.com/{result.get('id', '')}")
    
    return result


if __name__ == "__main__":
    main()
