from django.urls import path
from blog.views import kategori, yazilarim, anasayfa, iletisim, detay, yorum_sil, yazi_sil, yazi_guncelle, yazi_ekle
from django.views.generic import TemplateView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('hakkimda', TemplateView.as_view(template_name="pages/hakkimda.html"), name='hakkimda'),
    path('iletisim', iletisim, name= 'iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yorum-sil/<int:id>', yorum_sil, name='yorum-sil'),
    path('yazi-ekle', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle, name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', yazi_sil, name='yazi-sil'),



]