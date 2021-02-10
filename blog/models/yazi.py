from  django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel):
    baslik = models.CharField(max_length=150)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from='baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    resim = models.ImageField(upload_to='yazi_resimleri')
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')

    class Meta:
        db_table = 'Yazi'
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'

    def __str__(self):
        return self.baslik
