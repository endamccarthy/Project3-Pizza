from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Meal, Order, Meal_Type
from .forms import OrderForm

# Create your views here.
def index(request):
    context = {
        "meal": Meal.objects.all()
    }
    return render(request, "orders/index.html", context)
'''
def order(request):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('index')
    context = {
        "model": model,
        "form_class": form_class,
        "success_url": success_url
    }
    return render(request, "orders/order_form.html", context)
'''

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('index')


def load_meal_types(request):
    meal_id = request.GET.get('meal')
    meal_types = Meal_Type.objects.filter(meal_id=meal_id).order_by('name')
    return render(request, 'orders/meal_type_dropdown_list_options.html', {'meal_types': meal_types})