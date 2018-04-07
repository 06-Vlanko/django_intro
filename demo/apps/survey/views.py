# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def survey_index (request):
    return render (request, 'survey/survey_index.html')

def new_survey (request):
    return HttpResponse ('Placeholder for users to add a new survey')