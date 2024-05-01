from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def Registration(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    
    
    return render(request, 'account/registration.html')


def LogIn(request):
    if request.user.is_authenticated:
        return redirect('my_account')
    
    return render(request, 'account/login.html')

@login_required(login_url='/login/')
def my_account(request):
    return render(request, 'account/my_account.html')

