from django.contrib import admin
from .models import Meal, Meal_Type, Size, Order, Meal_Addition, Price

# Register your models here.
admin.site.register(Meal)
admin.site.register(Meal_Type)
admin.site.register(Meal_Addition)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(Price)