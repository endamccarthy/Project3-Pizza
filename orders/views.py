from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Meal, Order, Meal_Type, Size, Meal_Addition, Price
from .forms import OrderForm
from django.template.defaulttags import register

# used to extract values from menu dictionary on the html page
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.

# automatically generates the order_form.html page when navigated to
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_add')

    # pass data into html page
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        # get menu data and pass into context
        menu = {}
        price= []
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
            
        context['menu'] = menu
        context['sizes'] = Size.objects.all()
        context['meal_additions'] = Meal_Addition.objects.all()
        context['prices'] = price
        return context

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