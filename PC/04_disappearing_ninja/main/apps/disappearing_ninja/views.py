from django.shortcuts import render, redirect, HttpResponse

def index(request):
    context = {
        "message" : "No Ninjas Here!"
    }
    return render(request, 'disappearing_ninja/index.html', context)

def ninjas(request):
    return render(request, 'disappearing_ninja/ninjas.html')

def color(request, color):
    context = {
        'color' : color,
    }

    if color == 'blue':
        context['name'] = 'Leonardo'
        context['txt_color'] = 'color: #0082c3;'
        context['image_source'] = 'disappearing_ninja/img/leonardo.jpg'

    elif color == 'orange':
        context['name'] = 'Michelangelo'
        context['txt_color'] = 'color: #fea21e;'
        context['image_source'] = 'disappearing_ninja/img/michelangelo.jpg'

    elif color == 'red':
        context['name'] = 'Raphael'
        context['txt_color'] = 'color: #e2383e;'
        context['image_source'] = 'disappearing_ninja/img/raphael.jpg'

    elif color == 'purple':
        context['name'] = 'Donatello'
        context['txt_color'] = 'color: #5b6d9e;'
        context['image_source'] = 'disappearing_ninja/img/donatello.jpg'

    else:
        context['name'] = 'Not a Ninja!'
        # context['txt_color'] = 'color: ;'
        context['image_source'] = 'disappearing_ninja/img/notapril.jpg'


    return render(request, 'disappearing_ninja/color.html', context)
