from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('', home_page, name="home"),
    path('scooter/<str:slug_pk>/', item_page_scooter, name="item_page_scooter"),
    path('byke/<str:slug_id>/', item_page_byke, name="item_page_byke"),
    path('add_item_byke/', add_item_byke, name="add_item_byke"),
    path('add_item_scooter/', add_item_scooter, name="add_item_scooter"),
    path('register/', register, name="register"),


]