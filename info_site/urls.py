from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('visualize/', views.spacy_visualizer, name='visualizer'),
]