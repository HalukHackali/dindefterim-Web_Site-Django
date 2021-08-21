from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KonuModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class KonuListView(ListView):
    template_name = 'pages/konu.html'
    context_object_name = 'yazilar'
    paginate_by = 4



    def get_queryset(self):
        konu = get_object_or_404(KonuListView, slug=self.kwargs['konuSlug'])
        return konu.yazi.all().order_by('id')



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(KonuListView, self).get_context_data(**kwargs)
        self.konu = get_object_or_404(KonuListView, slug=self.kwargs['konuSlug'])
        context['konu'] = self.konu
        return context






############## CLASS BASE VIEW OLMADAN KULLANIM#################
# def etiket(request, etiketSlug):
#     etiket = get_object_or_404(EtiketModel, slug=etiketSlug)
#     yazilar = etiket.yazi.order_by('-id')
#     sayfa = request.GET.get('sayfa')
#     paginator = Paginator(yazilar, 2)
#
#     return render(request, 'pages/konu.html', context={
#         'yazilar': paginator.get_page(sayfa),
#         'etiket_isim': etiket.isim
#     })
