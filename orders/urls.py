from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('order/', views.OrderCreateView.as_view(), name='order_add'),
    path('ajax/load-meal_type/', views.load_meal_type, name='ajax_load_meal_type'),
    path('ajax/load-size/', views.load_size, name='ajax_load_size'),
    path('ajax/load-meal_addition/', views.load_meal_addition, name='ajax_load_meal_addition')
]
