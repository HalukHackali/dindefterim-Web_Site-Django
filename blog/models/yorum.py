from django.db import models
from blog.models import YazilarModel
from blog.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.CharField(max_length=250)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Yorum'
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.yazan.username

