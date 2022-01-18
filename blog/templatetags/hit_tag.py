from django import template
from blog.models import YazilarModel

register = template.Library()

@register.simple_tag(name='hit_tags')
def hit_tags():
    return YazilarModel.objects.order_by('-hit')[:4]