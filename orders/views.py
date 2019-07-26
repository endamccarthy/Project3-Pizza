from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Meal, Order, Meal_Type, Size, Meal_Addition
from .forms import OrderForm

# Create your views here.

# automatically generates the order_form.html page when navigated to
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_add')

# order form dropdown menu - meal types
def load_meal_type(request):
    meal_id = request.GET.get('meal')
    meal_type = Meal_Type.objects.filter(meal_id=meal_id).order_by('name')
    context = {
        "meal_type": meal_type
    }
    return render(request, 'orders/dropdown_list_options.html', context)

# order form dropdown menu - sizes
def load_size(request):
    meal_type = request.GET.get('meal_type')
    size = Size.objects.filter(meal_type=meal_type).order_by('size')
    context = {
        "size": size
    }
    return render(request, 'orders/dropdown_list_options.html', context)

# order form dropdown menu - meal additions
def load_meal_addition(request):
    meal_type = request.GET.get('meal_type')
    meal_addition = Meal_Addition.objects.filter(meal_type=meal_type).order_by('name')
    context = {
        "meal_addition": meal_addition
    }
    return render(request, 'orders/dropdown_list_options.html', context)