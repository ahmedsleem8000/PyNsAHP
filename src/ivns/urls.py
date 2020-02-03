from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('norm', views.norm, name='norm'),
    path('ahp', views.ahp, name='ahp'),
    path('similarity', views.similarity, name='similarity'),
]