# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render (request, 'ninja_gold/index.html')

def get_money(request):

    return redirect ('/')

def clear(request):
    return redirect ('/')