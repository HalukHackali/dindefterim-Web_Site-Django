from django import template
from blog.models import SinifModel

register = template.Library()

@register.simple_tag
def sinif_list():
    siniflar = SinifModel.objects.all()
    return siniflar