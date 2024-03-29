from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def index(request):
    courses = models.Course.objects.all()
    # return HttpResponse([''.join(course.title + '<br>') for course in courses])
    return render(request, 'courses.html',
                  {
                      'courses': courses
                      # ,'pageTitle': 'Courses'
                   })


def single_course(request, course_id):
    course = models.Course.objects.get(pk=course_id)
    return render(request, 'single_course.html', {'course': course})




