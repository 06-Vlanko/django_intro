# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index (request):

    return render (request, 'amadon/index.html')

def process (request):
    if 'total_purchase' not in request.session:
        request.session['total_purchase'] = 0
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
    request.session ['item'] = request.POST['item']
    request.session ['qty'] = int(request.POST['qty'])
    request.session['total_items'] += request.session ['qty']

    return redirect ('/amadon/checkout')

def checkout (request):
    total_purchases = {
        'this_purchase': 0
    }
    if request.session ['item'] == 'tshirt':
        total_purchases['this_purchase'] += 19.99*request.session['qty']
    elif request.session ['item'] == 'sweater':
        total_purchases['this_purchase'] += 29.99*request.session ['qty']
    elif request.session ['item'] == 'cup':
        total_purchases['this_purchase'] += 4.99*request.session ['qty']
    elif request.session ['item'] == 'book':
        total_purchases['this_purchase'] += 49.99*request.session ['qty']
    
    
    request.session ['total_purchase'] += total_purchases['this_purchase']

    return render (request, 'amadon/checkout.html', total_purchases)