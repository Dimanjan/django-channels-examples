from django.urls import path
from .consumers import PositionsConsumer

ws_urlpatterns = [
    path('ws/positions/',PositionsConsumer.as_asgi()),
]