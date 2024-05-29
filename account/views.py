from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, CustomerLoginForm
from django.contrib.auth import login, logout


def Registration(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'Customer'
            user.save()
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'account/registration.html', context)


def LogIn(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    
    form = CustomerLoginForm()
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            
            if user.user_type == 'Customer':
                login(request, user)
                # print(user)
                # return redirect(request.META['HTTP_REFERER'])
                return redirect('my_account')
            else:
                messages.warning(request, 'This is not customer accounts!')
                return redirect(request.META['HTTP_REFERER'])

    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required(login_url='/login/')
def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login/')
def my_account(request):
    return render(request, 'account/my_account.html')



# from django.contrib.auth.views import LoginView
# class LogIn(LoginView):
#     authentication_form = CustomerLoginForm
#     template_name = 'account/login.html'

