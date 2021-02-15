from django.shortcuts import render, redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from  django.contrib.auth.mixins import LoginRequiredMixin

class YaziEkleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi-ekle.html'
    model = YazilarModel
    fields = ('baslik', 'icerik', 'resim', 'etiketler', 'siniflar')

    def get_success_url(self):
        return reverse('detay', kwargs={
            'slug':self.object.slug
        })

    def form_valid(self, form):
        yazi = form.save(commit=False)
        yazi.yazar = self.request.user
        yazi.save()
        form.save_m2m()
        return super().form_valid(form)




# class YaziEkleCreateView(CreateView):
#     template_name = 'pages/yazi-ekle.html'
#     model = YazilarModel
#     fields = ('baslik', 'icerik', 'resim', 'kategoriler')
#
#     def get_success_url(self):
#         return reverse('detay', kwargs={
#             'slug':self.object.slug
#         })
#
#     def form_valid(self, form):
#         yazi = form.save(commit=False)
#         yazi.yazar = self.request.user
#         yazi.save()
#         form.save_m2m()
#         return super().form_valid(form)



############## CLASS BASE VIEW OLMADAN KULLANIM#################
# @login_required(login_url='/')
# def yazi_ekle(request):
#     form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
#     if form.is_valid():
#         yazi = form.save(commit=False)
#         yazi.yazar = request.user
#         yazi.save()
#         form.save_m2m()
#         return redirect('detay', slug=yazi.slug)
#
#     return render(request, 'pages/yazi-ekle.html', context={
#         'form': form
#     })

