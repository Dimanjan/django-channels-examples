from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notification-server/', consumers.NotificationConsumer.as_asgi()),
]