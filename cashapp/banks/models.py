from django.db import models

# Create your models here.


class Cards(models.Model):
    cardsname = models.CharField(max_length=255, unique=False)


class Banks(models.Model):
    banksname = models.CharField(max_length=255, unique=False)
    cards = models.ForeignKey(Cards, on_delete=models.CASCADE)


class Users(models.Model):
    username1 = models.CharField(max_length=255, unique=False)
    username2 = models.CharField(max_length=255, unique=False)
    useremail = models.EmailField(max_length=255, unique=False)
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    cards = models.ForeignKey(Cards, on_delete=models.CASCADE)