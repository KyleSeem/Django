from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description, Comment
# Create your views here.
def index(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def addCourse(request):
    if request.method == "POST":
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(course_id=course, description=request.POST['description'])
        return redirect('/')

def deleteCourse(request, id):
    if request.method == "GET":
        context = {
            'course':Course.objects.get(id=id)
        }
        return render(request, 'courses/delete.html', context)
    elif request.method == "POST":
        delete = Course.objects.get(id=id).delete()
        return redirect('/')


def comments(request, id):
    if request.method == "GET":
        context = {
            'course':Course.objects.get(id=id)
        }
        return render(request, 'courses/comments.html', context)
    elif request.method == "POST":
        course = Course.objects.get(id=id)
        Comment.objects.create(course_id=course, comment=request.POST['comment'])
        return redirect('/comments/{}'.format(id))
