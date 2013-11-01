from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from Courses.models import *
from django.shortcuts import get_object_or_404

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({'Course': Course.objects.all()})
    output = template.render(variables)
    return HttpResponse(output)

def course_view(request, course_title):
    course = get_object_or_404(Course, title=course_title)
    #course_title = course.title
    decks_from_this_course = course.deck.all()
    template = get_template('course_view.html')
    variables = Context(request, {
        'Course': course,
        })

    output = template.render(variables)
    return HttpResponse(output)
