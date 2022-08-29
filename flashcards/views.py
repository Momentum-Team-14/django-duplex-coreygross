from django.shortcuts import render
from django.views.generic import (ListView,)
from .models import Card
from django.shortcuts import redirect

# Create your views here.


def card_list(request):
    cards = Card.objects.all()
    return render(request, 'flashcards/card_list.html', {"cards": cards})


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")



