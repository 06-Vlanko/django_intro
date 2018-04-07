# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    content = {
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime() )
    }

    return render (request, 'show_time/index.html', content)