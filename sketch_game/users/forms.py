from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(UserCreationForm):
    # already has username and password fields
    email = forms.EmailField(required=True) # adds email field
    
    class Meta: # metadata about the model
        model = CustomUser
        fields = ['username', 'email']
    
    def get_user(self): # passes user info 
        username = self.cleaned_data.get('username')  
        password = self.cleaned_data.get('password')
        
        user = CustomUser.objects.get(username=username)  
        if user.check_password(password): # validates info
            return user
        else:
            return None   

class UpdateUserForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']


class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['bio']
