from django.shortcuts import render
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    games_first_player = Game.objects.filter(first_player = request.user,status='F')
    games_second_player = Game.objects.filter(second_player=request.user,status='S')
    all_games = list(games_first_player)+\
                list(games_second_player)
    return render(request, "player/home.html",
                  {'games':all_games})