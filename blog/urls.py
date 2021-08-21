from django.urls import path
from blog.views import KonuListView, yazilarim, anasayfa, IletisimFormView, DetayView, yorum_sil, \
    YaziSilDeleteView, YaziGuncelleUpdateView, YaziEkleCreateView, onemli_siteler, SinifListView, LikeView
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('onemli-siteler', onemli_siteler, name='onemli-siteler'),
    path('hakkimda', TemplateView.as_view(template_name="pages/hakkimda.html"), name='hakkimda'),
    path('iletisim', IletisimFormView.as_view(), name= 'iletisim'),
    path('konu/<slug:konuSlug>', KonuListView.as_view(), name='konu'),
    path('sinif/<slug:sinifSlug>', SinifListView.as_view(), name='sinif'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('like/<slug:slug>', LikeView, name='like_post'),
    path('yorum-sil/<int:id>', yorum_sil, name='yorum-sil'),
    path('yazi-ekle', YaziEkleCreateView.as_view(), name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', YaziSilDeleteView.as_view(), name='yazi-sil'),
    path('email-gonderildi', TemplateView.as_view(
        template_name='pages/email-gonderildi.html'
    ), name='email-gonderildi'),

    # ÖNEMLİ SİTELER URLS
    path('meb', RedirectView.as_view(url="http://www.meb.gov.tr/"), name='meb'),



]