import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from chat.rounting import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_assincrono.settings")

django_asgi_app = get_asgi_application()

import chat.rounting

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)
