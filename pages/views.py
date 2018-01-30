from django.shortcuts import render
from pages.models import Pages
from django.core.exceptions import ObjectDoesNotExist


def about(request):
    try:
        about_page = Pages.objects.get(slug='about')
    except ObjectDoesNotExist:
        about_page = {'body': 'Nope'}
    return render(request, 'pages/about.html', {'about': about_page})
