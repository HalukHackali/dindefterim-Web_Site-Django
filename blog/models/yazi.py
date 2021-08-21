from django.db import models
from autoslug import AutoSlugField
from .sinif_model import SinifModel
from blog.models import KonuModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel):
    baslik = models.CharField(max_length=150)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from='baslik', unique=True)
    konular = models.ManyToManyField(KonuModel, related_name='yazi')
    resim = models.ImageField(upload_to='yazi_resimleri')
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yazilar')
    siniflar = models.ForeignKey(SinifModel, null=True, on_delete=models.DO_NOTHING, related_name='yazi')
    hit = models.PositiveIntegerField(default=0)
    yayinlandi = models.BooleanField(default=True)
    likes = models.ManyToManyField('account.CustomUserModel', related_name='blog_post')

    class Meta:
        db_table = 'Yazi'
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'

    def __str__(self):
        return self.baslik

    def comment_count(self):
        return self.yorumlar.all().count()

    def total_likes(self):
        return self.likes.count()




