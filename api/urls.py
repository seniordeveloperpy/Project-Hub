from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('portfolio/', views.portfolio),
    path('team/', views.team),
    path('vacancy/', views.vacancy),
]