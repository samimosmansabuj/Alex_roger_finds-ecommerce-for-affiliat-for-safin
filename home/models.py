from django.db import models
from django.utils.text import slugify


class Home_Page_Slider(models.Model):
    image = models.ImageField(upload_to='home-page/slide/')
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.image.name


class Header_Offer_Title(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title


class Home_Page_Settings(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='home-page/logo/', blank=True, null=True)
    call_number = models.CharField(max_length=20, blank=True, null=True)
    offer_title = models.ManyToManyField(Header_Offer_Title, blank=True, null=True)
    slider = models.ManyToManyField(Home_Page_Slider, blank=True, null=True)
    
    category_title = models.CharField(max_length=100, default='All Categories')
    # category_section = models.ManyToManyField()
    
    product_title = models.CharField(max_length=100, default='Latest Product')
    product_description = models.TextField(blank=True, null=True)
    # product_category = models.ManyToManyField()
    
    blog_title = models.CharField(max_length=100, default='Latest Blog')
    blog_description = models.TextField(blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Home Page Setting - {self.id}"


class Footer_Contact_US(models.Model):
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=150)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    

class Footer_Useful_Links(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title


class Footer_Social_Link(models.Model):
    facebook = models.URLField(max_length=500, blank=True, null=True)
    twitter = models.URLField(max_length=500, blank=True, null=True)
    linkdin = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True,null=True)
    


class Blog_Model(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title


