# Generated by Django 2.2.3 on 2019-08-08 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0042_remove_meal_type_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal_addition',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='meal_type',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='meal_type',
            name='meal_addition',
        ),
        migrations.RemoveField(
            model_name='meal_type',
            name='size',
        ),
        migrations.RemoveField(
            model_name='order',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='order',
            name='meal_addition',
        ),
        migrations.RemoveField(
            model_name='order',
            name='meal_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
        migrations.RemoveField(
            model_name='price',
            name='meal_type',
        ),
        migrations.RemoveField(
            model_name='price',
            name='size',
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='Meal_Addition',
        ),
        migrations.DeleteModel(
            name='Meal_Type',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]