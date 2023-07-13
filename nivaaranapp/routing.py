from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers.model_consumers import DetectionWebSocket


routes = URLRouter([
    path("dashboard/", DetectionWebSocket.as_asgi()),
    
    # path("views/")
    # path("chat/", PublicChatConsumer.as_asgi()),
])
