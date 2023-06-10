from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("info/<int:pk>/", views.info, name='info'),
    path("cart", views.cart, name='cart'),
    path("add_good/<int:pk>/", views.add_good, name='add_good'),
    path("remove_good/<int:pk>/", views.remove_good, name='remove_good')
]
