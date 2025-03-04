from django.urls import path, include
from game.consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]