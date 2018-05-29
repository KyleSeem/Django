from django.shortcuts import render, redirect
from .models import User, Message, Comment
import re

# Create your views here.
def index(request):
    return render(request, 'the_wall/index.html')


def register(request):
    return redirect('/')


def login(request):
    return redirect('/')


def myWall(request, id):
    return render(request, 'the_wall/wall.html')
