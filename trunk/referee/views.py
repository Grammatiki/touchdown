from django.shortcuts import render_to_response
from referee.models import Game
from django.contrib.gis import admin
from datetime import datetime
    
def game(request, game_name):
    game=Game.objects.get(name=game_name)
    user=request.user
    
    return render_to_response('referee/gameMainPage.html', {'game':game,'user':user
    })

def index(request):
    time=datetime.now()
    games_in_play=Game.objects.filter(start_date__lte=datetime.now(), end_date__gte=time)
    planned_games=Game.objects.filter(start_date__gte=time)
    finished_games=Game.objects.filter(end_date__gte=time)
    
    return render_to_response('referee/index.html', locals())