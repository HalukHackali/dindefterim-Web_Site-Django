from django.urls import path, include
from blog.views import kategori, yazilarim, anasayfa, iletisim, detay, yorum_sil, yazi_sil


urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name= 'iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yorum-sil/<int:id>', yorum_sil, name='yorum-sil'),
    path('yazi-sil/<slug:slug>', yazi_sil, name='yazi-sil'),
]