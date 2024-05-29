from django.contrib import admin
from .models import *


@admin.register(Custom_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type', 'is_verified']
    list_filter = ['user_type', 'is_verified']
    search_fields = ['username', 'email', 'phone_number', 'user_type']


# admin.site.register(User_Authentication_Verification)
# admin.site.register(Customer_Profile)
# admin.site.register(AdminStaff_Profile)

