from django import template
from blog.models import KonuModel

register = template.Library()

@register.simple_tag
def konu_list():
    konular = KonuModel.objects.all()
    return konular