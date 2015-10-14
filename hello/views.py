from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from hello.utils import random_id, image_file, pokemon_name
from hello.models import Attempt, check

my_strings = ['string1', 'string2', ]


def index(request):
    # Delete the session if a user interrupted a game to navigate here
    if "attempt_id" in request.session:
        del request.session['attempt_id']

    return render(request, 'index.html')


@csrf_exempt
def game(request):
    # If attempt_id is set, a game is being continued
    if "attempt_id" in request.session:
        attempt = Attempt.objects.get(pk=request.session['attempt_id'])
        last_guess = request.POST.get('poke_name')
        attempt.last_guess = last_guess
        attempt.save()

        if check(attempt):
            attempt.score += 1
            attempt.save()
        else:
            return game_over(request, attempt)

    # Otherwise, a game is being started
    else:
        attempt = Attempt.objects.create()
        request.session['attempt_id'] = attempt.id

    pokemon_id = random_id()
    attempt.last_poke_id = pokemon_id
    attempt.save()
    image = image_file(pokemon_id)
    poke_name = pokemon_name(pokemon_id)

    data = {
        'image_file': "images/%s" % image,
        'pokemon_name': poke_name,
        'player_score': attempt.score,
    }

    template = get_template('game.html')
    html = template.render(Context(data))
    return HttpResponse(html)


def game_over(request, attempt):
    '''
    This page of high scores is returned after a player loses
    '''
    data = {
        'pokemon_name': pokemon_name(attempt.last_poke_id).capitalize(),
        'player_score': attempt.score,
    }
    template = get_template('game_over.html')
    html = template.render(Context(data))
    return HttpResponse(html)


@csrf_exempt
def scores(request):
    '''
    Display a table of high scores
    '''
    if "attempt_id" in request.session:
        # Record the player's name
        attempt = Attempt.objects.get(pk=request.session['attempt_id'])
        attempt.player_name = request.POST.get('player_name', 'unknown')
        attempt.save()

        # End the player's session
        del request.session['attempt_id']

    return render(request, 'high_scores.html',
                  {'attempts': Attempt.objects.all()[:10]})
