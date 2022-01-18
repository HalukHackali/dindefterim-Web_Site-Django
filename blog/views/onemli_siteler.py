from django.shortcuts import render


def onemli_siteler(request):

    return render(request, 'pages/onemli-siteler.html', context={})