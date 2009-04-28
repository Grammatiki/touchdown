from django.shortcuts import render_to_response
from referee.models import Game
from django.contrib.gis import admin

class PointAdmin(admin.GeoModelAdmin):
    list_filter = ('content_type','point' )
    list_display = ('object', 'point', 'content_type', 'object_id')

def map(request):
    return render_to_response('waypoints/index.html', {
    })
    
def game_map(request, game_name):
    game=Game.objects.get(name=game_name)
    user=request.user
    
    return render_to_response('gameMainPage.html', {'game':game,'user':user
    })