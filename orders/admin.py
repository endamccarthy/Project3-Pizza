from django.contrib import admin
from .models import Meal, Pizza, Meal_Type, Pizza_Topping, Sub_Type, Sub_Addition, Pasta_Type, Salad_Type, Dinner_Platter_Type, Size, Order

# Register your models here.
admin.site.register(Meal)
admin.site.register(Pizza)
admin.site.register(Meal_Type)
admin.site.register(Pizza_Topping)
admin.site.register(Sub_Type)
admin.site.register(Sub_Addition)
admin.site.register(Pasta_Type)
admin.site.register(Salad_Type)
admin.site.register(Dinner_Platter_Type)
admin.site.register(Size)
admin.site.register(Order)