from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView)
from .models import Card
from django.shortcuts import redirect
from django.conf.urls.static import static
from .forms import CreateCard
import random
from .forms import CardCheckForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index_page(request):
    return render(request, 'flashcards/index.html', {})


@login_required
def card_list(request):
    cards = Card.objects.filter(users=request.user)
    return render(request, 'flashcards/card_list.html', {"cards": cards})


def card_create(request):
    if request.method == "POST":
        form = CreateCard(request.POST, request.FILES)
        if form.is_valid():
            card = form.save()
            card.users.add(request.user)
            card.save()
            return redirect('card-list')
    else:
        form = CreateCard()
    return render(request, 'flashcards/card_form.html', {"form": form})


def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('card-list')


@login_required
def user_profile(request):
    cards = Card.objects.filter(users=request.user)
    return render(request, 'flashcards/profile.html', {"cards": cards})
    

def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        form = CreateCard(request.POST, request.FILES, instance=card)
        if form.is_valid():
            card = form.save()
            return redirect('card-list')
    else:
        form = CreateCard(instance=card)
    return render(request, 'flashcards/card_edit.html', {'form': form})


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    

class BoxView(CardListView):
    template_name = "flashcards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        username = self.request.user.username
        my_card_list = Card.objects.filter(users__username=username, box=self.kwargs["box_num"])
        return my_card_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))


