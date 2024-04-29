from django.contrib import admin
from .models import *

admin.site.register(Home_Page_Slider)
admin.site.register(Header_Offer_Title)
admin.site.register(Home_Page_Settings)
admin.site.register(Footer_Contact_US)
admin.site.register(Footer_Useful_Links)
admin.site.register(Footer_Social_Link)


@admin.register(Blog_Model)
class Blog_Model(admin.ModelAdmin):
    list_display = ['title', 'is_active','created_date', 'updated_date']
    list_filter = ['is_active', 'created_date', 'updated_date']
    search_fields = ['title']

