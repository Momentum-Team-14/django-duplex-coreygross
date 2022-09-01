from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.


class User(BaseUser):
    #could add customer attributes here
    pass


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card (models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField('User', related_name='cards')

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

    def __str__(self):
        return self.question
