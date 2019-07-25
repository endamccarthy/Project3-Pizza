from django import forms
from .models import Order, Meal_Type

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('meal', 'meal_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['meal_type'].queryset = Meal_Type.objects.none()

        if 'meal' in self.data:
            try:
                meal_id = int(self.data.get('meal'))
                self.fields['meal_type'].queryset = Meal_Type.objects.filter(meal_id=meal_id).order_by('meal')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['meal_type'].queryset = self.instance.meal.meal_type_set.order_by('meal')