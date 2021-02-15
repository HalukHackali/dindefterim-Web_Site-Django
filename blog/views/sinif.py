from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, SinifModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class SinifListView(ListView):
    template_name = 'pages/sinif.html'
    context_object_name = 'yazilar'
    paginate_by = 4



    def get_queryset(self):
        sinif = get_object_or_404(SinifModel, slug=self.kwargs['sinifSlug'])
        return sinif.yazi.all().order_by('id')



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SinifListView, self).get_context_data(**kwargs)
        self.sinif = get_object_or_404(SinifModel, slug=self.kwargs['sinifSlug'])
        context['sinif'] = self.sinif
        return context
