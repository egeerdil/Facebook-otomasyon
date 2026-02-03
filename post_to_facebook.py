#!/usr/bin/env python3
"""
Facebook Graph API ile otomatik post atma scripti
GitHub Actions ile çalışacak şekilde tasarlandı
"""

import os
import requests
import json
import tempfile
from datetime import datetime


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
        
        # URL'den fotoğraf yükleme - önce indirip sonra yükle
        if image_url.startswith('http://') or image_url.startswith('https://'):
            try:
                print(f"📥 Fotoğraf indiriliyor: {image_url}")
                # Fotoğrafı indir
                img_response = requests.get(image_url, timeout=30, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                })
                img_response.raise_for_status()
                
                # Geçici dosya oluştur
                with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                    tmp_file.write(img_response.content)
                    tmp_path = tmp_file.name
                
                print(f"✅ Fotoğraf indirildi, yükleniyor...")
                
                # Dosyayı Facebook'a yükle
                with open(tmp_path, 'rb') as image_file:
                    files = {'source': image_file}
                    response = requests.post(url, data=payload, files=files)
                    response.raise_for_status()
                    result = response.json()
                
                # Geçici dosyayı sil
                os.unlink(tmp_path)
                return result
                
            except requests.exceptions.RequestException as e:
                print(f"❌ Fotoğraf indirme/yükleme hatası: {e}")
                if hasattr(e, 'response') and e.response is not None:
                    print(f"Yanıt: {e.response.text}")
                # Geçici dosyayı temizle
                if 'tmp_path' in locals():
                    try:
                        os.unlink(tmp_path)
                    except:
                        pass
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
    
    # Fotoğraf URL'si (opsiyonel)
    image_url = os.getenv('POST_IMAGE_URL')
    
    print(f"📝 Post mesajı: {message}")
    if image_url:
        print(f"🖼️ Fotoğraf URL'si: {image_url}")
    print(f"📅 Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Facebook'a post at
    result = post_to_facebook(page_id, access_token, message, image_url)
    
    print(f"✅ Post başarıyla atıldı!")
    print(f"📌 Post ID: {result.get('id', 'N/A')}")
    print(f"🔗 Post URL: https://facebook.com/{result.get('id', '')}")
    
    return result


if __name__ == "__main__":
    main()
