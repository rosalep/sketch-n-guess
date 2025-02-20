from django.urls import path
from . import views

# sub routes for profile
urlpatterns = [
    path('', views.game, name='game-home'), # drawing board and teams
]