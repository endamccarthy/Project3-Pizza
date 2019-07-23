from django.db import models

# Create your models here.
class Pizza_Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

class Pizza_Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Sub_Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

class Sub_Addition(models.Model):
    addition = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.addition}"

class Pasta_Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

class Salad_Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

class Dinner_Platter_Type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"

class Size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class Pizza(models.Model):
    type = models.ForeignKey(Pizza_Type, on_delete=models.CASCADE, related_name="pizza_type")
    toppings = models.ForeignKey(Pizza_Topping, on_delete=models.CASCADE, related_name="pizza_toppings")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizza_size")

    def __str__(self):
        return f"{self.size} {self.type} pizza with {self.toppings}"