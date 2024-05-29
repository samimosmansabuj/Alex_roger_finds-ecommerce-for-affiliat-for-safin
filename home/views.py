from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import *

def home(request):
    context = {}
    print(request.user)
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def FavList(request):
    return render(request, 'list/fav_list.html')


