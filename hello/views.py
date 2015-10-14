from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from hello.utils import random_id, image_file, pokemon_name
from hello.models import Attempt, check

my_strings = ['string1', 'string2', ]


def index(request):
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
            del request.session['attempt_id']
            return high_score(request)

    # Otherwise, a game is being started
    else:
        player_name = request.POST.get('player_name', 'blank')
        attempt = Attempt.objects.create(player_name=player_name)
        request.session['attempt_id'] = attempt.id

    template = get_template('game.html')
    pokemon_id = random_id()
    attempt.last_poke_id = pokemon_id
    attempt.save()
    image = image_file(pokemon_id)
    poke_name = pokemon_name(pokemon_id)

    data = {
        'image_file': "images/%s" % image,
        'pokemon_name': poke_name,
        'player_name': attempt.player_name,
        'player_score': attempt.score,
    }

    html = template.render(Context(data))
    return HttpResponse(html)


def high_score(request):
    '''
    This page of high scores is returned after a player loses
    '''
    return HttpResponse("You lost!")
