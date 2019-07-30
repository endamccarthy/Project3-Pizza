from django import forms
from .models import Order, Meal_Type, Size, Meal_Addition, Price

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('meal', 'meal_type', 'size', 'meal_addition')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set both dropdown menus as empty until a meal is selected from the first dropdown menu
        self.fields['meal_type'].queryset = Meal_Type.objects.none()
        self.fields['size'].queryset = Size.objects.none()
        self.fields['meal_addition'].queryset = Meal_Addition.objects.none()

        # if a meal has been selected from the dropdown menu....
        if 'meal' in self.data:
            try:
                meal_id = int(self.data.get('meal'))
                self.fields['meal_type'].queryset = Meal_Type.objects.filter(meal_id=meal_id).order_by('meal')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['meal_type'].queryset = self.instance.meal.meal_type_set.order_by('meal')

        if 'meal_type' in self.data:
            try:
                meal_type = int(self.data.get('meal_type'))
                self.fields['size'].queryset = Size.objects.filter(meal_type=meal_type).order_by('size')
                self.fields['meal_addition'].queryset = Meal_Addition.objects.filter(meal_type=meal_type).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['size'].queryset = self.instance.meal_type.size_set.order_by('size')
            self.fields['meal_addition'].queryset = self.instance.meal_type.meal_addition_set.order_by('name')

    # limit the amount of meal additions to 3
    def clean_meal_addition(self):
        meal_addition = self.cleaned_data['meal_addition']
        meal_type = self.cleaned_data['meal_type']
        meal = str(self.cleaned_data['meal'])
        if 'Pizza' in meal:
            if '1 topping' in str(meal_type):
                if len(meal_addition) != 1:
                    raise forms.ValidationError('You must select 1 topping')
            if '2 toppings' in str(meal_type):
                if len(meal_addition) != 2:
                    raise forms.ValidationError('You must select 2 toppings')
            if '3 toppings' in str(meal_type):
                if len(meal_addition) != 3:
                    raise forms.ValidationError('You must select 3 toppings')

        size = self.cleaned_data['size']
        price1 = Price.objects.filter(meal_type=meal_type, size=size)
        price = float()
        for p in price1:
            print(p.price)
            price = float(p.price)
        print(price)
        
        if 'Sub' in meal:
            for item in meal_addition:
                price = price + float(item.price)

        print(price)
        return meal_addition