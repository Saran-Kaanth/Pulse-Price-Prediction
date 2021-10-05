from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
    path('',home,name='home'),
    path('result',result,name="result"),
    # reverse('',result,"result"),
]
