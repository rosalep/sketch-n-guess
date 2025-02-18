from django.urls import path
from . import views

# sub routes for profile
urlpatterns = [
    path('', views.home, name='user-home'), # temp home 
    path('about/', views.about, name='user-about'),
    path('login/', views.login_page, name='user-login'),
    path('profile/', views.profile, name='user-profile'),
    path('signup/', views.signup, name='user-signup'),
    path('logout/', views.logout_view, name='user-logout'),
]