from rest_framework import serializers

from database.models.match import Match


class MatchSchema(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'away_team', 'home_team', 'away_score', 'home_score',)
        read_only_fields = ('id', 'away_team', 'home_team',)
