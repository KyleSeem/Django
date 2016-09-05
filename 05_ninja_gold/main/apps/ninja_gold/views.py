from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime

def index(request):
    if('plunder' in request.session) == False:
        request.session['plunder'] = 0
    return render(request, 'ninja_gold/index.html')

def process_money(request, building):
    if request.method == "POST":

        if('messages' in request.session) == False:
            request.session['messages'] = []

        if building == 'farm':
            gold = random.randrange(10,21)
        elif building == 'cave':
            gold = random.randrange(5,11)
        elif building == 'house':
            gold = random.randrange(2,6)
        elif building == 'casino':
            gold = random.randrange(-50,51)

        request.session['plunder'] += gold
        time_stamp = strftime('(%Y/%m/%d %I:%M %p)',localtime())

        if gold > 0:
            request.session['messages'].insert(0,['You earned {} gold from the {}! {}'.format(gold, building, time_stamp), 'green'])
        elif gold < 0:
            request.session['messages'].insert(0,['You lost {} gold from the {}... Ouch! {}'.format(gold, building, time_stamp), 'red'])
        else:
            request.session['messages'].insert(0,['You broke even at the {}... Could be worse! {}'.format(building, time_stamp)])
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('/')
