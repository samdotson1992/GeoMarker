from django.urls import path
from django.conf.urls import url, include
from . import views


app_name = 'world'

urlpatterns = [
    # ex: /polls/
     path('', views.index, name='index'),
     path('Letterpost/', views.Letterpost, name='Letterpost')
]