from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Custom_User
from django.contrib.auth import authenticate
from .models import Custom_User

class CustomerLoginForm(forms.Form):
    email = forms.EmailField(
        label=("Email"),
        widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Enter Your email'})
    )
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your password'}))
    
    user_cache = None
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        try:
            user = Custom_User.objects.get(email=email)
        except Custom_User.DoesNotExist:
            raise forms.ValidationError('Email does not match any account!')
        
        self.user_cache = authenticate(email=email, password=password)
        
        if self.user_cache is None:
            raise forms.ValidationError('Incorrect password!')
        
        return cleaned_data

    def get_user(self):
        return self.user_cache

# class CustomerLoginForm(forms.Form):
#     email = forms.EmailField(label='Your Email Address', max_length=200, widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}
#     ))
#     password = forms.CharField(
#         label=("Password"), max_length=50,
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control', 'placeholder': 'Enter Your Password'}),
#     )
#     # user_cache = None
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         print('---------------------------------------------------')
#         print(email)
#         user = authenticate(email, self.cleaned_data.get('password'))
#         if user is not None:
#             if user.user_type != 'Customer':
#                 raise ValueError('This is not a customer account.')
#         else:
#             raise ValueError('Invalid email or password.')
#         return email
    
#     # def clean(self):
#     #     email = self.cleaned_data.get('email')
#     #     password = self.cleaned_data.get('password')
        
#     #     if User_Model.objects.get(email=email).DoesNotExist():
#     #         raise ValueError('Email Does not match!')
#     #     else:
#     #         self.user_cache = authenticate(email=email, password=password)
            
#     #         if self.user_cache is None:
#     #             raise ValueError('Incorrect Passwrod!')
#     #         else:
#     #             self.confirm_login_allowed(self.user_cache)
        
#     #     return self.cleaned_data
        
#     # def confirm_login_allowed(self, user):
#     #     if not user.is_active:
#     #         raise ValidationError(
#     #             self.error_messages["inactive"],
#     #             code="inactive",
#     #         )
    
#     # def get_user(self):
#     #     return self.user_cache
    
        
    

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Name'}
    ))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Username'}
    ))
    email = forms.EmailField(label='Email', max_length=200, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Email'}
    ))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password Repeat'}),
    )
    
    class Meta:
        model = Custom_User
        fields = ['first_name', 'username', 'email']

