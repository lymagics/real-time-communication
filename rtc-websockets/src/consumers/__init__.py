from django.urls import path

from consumers.match import MatchConsumer

websocket_urlpatterns = [
    path('ws/matches/<match_id>/', MatchConsumer.as_asgi()),
]
