from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

# displays profile info
def profile(request): # user account 
    return render(request, 'users/profile.html')

def login_page(request):
    if request.method == "POST": # form has been submitted
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            # username=form.cleaned_data.get('username')
            # messages.success(request, f'Account Created, Welcome {username}')
            return redirect("user-profile")
        
    else: 
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

def signup(request):
    if request.method == "POST": # form has been submitted
        form = UserRegisterForm(request.POST) # custom form
        if form.is_valid():
            login(request, form.save()) # saves new user & auto logs in
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account Created, Welcome {username}')
            return redirect("user-profile")
        
    else: 
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form':form})


def logout_view(request):
    messages.success(request, "You have been successfully logged out.")
    logout(request)
    return redirect('/')  


