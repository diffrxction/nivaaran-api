from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    
    path('',Index.as_view()),
    path('models/',GetModels.as_view())
]
