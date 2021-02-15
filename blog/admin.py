from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel, SinifModel

# Register your models here.

admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ( 'baslik', 'siniflar', 'olusturulma_tarihi', 'duzenlenme_tarihi', 'yazar')

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yazan', 'olusturulma_tarihi', 'duzenlenme_tarihi')
    search_fields = ('yazan__username',)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email', 'olusturulma_tarihi')
    search_fields = ('email',)

@admin.register(SinifModel)
class SinifAdmin(admin.ModelAdmin):
    list_display = ('isim', 'slug')