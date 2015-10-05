from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from hello.utils import random_image

my_strings = ['string1', 'string2', ]


# Create your views here.
def index(request):
    return render(request, 'index.html')


def game(request):
	template = get_template('game.html')
	image = random_image()
	html = template.render(Context({'image_file': image}))
	return HttpResponse(html)
