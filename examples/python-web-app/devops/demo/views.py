from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'demo1_site.html')
    return render(request, 'demo1_site.html')
