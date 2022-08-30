from django import forms

from .models import Card


class CardCheckForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)



class CreateCard(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('question', 'answer', 'box')
