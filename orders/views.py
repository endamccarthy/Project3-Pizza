from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Meal, Order, Meal_Type, Size, Meal_Addition, Price
from .forms import OrderForm
from django.template.defaulttags import register
from django.contrib.auth.mixins import LoginRequiredMixin
import json


# used to extract values from menu dictionary on the html page
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# Create your views here.

def home(request):
    # get menu data and pass into context
    menu = {}
    price = []
    toppings = []
    sub_additions = {}
    for item in Meal_Type.objects.all():
        l = list(item.meal_addition.values_list('name', flat=True))
        meal_additions_list = [str(i) for i in l]
        sub_additions[item.name] = meal_additions_list
    for item in Meal.objects.all():
        l = list(Meal_Type.objects.filter(meal=item).order_by('name'))
        meal_types_list = [str(i) for i in l]
        menu[item.name] = meal_types_list
    for item in Price.objects.all():
        l = list(item.meal_type.values_list('name', flat=True))
        meal_types_by_price_list = [str(i) for i in l]
        temp = {}
        temp['size'] = item.size
        temp['price'] = item.price
        temp['meal_types'] = meal_types_by_price_list
        price.append(temp)
    meal_additions = Meal_Addition.objects.all()
    for item in list(meal_additions):
        if "Pizza" in str(item):
            toppings.append(item)
    context = {
        'title': 'Home',
        'menu': menu,
        'prices': price,
        'toppings': toppings,
        'sub_additions': sub_additions
    }
    return render(request, 'orders/home.html', context)


# automatically generates the order_form.html page when navigated to
class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders-home')

    # assign the current user as the owner of the order
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


# 
temp = {}
temp1 = {}
def load_price(request):
    if (request.GET.get('meal_type')):
        temp['meal_type'] = request.GET.get('meal_type')
        return render(request, 'orders/price.html')
    
    if (request.GET.get('size')):
        temp['size'] = request.GET.get('size')
        # get the price for the meal type selected
        meal_price = Price.objects.filter(meal_type=temp['meal_type'], size=temp['size'])
        
        for item in meal_price:
            temp1['price'] = float(item.price)
            temp['price'] = temp1['price']
            total_price = float(item.price)
        context = {
            "total_price": temp['price']
        }
        return render(request, 'orders/price.html', context)

    if (request.GET.get('meal_addition')):
        meal_additions = json.loads(request.GET.get('meal_addition'))
        for item in meal_additions:
            temp2 = {'price': 0.0}
            for x in item:
                price = Meal_Addition.objects.get(pk=x)
                if (price.price):
                    temp2['price'] = (temp2['price'] + price.price)
            temp['price'] = (temp1['price'] + temp2['price'])
        context = {
            "total_price": temp['price']
        }
        return render(request, 'orders/price.html', context)