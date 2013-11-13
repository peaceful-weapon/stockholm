from django.db import models

class Deck(models.Model):
    title = models.CharField(max_length=200)
    #card = models.ForeignKey(Card)
    def __unicode__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    deck = models.ManyToManyField(Deck)

    def __unicode__(self):
        return self.title

class Card(models.Model):
    idea = models.CharField(max_length=200)
    gist = models.CharField(max_length=200)
    deck = models.ManyToManyField(Deck)
    #image = models.FileField(image.jpg)

    def __unicode__(self):
        return self.idea
