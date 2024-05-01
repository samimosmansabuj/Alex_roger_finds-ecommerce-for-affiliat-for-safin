from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', Registration, name='registration'),
    path('login/', LogIn, name='login'),
    path('my-account/', my_account, name='my_account'),
]