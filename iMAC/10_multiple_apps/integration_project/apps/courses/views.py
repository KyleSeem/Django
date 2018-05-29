# courses
from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count
from .models import Course, Comment, Student, User

# Create your views here.
def index(request):
    context = {
        'courses':Course.objects.all().order_by('name')
    }
    return render(request, 'courses/index.html', context)

def addCourse(request):
    if request.method == "POST":
        verify = Course.courseManager.create(request.POST)

        if verify[0] == False:
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('courses:index'))

        elif verify[0] == True:
            request.session.clear()
            for alert in verify[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('courses:index'))
    else:
        return redirect(reverse('courses:index'))

def deleteCourse(request, id):
    if request.method == "GET":
        context = {
            'course':Course.objects.get(id=id)
        }
        return render(request, 'courses/delete.html', context)
    elif request.method == "POST":
        delete = Course.objects.get(id=id).delete()
        return redirect(reverse('courses:index'))

def comments(request, id):
    if request.method == "GET":
        context = {
            'course':Course.objects.get(id=id)
        }
        return render(request, 'courses/comments.html', context)
    elif request.method == "POST":
        course = Course.objects.get(id=id)
        Comment.objects.create(course_id=course, comment=request.POST['comment'])
        return redirect(reverse('courses:comments', kwargs={'id':id}))

def manager(request):
    if request.method == "GET":
        # Student.objects.all().delete()
        count = Student.objects.all().values('course').annotate(num_students=Count('user'))
        context = {
            'courses':Course.objects.all().order_by('name'),
            'users':User.objects.all().order_by('first_name', 'last_name'),
            'students':Student.objects.all(),
            'count':count,
        }
        # print (count)
    return render(request, 'courses/manager.html', context)

def register(request):
    if request.method == "POST":
        register = Course.courseManager.bridge_connections(request.POST)

        if register[0] == True:
            for alert in register[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('courses:manager'))
        elif register[0] == False:
            for alert in register[1]:
                messages.add_message(request, messages.INFO, alert)
            return redirect(reverse('courses:manager'))
