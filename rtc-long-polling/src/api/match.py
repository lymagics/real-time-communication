from time import sleep

from django.urls import path

from rest_framework.generics import RetrieveUpdateAPIView

from database.models.match import Match
from schemas.match import MatchSchema, MatchUpdatedAt


class MatchRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = MatchSchema
    queryset = Match.objects.all()

    def get_object(self):
        schema = MatchUpdatedAt(data=self.request.query_params)
        schema.is_valid(raise_exception=True)

        updated_at = schema.validated_data.get('updated_at', None)
        if updated_at is None:
            return super().get_object()

        while True:
            match = super().get_object()
            if match.updated_at > updated_at:
                return match
            sleep(3.0)


urlpatterns = [
    path('<int:pk>/', MatchRetrieveUpdateAPIView.as_view()),
]
