from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('Customer', 'Customer')
    )
    
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=20)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.username

class User_Authentication_Verification(models.Model):
    user = models.OneToOneField(Custom_User, related_name='authentication_verification',on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=400, blank=True, null=True)
    otp = models.IntegerField(null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)
    
    def set_otp(self, otp):
        self.otp = otp
        self.otp_expiry = timezone.now() + datetime.timedelta(minutes=5)    # OTP expires in 5 minutes
        self.save()
    
    def verify_otp(self, otp):
        if timezone.now() <= self.otp_expiry and self.otp == otp:
            self.otp = None     # Clear OTP after successful verification
            self.user.is_verified = True
            self.user.save()
            self.save()
            return True
        else:
            return False
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} profile authentication verification file'



@receiver(post_save, sender=Custom_User)
def create_customer_or_admin_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Customer':
            Customer_Profile.objects.create(user=instance, email=instance.email)
        elif instance.user_type == 'Admin' or instance.user_type == 'Staff':
            AdminStaff_Profile.objects.create(user=instance, email=instance.email)


class Customer_Profile(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    user = models.ForeignKey(Custom_User, related_name='customer_profile', on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='customer/profile-picture/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"

class AdminStaff_Profile(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    user = models.ForeignKey(Custom_User, related_name='staff_profile', on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    designation = models.CharField(max_length=20, blank=True, null=True)
    nid = models.CharField(max_length=15, blank=True, null=True)
    nid_copy = models.ImageField(upload_to='admin/staff-nid-copy/', blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
    


