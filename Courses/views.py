from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from Courses.models import *
from django.shortcuts import get_object_or_404, render_to_response

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({'Course': Course.objects.all()})
    output = template.render(variables)
    return HttpResponse(output)

def course_view(request, course_title):
    Course_instance = Course.objects.get(title=course_title)
    Decks = Course_instance.deck.all() 
    template = get_template('course_view.html')
    variables = Context({
        'Course': Course_instance,
        'Decks': Decks,
        })

    output = template.render(variables)
    return HttpResponse(output)

def deck_view(request, course_title, deck_title):
    Course_instance = Course.objects.get(title=course_title)
    Deck_instance = Deck.objects.get(title=deck_title)
    Cards_from_deck = Card.objects.filter(deck=deck_title)
    template = get_template('deck_of_cards.html')
    variables = Context({
        'Course': Course_instance,
        'Deck': Deck_instance,
        'Cards': Cards_from_deck
        })
    output = template.render(variables)
    return HttpResponse(output)
