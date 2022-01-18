from django.shortcuts import get_object_or_404, redirect

from blog.models import YazilarModel


def LikeView(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    yazi.likes.add(request.user)
    return redirect('detay', slug=slug)