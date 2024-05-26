from django.db import models

from database.models.base import BaseModel


class Match(BaseModel):
    """
    Match model.
    """
    away_team = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    away_score = models.IntegerField(default=0)
    home_score = models.IntegerField(default=0)
