from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    return render(request, 'users/register.html',{'form':form})
from django.contrib.auth import logout
def logoutUser(request):
    logout(request)
    messages.success(request, f'Successfully logged out')
    return redirect('login')

# Create your views here