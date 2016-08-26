from django.shortcuts import render, HttpResponse
from time import strftime, localtime
# this is the controller
def index(request):
    date_time = {
        'date': strftime('%b %d, %Y'),
        'time': strftime('%I:%M %p', localtime())
    }
    return render(request, "timedisplay/index.html", date_time)
