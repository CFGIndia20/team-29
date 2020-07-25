from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('baseline/test', views.test, name = 'test'),
    path('baseline/test/submit', views.testSubmit, name = 'test submit'),
]