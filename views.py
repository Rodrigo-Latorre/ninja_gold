from django.shortcuts import render, HttpResponse, redirect
from random import randint

def ninjagold(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
   
    return render (request, 'ninjagold.html')

def process_money(request):
    cant_min = None
    cant_max = None
    form_place = request.POST['place']
    if form_place == 'farm':
        cant_min = 10
        cant_max = 20
    elif form_place == 'cave':
        cant_min = 5
        cant_max = 10
    elif form_place == 'house':
        cant_min = 2
        cant_max = 5
    else:
        cant_min = -50
        cant_max = 50
    cant_gold = randint(cant_min, cant_max)
    if cant_gold >= 0:
        message = 'won'
        gold = cant_gold
    else:
        message = 'lost'
        gold = cant_gold * -1
    request.session['gold'] += cant_gold
    request.session['activities'].append (
        {
            'message': f'You {message} {gold} in the {form_place}',
            'c_gold': cant_gold
        })
    request.session.save()
    return redirect('/ninjagold/')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/ninjagold/')