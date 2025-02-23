from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from .forms import UserRegisterForm,UpdateUserForm,UpdateProfileForm
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

def profileUpdate(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("user-profile")
        
    else:
        user_form=UpdateUserForm(instance=request.user)
        profile_form=UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profileUpdate.html', {'user_form': user_form, 'profile_form': profile_form})

