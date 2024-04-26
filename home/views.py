from django.shortcuts import render, HttpResponse
from .models import Home_Page_Settings

def home(request):
    context = {}
    home_page = Home_Page_Settings.objects.all().first()
    context['home_page'] = home_page
    
    return render(request, 'index.html', context)

