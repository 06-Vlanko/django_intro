# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from operator import itemgetter
from random import randint
import datetime

# Create your views here.
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render (request, 'ninja_gold/index.html')

def get_money(request):
    data = {
        'gold': 0,
        'time': datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'money_source': request.POST['money_source']
    }
    if request.POST['money_source'] == 'farm':
        data['gold'] += randint(10,20)
    elif request.POST['money_source'] == 'cave':
        data['gold'] += randint(5,10)
    elif request.POST['money_source'] == 'house':
        data['gold'] += randint(2,5)
    else:
        data['gold'] += randint(-50,50)

    request.session['total_gold'] += data['gold']

    request.session['activities'].append(data)
    request.session.modified = True

    request.session['activities']=sorted(request.session['activities'], key=itemgetter('time'), reverse=True)

    return redirect ('/')

def clear(request):
    request.session.clear()
    return redirect ('/')