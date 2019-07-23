# Generated by Django 2.2.3 on 2019-07-23 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190723_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_toppings', to='orders.Pizza_Topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_type', to='orders.Pizza_Type'),
        ),
    ]
