from django.contrib import admin
from django.urls import path

from calc import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('api', views.homeApi,name = 'homeapi'),
    path('<recipes_name>/', views.recipyview, name = 'recipyurl')
]
