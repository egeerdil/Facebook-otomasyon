#!/usr/bin/env python3
"""
Facebook Graph API ile otomatik post atma scripti
GitHub Actions ile çalışacak şekilde tasarlandı
"""

import os
import requests
import json
from datetime import datetime


def post_to_facebook(page_id, access_token, message):
    """
    Facebook sayfasına post atar
    
    Args:
        page_id: Facebook sayfa ID'si
        access_token: Page Access Token
        message: Post mesajı
    
    Returns:
        dict: API yanıtı
    """
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
    
    print(f"📝 Post mesajı: {message}")
    print(f"📅 Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Facebook'a post at
    result = post_to_facebook(page_id, access_token, message)
    
    print(f"✅ Post başarıyla atıldı!")
    print(f"📌 Post ID: {result.get('id', 'N/A')}")
    print(f"🔗 Post URL: https://facebook.com/{result.get('id', '')}")
    
    return result


if __name__ == "__main__":
    main()
