from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.
def intro(request):
    return render(request, 'web/intro.html')

def test(request):
    return render(request, 'web/test.html')

def base(request):
    return render(request, 'web/base.html')