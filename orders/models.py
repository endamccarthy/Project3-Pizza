from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Meal_Type(models.Model):
    name = models.CharField(max_length=64)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"

class Pizza_Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Sub_Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Sub_Addition(models.Model):
    addition = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.addition}"

class Pasta_Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Salad_Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Dinner_Platter_Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class Pizza(models.Model):
    name = models.ForeignKey(Meal_Type, on_delete=models.CASCADE, related_name="meal_type1")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizza_size")
    toppings = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    price = models.FloatField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.size} {self.name} pizza with {self.toppings} toppings (${self.price})"

class Order(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, related_name="meal")
    meal_type = models.ForeignKey(Meal_Type, on_delete=models.CASCADE, null=True, related_name="meal_type")

    def __str__(self):
        return f"{self.meal_type} {self.meal_type}"