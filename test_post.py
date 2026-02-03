#!/usr/bin/env python3
"""
POST_IMAGE_POSTS'u manuel test etmek için script
"""

import os
from post_to_facebook import post_to_facebook, get_daily_message

def test_post_image_posts():
    """
    POST_IMAGE_POSTS formatını test eder
    """
    # Test için örnek POST_IMAGE_POSTS formatı
    # Format: "URL|MESAJ,URL|MESAJ,URL|MESAJ"
    test_posts = "https://i.imgur.com/foto1.jpg|🌅 Günaydın! Bugün harika bir gün!,https://i.imgur.com/foto2.jpg|✨ Yeni fırsatlar kapınızda!,https://i.imgur.com/foto3.jpg|🚀 Hedeflerinize ulaşın!"
    
    print("=" * 60)
    print("🧪 POST_IMAGE_POSTS Test Scripti")
    print("=" * 60)
    print()
    
    # Environment variable'ı set et
    os.environ['POST_IMAGE_POSTS'] = test_posts
    
    # Facebook bilgilerini al (eğer varsa)
    page_id = os.getenv('FACEBOOK_PAGE_ID')
    access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
    
    if not page_id or not access_token:
        print("⚠️  Facebook bilgileri bulunamadı!")
        print("📝 Lütfen şu environment variable'ları set edin:")
        print("   - FACEBOOK_PAGE_ID")
        print("   - FACEBOOK_ACCESS_TOKEN")
        print()
        print("💡 Örnek kullanım:")
        print("   export FACEBOOK_PAGE_ID='your_page_id'")
        print("   export FACEBOOK_ACCESS_TOKEN='your_token'")
        print("   python test_post.py")
        print()
        print("🔍 Test formatı kontrolü yapılıyor...")
        print()
        
        # Sadece format kontrolü yap
        image_posts_str = test_posts
        posts = []
        for post_str in image_posts_str.split(','):
            post_str = post_str.strip()
            if '|' in post_str:
                parts = post_str.split('|', 1)
                img_url = parts[0].strip()
                post_msg = parts[1].strip() if len(parts) > 1 else "Mesaj yok"
                posts.append({'url': img_url, 'message': post_msg})
        
        print(f"✅ Format doğru! {len(posts)} post bulundu:")
        print()
        for i, post in enumerate(posts, 1):
            print(f"  {i}. Fotoğraf: {post['url']}")
            print(f"     Mesaj: {post['message']}")
            print()
        
        return
    
    # Gerçek test
    print("📋 Test POST_IMAGE_POSTS formatı:")
    print(f"   {test_posts}")
    print()
    
    # Formatı parse et
    image_posts_str = test_posts
    posts = []
    for post_str in image_posts_str.split(','):
        post_str = post_str.strip()
        if '|' in post_str:
            parts = post_str.split('|', 1)
            img_url = parts[0].strip()
            post_msg = parts[1].strip() if len(parts) > 1 else get_daily_message()
            posts.append({'url': img_url, 'message': post_msg})
    
    if not posts:
        print("❌ Hiç post bulunamadı! Formatı kontrol edin.")
        return
    
    print(f"✅ {len(posts)} post bulundu:")
    print()
    for i, post in enumerate(posts, 1):
        print(f"  {i}. Fotoğraf: {post['url']}")
        print(f"     Mesaj: {post['message']}")
        print()
    
    # İlk postu test et
    print("=" * 60)
    print("🚀 İlk postu test ediyoruz...")
    print("=" * 60)
    print()
    
    first_post = posts[0]
    print(f"📝 Mesaj: {first_post['message']}")
    print(f"🖼️  Fotoğraf: {first_post['url']}")
    print()
    
    try:
        result = post_to_facebook(page_id, access_token, first_post['message'], first_post['url'])
        print()
        print("=" * 60)
        print("✅ TEST BAŞARILI!")
        print("=" * 60)
        print(f"📌 Post ID: {result.get('id', 'N/A')}")
        print(f"🔗 Post URL: https://facebook.com/{result.get('id', '')}")
    except Exception as e:
        print()
        print("=" * 60)
        print("❌ TEST BAŞARISIZ!")
        print("=" * 60)
        print(f"Hata: {e}")
        print()
        print("💡 Kontrol edin:")
        print("   - FACEBOOK_PAGE_ID doğru mu?")
        print("   - FACEBOOK_ACCESS_TOKEN geçerli mi?")
        print("   - Fotoğraf URL'si erişilebilir mi?")


if __name__ == "__main__":
    test_post_image_posts()
