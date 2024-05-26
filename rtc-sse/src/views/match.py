from django.views.generic import DetailView
from django.urls import path

from database.models.match import Match


class MatchDetailView(DetailView):
    model = Match
    template_name = 'match.html'


urlpatterns = [
    path('<int:pk>/', MatchDetailView.as_view()),
]
