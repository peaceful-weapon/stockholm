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

def course_view1(request, course_title):
    Courses = Course.objects.get(title=course_title)
    Decks = Courses.deck.all() 
    template = get_template('course_view.html')
    variables = Context(request, {
        'Course': Courses,
        'Decks': Decks,
        })

    output = template.render(variables)
    return HttpResponse(output)

def course_view(request, course_title):

    Decks = Deck.objects.filter(course__title__exact=course_title)
    #Courses = Course.objects.get(title=course_title).deck.all()
    #Decks = Courses.deck.all() 
    return render_to_response('course_test.html',
            {'Decks': Decks})
