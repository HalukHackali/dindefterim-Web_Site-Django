from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, EtiketModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class EtiketListView(ListView):
    template_name = 'pages/etiket.html'
    context_object_name = 'yazilar'
    paginate_by = 4



    def get_queryset(self):
        etiket = get_object_or_404(EtiketModel, slug=self.kwargs['etiketSlug'])
        return etiket.yazi.all().order_by('id')



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EtiketListView, self).get_context_data(**kwargs)
        self.etiket = get_object_or_404(EtiketModel, slug=self.kwargs['etiketSlug'])
        context['etiket'] = self.etiket
        return context






############## CLASS BASE VIEW OLMADAN KULLANIM#################
# def etiket(request, etiketSlug):
#     etiket = get_object_or_404(EtiketModel, slug=etiketSlug)
#     yazilar = etiket.yazi.order_by('-id')
#     sayfa = request.GET.get('sayfa')
#     paginator = Paginator(yazilar, 2)
#
#     return render(request, 'pages/etiket.html', context={
#         'yazilar': paginator.get_page(sayfa),
#         'etiket_isim': etiket.isim
#     })
