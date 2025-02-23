from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# sub routes for profile
urlpatterns = [
    path('', views.home, name='user-home'), # temp home 
    path('about/', views.about, name='user-about'),
    path('login/', views.login_page, name='user-login'),
    path('profile/', views.profile, name='user-profile'),
    path('profile/edit/', views.profileUpdate, name='user-profile-update'),
    path('signup/', views.signup, name='user-signup'),
    path('logout/', views.logout_view, name='user-logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)