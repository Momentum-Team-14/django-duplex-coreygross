from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("flashcards/list", views.card_list, name="card_list"),
    path("", views.CardListView.as_view(), name="card-list"),

]
