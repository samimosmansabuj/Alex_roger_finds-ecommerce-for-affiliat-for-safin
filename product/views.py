from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

# Create your views here.
def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'product/product_details.html', context)


@login_required(login_url='/login/')
def add_to_fav(request, id):
    product = get_object_or_404(Product, id=id)
    
    if Fav_List.objects.filter(user=request.user).exists():
        fav_list = get_object_or_404(Fav_List, user=request.user)
        fav_list.product.add(product)
        fav_list.save()
    else:
        new_fav = Fav_List.objects.create(user=request.user)
        new_fav.product.add(product)
        new_fav.save()
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='/login/')
def remove_to_fav(request, id):
    product = get_object_or_404(Product, id=id)
    
    if Fav_List.objects.filter(user=request.user).exists():
        fav_list = get_object_or_404(Fav_List, user=request.user)
        if fav_list.product.filter(id=product.id).exists():
            fav_list.product.remove(product)
    
    return redirect(request.META['HTTP_REFERER'])



def buy_now_click_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        Buy_Now_Click.objects.create(user=request.user, product=product)
    else:
        # Generate a unique identifier for the anonymous user
        anonymous_identifier = request.session.get('anonymous_identifier')
        if not anonymous_identifier:
            request.session['anonymous_identifier'] = get_random_string(32)
        
        Buy_Now_Click.objects.create(anonymous_identifier=anonymous_identifier, product=product)
    
    return redirect(request.META['HTTP_REFERER'])


