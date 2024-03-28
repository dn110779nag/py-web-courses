from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def index(request):
    courses = models.Course.objects.all()
    # return HttpResponse([''.join(course.title + '<br>') for course in courses])
    return render(request, 'courses.html',
                  {
                      'courses': courses,
                      'pageTitle': 'Courses'
                   })


