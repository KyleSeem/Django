from django.shortcuts import render, HttpResponse
from time import strftime, localtime

# This is the Controller

def index(request):
    date_time = {
        'date': strftime('%b %d, %Y'),
        'time': strftime('%l:%M %p', localtime())
    }
    return render(request, "time_display/index.html", date_time)
