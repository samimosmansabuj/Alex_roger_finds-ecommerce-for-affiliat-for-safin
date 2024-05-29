from .models import Home_Page_Settings, Footer_Contact_US, Footer_Useful_Links, Footer_Social_Link, Blog_Model
from product.models import Product, Category, Fav_List
from django.shortcuts import get_object_or_404

def home_page_settings(request):
    home_page = Home_Page_Settings.objects.all().first()
    footer_contact_us = Footer_Contact_US.objects.all().first()
    footer_useful_links = Footer_Useful_Links.objects.filter(is_active=True)[:5]
    footer_social_links = Footer_Social_Link.objects.all().first()
    blogs = Blog_Model.objects.filter(is_active=True)
    return {'home_page': home_page, 'footer_contact_us': footer_contact_us, 'footer_useful_links': footer_useful_links, 'footer_social_links': footer_social_links, 'blogs': blogs}


def Product_Category_Cart(request):
    all_category = Category.objects.filter(is_active=True)
    all_product = Product.objects.filter(is_active=True)
    context = {'all_category': all_category, 'all_product': all_product}
    
    if request.user.is_authenticated:
        if Fav_List.objects.filter(user=request.user).exists():
            favourite_list = get_object_or_404(Fav_List, user=request.user)
        else:
            favourite_list = None
        
        context['favourite_list'] = favourite_list
    
    return context

