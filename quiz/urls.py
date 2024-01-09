from django.contrib import admin
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.home,name='home'),
    path('quiz/',views.quiz,name='quiz'),
    path('api/get-quiz/',views.get_quiz,name='get_quiz'),
]
