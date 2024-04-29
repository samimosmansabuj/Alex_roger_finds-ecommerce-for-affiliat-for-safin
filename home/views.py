from django.shortcuts import render, HttpResponse
from .models import Home_Page_Settings
from product.models import *

def home(request):
    context = {}
    return render(request, 'index.html', context)




