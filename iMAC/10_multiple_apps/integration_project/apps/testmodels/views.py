# testmodels
from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'testmodels/index.html')
