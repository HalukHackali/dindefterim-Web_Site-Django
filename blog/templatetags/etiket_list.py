from django import template
from  blog.models import EtiketModel

register = template.Library()

@register.simple_tag
def etiket_list():
    etiketler = EtiketModel.objects.all()
    return etiketler
