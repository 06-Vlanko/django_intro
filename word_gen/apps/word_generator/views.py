# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    content = {
        'word': get_random_string(length=10)
    }

    if 'attempts' not in request.session:
        request.session ['attempts'] = 1
        print '----> got in IF'
    
    print '----> Current session value:', request.session['attempts']
    print request.session
    return render (request, 'word_generator/index.html', content)

def generate(request):
    print '----> IN GENERATE'
    request.session['attempts'] += 1
    return redirect ('/random_word')

def reset(request):
    print '----> IN RESET'
    request.session.clear()
    return redirect ('/random_word')