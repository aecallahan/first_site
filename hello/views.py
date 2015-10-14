from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from hello.utils import random_id, image_file, pokemon_name
from hello.models import Attempt

my_strings = ['string1', 'string2', ]


def index(request):
    return render(request, 'index.html')

# Get rid of this exemption
@csrf_exempt
def game(request):
    # Set player_name to be 'blank' if nothing is entered
    player_name = request.POST.get('player_name', 'blank')
    attempt_id = request.POST.get('attempt_id', None)

    # If the attempt_id is blank, this is a new game
    if not attempt_id:
        # Create a new attempt object (score set to 0)
        attempt = Attempt.objects.create(player_name=player_name)
    else:
        attempt = Attempt.objects.get(pk=attempt_id)
        attempt.score += 1
        attempt.save()

    template = get_template('game.html')
    pokemon_id = random_id()
    image = image_file(pokemon_id)
    poke_name = pokemon_name(pokemon_id)

    data = {
        'image_file': "images/%s" % image,
        'pokemon_name': poke_name,
        'player_name': attempt.player_name,
        'player_score': attempt.score,
        'attempt_id': attempt.id,
    }

    html = template.render(Context(data))
    return HttpResponse(html)


def guess(request):
    name = HttpResponse(request.GET['name'])
    return HttpResponse(request.GET['name'])
