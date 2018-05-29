from django.shortcuts import render, HttpResponse
from time import localtime, strftime

# Create your views here.
def index(request):
    context = {
        'date':strftime("%b %d, %Y"),
        'time':strftime("%l:%M %p", localtime())
    }
    return render(request, 'time_display/index.html', context)
