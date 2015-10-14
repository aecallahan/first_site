from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from hello.utils import random_id, image_file, pokemon_name

my_strings = ['string1', 'string2', ]


# Create your views here.
def index(request):
    return render(request, 'index.html')


def game(request):
    template = get_template('game.html')
    pokemon_id = random_id()
    image = image_file(pokemon_id)
    name = pokemon_name(pokemon_id)

    data = {
        'image_file': "images/%s" % image,
        'pokemon_name': name,
    }

    html = template.render(Context(data))
    return HttpResponse(html)
