from django.urls import path

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.generics import UpdateAPIView

from database.models.match import Match
from schemas.match import MatchSchema


class MatchRetrieveUpdateAPIView(UpdateAPIView):
    serializer_class = MatchSchema
    queryset = Match.objects.all()

    def perform_update(self, serializer):
        match = serializer.save()
        match_ref = f'match_{match.id}'

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(match_ref, {
            'type': 'match.updated',
            **MatchSchema(match).data,
        })


urlpatterns = [
    path('<int:pk>/', MatchRetrieveUpdateAPIView.as_view()),
]
