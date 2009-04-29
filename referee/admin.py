from django.conf import settings
from django.contrib.gis import admin
from models import *
from referee.scoring import score_touchdown

def make_point_sets(modeladmin, request, queryset):
    """Custom action for the django admin which allows generation of point sets
    for games."""

    for game in queryset:
        make_point_set(settings.GAME_POINT_COUNT, game)

def score_touchdowns(modeladmin, request, queryset):
    """Custom action for the django admin which allows generation of point sets
    for games."""
    print request.user
    for point in queryset:
        score_touchdown(point=point,player=request.user)

class GameAdmin(admin.GeoModelAdmin):
    actions = [make_point_sets]

class PointAdmin(admin.GeoModelAdmin):
    actions = [score_touchdowns]

admin.site.register(GamePoint, PointAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Touchdown, admin.GeoModelAdmin)