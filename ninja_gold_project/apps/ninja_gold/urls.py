from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^get_money$', views.get_money),
    url(r'^clear$', views.clear)
]