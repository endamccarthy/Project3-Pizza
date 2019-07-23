# Generated by Django 2.2.3 on 2019-07-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_dinner_platter_type_pasta_type_pizza_pizza_topping_pizza_type_salad_type_size_sub_addition_sub_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('pizzaType', models.ManyToManyField(blank=True, related_name='pizza', to='orders.Pizza')),
            ],
        ),
    ]
