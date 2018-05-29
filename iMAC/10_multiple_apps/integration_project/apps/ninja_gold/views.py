from django.shortcuts import render, redirect
import random
from time import strftime

# Create your views here.
def index(request):
    if('wallet' in request.session) == False:
        request.session['wallet'] = 0
    return render(request, 'ninja_gold/index.html')

def process(request, location):
    if request.method == "POST":

        if ('messages' in request.session) == False:
            request.session['messages'] = []

        if location == 'farm':
            gold = random.randrange(10,20)
        elif location == 'cave':
            gold = random.randrange(5,10)
        elif location == 'house':
            gold = random.randrange(2,5)
        elif location == 'casino':
            gold = random.randrange(-50,50)

        request.session['wallet'] += gold
        timeStamp = strftime('%m/%d/%Y at %l:%M %p')

        if gold > 0:
            request.session['messages'].insert(0, ['You earned {} gold from the {}! {}'.format(gold, location, timeStamp), 'green'])
        elif gold < 0:
            request.session['messages'].insert(0, ['You lost {} gold at the casino...Ouch! {}'.format(gold, timeStamp), 'red'])
        elif gold == 0:
            request.session['messages'].insert(0, ['You broke even at the casino...could be worse! {}'.format(timeStamp), 'black'])

        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
