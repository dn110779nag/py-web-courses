from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course

# Create your views here.


def index(request):
    courses = Course.objects.all()
    # return HttpResponse([''.join(course.title + '<br>') for course in courses])
    return render(request, 'courses.html',
                  {
                      'courses': courses
                      # ,'pageTitle': 'Courses'
                   })


def single_course(request, course_id):
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'single_course.html', {'course': course})


