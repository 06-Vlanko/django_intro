# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Placeholder to later display all the list of blogs'
    return HttpResponse (response)

def new(request):
    response = 'Placeholder to display a new form to create a new blog'
    return HttpResponse (response)

def create(request):
    print '----> CREATE() REDIRECTING TO /', number
    return redirect ('/')

def show(request, number):
    print '----> SHOW()', number
    response = 'placeholder to display blog ', number
    return HttpResponse (response)

def edit(request, number):
    print '----> EDIT()'
    response = 'placeholder to edit blog ', number
    return HttpResponse (response)

def destroy(request, number):
    print '----> DESTROY() REDIRECTING TO /', number
    return redirect ('/')