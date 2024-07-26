from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('play/', views.play_game, name='play_game'),
    path('end/', views.end_game, name='end_game'),
]
