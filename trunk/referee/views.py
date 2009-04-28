from django.shortcuts import render_to_response
from referee.models import Game
from django.contrib.gis import admin
    
def game(request, game_name):
    game=Game.objects.get(name=game_name)
    user=request.user
    
    return render_to_response('gameMainPage.html', {'game':game,'user':user
    })