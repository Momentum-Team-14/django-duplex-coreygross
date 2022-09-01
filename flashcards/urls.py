from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index_page, name="index-page"),
    path("flashcards/list", views.card_list, name="card-list"),
    path("flashcards/create", views.card_create, name="card-create"),
    path('flashcards/<int:pk>/edit', views.edit_card, name="card-edit"),
    path('flashcards/delete/<int:pk>', views.delete_card, name='delete-card'),
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
    path("profile", views.user_profile, name="user-profile")

]
