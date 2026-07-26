from django.urls import path
from . import views

app_name = 'trophies'

urlpatterns = [
    path('', views.trophy_list, name='list'),
]