from django.contrib import admin
from django.urls import path, include

from . import views

# app_name = 'Poll'

urlpatterns = [
    path('', views.index, name='index'),
    # path('question/', views.question, name='question'),
]
