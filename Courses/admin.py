from django.contrib import admin
from Courses.models import *

myModels = [Course, Deck, Card]
admin.site.register(myModels)
