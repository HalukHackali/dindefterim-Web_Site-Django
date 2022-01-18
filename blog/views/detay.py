from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import YazilarModel, KonuModel
from blog.forms import YorumEkleModelForm
from django.views import View
from django.contrib import messages
import logging
from django.views.generic import ListView

logger = logging.getLogger('konu_okuma')


class DetayView(View):
    http_method_names = ['get', 'post']
    yorum_ekle_form = YorumEkleModelForm
    yazi = YazilarModel

    def get(self, request, slug, *args, **kwargs):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        self.total_likes = yazi.total_likes()
        self.hit = YazilarModel.objects.filter(slug=self.kwargs['slug']).update(hit=F('hit') + 1)

        if request.user.is_authenticated:
            logger.info('konu okundu ' + request.user.username)

        yorumlar = yazi.yorumlar.all().order_by('-id')
        return render(request, 'pages/detay.html', context={
            'yazi': yazi,
            'yorumlar': yorumlar,
            'yorum_ekle_form': self.yorum_ekle_form()
        })




    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorum_ekle_form = self.yorum_ekle_form(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
            messages.success(request, 'Yorumunuz eklendi')
        return redirect('detay', slug=slug)




############## CLASS BASE VIEW OLMADAN KULLANIM#################
# def detay(request, slug):
#    yazi = get_object_or_404(YazilarModel, slug=slug)
#    yorumlar = yazi.yorumlar.all()
#
#    if request.method == 'POST':
#        yorum_ekle_form = YorumEkleModelForm(data=request.POST)
#        if yorum_ekle_form.is_valid():
#            yorum = yorum_ekle_form.save(commit=False)
#            yorum.yazan = request.user
#            yorum.yazi = yazi
#            yorum.save()
#    yorum_ekle_form = YorumEkleModelForm()
#
#   return render(request, 'pages/detay.html', context={
#        'yazi': yazi,
#        'yorumlar': yorumlar,
#        'yorum_ekle_form' : yorum_ekle_form
#    })