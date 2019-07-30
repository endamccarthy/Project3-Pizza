from django.db import models
from django.db.models import F

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Meal_Addition(models.Model):
    name = models.CharField(max_length=64)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.meal})"

class Size(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.size}"

class Meal_Type(models.Model):
    name = models.CharField(max_length=64)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    size = models.ManyToManyField(Size)
    meal_addition = models.ManyToManyField(Meal_Addition, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Price(models.Model):
    price = models.FloatField(default = 0)
    meal_type = models.ManyToManyField(Meal_Type)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    
    def __str__(self):
        # extract values from list of meal types and convert them to a string
        l = list(self.meal_type.values_list('name', flat=True))
        s = [str(i) for i in l] 
        meal_types_list = ", ".join(s)

        return f"{self.size} ({meal_types_list}) (${self.price})"

class Order(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    meal_type = models.ForeignKey(Meal_Type, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    meal_addition = models.ManyToManyField(Meal_Addition, blank=True)

    def __str__(self):
        price1 = Price.objects.filter(meal_type=self.meal_type, size=self.size)
        print([p.price for p in price1])
        return f"{price1}"
        #return f"{self.size} {self.meal_type}"
