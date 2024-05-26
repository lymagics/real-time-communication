from django.db import transaction
from django.urls import path

from django_eventstream import send_event
from rest_framework.generics import UpdateAPIView

from database.models.match import Match
from schemas.match import MatchSchema


class MatchRetrieveUpdateAPIView(UpdateAPIView):
    serializer_class = MatchSchema
    queryset = Match.objects.all()

    def perform_update(self, serializer):
        with transaction.atomic():
            match = serializer.save()
            send_event(f'match-{match.pk}', 'match_updated', serializer.data),


urlpatterns = [
    path('<int:pk>/', MatchRetrieveUpdateAPIView.as_view()),
]
