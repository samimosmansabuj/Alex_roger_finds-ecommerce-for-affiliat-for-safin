from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/<slug>/', product_details, name='product_details'),
    path('add-to-fav/<int:id>/', add_to_fav, name='add_to_fav'),
    path('remove-to-fav/<int:id>/', remove_to_fav, name='remove_to_fav'),
]