from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Meal, Order, Meal_Type, Size, Meal_Addition
from .forms import OrderForm

# Create your views here.
def index(request):
    context = {
        "meal": Meal.objects.all()
    }
    return render(request, "orders/index.html", context)

# automatically generates the order_form.html page when navigated to
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('index')

# order form dropdown menu - meal types
def load_meal_type(request):
    meal_id = request.GET.get('meal')
    meal_type = Meal_Type.objects.filter(meal_id=meal_id).order_by('name')
    return render(request, 'orders/dropdown_list_options.html', {'meal_type': meal_type})

# order form dropdown menu - sizes
def load_size(request):
    meal_id = request.GET.get('meal')
    size = Size.objects.filter(meal_id=meal_id).order_by('size')
    return render(request, 'orders/dropdown_list_options.html', {'size': size})

# order form dropdown menu - meal additions
def load_meal_addition(request):
    meal_type_id = request.GET.get('meal_type')
    meal_addition = Meal_Addition.objects.filter(meal_type_id=meal_type_id).order_by('name')
    return render(request, 'orders/dropdown_list_options.html', {'meal_addition': meal_addition})