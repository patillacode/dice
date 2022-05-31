from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def game(request):
    # context = {'game_id': game.id}
    context = {}
    return render(request, 'game.html', context)
