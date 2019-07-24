from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('order/', views.order, name='order_add'),
    path('ajax/load-meal_types/', views.load_meal_types, name='ajax_load_meal_types')
]
