from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.survey_index),
    url(r'^/new$', views.new_survey)
]