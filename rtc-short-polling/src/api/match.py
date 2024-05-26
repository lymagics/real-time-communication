from django.urls import path

from rest_framework.generics import RetrieveUpdateAPIView

from database.models.match import Match
from schemas.match import MatchSchema


class MatchRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MatchSchema
    queryset = Match.objects.all()


urlpatterns = [
    path('<int:pk>/', MatchRetrieveUpdateAPIView.as_view()),
]
