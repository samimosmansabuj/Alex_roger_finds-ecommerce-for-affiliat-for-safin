from django.db import models
from django.utils.text import slugify
from account.models import Custom_User
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='category/image/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='sub_category')
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='sub-category/image/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.title} sub category in {self.category.title}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='product_category')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.DO_NOTHING, related_name='product_sub_category')
    
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    discount_price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='product/image/')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title



class Fav_List(models.Model):
    user = models.ForeignKey(Custom_User, related_name='fav_list', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name='products')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username



class Buy_Now_Click(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='buy_now_click', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='buy_click_products', on_delete=models.CASCADE)
    anonymous_identifier = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username if self.user else self.anonymous_identifier



