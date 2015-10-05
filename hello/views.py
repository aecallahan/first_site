from django.shortcuts import render

my_strings = ['string1', 'string2', ]


# Create your views here.
def index(request):
    return render(request, 'index.html')


def game(request):
	return render(request, 'game.html')
