from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def ninjas(request):
    return render(request, 'disappearing_ninjas/ninjas.html')


def color(request, color):
    context = {
        'color':color
    }

    if color == 'blue':
        context['name'] = 'Leonardo'
        context['textColor'] = 'color: #008ac2'
        context['imageSource'] = 'disappearing_ninjas/img/leonardo.jpg'

    elif color == 'orange':
        context['name'] = 'Michelangelo'
        context['textColor'] = 'color: #fe9b18'
        context['imageSource'] = 'disappearing_ninjas/img/michelangelo.jpg'

    elif color == 'red':
        context['name'] = 'Raphael'
        context['textColor'] = 'color: #df3b3e'
        context['imageSource'] = 'disappearing_ninjas/img/raphael.jpg'

    elif color == 'purple':
        context['name'] = 'Donatello'
        context['textColor'] = 'color: #575b9d'
        context['imageSource'] = 'disappearing_ninjas/img/donatello.jpg'

    else:
        context['name'] = 'not a ninja!'
        context['imageSource'] = 'disappearing_ninjas/img/notapril.jpg'


    return render(request, 'disappearing_ninjas/color.html', context)
