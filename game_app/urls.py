from django.urls import path
from . import views

urlpatterns = [
    path('', views.game),
    path('Snake/', views.snake),
    path('Minesweeper/', views.minesweeper),
    path('Study/', views.study),
]
