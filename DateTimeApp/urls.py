from django.conf.urls import url
from DateTimeApp import views
import datetime

urlpatterns = [
    url(r'^punejobinfo/', views.punejobinfo),
    url(r'^mumbaijobinfo/', views.mumbaijobinfo),
    url(r'^chennaijobinfo/', views.chennaijobinfo),
    url(r'^date/', views.CurrentDate),
]
