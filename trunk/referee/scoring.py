from django.conf import settings
from referee.models import Game, GamePointSet, GamePoint, Touchdown
from django.contrib.gis.geos import Point, MultiPoint
from datetime import datetime

def score_touchdown(point, player):
    td = Touchdown(point=point, player=player, date=datetime.now())
    td.save()