from django.conf import settings
from referee.models import Game, GamePoint, Touchdown
from django.contrib.gis.geos import Point, MultiPoint
import random

def make_multipoint(pointCount, game):
    """DEPRICATED! Use make_point_set. Given a Game, produces a GamePointSet of pointCount points
    linked to it via a OneToOneField, and saves it in the database."""

    points=[]
    for point in range(pointCount):
        xCoord=random.uniform(game.northwest_corner.x, game.southeast_corner.x)
        yCoord=random.uniform(game.northwest_corner.y, game.southeast_corner.y)
        points.append(Point(xCoord,yCoord))
    mp=MultiPoint(points)
    new_game_point_set=GamePointSet(game=game)
    new_game_point_set.save()
    new_game_point_set.points=mp
    new_game_point_set.save()
    
def make_point_set(pointCount, game):
    """Given a Game, produces a set of pointCount GamePoints each linked to
    it via a foreignkey and saves it in the database."""

    points=[]
    for point in range(pointCount):
        xCoord=random.uniform(game.northwest_corner.x, game.southeast_corner.x)
        yCoord=random.uniform(game.northwest_corner.y, game.southeast_corner.y)
        newgp=GamePoint(point=Point(xCoord,yCoord), game=game)
        newgp.save()