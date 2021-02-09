from django.contrib import admin
from blog.models import KategoriModel
from blog.models import YazilarModel

# Register your models here.

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = ('baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi', 'yazar')

admin.site.register(YazilarModel, YazilarAdmin)